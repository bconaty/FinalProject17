def space():
    x =1
    while (x <= 6):
        print("###")
        x=x+1
#this function prints lines of "###" to leave space between code
def end():
    print("GAME OVER :(")
    print("RESET THE GAME TO TRY AGAIN")
#this function prints "GAME OVER :(" when you get a question wrong
print("Hello and welcome to my game!")
space()
print("HACKER")
space()
game_description="In this game you will play the role of an high level FBI hacker who must find out who hacked the Pentagon and what they took in the last cyber attack"
#defining game_description
print(f"{game_description}")
#printing game_description
print("Lets become a FBI agent")

name=input("What is your name?")
code_name=input("What is your code name?")
#personalizing the game by defining values with inputs
print("running super offical backround check....")

a=0
while (a<101):
    print(f"{a}% done")
    a=a+10
#loop to print progress until finshed/reaches 100%
print("CONGRATS YOUR A REAL FBI AGENT!!!")

print("Here's your badge")
print(f"""-------------------
         --------FBI---------
         --------------------
         --------------------
         -------{name}-------
         ----'{code_name}'----
         --------------------""")
#prints badge with "name" and "code_name"
space()
print("Ok, you are all ready and you have been assiged to project PHOENIX.")
print("You open your PHOENIX case files and you are ready to start.")
space()
print("Stage One: Disable The Fire Wall")

print("After many tries, you try a more direct route into the fire wall and you get stopped by a riddle.")
answer_1=input("Close beside the Potomac I am made up of 5 parts but also many peopel what am I?")

if answer_1!="pentagon":
    print("You could not do it; Your Fired!")
    end()
    #if answer is worng this code will run and end the game
if answer_1=="pentagon":
    print("Stage Two: Find the Backdoor")
    print("You made it past the wall but now you need to find a backdoor into the evil hackers network.")
    print("Wow another riddle!")
    #if answer is right this code wil run and move on to the next question that will take another input
    answer_2=input("I drift forever with the current down these long canals they've made.Tame, yet wild, I run elusive, multitasking to your aid.Before I came, the world was darker. Colder, sometimes, rougher, true.But though I might make living easy, I'm good at killing people too. What am I?")
if answer_2!="electricity":
    print("Fatal Error................Computer Crash")
    print("!@#$%^&*()[]{}\|;:'/?.><,`~")
    end()
    #if answer is worng this code will run and end the game
if answer_2=="electricity":
    print("Stage Three: Plant The Bug")
    print("To scan all the files you need to inplant the bug but you must start it with the secreet activation code.")
    print("To get the code slove this....")
    print("a+a+a=60 a+b+b=30 b-c+c=3 c+(a*b)=code")
     #if answer is right this code wil run and move on to the next question that will take another input
    answer_3=input("The code is?")
if answer_3!="101":
    print("self destruct initiated")
    z =5
    while (z > 0):
        print(f"{z}....")
        z=z-1
    print ("Good bye!")
    end()
    #if answer is worng this code will run and end the game
    #count down loop from 5 to 0
if answer_3=="101":
    print("Stage Four: Find The Suspect")
    print("The bug gets you a sketchy looking file but it has a complicated incription.")
    print("You will have to solve for ? using 2,3,4,5,6,7 and it must equal 15 both up and down.")
    print("-------|   4  |------")
    print("|   #  |   #  |  #  |")
    print("       |   ?  |")
    print("       |   #  |")
    answer_4=input("What is the vaule of ?")
if answer_4=="4"or"7"or"5":
    print("STOP RIGHT THERE!!!")
    print("You thought you could hack me?")
    print(f"Well I know who you are {code_name} or should I say {name}")
    print("I will find you and I will kill you!!!")
    end()
    #if answer is worng this code will run and end the game
if answer_4=="3"or"6"or"2":
    print:("You open the file and you find out the hacker is a Russian Spy called Vlad and he stole top secret nuclear lanch codes.")
    print:("You must get this information back to the FBI but you must exit the network the right way.")
    print("Stage Five: Safe Exstration")
    #if answer is right this code wil run and move on to the next question that will take another input
    answer_5=input("You must type the aphabet backwards!")
if answer_5!="zyxwvutsrqponmlkjihgfedcba":
    print("You were so close but you lose the files and Vald gets away.")
    end()
    #if answer is worng this code will run and end the game
if answer_5=="zyxwvutsrqponmlkjihgfedcba":
    print("CONGRATS YOU WON AND SAVED THE DAY!!!")
    print("You got a promation and Vald got thrown in jail.")
    #wining end of game
space()
space()
space()
print("I hope you enjoyed my game.")





