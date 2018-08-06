import sys
class Node(object):

    def __init__(self, x=None,y=None,t=None,force=None, next_node=None):
        self.x = x
        self.y=y
        self.t=t
        self.force=force
        self.next_node = next_node

    def get(self,choice):
        if choice=='x':
            return self.x
        if choice=='t':
            return self.t
        if choice=='y':
            return self.y
        if choice=='force':
            return self.force

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None,tail=None):
        self.head = head
        self.tail=tail

    def headx(self):
        return self.head.get('x')

    def heady(self):
        return self.head.get('y')

    def headforce(self):
        return self.head.get('force')

    def headt(self):
        return self.head.get('t')



        # Function to add newnode at end
    def AtEnd(self, x,y,t,force):
        NewNode = Node(x,y,t,force)
        if self.head is None:
            self.head = NewNode
            self.tail=NewNode
            return
        else:
            self.tail.set_next(NewNode)
            self.tail=NewNode
            return

    def DeleteHead(self):
        target=self.head
        if target is not None:
            self.head=target.next_node
            target=None
            return
        else:
            return


    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.get('force'), "x:",printval.get('x'),"y:",printval.get('y'))
            printval = printval.get_next()

filename = sys.argv[-1]
# print(sys.argv)
# print(filename)
# i=0

with open(filename) as file:
    row=[]
    matrix=[]
    i=0
    j=0
    max_row=0
    max_column=0
    boomFlag=None
    list = LinkedList()
    time=0
    while True:
        c = file.read(1)
        if not c:
            break
        if c=='\n':
            j=j+1
            matrix.append(row[:])
            row.clear()
            i=0
        else:
            row.append(c)
            if c=='+':
                list.AtEnd(x=i, y=j, t=time, force='+')
            if c=='-':
                list.AtEnd(x=i, y=j, t=time, force='-')
            i=i+1
            if max_row<=i:
                max_row=i
    max_column=j
    # print("row=",max_row)
    # print("column=",max_column)
    # print(matrix[0][4])
    # for ex in matrix:
    #     print("")
    #     for r in ex:
    #         print(r,end=" ")

# list.listprint()
# print(list.headx()+1)
time=time+1
while (list.head):
    if list.headt() == time:   #we covered all the cells of current time,move to next time unit,or break if explosion is about to go
        if boomFlag:
            break
        else:
            time=time+1

    if list.headx()+1 < max_row:      #check if there is east space to move(if we are in the edge of the matrix) welcome neo

        if matrix[list.heady()][list.headx()+1]=='.':   #chech if it is empty space to move
            matrix[list.heady()][list.headx() + 1] = list.headforce()   #add change to linked list at the end
            list.AtEnd(x=list.headx()+1,y=list.heady(),t=time,force=list.headforce())

        if matrix[list.heady()][list.headx() + 1] != 'X' and matrix[list.heady()][list.headx()+1]!=list.headforce():
            #check if east cell has an opposing force,meaning not x and not us and not empty space
            matrix[list.heady()][list.headx() + 1] ='*' #assign in matrxi explosion icon
            boomFlag=True

    if list.headx()-1 >= 0:      #check if there is west space to move(if we are in the edge of the matrix) welcome neo

        if matrix[list.heady()][list.headx()-1]=='.':   #chech if it is empty space to move
            matrix[list.heady()][list.headx() - 1] = list.headforce()   #add change to linked list at the end
            list.AtEnd(x=list.headx()-1,y=list.heady(),t=time,force=list.headforce())

        if matrix[list.heady()][list.headx() - 1] != 'X' and matrix[list.heady()][list.headx()-1]!=list.headforce():
            #check if east cell has an opposing force,meaning not x and not us and not empty space
            matrix[list.heady()][list.headx() - 1] ='*' #assign in matrix explosion icon
            boomFlag=True

    if list.heady()+1 < max_column:      #check if there is north space to move(if we are in the edge of the matrix) welcome neo

        if matrix[list.heady()+1][list.headx()]=='.':   #chech if it is empty space to move
            matrix[list.heady()+1][list.headx()] = list.headforce()   #add change to linked list at the end
            list.AtEnd(x=list.headx(),y=list.heady()+1,t=time,force=list.headforce())

        if matrix[list.heady()+1][list.headx()] != 'X' and matrix[list.heady()+1][list.headx()] != list.headforce():
            #check if east cell has an opposing force,meaning not x and not us and not empty space
            matrix[list.heady()+1][list.headx()] = '*'  #assign in matrxi explosion icon
            boomFlag=True

    if list.heady()-1 >= 0:      #check if there is south space to move(if we are in the edge of the matrix) welcome neo

        if matrix[list.heady()-1][list.headx()]=='.':   #chech if it is empty space to move
            matrix[list.heady()-1][list.headx()] = list.headforce()   #add change to linked list at the end
            list.AtEnd(x=list.headx(),y=list.heady()-1,t=time,force=list.headforce())

        if matrix[list.heady()-1][list.headx()] != 'X' and matrix[list.heady()-1][list.headx()]!=list.headforce():
            #check if east cell has an opposing force,meaning not x and not us and not empty space
            matrix[list.heady()-1][list.headx() ] ='*' #assign in matrix explosion icon
            boomFlag=True

    list.DeleteHead()

if not boomFlag:
    print("the world is saved")
    for ex in matrix:

        for r in ex:
            print(r,end="")
        print("")
else:
    print(time)
    for ex in matrix:

        for r in ex:
            print(r,end="")
        print("")






# list.DeleteHead()
# list.listprint()