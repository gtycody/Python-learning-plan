class Node:
    def __init__(self,val,nextNode):
        self.val = val
        self.next = nextNode

    def recursive2(self,node,count,count_list):
        if node:
            count += 1
            self.recursive2(node.next,count,count_list)
            print(count)
        else:
            count_list.append(count)


    def recursive1(self,node,count):
        if node.next.val == count:
            node.next = node.next.next
        else:
            self.recursive1(node.next,count)
            
    def length(self,root):
        count = 0
        count_list = []
        self.recursive2(root,count,count_list)
        return max(count_list)

    def remove(self,root,key):
        self.recursive1(root,key)

    def recursive_print(self,root):
        if root:
            print(root.val)
            self.recursive_print(root.next)

    def recursive_pick(self,root,key):
        if root.val == key:
            return root
        else:
            self.recursive_pick(root.next,key)

        
    def recursive_swap(self,root,key1,key2):
        node1 = self.recursive_pick(root,key1)
        node2 = self.recursive_pick(root,key2)
        temp = Node(0,None)
        temp = node1.next
        node1.next = node2.next
        node2.next = temp
            

        

Node9 = Node(9,None)
Node8 = Node(8,Node9)
Node7 = Node(7,Node8)
Node6 = Node(6,Node7)
Node5 = Node(5,Node6)
Node4 = Node(4,Node5)
Node3 = Node(3,Node4)
Node2 = Node(2,Node3)
Node1 = Node(1,Node2)

print("length",Node1.length(Node1))
#Node1.remove(Node1,3)
Node1.recursive_print(Node1)
Node1.recursive_swap(Node1,3,4)
Node1.recursive_print(Node1)

