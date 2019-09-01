
class Node :

    def __init__(self, val=None):
        self.value = val
        self.nextnode = None

def newnode(val = None) :
    return Node(val)

def nextnode(nodeobj) :
    if instanceof(nodeobj, Node) :
        return nodeobj.nextnode
