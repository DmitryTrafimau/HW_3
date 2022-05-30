print('<<<<<< Ассистент садовника >>>>>>')
x = 1
while x == 1:
    grass = input('Добрый день! У Вас есть газон? ')
    grass = grass.strip()
    grass = grass.capitalize()
    if grass == 'Да':
        s_grass = float(input('Введите его площадь в сотках - '))
        grass_price = s_grass * 2
    else:
        grass_price = 0
    tree_1 = input('У Вас есть лиственные деревья? ')
    tree_1 = tree_1.strip()
    tree_1 = tree_1.capitalize()
    if tree_1 == 'Да':
        qt_tree_1 = int(input('Сколько у Вас лиственных деревьев? - '))
        tree_1_price = qt_tree_1 * 20
    else:
        tree_1_price = 0
    tree_2 = input('У Вас есть хвойные деревья? ')
    tree_2 = tree_2.strip()
    tree_2 = tree_2.capitalize()
    if tree_2 == 'Да':
        qt_tree_2 = int(input('Сколько у Вас хвойных деревьев? - '))
        tree_2_price = qt_tree_2 * 8
    else:
        tree_2_price = 0
    water = input('У Вас есть водоем? ')
    water = water.strip()
    water = water.capitalize()
    if water == 'Да':
        v_water = float(input('Введите его объем в кубических метрах - '))
        if v_water <= 20:
            water_price = v_water * 6
        else:
            water_price = v_water * 4
        filter_change = input('Хотите произвести замену фильтров? ')
        filter_change = filter_change.strip()
        filter_change = filter_change.capitalize()
        if filter_change == 'Да':
            water_price = water_price + 60
    else:
        water_price = 0
    if grass_price+tree_1_price+tree_2_price+water_price == 0:
        final_price = 0
    else:
        final_price = grass_price + tree_1_price + tree_2_price + water_price + 10
    print('Наши услуги будут стоить', final_price, '$.\n')
