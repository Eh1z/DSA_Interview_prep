# Exercise: Linked List
1. Create the following methods for interacting with the Linked List
```
def append(self, value):
    # Adds an extra node with **value** to the the last node

def insert(self, target_value, value_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert **value_inser**t after **target_value** node

def remove(self, value):
    # Remove first node that contains specified value
```
Now make following calls,
```
    ll = LinkedList()
    ll.append("3")
    ll.addList(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert("mango","apple") # insert apple after mango
    ll.print()
    ll.remove("orange") # remove orange from linked list
    ll.print()
    ll.remove("figs")
    ll.print()
    ll.remove("banana")
    ll.remove("mango")
    ll.remove("apple")
    ll.remove("grapes")
    ll.print()
```
[Solution](https://github.com/Eh1z/DSA_Interview_prep/blob/main/2-Linked_lists/Solution/singly_linked_list)

2. Implement a doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction.
Your node class will look this this,
```
class Listnode:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
```
Add following new methods,
```
def print_forward(self):
    # This method prints list in forward direction. Use cnode.next

def print_backward(self):
    # Print linked list in reverse direction. Use cnode.prev for this.
```
[Solution](https://github.com/Eh1z/DSA_Interview_prep/blob/main/2-Linked_lists/Solution/)
