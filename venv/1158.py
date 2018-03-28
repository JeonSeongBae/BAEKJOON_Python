# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1158번
# 조세퍼스 문제

class Node:
    element = None
    next = None

    def __init__(self, element, next):
        self.element = element
        self.next = next
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
    size = 0

    def add(self, node):
        if self.size == 0:
            self.head = node
        else:
            node.setNext(self.head)
            self.head = node

        self.size += 1

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
                    self.head = None
                else:
                    self.head = node.getNext()

            else:
                if node.getNext() == None:
                    previous.setNext(None)
                else:
                    previous.setNext(node.getNext())
            self.size -= 1

    def  __repr__(self):
        result = "[ "
        node = self.head
        for i in range(0, self.getSize()):
            result += str(node.getElement()) + " "
            node = node.getNext()

        return result + "]"

    def getSize(self):
        return self.size


list = LinkedList()
n = Node(7,None)
list.add(n)
list.add(Node(8,None))
list.remove(0)
print(list)