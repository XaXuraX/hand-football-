# Hand Football 

rules = """ 1. Toss :- Choose odd or even ( eg say odd )then choose a number between 1 to 6 . if the number choosen by you and the computer sums to odd you win and the to choose side or kickoff 
2. start """
import random

L = [1,2,3,4,5,6]

# toss

choice1 = input("choose odd or even ? : ")
    
user_toss = int(input("Type a number between 1 and 6:"))
pc_toss = random.choice(L)
Sum1 = user_toss + pc_toss

if Sum1 % 2 ==0:
    Sum1 = "even"
else:
    Sum1 = "odd"
    

if choice1 == Sum1:
    print("Congrats! you won the toss!!") 
else:
    print("Oops! you lost the toss.")
    print("Computer chooses side",)
    
    
#game 

L2 = [1,2,3]
count = 0 
if choice1 == Sum1:
         toss_win = input("Choose side or start ? :")
         if toss_win == "start":
            while True:
                b = int(input("type 1/2/3 to pass :"))
                c = (random.choice(L2))
                print ("Computer chooses",c)
                
                if b != c:
                    count += 1
                    print((3-count),"passes to go!")
                else:
                    print ("Computer takes the ball!")
                    count +=1
                
                    
                    
                    
                
             
             

