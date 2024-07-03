from tkinter import *


def abc(id):
    print(id)


def select(event):
    evWidget = event.widget
    value = evWidget["text"]

    if value == correctAnswer[0]:
        questionArea.delete(1.0, END)
        questionArea.insert(END, question[1])
        optionOneButton.config(text=optionOne[1],command=lambda: abc(optionOne[1]))
        optionTwoButton.config(text=optionTwo[1],command=lambda: abc(optionTwo[1]))
        optionThreeButton.config(text=optionThree[1],command=lambda: abc(optionThree[1]))
        optionFourButton.config(text=optionFour[1],command=lambda: abc(optionFour[1]))

# QUESTIONS


question = [
    "What is the capital city of Australia?",
    "What is the chemical symbol for Gold?",
    "In what year was the first iPhone released?"
]

optionOne = [
    'Brisbane',
    'Gd',
    '2005'
]

optionTwo = [
    'Canberra',
    'Go',
    '2006'
]

optionThree = [
    'Melbourne',
    'Ag',
    '2007'
]

optionFour = [
    'Sydney',
    'Au',
    '2008'
]

correctAnswer = [
    'Canberra',
    'Au',
    '2007'
]

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

questionArea.insert(END, question[0])

aLabel = Label(bottomLeftFrame, text="A: ", bg="black", font=('arial', 14, 'bold'), fg="white")
aLabel.place(x=55, y=110)
optionOneButton = Button(bottomLeftFrame, text=optionOne[0], bg="black", font=('arial', 14, 'bold'), fg="white", bd=0,
                         activebackground='black', activeforeground='white', cursor='hand2')
optionOneButton.place(x=80, y=107)

bLabel = Label(bottomLeftFrame, text="B: ", bg="black", font=('arial', 14, 'bold'), fg="white")
bLabel.place(x=335, y=110)
optionTwoButton = Button(bottomLeftFrame, text=optionTwo[0], bg="black", font=('arial', 14, 'bold'), fg="white", bd=0,
                         activebackground='black', activeforeground='white', cursor='hand2')
optionTwoButton.place(x=360, y=107)

cLabel = Label(bottomLeftFrame, text="C: ", bg="black", font=('arial', 14, 'bold'), fg="white")
cLabel.place(x=55, y=190)
optionThreeButton = Button(bottomLeftFrame, text=optionThree[0], bg="black", font=('arial', 14, 'bold'), fg="white",
                           bd=0,
                           activebackground='black', activeforeground='white', cursor='hand2')
optionThreeButton.place(x=80, y=187)

dLabel = Label(bottomLeftFrame, text="D: ", bg="black", font=('arial', 14, 'bold'), fg="white")
dLabel.place(x=335, y=190)
optionFourButton = Button(bottomLeftFrame, text=optionFour[0], bg="black", font=('arial', 14, 'bold'), fg="white", bd=0,
                          activebackground='black', activeforeground='white', cursor='hand2')
optionFourButton.place(x=360, y=187)

optionOneButton.bind('<Button-1>', select)
optionTwoButton.bind('<Button-1>', select)
optionThreeButton.bind('<Button-1>', select)
optionFourButton.bind('<Button-1>', select)

rightFrame = Frame(root)
rightFrame.grid(row=0, column=1)

amountImage = PhotoImage(file="images/Picture0.png")

amountLabel = Label(rightFrame, image=amountImage, bg="black")
amountLabel.grid(row=0, column=0)

root.mainloop()
