"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

prodacts_list = []
product_id = 1
product_name = ''
product_price = 0
product_count = 0
product_unit = ''
product_data = tuple()
AddProductOption = 1


#ADD NEW PRODUCT
while AddProductOption == 1:
    AddProductOption = int(input('1) Add product\n2) Cancel\n\nChoose one option (1 or 2): '))

    #ALL PRODUCTS ADDED
    if AddProductOption == 2:
        print('\n\nAll products:\n')
        for p in prodacts_list:
            print(p)
        print('\n\nCOLLICTING STATISTICS\n\n')
        break

    #ADD EVERY NEW PRODUCT
    product_name = input('\nEnter name of product: ')
    product_price = input('\nEnter price of product: ')
    product_count = input('\nEnter count of product: ')
    product_unit = input('\nEnter unit of product: ')

    product_data = (product_id, {"Name": product_name, "Price": product_price, "Count": product_count, "Unit": product_unit})
    product_id += 1
    prodacts_list.append(product_data)
    print(f"\nNew prodact added:\n\n{prodacts_list[product_id - 2]}\n\n========================================================================================\n")

#COLLECT STATISTICS
product_statistics = {"Names": [], "Prices": [], "Volumes": [], "Units": []}

for p in prodacts_list:
    product_statistics["Names"].append(p[1]["Name"])
    product_statistics["Prices"].append(p[1]["Price"])
    product_statistics["Volumes"].append(p[1]["Count"])
    product_statistics["Units"].append(p[1]["Unit"])

print('Product statistics:\n')
for keys, values in product_statistics.items():
    print(f"{keys}: {values}\n")



