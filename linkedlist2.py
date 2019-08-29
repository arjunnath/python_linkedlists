
class Node :

    def __init__(self, val):
        self.value = val
        self.nextnode = None
        self.prevnode = None


class DoubleLinkedList :
    
    def __init__(self, val=None):
        self.listptr = None
        if val is None :
            return None
        self.listptr = Node(val)
        self.__head__ = self.listptr

    def new(self, val=None) :
        if self.listptr is None :
            raise Exception("List object has no Node")
        if val is None :
            pass # do nothing
        i = Node(val)
        if self.listptr.nextnode is None:
            self.listptr.nextnode = i
            i.prevnode = self.listptr
            self.listptr = i
        else :
            x = self.listptr.nextnode
            x.prevnode = i
            i.prevnode = self.listptr
            i.nextnode = x
            self.listptr.nextnode = i
            self.listptr = i

    def next(self) :
        if self.listptr.nextnode is not None :
            self.listptr = self.listptr.nextnode

    def prev(self):
        if self.listptr.prevnode is not None :
            self.listptr = self.listptr.prevnode

    def value(self):
        return self.listptr.value

