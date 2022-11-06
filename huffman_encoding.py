
import heapq  # модуль для работы с мин. кучей из стандартной библиотеки Python
from collections import Counter  # алфавит со счетчиком
from collections import namedtuple

# добавим классы дерева
class Node(namedtuple("Node", ["left", "right"])):  # класс для веток (потомки)
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")  # пойти в левого потомка, добавить "0"
        self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавить "1"

class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев (нет потомков)
    def walk(self, code, acc):
        code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"

def huffman_encode(s):  
    h = []  # очередь с приоритетами
    for ch, freq in Counter(s).items(): # постоим очередь с помощью цикла, добавив счетчик, уникальный для всех листьев
        h.append((freq, len(h), Leaf(ch)))  # очередь будет представлена частотой символа, счетчиком и самим символом
    heapq.heapify(h)  # очередь с приоритетами
    count = len(h) # значение счетчика длиной очереди
    while len(h) > 1: 
        freq1, _count1, left = heapq.heappop(h)  # минимальная частота - левый узел
        freq2, _count2, right = heapq.heappop(h)  # вминимальная частота - правый узел
        # сумма частот
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right))) 
        count += 1 
    code = {}  # инициализируем словарь кодов символов
    if h:  # если строка пустая, то очередь будет пустая и обходить нечего
        [(_freq, _count, root)] = h  # корень дерева
        root.walk(code, "")  # обойдем дерева от корня
    return code  # возвращаем словарь символов и соответствующих им кодов

def main():
    s = input() 
    code = huffman_encode(s) 
    encoded = "".join(code[ch] for ch in s)  # отобразим закодированную версию
    print(len(code), len(encoded))  # число символов, длина строки
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))  # код для символа
    print(encoded)  # вывод

if __name__ == "__main__":
    main()
