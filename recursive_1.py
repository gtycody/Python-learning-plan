class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

    def returnnext(self):
        return self.nextNode

    def returnvalue(self):
        return self.value

    def returnAll(self,nextNodeInput):
        if nextNodeInput.nextNode is not None:
            print(nextNodeInput.value,"Loop!!!!")
            print(nextNodeInput.nextNode.value)
            self.returnAll(nextNodeInput.nextNode)
        else:
            print(self.value,"GG bro")



n3 = Node(4, None)
n2 = Node(2, n3)
n1 = Node(3, n2)

print(n3.returnnext() == None)
n1.returnAll(n1)




