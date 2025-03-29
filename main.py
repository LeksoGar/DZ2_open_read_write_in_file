def read_recipes(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break

            ingredients_count = int(f.readline().strip())
            ingredients = []

            for _u in range(ingredients_count):
                ingredient_line = f.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_line[0],
                    'quantity': int(ingredient_line[1]),
                    'measure': ingredient_line[2],
                }
                ingredients.append(ingredient)

            f.readline()
            cook_book[dish_name] = ingredients

    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    """Формирует список ингредиентов для указанных блюд и количества персон"""
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': ingredient['measure'],
                                                  'quantity': quantity}
    return shop_list


# Проверка работы
file_path = "recipes.txt"
cook_book = read_recipes("recipes.txt")
from pprint import pprint
pprint(cook_book)
print()

# Вызов функции для получения списка покупок
dishes =['Запеченный картофель', 'Омлет']
person_count = 2
pprint(get_shop_list_by_dishes(dishes, person_count))