class Node:
    def __init__(self):
        self.val=None
        self.next=None


def memeber(el,zb): # sprawdzamy czy el nalezy do zbiioru
    r = zb #roboczy wskaznik
    while r!=None:
        if r.val==el:
            return True
        r=r.next
    
    return False