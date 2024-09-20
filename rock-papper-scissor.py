import random

def random1():
    c=random.randrange(1,4)
    return c
while True:
    value=input('Enter "Y" to play the game or "N" to exit ')
    if value=='n' or value=='N':
        break
    elif value=='y' or value=='Y':
            
        a=int(input("How Many Times To Play : "))
        user=0
        computer=0
        for i in range(a):
            print(end='\n\n')
            print("Enter 1 to choose 'Rock'" )
            print("Enter 2 to choose 'Paper'" )
            print("Enter 3 to choose 'Scissor'" )
            b=int(input("Enter Your Choice : "))
            print(end='\n\n')
            #Output For The User Input
            if b==1:
                print('Your Choice Is Rock')
            elif b==2:
                print('Your Choice Is Paper')
            elif b==3:
                print('Your Choice Is Scissor')
            #Output For The computer Input
            c=random1()
            if c==1:
                print('Computer Choice Is Rock')
            elif c==2:
                print('Computer Choice Is Paper')
            elif c==3:
                print('Computer Choice Is Scissor')

 
            if c==b:
                print("The match is Tie")
            if c==1<b==2:
                print("You Won The Match")
                user+=1
            if c==1<b==3:
                print("Computer Won The Match")
                computer+=1
            if c==2<b==3:
                print("You Won The Match")
                user+=1
            if c==2>b==1:
                print("Computer Won The Match")
                computer+=1
            if c==3>b==2:
                print("Computer Won The Match")
                computer+=1
            if c==3>b==1:
                print("You Won The Match")
                user+=1
        print(end='\n')
        print("***************************")
        print("!!!!    GAME OVER   !!!")
        if user==computer:
            print("----- Match Draw -----")
        elif user<computer:
            print('Your Points : ',user)
            print('Compuer  Points : ',computer)
            print("----- Computer Won The match -----")
        elif user>computer:
            print('Your Points : ',user)
            print('Compuer Points : ',computer)
            print("----- Yow Won The Match -----")
        print("***************************")

    else:
        print("Enter Valid Input")
