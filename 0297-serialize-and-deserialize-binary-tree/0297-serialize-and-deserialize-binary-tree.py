# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None :
            return ' '
        
        is_ground = False
        ret = ''
        tL = [root]
        
        while is_ground == False :
            
            is_ground = True
            tmp = []
            
            for target in tL :
                if target.val == 1001 :
                    ret += (', ')
                else :
                    ret += (',' + str(target.val))
                
                if target.val < 1001 :
                    if target.left is not None :
                        is_ground = False
                        tmp.append(target.left)
                    else :
                        tmp.append(TreeNode(1001,None,None))

                    if target.right is not None :
                        is_ground = False
                        tmp.append(target.right)  
                    else :
                        tmp.append(TreeNode(1001,None,None))
            
            tL = tmp[:]
            
        ret = ret[1:]
        
        return ret
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == ' ':
            return None
        
        value_list = data.split(',')
        
        head = TreeNode(value_list[0], None, None)
        
        if len(value_list) == 1 :
            return head
    
        L = len(value_list)
        node_list = [head]
        
        open_list = [[head, 'L'], [head, 'R']]
        
        for i in range(1, L):
            #print(f'========== {i} ==========')
            #print(value_list[i])
            #print(open_list[0])
            
            if value_list[i] == ' ':
                open_list.pop(0)
            else :
                child = TreeNode(int(value_list[i]), None, None)
                parent, LR = open_list[0][0], open_list[0][1]
                open_list.pop(0)
                if LR == 'L':
                    parent.left = child
                else :
                    parent.right = child
                open_list.append([child, 'L'])
                open_list.append([child, 'R'])
                    
        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))