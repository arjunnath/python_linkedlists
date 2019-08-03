
class Node :

    def __init__(self, val):
        self.value = val
        self.nextnode = None
        self.prevnode = None

    def next(self) :
        return self.nextnode

    def prev(self):
        return self.prevnode

    def new(self, val) :
        i = Node(val)
        self.nextnode = i
        i.prevnode = self
        return i
