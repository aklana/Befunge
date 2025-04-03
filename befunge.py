from sys import *
import random


class Pointer:
    def __init__(self, x=0, y=0, vector=2, value=None):
        self.x = x
        self.y = y
        self.vector = vector  # 1 ^, 2 >, 3 v, 4 <, изначально >
        self.value = value
        self.stack = []
        self.str_flag = 0

    def __str__(self):
        return 'Point ({},{}) vektor:{} value:{} stack_sf:{} stack:{}'.format(self.x, self.y, self.vector, self.value,
                                                                              self.str_flag, self.stack)

    def step(self):
        if self.vector == 1:
            self.x -= 1
        elif self.vector == 2:
            self.y += 1
        elif self.vector == 3:
            self.x += 1
        elif self.vector == 4:
            self.y -= 1

    def action(self):
        if self.str_flag == 1:
            if self.value == '"':
                self.str_flag = 0
            else:  # символы строки в стек кодами
                self.stack.append(ord(self.value))

        else:
            if self.value == '"':  # началась строка
                self.str_flag = 1
            elif self.value in numbers:  # цифры в стек не кодами
                self.stack.append(int(self.value))

            elif self.value in operators and self.str_flag == 0:
                b = self.stack.pop()
                a = self.stack.pop()
                if self.value == '+':
                    res = a + b
                elif self.value == '-':
                    res = a - b
                elif self.value == '*':
                    res = a * b
                elif self.value == '/':
                    if b == 0:
                        res = 0
                    else:
                        res = a // b
                elif self.value == '%':
                    res = a % b
                self.stack.append(res)

            elif self.value == '!':
                a = self.stack.pop()
                if a == 0:
                    a = 1
                else:
                    a = 0
                self.stack.append(a)

            elif self.value == '`':
                a = self.stack.pop()  # вершина
                b = self.stack.pop()  # подвершина
                if b > a:
                    res = 1
                else:
                    res = 0
                self.stack.append(res)

            elif self.value == '?':
                a = random.randint(1, 4)
                self.vector = a

            elif self.value == ':':
                last = self.stack.pop()
                self.stack.append(last)
                self.stack.append(last)

            elif self.value == "\\":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a)
                self.stack.append(b)

            elif self.value == '#':
                self.step()

            elif self.value == ',':
                value = self.stack.pop()
                print(chr(value), end='')

            elif self.value == '.':
                a = self.stack.pop()
                print(a, end='')

            elif self.value == '_':
                test = self.stack.pop()
                if test == 0:
                    self.vector = 2
                else:
                    self.vector = 4

            elif self.value == '|':
                test = self.stack.pop()
                if test == 0:
                    self.vector = 3
                else:
                    self.vector = 1

            elif self.value == '$':
                self.stack.pop()

            elif self.value == '~':
                val = input('Введите символ: ')
                self.stack.append(ord(val[0]))

            elif self.value == '&':  # Input: 65 => 65
                val = int(input('Введите число: '))
                self.stack.append(val)

            elif self.value == 'p':
                x = self.stack.pop()
                y = self.stack.pop()
                new_char = self.stack.pop()
                programm_field[x][y] = chr(new_char)

            elif self.value == 'g':
                x = self.stack.pop()
                y = self.stack.pop()
                value = programm_field[x][y]
                self.stack.append(ord(value))

            elif self.value == '>':
                self.vector = 2
            elif self.value == '<':
                self.vector = 4
            elif self.value == '^':
                self.vector = 1
            elif self.value == 'v':
                self.vector = 3
        self.step()


def open_file(name):
    data = open(name, 'r').read()
    return data


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*', '/', '%']
point = Pointer()
text = open_file(argv[1]).split("\n")
rows = len(text)
columns = max(len(line) for line in text)

programm_field = [[' ' for _ in range(columns)] for _ in range(rows)]

for i, line in enumerate(text):
    for j, char in enumerate(line):
        programm_field[i][j] = char

while point.value != '@':
    try:
        point.value = programm_field[point.x][point.y]
        point.action()
    except IndexError:
        print('Кончился стек или вышли за поле')
        break

print()
