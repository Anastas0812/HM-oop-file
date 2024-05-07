
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
print(f'Ответ к задаче №1: {cook_book}')

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

print(f'Ответ к задаче №2: {get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)}')

with open('1111/1.txt') as f:
    lines1 = f.readlines()
    lines1 = len(lines1)

with open('1111/2.txt') as f:
    lines2 = f.readlines()
    lines2 = len(lines2)

with open('1111/3.txt') as f:
    lines3 = f.readlines()
    lines3 = len(lines3)

#2.txt < 1.txt < 3.txt
# print(lines1, lines2, lines3)
# min_line = min(lines1, lines2, lines3)
# max_line = max(lines1, lines2, lines3)
# print(min_line, max_line)

with open('1111/new.txt', 'w') as f:
    f.write('2.txt\n')
with open('1111/new.txt', 'a') as f:
    f.write('1\n')
with open('1111/2.txt') as f:
    text2 = f.read()
with open('1111/new.txt', 'a') as f:
    f.write(text2)
    f.write('\n\n')

with open('1111/new.txt', 'a') as f:
    f.write('1.txt\n')
with open('1111/new.txt', 'a') as f:
    f.write('8\n')
with open('1111/1.txt') as f:
    text1 = f.read()
with open('1111/new.txt', 'a') as f:
    f.write(text1)
    f.write('\n\n')

with open('1111/new.txt', 'a') as f:
    f.write('3.txt\n')
with open('1111/new.txt', 'a') as f:
    f.write('9\n')
with open('1111/3.txt') as f:
    text3 = f.read()
with open('1111/new.txt', 'a') as f:
    f.write(text3)
    f.write('\n')

with open('1111/new.txt') as f:
    result = f.read()

print(f'Ответ к задаче №3:\n{result}')