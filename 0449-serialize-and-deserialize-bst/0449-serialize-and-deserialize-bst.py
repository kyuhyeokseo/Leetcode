# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        tree = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                tree.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                tree.append('*')

        ret = ','.join(tree)
        return ret
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data :
            return None
        
        val_list = data.split(',')
        root = TreeNode(int(val_list[0]))
        queue = deque([root])

        idx = 1

        while queue:
            curr_node = queue.popleft()

            if val_list[idx] != '*':
                curr_node.left = TreeNode(int(val_list[idx]))
                queue.append(curr_node.left)
            idx += 1

            if val_list[idx] != '*':
                curr_node.right = TreeNode(int(val_list[idx]))
                queue.append(curr_node.right)
            idx += 1

        return root


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans