from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients

pprint(cook_book, width=100)
print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                ingr['quantity'] *= person_count
                quantity_dict = ingr.pop('ingredient_name')
                shop_list[quantity_dict] = ingr

    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))
