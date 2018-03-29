# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1158번
# 조세퍼스 문제

class Node:
    element = None
    next = None

    def __init__(self, element):
        self.element = element
        self.next = None
        return

    def setNext(self, next):
        self.next = next
        return

    def setElement(self, element):
        self.element = element

    def getElement(self):
        return self.element

    def getNext(self):
        return self.next


class LinkedList:
    head = None
    tail = None
    size = 0

    def add(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.setNext(self.head)
            self.head = node
            self.tail.setNext(self.head)

        self.size += 1

    def remove_circle(self, index):
        temp = index % self.size
        remove_element = self.remove(temp)

        node = self.head
        for i in range(temp):
            node = node.getNext()

        self.head = node

        return remove_element

    def remove(self, index):
        if index > self.size:
            print("error")
            return
        else:
            previous = None
            node = self.head
            for i in range(index):
                previous = node
                node = node.getNext()

            if previous == None:
                if node.getNext() == None:
                    remove_element = self.head.getElement()
                    self.head = None
                else:
                    remove_element = node.getElement()
                    self.head = node.getNext()

            else:
                if node.getNext() == None:
                    remove_element = node.getElement()
                    previous.setNext(None)
                else:
                    remove_element = node.getElement()
                    previous.setNext(node.getNext())
            self.size -= 1
            return remove_element

    def  __repr__(self):
        result = "< "
        node = self.head
        for i in range(0, self.getSize()):
            result += str(node.getElement()) + " "
            node = node.getNext()

        return result + ">"

    def getSize(self):
        return self.size

list = LinkedList()
temp = input().split(" ")
input_num = int(temp[0])
remove_num = int(temp[1])

for i in range(input_num):
    list.add(Node(input_num - i))

result = "<"
for i in range(1, input_num):
    removed = list.remove_circle(remove_num-1)
    result += str(removed) + ", "

removed = list.remove_circle(remove_num-1)
result += str(removed) + "> "
print(result)

