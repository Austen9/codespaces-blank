print("hi i'm a chatbot!")

name= input('what is your name')

age = input('hello '+ name + ', how old are you' )
ageconfirm = input('your current age is:' +age+"is this correct? (Y/N)")

def ageconfirmer():
    ageconfirm = input('your current age is: '+age+" is this correct? (Y/N)")
    return ageconfirm

active = True

while active:

    if ageconfirm == 'Y':
        menusel = input("how may i assist you today? \n 1. how old will i be in 5 years \n 2. how many letters are within my name  " )
        if menusel == '1':
            agecalc = int(age) + 5
            print(f"you'll be "+str(agecalc)+" in 5 years." )
            active = False
        else:
            lcount=len(name)
            print(lcount)
                
    elif ageconfirm == 'N':

        ac = ageconfirm()