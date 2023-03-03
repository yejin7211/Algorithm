import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.cur = self.head
        self.ptr = None

    def make_list(self, ss):
        for c in ss:
            node = Node(c)
            self.cur.next = node
            node.prev = self.cur
            self.cur = node

    def move_left(self):
        if self.cur.prev is not None:
            prev_node = self.cur.prev
            self.cur = prev_node

    def move_right(self):
        if self.cur.next is not None:
            next_node = self.cur.next
            self.cur = next_node

    def remove_character(self):
        if self.cur == self.head:
            return
        if self.cur.next is None:
            prev_node = self.cur.prev
            self.cur = prev_node
            prev_node.next = None
        else:
            prev_node = self.cur.prev
            next_node = self.cur.next
            self.cur = prev_node
            self.cur.next = next_node
            next_node.prev = self.cur

    def insert_character(self, c):
        new_node = Node(c)
        if self.cur.next is None:
            self.cur.next = new_node
            new_node.prev = self.cur
            self.cur = new_node
        else:
            next_node = self.cur.next
            self.cur.next = new_node
            new_node.prev = self.cur
            new_node.next = next_node
            next_node.prev = new_node
            self.cur = new_node

    def print_list(self):
        self.ptr = self.head
        while self.ptr.next is not None:
            self.ptr = self.ptr.next
            print(self.ptr.data, end='')


s = input().rstrip()
List = LinkedList()
List.make_list(s)

m = int(input())
for _ in range(m):
    cmds = list(input().split())
    if cmds[0] == 'L':
        List.move_left()
    elif cmds[0] == 'D':
        List.move_right()
    elif cmds[0] == 'B':
        List.remove_character()
    elif cmds[0] == 'P':
        List.insert_character(cmds[1])

List.print_list()
