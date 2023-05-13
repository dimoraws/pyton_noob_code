# создание нового словаря
# new_dist = dict() # {}

# country_1 = {'name':'Thailand', 'sea':True}
# country_2 = {'name':'Hungary', 'sea':False}

#Подход2 - словарь
countries = {
    'Thailand':{'sea': True, 
                'schengen':False, 
                'average_temperature':30, 
                'currency_rate':1.8},
    'Hungary':{'sea': False, 
               'schengen':True, 
               'average_temperature':10, 
               'currency_rate':0.3},
    'Germany':{'sea': True, 
               'schengen':True, 
               'average_temperature':5, 
               'currency_rate':80},
    'Japan':{'sea': True, 
             'schengen':False, 
             'average_temperature':15, 
             'currency_rate':0.61}
}

#Подход1 - Список
#countries = [
#    {'name':'Thailand', 'sea': True, 'schengen':False, 'average_temperature':30, 'currency_rate':1.8},
#    {'name':'Hungary', 'sea': False, 'schengen':True, 'average_temperature':10, 'currency_rate':0.3},
#    {'name':'Germany', 'sea': True, 'schengen':True, 'average_temperature':5, 'currency_rate':80},
#    {'name':'Japan', 'sea': True, 'schengen':False, 'average_temperature':15, 'currency_rate':0.61}
#    ]

# Как заполнить словарь
# d = dict()
# d['name'] = 'Thailand'

# Множества - удобная структура для пераций пересечения и обьединения, 
#   поддерживает уникальность элементов
# В отличии от списков, элементы множества не упорядочены
shengen_countries = set()
sea_countries = set()

for country_name, properties in countries.items():
    # if country['schengen'] and country['sea'] and country['average_temperature'] > 10:
    if properties['schengen']: 
        shengen_countries.add(country_name)
    if properties['sea']: 
        sea_countries.add(country_name)

print(sea_countries)
print(shengen_countries)
print('Старны в шенгене и с морем:', shengen_countries & sea_countries)

sea_shengen_countries = shengen_countries & sea_countries

#Форматирование вывода
#money_amount = 10000
#for country in countries:
#    # print('У нас будет',money_amount / country['currency_rate'] ,'денег в местной валюте')
#    print('У нас будет %.2f денег в местной валюте' % (money_amount / country['currency_rate']))

#for country_name in sea_shengen_countries:
#    for country in countries:
#        if country['name'] == country_name:
#            print(country)
#            break

for country_name in sea_shengen_countries:
    print(country_name, countries[country_name])