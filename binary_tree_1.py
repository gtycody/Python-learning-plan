class Node:     
    def __init__(self,val,left,right):
        self.val = val
        self.right = right
        self.left = left

    def recursive(self,root,count,count_list):
        if root:
            #print(root.val)
            count += 1
            self.recursive(root.left,count,count_list)
            self.recursive(root.right,count,count_list)
        else:
            count_list.append(count)    

    def maxDepth(self,root):
        count = 0
        count_list = []
        self.recursive(root,count,count_list)
        return max(count_list)

    def minDepth(self,root):
        count = 0
        count_list = []
        self.recursive(root,count,count_list)
        return min(count_list)
    
    def balanceTree(self,root):
        count = 0
        count_list = []
        self.recursive(root,count,count_list)
        if max(count_list)-min(count_list)<2:
            return True
        else: 
            return False


Node9 = Node(9,None,None)
Node8 = Node(8,Node9,None)
Node7 = Node(7,Node8,None)
Node6 = Node(6,None,None)
Node5 = Node(5,None,None)
Node4 = Node(4,None,None)
Node3 = Node(3,Node6,Node7)
Node2 = Node(2,Node4,Node5)
Node1 = Node(1,Node2,Node3)
    
print(Node1.maxDepth(Node1))
print(Node1.minDepth(Node1))
print(Node1.balanceTree(Node1))


