from random import randint

"""Характеристики персонажа."""


def attack(char_name: str, char_class: str) -> str:
    """Урон нанесённый выбраным персонажем."""
    wr = 5 + randint(3, 5)
    mag = 5 + randint(5, 10)
    heal = 5 + randint(-3, -1)
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный {wr}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный {mag}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный {heal}')


def defence(char_name: str, char_class: str) -> str:
    """Навык защиты персонажа."""
    wr = 10 + randint(5, 10)
    mag = 10 + randint(-2, 2)
    heal = 10 + randint(2, 5)
    if char_class == 'warrior':
        return (f'{char_name} блокировал {wr} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {mag} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {heal} урона')


def special(char_name: str, char_class: str) -> str:
    """Специальный навык персонажа."""
    wr = {80 + 25}
    mag = {5 + 40}
    heal = {10 + 30}
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость {wr}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {mag}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {heal}»')


def start_training(char_name: str, char_class: str):
    """Старт тренировки за персонажа."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: ', end='')
    print('attack — чтобы атаковать противника,', end='')
    print('defence — чтобы блокировать атаку противника ', end='')
    print('или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        print('Введи название персонажа, за которого хочешь играть: ', end='')
        char_class = input('Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. ', end='')
            print('Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. ', end='')
            print('Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. ', end='')
            print('Черпает силы из природы, веры и духов.')
        print('Нажми (Y), чтобы подтвердить выбор, или любую ', end='')
        print('другую кнопку, чтобы выбрать другого персонажа ', end='')
        approve_choice = input().lower()
    return char_class


def main() -> str:
    """Функция обращения к игроку и выбор имени."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))

main()