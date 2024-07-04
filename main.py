from tkinter import *
from random import randint

# VARIABLES
global id, questionArea
lang = 'en'
selectedIds = []

if lang == "en":
    questionArray = [
        {
            'question': 'What is the capital city of Australia?',
            'a': 'Brisbane',
            'b': 'Canberra',
            'c': 'Melbourne',
            'd': 'Sydney',
            'correct': 'Canberra'
        },
        {
            'question': 'What is the chemical symbol for Gold?',
            'a': 'Ag',
            'b': 'Gd',
            'c': 'Go',
            'd': 'Au',
            'correct': 'Au'
        },
        {
            'question': 'In what year was the first iPhone released?',
            'a': '2005',
            'b': '2006',
            'c': '2007',
            'd': '2008',
            'correct': '2007'
        }
    ]
else:
    questionArray = [
        {
            'question': 'ඕස්ට්‍රේලියාවේ අගනුවර කුමක්ද?',
            'a': 'බ්‍රිස්බේන්',
            'b': 'කැන්බරා',
            'c': 'මෙල්බර්න්',
            'd': 'සිඩ්නි',
            'correct': 'කැන්බරා'
        },
        {
            'question': 'රන් සඳහා රසායනික සංකේතය කුමක්ද?',
            'a': 'Ag',
            'b': 'Gd',
            'c': 'Go',
            'd': 'Au',
            'correct': 'Au'
        },
        {
            'question': 'පළමු iPhone නිකුත් කළ කුමන වසරේද?',
            'a': '2005',
            'b': '2006',
            'c': '2007',
            'd': '2008',
            'correct': '2007'
        }
    ]


def addQuestion(questionId, answer):
    print(questionId, answer)

    def won():
        wonWindow = Toplevel()
        wonWindow.overrideredirect(True)
        wonWindow.config(bg="black", bd=0)
        wonWindow.geometry("500x400+100+100")
        imgLabel = Label(wonWindow, image=imageMiddle, bg="black")
        imgLabel.pack(pady=30)

        correctAnswerLabel = Label(wonWindow, text="Congratulations", font=('arial', 14, 'bold'), background='black',
                                   foreground='yellow')
        correctAnswerLabel.pack()
        loseLabel = Label(wonWindow, text="You Won.", font=('arial', 20, 'bold'), background='black',
                          foreground='white')
        loseLabel.place(x=180, y=270)
        tryAgainButton = Button(wonWindow, font=('arial', 15, 'bold'), text='Try Again', background="black", bd=0,
                                foreground="white",
                                activebackground='black', activeforeground='white',
                                command=lambda: tryAgain(wonWindow))
        tryAgainButton.place(x=190, y=300)
        exitButton = Button(wonWindow, font=('arial', 15, 'bold'), text='Exit', background="black", bd=0,
                            foreground="white",
                            activebackground='black', activeforeground='white', command=lambda: exit(wonWindow))
        exitButton.place(x=215, y=330)
        happyLabel = Label(wonWindow, image=happyImage, bg='black', bd=0)
        happyLabel.place(x=60, y=280)
        happyLabel1 = Label(wonWindow, image=happyImage, bg='black', bd=0)
        happyLabel1.place(x=360, y=280)

    def showQuestion():
        print('showQuestion')
        isNotAdded = True
        while isNotAdded:
            id = randint(0, len(questionArray) - 1)
            if id not in selectedIds:
                selectedIds.append(id)
                isNotAdded = False

        questionArea.delete(1.0, END)
        questionArea.insert(END, questionArray[id]['question'])
        optionOneButton.config(text=questionArray[id]['a'],
                               command=lambda: addQuestion(questionId=id, answer=questionArray[id]['a']))
        optionTwoButton.config(text=questionArray[id]['b'],
                               command=lambda: addQuestion(questionId=id, answer=questionArray[id]['b']))
        optionThreeButton.config(text=questionArray[id]['c'],
                                 command=lambda: addQuestion(questionId=id, answer=questionArray[id]['c']))
        optionFourButton.config(text=questionArray[id]['d'],
                                command=lambda: addQuestion(questionId=id, answer=questionArray[id]['d']))
        amountLabel.config(image=amountImageArray[len(selectedIds) - 1])
        print(selectedIds)

    def tryAgain(window):
        selectedIds.clear()
        window.destroy()
        addQuestion(questionId="", answer="")

    def exit(widow):
        widow.destroy()
        root.destroy()

    def fail(questionId):
        failWindow = Toplevel()
        failWindow.overrideredirect(True)
        failWindow.config(bg="black", bd=0)
        failWindow.geometry("500x400+100+100")
        imgLabel = Label(failWindow, image=imageMiddle, bg="black")
        imgLabel.pack(pady=30)

        correctAnswer = questionArray[questionId]['correct']

        correctAnswerLabel = Label(failWindow, text=correctAnswer, font=('arial', 14, 'bold'), background='black',
                                   foreground='yellow')
        correctAnswerLabel.pack()
        loseLabel = Label(failWindow, text="You Lose.", font=('arial', 20, 'bold'), background='black',
                          foreground='white')
        loseLabel.place(x=180, y=270)
        tryAgainButton = Button(failWindow, font=('arial', 15, 'bold'), text='Try Again', background="black", bd=0,
                                foreground="white",
                                activebackground='black', activeforeground='white',
                                command=lambda: tryAgain(failWindow))
        tryAgainButton.place(x=190, y=300)
        exitButton = Button(failWindow, font=('arial', 15, 'bold'), text='Exit', background="black", bd=0,
                            foreground="white",
                            activebackground='black', activeforeground='white', command=lambda: exit(failWindow))
        exitButton.place(x=215, y=330)
        sadLabel = Label(failWindow, image=sadImage, bg='black', bd=0)
        sadLabel.place(x=60, y=280)
        sadLabel1 = Label(failWindow, image=sadImage, bg='black', bd=0)
        sadLabel1.place(x=360, y=280)

    if questionId == "":
        # FIRST QUESTION
        showQuestion()
    else:
        if questionArray[questionId]['correct'] == answer:
            print('correct answer')
            if len(selectedIds) != 3:
                showQuestion()
            else:
                won()
        else:
            print("wrong answer")
            fail(questionId)


root = Tk()

root.geometry("1000x600+0+0")
root.resizable(False, False)
root.title("who wants to be a millionaire")

root.config(background="black")

leftFrame = Frame(root, bg='black')
leftFrame.grid(row=0, column=0)

topLeftFrame = Frame(leftFrame, padx=10, bg="black")
topLeftFrame.grid(row=0, column=0)

middleLeftFrame = Frame(leftFrame, bg="black")
middleLeftFrame.grid(row=1, column=0)

bottomLeftFrame = Frame(leftFrame, bg="black")
bottomLeftFrame.grid(row=2, column=0)

image50 = PhotoImage(file="images/50-50.png")

lifeLine50Button = Button(topLeftFrame, image=image50, background="black", bd=0, activebackground="black", width=170,
                          height=75)
lifeLine50Button.grid(row=0, column=0)

imageAudiencePole = PhotoImage(file="images/audiencePole.png")

lifeLineAudienceButton = Button(topLeftFrame, image=imageAudiencePole, background="black", bd=0,
                                activebackground="black", width=170, height=75)
lifeLineAudienceButton.grid(row=0, column=1)

imageCaller = PhotoImage(file="images/phoneAFriend.png")

lifeLineCallButton = Button(topLeftFrame, image=imageCaller, background="black", bd=0, activebackground="black",
                            width=170, height=75)
lifeLineCallButton.grid(row=0, column=2)

imageMiddle = PhotoImage(file="images/center.png")

middleLabel = Label(middleLeftFrame, image=imageMiddle, bg="black", height=250)
middleLabel.grid(row=0, column=0)

imageLayout = PhotoImage(file="images/lay.png")

layoutLabel = Label(bottomLeftFrame, image=imageLayout, bg="black")
layoutLabel.grid(row=0, column=0)

questionArea = Text(bottomLeftFrame, font=('arial', 16, 'bold'), bg='black', fg='white', width=35, height=2,
                    wrap='word', bd=0)
questionArea.place(x=70, y=10)

# questionArea.insert(END, question[0])

aLabel = Label(bottomLeftFrame, text="A: ", bg="black", font=('arial', 14, 'bold'), fg="white")
aLabel.place(x=55, y=110)
optionOneButton = Button(bottomLeftFrame, bg="black", font=('arial', 14, 'bold'), fg="white", bd=0,
                         activebackground='black', activeforeground='white', cursor='hand2')
optionOneButton.place(x=80, y=107)

bLabel = Label(bottomLeftFrame, text="B: ", bg="black", font=('arial', 14, 'bold'), fg="white")
bLabel.place(x=335, y=110)
optionTwoButton = Button(bottomLeftFrame, bg="black", font=('arial', 14, 'bold'), fg="white", bd=0,
                         activebackground='black', activeforeground='white', cursor='hand2')
optionTwoButton.place(x=360, y=107)

cLabel = Label(bottomLeftFrame, text="C: ", bg="black", font=('arial', 14, 'bold'), fg="white")
cLabel.place(x=55, y=190)
optionThreeButton = Button(bottomLeftFrame, bg="black", font=('arial', 14, 'bold'), fg="white",
                           bd=0,
                           activebackground='black', activeforeground='white', cursor='hand2')
optionThreeButton.place(x=80, y=187)

dLabel = Label(bottomLeftFrame, text="D: ", bg="black", font=('arial', 14, 'bold'), fg="white")
dLabel.place(x=335, y=190)
optionFourButton = Button(bottomLeftFrame, bg="black", font=('arial', 14, 'bold'), fg="white", bd=0,
                          activebackground='black', activeforeground='white', cursor='hand2')
optionFourButton.place(x=360, y=187)

rightFrame = Frame(root)
rightFrame.grid(row=0, column=1)

amountImage0 = PhotoImage(file="images/Picture0.png")
amountImage1 = PhotoImage(file="images/Picture1.png")
amountImage2 = PhotoImage(file="images/Picture2.png")
amountImage3 = PhotoImage(file="images/Picture3.png")
amountImage4 = PhotoImage(file="images/Picture4.png")
amountImage5 = PhotoImage(file="images/Picture5.png")
amountImage6 = PhotoImage(file="images/Picture6.png")
amountImage7 = PhotoImage(file="images/Picture7.png")
amountImage8 = PhotoImage(file="images/Picture8.png")
amountImage9 = PhotoImage(file="images/Picture9.png")
amountImage10 = PhotoImage(file="images/Picture10.png")
amountImage11 = PhotoImage(file="images/Picture11.png")
amountImage12 = PhotoImage(file="images/Picture12.png")
amountImage13 = PhotoImage(file="images/Picture13.png")
amountImage14 = PhotoImage(file="images/Picture14.png")
amountImage15 = PhotoImage(file="images/Picture15.png")

# SAD AND HAPPY IMAGES
happyImage = PhotoImage(file="images/happy.png")
sadImage = PhotoImage(file="images/sad.png")

amountImageArray = [
    amountImage0,
    amountImage1,
    amountImage2,
    amountImage3,
    amountImage4,
    amountImage5,
    amountImage6,
    amountImage7,
    amountImage8,
    amountImage9,
    amountImage10,
    amountImage11,
    amountImage12,
    amountImage13,
    amountImage14,
    amountImage15
]

amountLabel = Label(rightFrame, bg="black")
amountLabel.grid(row=0, column=0)

# ADD FIRST QUESTION
addQuestion(questionId="", answer="")

root.mainloop()
