class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class MyLinkedList:

    def __init__(self):
        # creating 2 dummy nodes (sentinels)
        self.left=Node(0)
        self.right=Node(0)
        # linking sentinels: left <-> right
        self.left.next=self.right
        self.right.prev=self.left
        # maintaining the length of LL
        self.length=0


    def get(self, index: int) -> int:
        # O(1) Boundary check: index must be 0 <= index < length
        if index<0 or index>=self.length:
            return -1
        
        # starting with the actual data node
        current=self.left.next
        
        # iterating exactly 'index' steps (O(k))
        for _ in range(index):
            current=current.next
            
        # now we are at the required index position
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        
        next_node=self.left.next
        prev_node=self.left
        
        # establishing 4 connections to insert at head (O(1))
        new_node.next=next_node
        new_node.prev=prev_node
        
        prev_node.next=new_node
        next_node.prev=new_node
        
        self.length+=1 # Increment length
        

    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        
        next_node=self.right
        prev_node=self.right.prev
        
        # establishing 4 connections to insert at tail (O(1))
        new_node.next=next_node
        new_node.prev=prev_node
        
        prev_node.next=new_node
        next_node.prev=new_node
        
        self.length+=1 # Increment length
        
    def addAtIndex(self, index: int, val: int) -> None:
        # O(1) Boundary check for insertion: 0 <= index <= length
        if index < 0 or index > self.length:
            return
            
        # Delegate to O(1) head/tail methods
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
            
        # Find the node at index (O(k))
        current=self.left.next
        for _ in range(index):
            current=current.next
            
        # Insertion in the middle
        new_node=Node(val)
        next_node=current
        prev_node=current.prev
        
        # establishing 4 connections (O(1))
        new_node.next=next_node
        new_node.prev=prev_node
        
        prev_node.next=new_node
        next_node.prev=new_node
        
        self.length+=1 # Increment length
        

    def deleteAtIndex(self, index: int) -> None:
        # O(1) Boundary check for deletion: 0 <= index < length
        if index < 0 or index >= self.length:
            return
            
        # Find the node to be deleted (O(k))
        current=self.left.next
        for _ in range(index):
            current=current.next
            
        # Disconnect the current node (O(1))
        prev_node=current.prev
        next_node=current.next
        
        # connecting surrounding nodes, skipping current
        prev_node.next=next_node
        next_node.prev=prev_node
        
        self.length-=1 # Decrement length