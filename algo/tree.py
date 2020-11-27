import sys
from collections import deque


class Tree(object):
    class Node(object):
        def __init__(self, v, l, r):
            self.value = v
            self.lChild = l
            self.rChild = r

    def __init__(self):
        self.root = None

    def PrintPreOrder(self):
        self.PrintPreOrderUtil(self.root)

    def PrintPreOrderUtil(self, node):  # pre order
        if node != None:
            print(node.value)
            self.PrintPreOrderUtil(node.lChild)
            self.PrintPreOrderUtil(node.rChild)

    def PrintPostOrder(self):
        self.PrintPostOrderUtil(self.root)

    def PrintPostOrderUtil(self, node):  # pre order
        if node != None:
            self.PrintPostOrderUtil(node.lChild)
            self.PrintPostOrderUtil(node.rChild)
            print(node.value)

    def PrintInOrder(self):
        self.PrintInOrderUtil(self.root)

    def PrintInOrderUtil(self, node):  # pre order
        if node != None:
            self.PrintInOrderUtil(node.lChild)
            print(node.value)
            self.PrintInOrderUtil(node.rChild)

    def printBredthFirst(self):
        que = deque([])
        tmp = None
        if(self.root != None):
            que.append(self.root)
        while len(que) != 0:
            tmp = que.popleft()
            print(tmp.value)
            if(tmp.lChild != None):
                que.append(tmp.lChild)
            if(tmp.rChild != None):
                que.append(tmp.rChild)

    def printDepthFirst(self):
        stk = []
        tmp = None
        if(self.root != None):
            stk.append(self.root)
        while(len(stk) != 0):
            tmp = stk.pop()
            print tmp.value
            if(tmp.lChild != None):
                stk.append(tmp.lChild)
            if(tmp.rChild != None):
                stk.append(tmp.rChild)

    def TreeDepth(self):
        return self.TreeDepthUtil(self.root)

    def TreeDepthUtil(self, root):
        if root == None:
            return 0
        else:
            lDepth = self.TreeDepthUtil(root.lChild)
            rDepth = self.TreeDepthUtil(root.rChild)
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1

    def levelOrderBinaryTree(self, arr):
        self.root = self.levelOrderBinaryTreeUtil(arr, 0)

    def levelOrderBinaryTreeUtil(self, arr, start):
        size = len(arr)
        curr = self.Node(arr[start], None, None)

        left = 2 * start + 1
        right = 2 * start + 2

        if left < size:
            curr.lChild = self.levelOrderBinaryTreeUtil(arr, left)
        if right < size:
            curr.rChild = self.levelOrderBinaryTreeUtil(arr, right)

        return curr

    def CreateBinaryTree(self, arr):
        self.root = self.CreateBinaryTreeUtil(arr, 0, len(arr)-1)

    def CreateBinaryTreeUtil(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        curr = self.Node(arr[mid], None, None)
        curr.lChild = self.CreateBinaryTreeUtil(arr, start, mid-1)
        curr.rChild = self.CreateBinaryTreeUtil(arr, mid + 1, end)
        return curr

    def printAllPath(self):
        stk = []
        self.printAllPathUtil(self.root, stk)

    def printAllPathUtil(self, curr, stk):
        if curr == None:
            return None
        stk.append(curr.value)
        print stk
        if curr.lChild == None and curr.rChild == None:
            print stk
            stk.pop()
            return
        self.printAllPathUtil(curr.lChild, stk)
        self.printAllPathUtil(curr.rChild, stk)
        stk.pop()


t = Tree()
t.root = Tree.Node(6, Tree.Node(2,  Tree.Node(1, None, None),
                                Tree.Node(3, None, None)), Tree.Node(8, Tree.Node(7, None, None), Tree.Node(9, None, None)))


# t.printBredthFirst()
# print('(-----)')
# t.PrintPreOrder()
# print('(-----)')
# t.PrintPostOrder()
# print('(-----)')
# t.PrintInOrder()
# print('(-----)')
# t.printDepthFirst()

# print('(-----)')
# print t.TreeDepth()


def main(cls, args):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t2 = Tree()
    t2.CreateBinaryTree(arr)
    t2.levelOrderBinaryTree([6, ])
    t2.PrintPreOrder()
    print "----"
    t2.printAllPath()


if __name__ == "__main__":
    main(Tree, sys.argv)
