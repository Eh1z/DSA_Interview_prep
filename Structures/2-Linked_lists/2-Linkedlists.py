class Listnode:
    def __init__ (self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, value):
        node = Listnode(value)
        if self.head is None:
            self.head = node
            return
    
        currentNode = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = node
                break
            currentNode = currentNode.next
            
    def printList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.value, "==>", end=" ")
            currentNode = currentNode.next
        print("None")
        




ll = LinkedList()
ll.insert("3")
ll.printList()
ll.insert("6")
ll.printList()
ll.insert("9")
ll.printList()
