def preorder(node):
    if node == '.':
        return
    left, right = tree[node]

    print(node, end='')
    preorder(left)
    preorder(right)

def inorder(node):
    if node == '.':
        return
    left, right = tree[node]
    inorder(left)
    print(node, end='')
    inorder(right)

def postorder(node):
    if node == '.':
        return

    left, right = tree[node]
    postorder(left)
    postorder(right)
    print(node, end='')

N = int(input())
tree = {}

for _ in range(N):
    n, l, r = map(str, input().split())
    tree[n] = [l, r]


preorder('A')
print()
inorder('A')
print()
postorder('A')