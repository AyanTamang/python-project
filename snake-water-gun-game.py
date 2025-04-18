'''
1 for snake
-1 for water
0 for gun 


'''
computer=-1
youstr=input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
reverseDict={1:"snake",-1:"water",0:"Gun"}
print(f"you chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")
if(computer==you):
    print("Draw")

else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("You lose")
    elif(computer==1 and you==-1):
        print("You lose")
    elif(computer==1 and you==0):
        print("You win")
    elif(computer==0  and you==-1):
        print("You win ")
    elif(computer==0 and you==1):
        print("You Lose ")

    else:
        print("something went wrong")
