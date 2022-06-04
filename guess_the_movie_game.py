import random
from sre_parse import State
from tkinter import *
from customtkinter import *

# Modes: "System" (standard), "Dark", "Light"
set_appearance_mode("dark")
# Themes: "blue" (standard), "green", "dark-blue"
set_default_color_theme("blue")

root = CTk()
root.geometry("1200x700")
root.title("GUESS THE MOVIE GAME BY ROHAN MOJUMDER :).py")


def unlockCharacter(chosenChar, question):
    temp = []
    # converting the characters to *  except the chosen character and store in list
    for i in question:
        if i in chosenChar:
            temp.append(i)
        elif i == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    # converted * string
    newStr = "".join(str(x) for x in temp)
    return newStr


def createQuestion(question):
    temp = []
    # converting the characters to * and store in list
    for i in question:
        if i == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    # converted * string
    newStr = "".join(str(x) for x in temp)
    return newStr


def movie():
    global scoreVal  # score variable
    global score  # score
    global scValue  # display variable
    global subStr  # choice variable
    global question  # original movie name
    global statusVar  # status variable
    # global chances          #   total chances
    global chanceVal  # chances variable
    global ques  # hidden question variable
    global statusOpt  # option variable
    global ansVar  # answer area
    global ans  # fetching the answer of the player
    global label
    global label2

    movies_list = ['war', 'drishyam', 'avengers', 'avengers endgame', 'thor', '1917', 'commando', 'harry potter deadly hallows', 'sultan', 'dhoom', 'spiderman far from home', 'avengers infinity war', 'spiderman no way home', 'avatar',
                   'doctor strange', 'doctor strange the multiverse of madness', 'jaws', 'doraemon and the steel troops the new age', 'star wars the last jedi', 'fifty shades of grey', 'bhool bhoolaiya', 'sooryavanshi', 'the family man', 'omg oh my god', '1920']

    # choosing an item from list randomly
    question = random.choice(movies_list)
    # creating question
    ques = createQuestion(question)
    scValue.set(f'{ques}')

    b.configure(state=DISABLED)
    screenChoice.configure(state=NORMAL)

    ansVar.set('')
    ansArea.update()

    subStr.set('')
    screenChoice.update()

    label['text'] = "Choose either from 'a - z' or from '0 - 9':"
    label2['text'] = ""

    choose = ''
    chances = 6
    chosenChar = []
    statusVar.set('START GUESSING')
    screenStatus.update()
    status = True
    while status:
        while chances >= 0:
            if chances == 6:
                chanceVal.set(chances)
                screenChances.update()

            elif chances > 0:
                chanceVal.set(chances)
                screenChances.update()

            elif chances == -1:
                break

            else:
                chanceVal.set(chances)
                screenChances.update()

                scValue.set('')
                screenDisplay.update()

                ansVar.set(question)
                ansArea.update()
                ansArea.configure(state=DISABLED)

                screenChoice.configure(state=DISABLED)

                label2['text'] = 'FOLLOW THE ABOVE INSTRUCTIONS'
                b.configure(state=NORMAL)

                statusOpt.set(f'Original answer: {question}')
                screenOption.update()

                statusVar.set('BETTER LUCK NEXT TIME !')
                screenStatus.update()
                status = False
                break

            cond = True
            while cond:
                statusOpt.set('Choose either an alphabet or an integer')
                screenOption.update()

                b.wait_variable(subStr)
                choose = subStr.get()

                statusOpt.set(f'Chosen Character: {choose}')
                screenOption.update()

                if len(choose) == 1:
                    subStr.set('')
                    screenChoice.update()
                    cond = False
                else:
                    subStr.set('')
                    screenChoice.update()

            if choose in question:
                statusVar.set(f'Chosen: {choose}. Right Choice !')
                screenStatus.update()

                subStr.set('')
                screenChoice.update()

                chosenChar.append(choose)
                ques = unlockCharacter(chosenChar, question)
                scValue.set(ques)
                screenDisplay.update()

                opt = True
                while opt:
                    try:
                        label['text'] = "FOLLOW THE 'OPTIONS AVAILABLE'"
                        statusOpt.set(
                            'Press: 0 to guess the answer || 1 to choose another character || 2 to quit:')
                        screenOption.update()
                        b.wait_variable(subStr)
                        choice = int(subStr.get())
                    except:
                        statusVar.set(f'Chosen: {subStr.get()}. INVALID !')
                        subStr.set('')
                        screenChoice.update()
                    else:
                        statusOpt.set(f'Chosen Character: {choice}')
                        screenOption.update()

                        if choice == 0:
                            statusVar.set(
                                "Don't rush! Follow the above instructions")
                            screenStatus.update()

                            textArea['text'] = '1. Write the answer in the answer textfield\n2. Copy whole answer by clicking "Ctrl+A" and "Ctrl+P"\n3. Paste the answer in the above textfield by clicking "Ctrl+V"'

                            label['text'] = "Don't rush! Follow the above instructions"

                            statusOpt.set('Your answer:')
                            screenOption.update()

                            subStr.set('')
                            screenChoice.update()

                            ansArea.configure(state=NORMAL)
                            b.wait_variable(subStr)
                            ans = ansVar.get()

                            ansArea.configure(state=DISABLED)
                            ansVar.set('')
                            ansArea.update()

                            statusOpt.set(f'Answer Written: {ans}')
                            screenOption.update()

                            if ans == question:
                                statusVar.set('Correct !')
                                screenStatus.update()

                                label['text'] = 'CORRECT CHOICE ! SCORE INCREASED'

                                subStr.set("CORRECT CHOICE !")
                                screenChoice.configure(state=DISABLED)
                                screenChoice.update()

                                chanceVal.set(0)
                                screenChances.update()

                                ansVar.set(ans)
                                ansArea.update()

                                score += 1
                                scoreVal.set(score)
                                screenScore.update()

                                textArea['text'] = 'To play another game, click the "START GAME" button (SCORE WILL REMAIN SAME, MOVIE NAME WILL CHANGE).\n\nTo EXIT, Click "FILE" in menubar, select "EXIT"'
                                b.configure(state=NORMAL)

                                label2['text'] = "FOLLOW THE ABOVE INSTRUCTIONS"

                                status = False
                                opt = False
                                chances = -1
                            else:
                                statusVar.set('WRONG ANSWER !')
                                screenStatus.update()

                                label['text'] = 'BETTER LUCK NEXT TIME !'

                                screenChoice.configure(state=DISABLED)
                                subStr.set('')
                                screenChoice.update()

                                chanceVal.set(0)
                                screenChances.update()

                                ansVar.set(question)
                                ansArea.update()

                                statusOpt.set(f'Original answer: {question}')
                                screenOption.update()

                                textArea[
                                    'text'] = 'To play another game, click the "START GAME" button (SCORE WILL REMAIN SAME).\n\nTo quit, Click "FILE" in menubar, select "QUIT"'
                                b.configure(state=NORMAL)

                                label2['text'] = "FOLLOW THE ABOVE INSTRUCTIONS"

                                chances = -1
                                status = False
                                opt = False

                        elif choice == 1:
                            statusOpt.set('Choose another character:')
                            screenOption.update()

                            statusVar.set('')
                            screenStatus.update()

                            subStr.set('')
                            screenChoice.update()

                            opt = False
                            chances -= 1

                        elif choice == 2:
                            statusVar.set('BETTER LUCK NEXT TIME !')
                            screenStatus.update()

                            screenChoice.configure(state=DISABLED)
                            screenChoice.update()

                            chanceVal.set(0)
                            screenChances.update()

                            ansVar.set(question)
                            ansArea.update()

                            statusOpt.set(f'Original answer: {question}')
                            screenOption.update()

                            subStr.set('')
                            screenChoice.update()

                            label['text'] = "FOLLOW THE ABOVE INSTRUCTIONS"

                            textArea[
                                'text'] = 'To play another game, click the "START GAME" button (SCORE WILL REMAIN SAME).\n\nTo quit, Click "FILE" in menubar, select "QUIT"'
                            b.configure(state=NORMAL)

                            label2['text'] = "FOLLOW THE ABOVE INSTRUCTIONS"

                            status = False
                            opt = False
                            chances = 0

                        else:
                            statusVar.set('Choose a Valid Option:')
                            screenChoice.update()

                            subStr.set('')
                            screenChoice.update()

            else:
                if chances > 1:
                    statusVar.set(f'Chosen: {choose}. WRONG CHOICE, TRY AGAIN')
                    screenStatus.update()

                subStr.set('')
                screenChoice.update()

                chances -= 1


'''-------------------- DISPLAY QUESTION FRAME --------------------'''

scValue = StringVar()
scValue.set('')

# entry_1 = CTkEntry(master=frame_1, placeholder_text="CTkEntry")
# entry_1.pack(pady=12, padx=10)

screenDisplay = CTkEntry(master=root, height=60, text_font=(
    'Roboto Medium', 30, 'bold'), border_color='#33ccff', textvariable=scValue, state=DISABLED)
# ipad --> internal padding
screenDisplay.pack(fill=X, padx=10, pady=10)

'''-------------------- INSTRUCTION FRAME --------------------'''


f = CTkFrame(master=root)
# instruction label
l = CTkLabel(
    master=f, text='INSTRUCTIONS:', text_font=('Roboto Medium', 20, 'bold'))
l.pack(side=LEFT, padx=10)

# instruction textfield
insValue = StringVar()
insValue.set("")
textArea = CTkLabel(master=f, height=5, text="1. Players needs to guess the movie name.\n2. Player can only choose a single character or an integer at a time.\n3. Player will get 1 point for guessing correct movie.\n4. Player will get only 6 chances.",
                    text_color='yellow', text_font=('Roboto Medium', 15, 'italic'))
textArea.pack(ipadx=10, ipady=10)
f.pack(fill=X, anchor='w', padx=10)


'''-------------------- ANSWER STATUS --------------------'''


f4 = CTkFrame(master=root)
# status label
l = CTkLabel(
    master=f4, text='STATUS:', text_font=('Roboto Medium', 20, 'bold'))
l.pack(side=LEFT, padx=10, pady=5)

# status textfield
statusVar = StringVar()
statusVar.set('PRESS START BUTTON TO BEGIN')

screenStatus = CTkEntry(master=f4, width=10, textvariable=statusVar, text_font=(
    'Roboto Medium', 15, 'bold'), border_color='#33ccff', state=DISABLED)
screenStatus.pack(fill=X, ipadx=8, padx=10, pady=10)

f4.pack(anchor='w', padx=10, fill=X)

'''-------------------- OPTION STATUS --------------------'''

f6 = CTkFrame(master=root)
# status label
l = CTkLabel(master=f6, text='OPTIONS AVAILABLE:',
             text_font=('ROBOTO MEDIUM', 20, 'bold'))
l.pack(side=LEFT, padx=10, pady=5)

# status textfield
statusOpt = StringVar()
statusOpt.set('')
screenOption = CTkEntry(master=f6, width=60, textvariable=statusOpt, text_font=(
    'Roboto Medium', 15, 'bold'), border_color='#33ccff', state=DISABLED)
screenOption.pack(ipadx=8, padx=10, pady=10, fill=X)
f6.pack(anchor='w', padx=10, fill=X)

'''-------------------- CHANCES LEFT --------------------'''

f5 = CTkFrame(master=root)
# chances label
l = CTkLabel(master=f5, text='CHANCES LEFT:',
             text_font=('Roboto Medium', 20, 'bold'))
l.pack(side=LEFT, padx=10, pady=5)

# chances textfield
chanceVal = IntVar()
chanceVal.set('')

screenChances = CTkEntry(master=f5, width=60, textvariable=chanceVal, text_font=(
    'Roboto Medium', 15, 'bold'), border_color='#33ccff', state=DISABLED)
screenChances.pack(ipadx=8, padx=10, pady=10, fill=X)

f5.pack(anchor='w', padx=10)


'''-------------------- ENTER CHOICE --------------------'''
label = CTkLabel(text="", text_font=('Roboto Medium', 12, 'bold'))
label.pack()
f3 = CTkFrame(master=root)

l2 = CTkLabel(master=f3, text='YOUR CHOICE:',
              text_font=('Roboto Medium', 20, 'bold'))
l2.pack(side=LEFT, padx=10, pady=5)

# enter your answer
subStr = StringVar()
subStr.set('')
screenChoice = CTkEntry(master=f3, height=40, width=300, textvariable=subStr, text_font=(
    'Roboto Medium', 20, 'bold'), border_color='#33ccff', state=DISABLED)
screenChoice.pack(ipadx=8, padx=10, pady=10)

f3.pack()

'''-------------------- ANSWER AREA --------------------'''

f7 = CTkFrame(master=root)
la = CTkLabel(master=f7, text='ANSWER:',
              text_font=('Roboto Medium', 20, 'bold'))
la.pack(side=LEFT, padx=10, pady=5)

# status textfield
ansVar = StringVar()
ansVar.set('')
ansArea = CTkEntry(f7, width=45, height=40, textvariable=ansVar, text_font=(
    'Roboto Medium', 20, 'bold'), border_color='#33ccff', state=DISABLED)
ansArea.pack(ipadx=8, padx=10, pady=10, fill=X)
f7.pack(anchor='w', padx=10, pady=2, fill=X)


'''-------------------- SCORE FRAME --------------------'''
f2 = CTkFrame(master=root)
l = CTkLabel(master=f2, height=40, text='SCORE:',
             text_font=('Roboto Medium', 20, 'bold'))
l.pack(side=LEFT, padx=10, pady=5)

scoreVal = IntVar()
score = 0
scoreVal.set(score)
screenScore = CTkEntry(master=f2, height=40, textvariable=scoreVal, text_font=(
    'Roboto Medium', 20, 'bold'), border_color='#33ccff', state=DISABLED)
screenScore.pack(ipadx=8, padx=10, pady=10)
f2.pack(anchor='w', pady=10, padx=10)


''' --------- BUTTON --------- '''

f8 = CTkFrame(master=root)
label2 = CTkLabel(f8, text='PRESS THE BUTTON BELOW TO START GAME',
                  text_font=('ROBOTO MEDIUM', 10, 'bold'))
label2.pack()
b = CTkButton(f8, text='START GAME', text_font=(
    'Roboto Medium', 15, 'bold'), command=movie)
b.configure(state=NORMAL)
b.pack()
f8.pack(ipady=2)


''' -------------------- MENU -------------------- '''

menuBar = Menu(root)
FileMenu = Menu(menuBar, tearoff=0)
FileMenu.add_command(label='Exit', command=quit)
menuBar.add_cascade(label='File', menu=FileMenu)
root.config(menu=menuBar)


root.mainloop()
