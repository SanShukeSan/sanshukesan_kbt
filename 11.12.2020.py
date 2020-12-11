data = [
['Лицо со слезами радости', 2.26, 1.02, 87.3],
['Подмигивающее лицо', 19.1, 1.69, 150.0],
['Напуганное лицо', 25.6, 0.774, 0.0],
['Сердце', 233.0, 7.31, 2270.0],
['Воздушный поцелуй', 15.2, 2.36, 264.0],
['Поцелуй', 22.7, 4.26, 565.0],
['Как вкусно!', 64.6, 11.2, 834.0],
['Лицо с языком', 87.5, 5.13, 432.0],
['Обнимашки', 6.81, 0.636, 0.0],
['Задумчивое лицо', 6.0, 0.236, 478.0],
['Лицо с поднятой бровью', 4.72, 3.93, 198.0],
['Нейтральное лицо', 24.7, 1.35, 654.0],
['Умиротворенное лицо', 21.7, 2.87, 98.7],
['Ошеломленное лицо', 10.0, 5.69, 445.0],
['Спяшее лицо', 118.0, 26.0, 1080.0],
['Лицо в солнцезащитных очках', 3.31, 1.82, 697.0],
['Смущенное лицо', 23.1, 3.75, 227.0],
['Плачущее лицо', 1.74, 0.11, 0.0],
['Изнывающее лицо', 4.5, 2.49, 150.0],
['Сердитое лицо', 0.0333, 0.056, 932.0]
]


emojixpress_sum = 0
instagram_sum = 0
twitter_sum = 0
for row in data:
    emojixpress_sum += row[1]
    instagram_sum += row[2]
    twitter_sum += row[3]
    

emojixpress_sr = emojixpress_sum / len(data)
instagram_sr = instagram_sum / len(data)
twitter_sr = twitter_sum / len(data)



for i in range(len(data)):
    emojixpress_norm = data[i][1] / emojixpress_sr
    instagram_norm = data[i][2] / instagram_sr
    twitter_norm = data[i][3] / twitter_sr
    index = emojixpress_norm + instagram_norm + twitter_norm
    data[i].append(index)



data.sort(key=lambda row: row[4], reverse=True)
print('Название эмодзи  | Emojixpress, млн | Instagram, млн | Твиттер, млн | Индекс использования')
print('-------------------------------------------------------------------------------------------')
for row in data[:5]:
    print('{: <16} | {: >16.2f} | {: >14.2f} | {: >12.2f} | {: >12.2f}'.format(row[0], row[1], row[2], row[3], row[4]))
    print()
print()
