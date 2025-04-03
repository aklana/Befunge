# Befunge
Befunge — стековый эзотерический язык программирования. Считается двумерным, так как программа на Befunge записывается в таблицу со сшитыми краями (тор), по которой в различных направлениях перемещается интерпретатор, исполняя команды, расположенные в её ячейках. Название языка родилось из опечатки в слове «before».

Версия Befunge-93 ограничена таблицей 25X80 (стандартный размер текстового экрана).

# Система команд Befunge93
## Система команд

### Управление потоком
| Команда | Описание |
|---------|----------|
| `>`     | Двигаться вправо |
| `<`     | Двигаться влево |
| `^`     | Двигаться вверх |
| `v`     | Двигаться вниз |
| `_`     | Двигаться вправо, если на вершине стека 0, иначе — влево |
| `\|`     | Двигаться вниз, если на вершине стека 0, иначе — вверх |
| `?`     | Двигаться в случайном направлении |
| `#`     | Пропустить следующую ячейку |
| `@`     | Конец программы |

### Операции со стеком
| Команда | Описание |
|---------|----------|
| `:`     | Дублировать вершину стека |
| `\\`    | Обменять местами вершину и подвершину |
| `$`     | Удалить вершину стека |

### Модификация кода
| Команда | Описание |
|---------|----------|
| `p`     | PUT: записать символ по координатам (y, x, ASCII-код) |
| `g`     | GET: получить ASCII-код символа по координатам (y, x) |

### Константы
| Команда | Описание |
|---------|----------|
| `0-9`   | Поместить число в стек |
| `"`     | Символьный режим (помещает ASCII-коды символов в стек) |

### Арифметические операции
| Команда | Описание |
|---------|----------|
| `+`     | Сложение |
| `-`     | Вычитание |
| `*`     | Умножение |
| `/`     | Целочисленное деление |
| `%`     | Остаток от деления |

### Логические операции
| Команда | Описание |
|---------|----------|
| `!`     | Отрицание: нуль на вершине заменяется на 1, ненулевое значение — на 0|
| `` ` `` | Сравнение "больше, чем": если подвершина больше вершины, в стек помещается 1, иначе 0  |

### Ввод-вывод
| Команда | Описание |
|---------|----------|
| `&`     | Запросить у пользователя число и поместить его в стек |
| `~`     | Запросить у пользователя символ и поместить в стек его ASCII-код |
| `.`     | Распечатать вершину стека как целое число  |
| `,`     | Распечатать символ, соответствующий ASCII-коду на вершине стека |
# Запуск программы
python3 Befunge.py programm.txt
programm.txt - текстовый файл с кодом на языке Befunge
