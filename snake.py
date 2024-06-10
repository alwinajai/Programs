#snake and ladder game using random module
import random
class Board:
    board=[i for i in range(1,101)]
    def __init__(self,pname):
        self.piece=0
        self.pname=pname
        self.entering_flag=0    
    def dice(self):
        print(self.pname," rolling!")
        throw=random.randint(1,6)
        print("Roll value: ",throw)
        return throw
    def move(self):
        throwvalue=self.dice()
        if self.entering_flag==0:
            if throwvalue==6 or throwvalue==1:
                self.piece=1 
                print(self.pname," enters the board")                    
                self.entering_flag=1
            else:
                print("roll 6 or 1 to enter the board")
        else:
            if self.piece>93:
                if throwvalue+self.piece>100:
                    print("Cannot advance",self.piece)
                else:
                    self.piece=self.board[(self.piece+throwvalue)-1]
                    print(self.pname," moves to ",self.piece)
                    self.piece=self.items(self.piece)
                    return self.piece 
            else:
                self.piece=self.board[(self.piece+throwvalue)-1]
                print(self.pname," moves to ",self.piece) 
                self.piece=self.items(self.piece)
                return self.piece   
    def items(self,slot):
        snakes={95:56,97:78,88:24,62:18,48:26,36:6,32:10}
        ladders={1:38,4:14,8:30,21:42,28:76,50:67,88:99,71:92}
        for i,j in snakes.items():
            if slot==i:
                print(self.pname," got eaten by a snake and moves to ",j)
                slot=j     
        for i,j in ladders.items():
            if slot==i:
                print(self.pname," climbs a ladder and moves to ",j)
                slot=j
        return slot
Player1=Board("Player1")
Player2=Board("Player2")
i=1
while 1:
    i+=1
    if i%2==0:
        x=input("\nPlayer 1 press Enter to roll dice: ")
        if x=="":
            p1=Player1.move()
            if p1==100:
                print("Player 1 won")
                exit(0)
    else:
        x=input("\nPlayer 2 press Enter to roll dice : ")
        if x=="":
            p2=Player2.move()
            if p2==100:
                print("Player 2 won")
                exit(0)