
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

# print(f'Ответ к задаче №2: {get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)}')



import os
list_files = os.listdir('1111')
folder_path = '1111'
full_paths = [os.path.join(folder_path, file_name) for file_name in list_files]

dict_lines = {}
for file in full_paths:
    with open(f'{file}') as f:
        for idx, line in enumerate(f):
            pass
            with open(f'{file}') as f:
                data = f.read()
                dict_lines[file.replace('1111/', '')] = idx + 1, data
items = dict_lines.items()

# if list(items)[0][1][0] <= list(items)[1][1][0] <= list(items)[2][1][0]:
#     print(f'Возрастание построчно1: {list(items)[0], list(items)[1], list(items)[2]}')
# elif list(items)[0][1][0] <= list(items)[2][1][0] <= list(items)[1][1][0]:
#     print(f'Возрастание построчно2: {list(items)[0], list(items)[2], list(items)[1]}')
# elif list(items)[1][1][0] <= list(items)[0][1][0] <= list(items)[2][1][0]:
#     print(f'Возрастание построчно3: {list(items)[1], list(items)[0], list(items)[2]}')
# elif list(items)[1][1][0] <= list(items)[2][1][0] <= list(items)[0][1][0]:
#     print(f'Возрастание построчно4: {list(items)[1], list(items)[2], list(items)[0]}')
# elif list(items)[2][1][0] <= list(items)[0][1][0] <= list(items)[1][1][0]:
#     print(f'Возрастание построчно5: {list(items)[2], list(items)[0], list(items)[1]}')
# elif list(items)[2][1][0] <= list(items)[1][1][0] <= list(items)[0][1][0]:
#     print(f'Возрастание построчно6: {list(items)[2], list(items)[1], list(items)[0]}')
# else:
#     print('Ошибка')

text = []
result = list(items)[1], list(items)[2], list(items)[0]
# print(result)
for i in result:
    for line in i:
        for name in line:
            text.append(name)

text = ['2.txt\n', '1\n', 'Тревога началась в тринадцать часов ноль две минуты.\n', '1.txt\n', '8\n', 'Начальник  полиции\nлично позвонил в шестнадцатый участок. А спустя  одну минуту тридцать секунд\nв дежурке и других комнатах нижнего этажа раздались звонки\n     Когда Иенсен  --  комиссар  шестнадцатого  участка --  вышел  из своего\nкабинета,  звонки еще  не смолкли. Иенсен был мужчина средних лет,  обычного\nсложения, с лицом плоским и невыразительным. На последней ступеньке винтовой\nлестницы  он задержался  и  обвел взглядом помещение дежурки. Затем поправил\nгалстук и проследовал к машине.', '3.txt\n', '9\n', '     В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди\nпотока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире\nрезких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными.\nОдеты они были хорошо, но как-то удивительно походили друг на друга и все до\nодного спешили. Они шли нестройными  вереницами, широко разливались, завидев\nкрасный  светофор или  металлический  блеск кафе-автоматов.  Они непрестанно\nозирались по сторонам и теребили портфели и сумочки.\n     Полицейские  машины  с  включенными  сиренами  пробивались  сквозь  эту\nтолчею.']

with open('new_file.txt', 'w') as f:
    f.writelines(text)
with open('new_file.txt', 'r') as f:
    print(f'Ответ к задаче №3:\n{f.read()}')

