import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = pd.read_csv('fatal-police-shootings-data.csv')
stany = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations', header=0)
populacja = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population', header=0)

pivot_table = pd.pivot_table(data, index='race', columns='signs_of_mental_illness', aggfunc='size', fill_value=0)

pivot_table['Percent_with_Mental_Illness'] = pivot_table.apply(lambda row: (row[True] / (row[True] + row[False])) * 100, axis=1)
najwyzszy_odsetek_rasy = pivot_table['Percent_with_Mental_Illness'].idxmax()
najwyzszy_odsetek = pivot_table['Percent_with_Mental_Illness'].max()

data['date'] = pd.to_datetime(data['date'])
data['Day_of_Week'] = data['date'].dt.day_name()
interwencje = data['Day_of_Week'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

print(data.head())
print("\n", pivot_table)
print("\nRasa z największym odsetkiem znamion choroby psychicznej: {}, Odsetek: {:.2f}%".format(najwyzszy_odsetek_rasy, najwyzszy_odsetek))

plt.figure(figsize=(10, 6))
interwencje.plot(kind='bar', color='skyblue')
plt.title('Interwencje Policji według Dnia Tygodnia')
plt.xlabel('Dzień Tygodnia')
plt.ylabel('Liczba Interwencji')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

