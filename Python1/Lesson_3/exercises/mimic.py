#!/usr/bin/python3

__author__ = "Чепелев Антон"

"""Имитация текста

Прочитайте файл, указанный в командной строке.
Используйте str.split() (без аргументов) для получения всех слов в файле.
Вместо того, чтобы читать файл построчно, проще считать
его в одну гигантскую строку и применить к нему split() один раз.

Создайте "имитационный" словарь, который связывает каждое слово
со списком всех слов, которые непосредственно следуют за этим словом в файле.
Список слов может быть в любом порядке и должен включать дубликаты. 

Так, например, для текста "Привет, мир! Привет, Вселенная!" мы получим такой
имитационный словарь:
{'': ['Привет,'], 'Привет,': ['мир!', 'Вселенная!'], 'мир!': ['Привет,']}
Будем считать, в качестве ключа для первого слова в файле используется пустая строка.

С помощью имитационного словаря довольно просто генерировать случайные тексты, 
имитирующие оригинальный. Возьмите слово, посмотрите какие слова могут за ним, 
выберите одно из них наугад, выведите его и используйте это слово 
в следующей итерации.

Используйте пустую строку в качестве ключа для первого слова.
Если вы когда-нибудь застрянете на слове, которого нет в словаре,
вернетесь к пустой строке, чтобы продолжать генерацию текста.

Примечание: стандартный python-модуль random включает в себя метод 
random.choice(list), который выбирает случайный элемент из непустого списка.

"""

import random
import sys


def mimic_dict(filename):
    """Возвращает имитационный словарь, сопоставляющий каждое слово 
    со списом слов, которые непосредственно следуют за ним в тексте"""
    # Получим список всех слов
    with open(filename, 'r', encoding="UTF-8") as f:
        lst = (f.read()).split()
    d = {'': [lst[0]]}
    for key in (d.copy()).keys():
        elem = d.get(key)[0]
        ind = lst.index(elem)
        d.update({elem: [lst[ind + 1]]})
        if lst.count(elem) > 1:
            for i in range(1, lst.count(elem)):
                try:
                    ind = lst.index(elem, ind + 1)
                    d.get(elem).append(lst[ind + 1])
                except IndexError:
                    continue
    return d


def print_mimic(mimic_dict, word):
    """Принимает в качестве аргументов имитационный словарь и начальное слово,
    выводит 200 случайных слов."""
    # +++ваш код+++
    return


def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()