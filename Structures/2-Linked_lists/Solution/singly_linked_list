class Listnode:
    def __init__ (self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def append(self, value):
        node = Listnode(value)
        if self.head is None:
            self.head = node
            return
    
        cnode = self.head
        while True:
            if cnode.next is None:
                cnode.next = node
                break
            cnode = cnode.next
            
    def print(self):
        cnode = self.head
        while cnode != None:
            print(cnode.value, "==>", end=" ")
            cnode = cnode.next
        print("None")
        
    def insert(self, target_value, value_insert):
        if self.head is None:
            return
        if self.head.value == target_value:
            self.head.next = Listnode(value_insert, self.head.next)
            return
        cnode = self.head
        while cnode:
            if cnode.value == target_value:
                cnode.next = Listnode(value_insert, cnode.next)
                break
            cnode = cnode.next
            
    def remove(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        cnode = self.head
        while cnode.next:
            if cnode.next.value == value:
                cnode.next = cnode.next.next
                break
            cnode = cnode.next
            
    def addList(self, List):
        if self.head is None:
            return
        for value in List:
            self.append(value)




ll = LinkedList()
ll.append("3")
ll.print()
ll.addList(["banana","mango","grapes","orange"])
ll.print()
ll.insert("mango","apple")
ll.print()
ll.remove("orange")
ll.print()
ll.remove("figs")
ll.print()
ll.remove("banana")
ll.remove("mango")
ll.remove("apple")
ll.remove("grapes")
ll.print()
