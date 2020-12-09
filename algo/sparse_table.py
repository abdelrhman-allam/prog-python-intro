class LinkedList:

    ''' Node 
    '''
    class Node:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def __init__(self):
        self.head = None

    def addTail(self, val):
        tail = self.Node(val, None)

        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = tail
        self.size += 1

    def isPresented(self, val):
        curr = self.head

        while curr != None:
            if curr.val == val:
                return True
            curr = curr.next
        return False


class University():

    def __init__(self):
        self.colleges = []
        self.departments = []
        self.courses = []
        self.students = []

    def addCollege(self, val):
        pass
