class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key=key
        self.left=left
        self.right=right


def tree_insert(root, node):  # O(h), h - height of a tree; for balanced tree - lg(n)
    if root is None:
        root = node
    else:
        if root.key > node.key:
            if root.left is None:
                root.left = node
            else:
                tree_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                tree_insert(root.right, node)


def in_order_tree_walk(x):
    if x is not None:
        in_order_tree_walk(x.left)
        print(x.key)
        in_order_tree_walk(x.right)

    return


def pre_order_tree_walk(x):
    if x is not None:
        print(x.key)
        pre_order_tree_walk(x.left)
        pre_order_tree_walk(x.right)

    return


def postorder_tree_walk(x):
    if x is not None:
        postorder_tree_walk(x.left)
        postorder_tree_walk(x.right)
        print(x.key)
    return


def tree_search(x,k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left,k)
    else:
        return tree_search(x.right,k)


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_parent(root, key):
    parent, node = None, root
    while True:
        if node is None:
            return None, None

        if node.key == key:
            return parent, node

        parent, node = (node, node.left) if key < node.key else (node, node.right)


def tree_successor(root,x):
    if x.right is not None:
        return tree_minimum(x.right)
    y, _ = tree_parent(root, x.key)
    while y is not None and x == y.right:
        x = y
        y, _ = tree_parent(root, y.key)
    return y


def tree_predecessor(root, x):
    if x.left is not None:
        return tree_maximum(x.left)
    y, _ = tree_parent(root, x.key)
    while y is not None and x == y.left:
        x = y
        y, _ = tree_parent(root, y.key)
    return y


# This function might not be entirely correct!
def transplant(root, u, v):
    up, _ = tree_parent(root, u.key)
    if up is None:
        root = v
    elif u == up.left:
        up.left = v
    else:
        up.right = v

    if v is not None:
        vp, _ = tree_parent(root, v.key)
        vp.key = up.key

    # This function might not be entirely correct!


def tree_delete(root, z):
    if z.left is None:
        transplant(root, z, z.right)
    elif z.right is None:
        transplant(root, z, z.left)
    else:
        y = tree_minimum(root)
        yp, _ = tree_parent(root, y.key)
        if yp.key != z.key:
            transplant(root, y, y.left)
            y.right = z.right
            yrp, _ = tree_parent(root, y.right.key)
            yrp.key = y.key
        transplant(root, z, y)
        y.left = z.left
        ylp, _ = tree_parent(root, y.left.key)
        if ylp is not None:
            ylp.key = y.key


def iter_pre_order_tree_walk(root):
    # Base CAse
    if root is None:
        return

        # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    #  Pop all items one by one. Do following for every popped item
    #   a) print it
    #   b) push its right child
    #   c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while len(nodeStack) > 0:

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.key)

        # Push right and left children of the popped node
        # to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
