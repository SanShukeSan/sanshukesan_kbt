import pandas as pd
df = pd.read_csv('cholera.csv')
#Задание 0
table_size = df.shape
print(table_size)
#Задание 1
last_line = df.head(-12)
print(last_line)
#Задание 2
first_line = df.head(3)
print(first_line)
#Задание 3
rso = df.loc[:,['region','country','total_cases']]
print(rso)
#Задание 4
srez = df.iloc[3:12]
print(srez)
#Задание 5
more = [df['total_cases'] > 50]
print(more)
#Задание 6
okay=df.loc[df.loc[:,'region']=='Азия']['region'].count()
not_okay=df.loc[df.loc[:,'region']!='Азия']['region'].count()
if okay > not_okay:
    print("Стран Азии больше и тут без обговорок")