
class Node:  
    def __init__(self, dato):
        self.dato = dato
        self.next = None
        self.prev = None


class DoublyLinkedList:  
    def __init__(self):
        self.head = None
    
    def push(self, valor):
        NewNode = Node(valor)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
    
    def isEmpty(self):
        return self.head == None  

    def agregarDespues(self, nodo, valor): 
        if nodo == None:
            print('El nodo es vacío')

        if nodo != None:
            new_node = Node(valor)
            new_node.next = nodo.next
            nodo.next = new_node
            new_node.prev = nodo
        if new_node.next != None:
            new_node.next.prev = new_node

    def agregarAntes(self, nodo, valor):
        if nodo == None:
            print('El nodo es vacío')

        if nodo != None:
            new_node = Node(valor)
            new_node.prev = nodo.prev
            nodo.prev = new_node
            new_node.next = nodo
        if new_node.prev != None:
            new_node.prev.next = new_node

    def peek(self): 
        if self.head == None: 
            print('Lista vacía')
        else:
            return self.head
