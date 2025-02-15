class Node:
    def __init__(self, key, val):
        self.key   = key
        self.value = val
        self.prev  = None
        self.next  = None
        self.count = 1

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def append(self, node):
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev
        self.size += 1
    
    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.size -= 1
        node.prev, node.next = None, None
        return node


class LFUCache:
    def __init__(self, capacity: int):

        self.MIN_COUNT = 0
        self.SIZE      = 0
        self.LIMIT     = capacity
        self.KEY2NODE  = {}
        self.CNT2DLL   = {}
        

    def get(self, key: int) -> int:

        if key not in self.KEY2NODE :
            return -1
        else :
            target_node = self.KEY2NODE[key]
            cnt = target_node.count
            DLL = self.CNT2DLL[cnt]
            DLL.pop(target_node)
            new_cnt = cnt + 1
            target_node.count = new_cnt

            if new_cnt in self.CNT2DLL:
                self.CNT2DLL[new_cnt].append(target_node)
            else :
                self.CNT2DLL[new_cnt] = DoubleLinkedList()
                self.CNT2DLL[new_cnt].append(target_node)
            
            if self.CNT2DLL[cnt].size == 0 :
                del self.CNT2DLL[cnt]
            
            if cnt == self.MIN_COUNT and cnt not in self.CNT2DLL :
                self.MIN_COUNT += 1

            return target_node.value


    def put(self, key: int, value: int) -> None:
        if key in self.KEY2NODE :
            target_node = self.KEY2NODE[key]
            target_node.value = value
            self.get(key)
        else :
            if self.SIZE == self.LIMIT:
                MIN_DLL = self.CNT2DLL[self.MIN_COUNT]
                lru_node = MIN_DLL.head.next
                del self.KEY2NODE[lru_node.key]
                MIN_DLL.pop(lru_node)
                self.SIZE -= 1
            
            new_node = Node(key, value)
            self.KEY2NODE[key] = new_node
            self.MIN_COUNT = 1
            if 1 in self.CNT2DLL:
                self.CNT2DLL[1].append(new_node)
            else :
                self.CNT2DLL[1] = DoubleLinkedList()
                self.CNT2DLL[1].append(new_node)
            self.SIZE += 1
        

            


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)