
def do_cook_book():
    with open('cook_book_file.txt') as file:
        cook_book = {}
        for text in file.read().split('\n\n'):
            dish_name, amount, *ingridients = text.split('\n')
            list_ingr = []
            for ingridient in ingridients:
                ingredient_name, quantity, measure = list(map(lambda x: int(x) if x.isdigit() else x, ingridient.split(' | ')))
                list_ingr.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish_name] = list_ingr
    return cook_book
cook_book = do_cook_book()
# print(f'Ответ к задаче №1: {cook_book}')

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = do_cook_book()
    list_ = {}
    d = {}
    for dish_name in dishes:
        for ingridient in cook_book[dish_name]:
            new_list = dict()
            new_list['measure'] = ingridient['measure']
            new_list['quantity'] = ingridient['quantity'] * person_count
            if ingridient['ingredient_name'] not in new_list:
                list_[ingridient['ingredient_name']] = new_list
            else:
                list_[ingridient['ingredient_name']]['quantity'] += new_list['quantity']
            x = ingridient['ingredient_name']
            d[x] = new_list
    return d

# print(f'Ответ к задаче 2: {get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)}')