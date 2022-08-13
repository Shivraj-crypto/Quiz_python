import sys
print("**************** Quiz Application ****************")
print("The Ultimate Naruto Quiz")
def q1_1():
    Score = 0
    qi = input("Q1) Which of these is another word for ninja?\n1)Genjutsu\n2)Shinobi\n3)Arigato\n4)Gelato\n: ")
    match qi:
        case "2":
            Score += 1
        case "1" | "3" | "4":
            Score += 0
        case _:
            print(qi,"is Invalid value, Please enter numeric value from 1 to 4")
            q1_1()
    return Score
def q2():
    Score = 0
    qi = input("Q2) What is the name of Kakashi's smallest Ninken??\n1)Urushi\n2)Shiba\n3)Pakkun\n4)Bisuke\n: ")
    match qi:
        case "3":
            Score += 1
        case "1" | "2" | "4":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q2()
    return Score
def q3():
    Score = 0
    qi = input("Q3) How old was Naruto in the original Naruto???\n1)10\n2)11\n3)12\n4)17\n: ")
    match qi:
        case "2":
            Score += 1
        case "1" | "3" | "4":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q3()
    return Score
def q4():
    Score = 0
    qi = input("Q4) Who is terrified of Toads??\n1)Shino\n2)Sakura\n3)Naruto\n4)Kiba Inuzuka\n: ")
    match qi:
        case "2":
            Score += 1
        case "1" |"3" | "4":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q4()
    return Score
def q5():
    Score = 0
    qi = input("Q5)Whose hobby is pressing flowers?\n1)Kushina\n2)Temari\n3)Hinata\n4)Kurenai\n: ")
    match qi:
        case "4":
            Score += 1
        case "1" | "3" | "2":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q5()
    return Score
def q6():
    Score = 0
    qi = input(
        "Q6)Who else has the same ability as Kakashi to create lightning with the hand?\n1)Kakuzu\n2)Indra\n3)Naruto\n4)Sakura\n: ")
    match qi:
        case "2":
            Score += 1
        case "1" | "3" | "4":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q6()
    return Score
def q7():
    Score = 0
    qi = input("Q7) Which one is not a member of Team Kurenai?\n1)kibha\n2)shino\n3)hinata\n4)naruto\n: ")
    match qi:
        case "4":
            Score += 1
        case "1" | "3" | "2":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q7()
    return Score
def q8():
    Score = 0
    qi = input(
        "Q8) What is Naruto's catchphrase?\n1)Believe it!\n2)Fool, you fool.\n3)Sorry, I'm late.\n4)What a drag.\n: ")
    match qi:
        case "1":
            Score += 1
        case "2" | "3" | "4":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q8()
    return Score
def q9():
    Score = 0
    qi = input("Q9) Who was the youngest ninja graduate from the academy?\n1)Rin\n2)Obito\n3)Kakashi\n4)Itachi\n: ")
    match qi:
        case "3":
            Score += 1
        case "1" | "2" | "4":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q9()
    return Score
def q10():
    Score = 0
    qi = input("Q10) What is Boruto's favorite food?\n1)Ramen\n2)BBQ\n3)Sushi\n4)Yakisoba Bun\n: ")
    match qi:
        case "4":
            Score += 1
        case "1" | "3" | "2":
            Score += 0
        case _:
            print(qi, "is Invalid value, Please enter numeric value from 1 to 4")
            q10()
    return Score
def numf():
    Score = q1_1() + q2() + q3() + q4() + q5() + q6() + q7() + q8() + q9() + q10()
    endm(Score)
def endm(sc):
    if (sc < 5):
        print("*/*/*/*/*/*/*/* Your score is ", sc, "Better luck next time!! */*/*/*/*/*/*/*/*/*/*/")
        ch = int(input("Enter 1 to play again \nEnter 2 to exit\n: "))
        match ch:
            case 1:
                numf()
            case 2:
                sys.exit()
    else:
        print("*/*/*/*/*/*//*/*/*/ Your score is ", sc, "Excellent! */*/*/*/*/*//*/*/*/*/*/*")
        ch = int(input("Enter 1 to play again \nEnter 2 to exit\n: "))
        match ch:
            case 1:
                numf()
            case 2:
                sys.exit()
numf()