import sys, math

input = sys.stdin.readline

MOD = 1000000007


def tree_mul(node, start, end, l, r):
    if r < start or end < l:
        return 1
    if l <= start and end <= r:
        return tree[node]

    mid = (start + end) // 2
    return (tree_mul(node * 2, start, mid, l, r) * tree_mul(node * 2 + 1, mid + 1, end, l, r)) % MOD


def update(no, s, e, idx, val):
    if idx < s or e < idx:
        return
    if s == e:
        tree[no] = val
        return
    mid = (s + e) // 2
    update(no * 2, s, mid, idx, val)
    update(no * 2 + 1, mid + 1, e, idx, val)
    tree[no] = (tree[no * 2] * tree[no * 2 + 1]) % MOD


n, m, k = map(int, input().split())
tree_size = math.ceil(math.log2(n))
tree_size = 1 << (tree_size + 1)
tree = [0] * tree_size

for i in range(n):
    num = int(input())
    update(1, 0, n - 1, i, num)

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, n - 1, b - 1, c)
    else:
        print(tree_mul(1, 0, n - 1, b - 1, c - 1))