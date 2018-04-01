# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 10828번
# 스택 기본

class stack:
    data = []
    index = 0

    def push(self, num):
        self.data.append(num)
        self.index += 1

    def pop(self):
        if self.size() > 0:
            self.index -= 1
            return self.data.pop(self.size())
        else:
            return -1

    def size(self):
        return self.index

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size() == 0:
            return -1
        else:
            return self.data[self.size()-1]


op_num = int(input())
user_stack = stack()

for i in range(op_num):
    op = input().split(" ")

    if op[0] == "push":
        user_stack.push(op[1])
    elif op[0] == "pop":
        print(user_stack.pop())
    elif op[0] == "top":
        print(user_stack.top())
    elif op[0] == "size":
        print(user_stack.size())
    elif op[0] == "empty":
        print(user_stack.empty())
    else:
        print("not op")

