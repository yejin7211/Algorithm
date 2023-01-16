import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
for _ in range(n):
    node, left_node, right_node = input().strip().split()
    tree[node].append(left_node)
    tree[node].append(right_node)


def pre_order(cur):  # 전위 순회
    result = cur
    for child in tree[cur]:
        if child != '.':
            result += pre_order(child)
    return result


def in_order(cur):
    result = ''
    if tree[cur][0] != '.':
        result += in_order(tree[cur][0])
    result += cur
    if tree[cur][1] != '.':
        result += in_order(tree[cur][1])
    return result


def post_order(cur):
    result = ''
    if tree[cur][0] != '.':
        result += post_order(tree[cur][0])
    if tree[cur][1] != '.':
        result += post_order(tree[cur][1])
    return result + cur


print(pre_order('A'))
print(in_order('A'))
print(post_order('A'))
