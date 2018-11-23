import random

print("paper rock scissors 1.00\n")

vyber =["paper", "rock", "scissors","paper", "rock", "scissors",]
hrac = 0
PC = 0
win  = 0
_error_ = True


vyhra = input("Points for win >>>")
while _error_ is True:
    try:
        int(vyhra)
        _error_ = False
    except:
        print("Only numbers ! ")
        vyhra = input("Points for win >>>")
        _error_ = True
while int(vyhra) == 0:
    print("Why you wasting time ? :(")
    vyhra = input("Points for win >>>")


while win ==0:
    r = random.choice(vyber)
    a = input(">>>")

    while a.lower() not in vyber:
        print("invalid syntax")
        a = input(">>>")

    pap = "paper"
    kam = "rock"
    nuz = "scissors"

    print(r)

    if r == a:
        print("draw:/")
    if  r == pap and a == kam:
        print("I win :)")
        PC = PC +1
        print(str(PC) +":" + str(hrac))

    if r == pap and a == nuz:
        print("you win :( ")
        hrac = hrac + 1
        print(str(PC) + ":" + str(hrac))

    if r == nuz and a == pap:
        print("I win :)")
        PC = PC + 1
        print(str(PC) + ":" + str(hrac))

    if r == nuz and a == kam:
        print("you win ")
        hrac = hrac + 1
        print(str(PC) + ":" + str(hrac))

    if r == kam and a == nuz:
        print("I win :)")
        PC = PC + 1
        print(str(PC) + ":" + str(hrac))

    if r == kam and a == pap:
        print("you win ")
        hrac = hrac + 1
        print(str(PC) + ":" + str(hrac))

    if PC == int(vyhra):
        win = vyhra
        print("I beat you :)")

    if hrac == int(vyhra):
        win= vyhra
        print("You beat me :(")

input("end ?")