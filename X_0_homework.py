#Крестики-нолики

battlefield = [1, 2, 3, 4, 5, 6 ,7, 8, 9] # Поле
field_size = 3 # Размер поля == 3x3

def field_start(): # Вывод поля
    print(('_' * 3 + ' ') * 3)
    for i in range(field_size):
        print((' '* 3 + '|') * 3)
        print('', battlefield[i * 3], '|', battlefield[1+ i * 3], '|', battlefield[2+ i * 3], '|')
        print(('_' * 3 + ' ') * 3)

def game_step(index, char): # Функция ограничения хода игрока( поле занято/ход на несуществующие поле)
    if (index > 9 or index < 1 or battlefield[index - 1] in ('X', 'O')):
        return False

    battlefield[index - 1] = char
    return True

def win(): # Проверка победы
    win_check = False

    win_combination = (
        (0, 1 , 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    for pos in win_combination:
        if (battlefield[pos[0]] == battlefield[pos[1]] and battlefield[pos[1]] == battlefield[pos[2]]):
            win_check = battlefield[pos[0]]
    return  win_check

def start_game(): #Ход игрока
    player = 'X' # Первый игрок
    step = 1 # Номер шага
    field_start()
    while (step < 10) and (win() == False):
        index = int(input('Ход игрока: ' +  player + '. Введите номер поля (0 - выход): '))
        if (index == 0):
            break

        if game_step(int(index), player):
            print('Ход совершен!')

            if (player == 'X'):
                player = 'O'
            else:
                player = 'X'

            field_start()
            step += 1
        else:
            print('Неверный номер поля! Повторите!')
    if (step == 10 and not win()):
        print('Ничья!')
    else:
        print('Победа: ', win())

print('Wlecome to X-0')
start_game()
