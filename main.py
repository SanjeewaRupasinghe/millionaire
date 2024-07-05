import time
from tkinter import *
from random import randint
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

# VARIABLES
global idValue, questionArea
lang = 'en'
selectedIds = []

if lang == "en":
    questionArray = [
        {
            "question": "What is the main ingredient in traditional paella?",
            "a": "Rice",
            "b": "Potato",
            "c": "Pasta",
            "d": "Bread",
            "correct": "Rice",
            "speak": "Rice"
        },
        {
            "question": "Which planet is closest to the sun?",
            "a": "Venus",
            "b": "Mars",
            "c": "Mercury",
            "d": "Earth",
            "correct": "Mercury",
            "speak": "Mercury"
        },
        {
            "question": "What is the largest desert in the world?",
            "a": "Sahara Desert",
            "b": "Arabian Desert",
            "c": "Gobi Desert",
            "d": "Kalahari Desert",
            "correct": "Sahara Desert",
            "speak": "Sahara Desert"
        },
        {
            "question": "Who painted the 'Starry Night'?",
            "a": "Pablo Picasso",
            "b": "Leonardo da Vinci",
            "c": "Vincent van Gogh",
            "d": "Claude Monet",
            "correct": "Vincent van Gogh",
            "speak": "Vincent van Gogh"
        },
        {
            "question": "What is the smallest bone in the human body?",
            "a": "Stapes",
            "b": "Femur",
            "c": "Tibia",
            "d": "Fibula",
            "correct": "Stapes",
            "speak": "Stapes"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "a": "Harper Lee",
            "b": "Mark Twain",
            "c": "F. Scott Fitzgerald",
            "d": "Ernest Hemingway",
            "correct": "Harper Lee",
            "speak": "Harper Lee"
        },
        {
            "question": "What is the chemical symbol for sodium?",
            "a": "Na",
            "b": "So",
            "c": "Sa",
            "d": "N",
            "correct": "Na",
            "speak": "Na"
        },
        {
            "question": "Who developed the theory of relativity?",
            "a": "Isaac Newton",
            "b": "Galileo Galilei",
            "c": "Albert Einstein",
            "d": "Niels Bohr",
            "correct": "Albert Einstein",
            "speak": "Albert Einstein"
        },
        {
            "question": "Which planet is known as the 'Blue Planet'?",
            "a": "Mars",
            "b": "Earth",
            "c": "Neptune",
            "d": "Uranus",
            "correct": "Earth",
            "speak": "Earth"
        },
        {
            "question": "What is the tallest building in the world?",
            "a": "Shanghai Tower",
            "b": "Abraj Al-Bait Clock Tower",
            "c": "Burj Khalifa",
            "d": "One World Trade Center",
            "correct": "Burj Khalifa",
            "speak": "Burj Khalifa"
        },
        {
            "question": "What is the currency of Japan?",
            "a": "Yuan",
            "b": "Won",
            "c": "Yen",
            "d": "Dollar",
            "correct": "Yen",
            "speak": "Yen"
        },
        {
            "question": "Who invented the telephone?",
            "a": "Thomas Edison",
            "b": "Nikola Tesla",
            "c": "Alexander Graham Bell",
            "d": "Guglielmo Marconi",
            "correct": "Alexander Graham Bell",
            "speak": "Alexander Graham Bell"
        },
        {
            "question": "What is the smallest country in the world?",
            "a": "Monaco",
            "b": "San Marino",
            "c": "Vatican City",
            "d": "Liechtenstein",
            "correct": "Vatican City",
            "speak": "Vatican City"
        },
        {
            "question": "Which ocean is the largest?",
            "a": "Atlantic Ocean",
            "b": "Indian Ocean",
            "c": "Arctic Ocean",
            "d": "Pacific Ocean",
            "correct": "Pacific Ocean",
            "speak": "Pacific Ocean"
        },
        {
            "question": "What is the largest island in the world?",
            "a": "Greenland",
            "b": "New Guinea",
            "c": "Borneo",
            "d": "Madagascar",
            "correct": "Greenland",
            "speak": "Greenland"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "a": "Leonardo da Vinci",
            "b": "Vincent van Gogh",
            "c": "Pablo Picasso",
            "d": "Claude Monet",
            "correct": "Leonardo da Vinci",
            "speak": "Leonardo da Vinci"
        }
    ]
else:
    questionArray = [
        {
            "question": "සාම්ප්රදායික paella හි ප්රධාන අමුද්රව්යය කුමක්ද?",
            "a": "සහල්",
            "b": "අල",
            "c": "පැස්ටා",
            "d": "පාන්",
            "correct": "සහල්",
            "speak": "sahal"
        },
        {
            "question": "සූර්යයාට සමීපතම ග්‍රහලෝකය කුමක්ද?",
            "a": "සිකුරු",
            "b": "අඟහරු",
            "c": "රසදිය",
            "d": "පොළොවේ",
            "correct": "රසදිය",
            "speak": "buda"
        },
        {
            "question": "ලෝකයේ විශාලතම කාන්තාරය කුමක්ද?",
            "a": "සහරා කාන්තාරය",
            "b": "අරාබි කාන්තාරය",
            "c": "ගෝබි කාන්තාරය",
            "d": "කලහාරි කාන්තාරය",
            "correct": "සහරා කාන්තාරය",
            "speak": "Sahara kantharaya"
        },
        {
            "question": "'තරු සහිත රාත්‍රිය' සිතුවම් කළේ කවුද?",
            "a": "පැබ්ලෝ පිකාසෝ",
            "b": "ලියනාඩෝ ඩා වින්චි",
            "c": "වින්සන්ට් වැන් ගොග්",
            "d": "ක්ලෝඩ් මොනේට්",
            "correct": "වින්සන්ට් වැන් ගොග්",
            "speak": "Vincent van Gogh"
        },
        {
            "question": "මිනිස් සිරුරේ කුඩාම අස්ථිය කුමක්ද?",
            "a": "ස්ටේප්ස්",
            "b": "Femur",
            "c": "ටිබියා",
            "d": "ෆයිබුලා",
            "correct": "ස්ටේප්ස්",
            "speak": "Stapes"
        },
        {
            "question": "'To Kill a Mockingbird' ලිව්වේ කවුද?",
            "a": "හාපර් ලී",
            "b": "මාර්ක් ට්වේන්",
            "c": "F. Scott Fitzgerald",
            "d": "අර්නස්ට් හෙමිංවේ",
            "correct": "හාපර් ලී",
            "speak": "Harper Lee"
        },
        {
            "question": "සෝඩියම් සඳහා රසායනික සංකේතය කුමක්ද?",
            "a": "නා",
            "b": "ඒ නිසා",
            "c": "සා",
            "d": "එන්",
            "correct": "නා",
            "speak": "Na"
        },
        {
            "question": "සාපේක්ෂතාවාදයේ න්යාය වර්ධනය කළේ කවුද?",
            "a": "අයිසැක් නිව්ටන්",
            "b": "ගැලීලියෝ ගැලීලි",
            "c": "ඇල්බට් අයින්ස්ටයින්",
            "d": "නීල්ස් බෝර්",
            "correct": "ඇල්බට් අයින්ස්ටයින්",
            "speak": "Albert Einstein"
        },
        {
            "question": "'නිල් ග්‍රහලෝකය' ලෙස හඳුන්වන්නේ කුමන ග්‍රහලෝකයද?",
            "a": "අඟහරු",
            "b": "පොළොවේ",
            "c": "නෙප්චූන්",
            "d": "යුරේනස්",
            "correct": "පොළොවේ",
            "speak": "pruthiwiya"
        },
        {
            "question": "ලෝකයේ උසම ගොඩනැගිල්ල කුමක්ද?",
            "a": "ෂැංහයි කුළුණ",
            "b": "Abraj Al-Bait ඔරලෝසු කණුව",
            "c": "බර්ජ් කලීෆා",
            "d": "එක් ලෝක වෙළඳ මධ්යස්ථානයක්",
            "correct": "බර්ජ් කලීෆා",
            "speak": "Burj Khalifa"
        },
        {
            "question": "ජපානයේ මුදල් ඒකකය කුමක්ද?",
            "a": "යුවාන්",
            "b": "දිනුවා",
            "c": "යෙන්",
            "d": "ඩොලර්",
            "correct": "යෙන්",
            "speak": "Yen"
        },
        {
            "question": "දුරකථනය සොයාගත්තේ කවුද?",
            "a": "තෝමස් එඩිසන්",
            "b": "නිකොලා ටෙස්ලා",
            "c": "ඇලෙක්සැන්ඩර් ග්රැහැම් බෙල්",
            "d": "ගුග්ලියෙල්මෝ මාකෝනි",
            "correct": "ඇලෙක්සැන්ඩර් ග්රැහැම් බෙල්",
            "speak": "Alexander Graham Bell"
        },
        {
            "question": "ලෝකයේ කුඩාම රට කුමක්ද?",
            "a": "මොනාකෝ",
            "b": "සැන් මරිනෝ",
            "c": "වතිකානු නගරය",
            "d": "ලිච්ටෙන්ස්ටයින්",
            "correct": "වතිකානු නගරය",
            "speak": "Vaticanu nagaraya"
        },
        {
            "question": "විශාලතම සාගරය කුමක්ද?",
            "a": "අත්ලාන්තික් සාගරය",
            "b": "ඉන්දියන් සාගරය",
            "c": "ආක්ටික් සාගරය",
            "d": "ශාන්තිකර සාගරය",
            "correct": "ශාන්තිකර සාගරය",
            "speak": "Pacific sagaraya"
        },
        {
            "question": "ලෝකයේ විශාලතම දූපත කුමක්ද?",
            "a": "ග්රීන්ලන්තය",
            "b": "නිව් ගිනියාව",
            "c": "බෝර්නියෝ",
            "d": "මැඩගස්කරය",
            "correct": "ග්රීන්ලන්තය",
            "speak": "Greenlanthaya"
        },
        {
            "question": "මොනාලිසා සිතුවම් කළේ කවුද?",
            "a": "ලියනාඩෝ ඩා වින්චි",
            "b": "වින්සන්ට් වැන් ගොග්",
            "c": "පැබ්ලෝ පිකාසෝ",
            "d": "ක්ලෝඩ් මොනේට්",
            "correct": "ලියනාඩෝ ඩා වින්චි",
            "speak": "Leonardo da Vinci"
        }
    ]

# INITIATE MIXER
mixer.init()

# BACKGROUND SOUND
def payBakgroudMusic():
    mixer.music.load('images/kbc.mp3')
    mixer.music.play(-1)

payBakgroudMusic()

# INITIATE TEXT TO SPEECH
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def wrongAnswers(questionId):
    question = questionArray[questionId]
    wrongAnswersArray = []
    if question['a'] != question['correct']:
        wrongAnswersArray.append("a")
    if question['b'] != question['correct']:
        wrongAnswersArray.append("b")
    if question['c'] != question['correct']:
        wrongAnswersArray.append("c")
    if question['d'] != question['correct']:
        wrongAnswersArray.append("d")

    return wrongAnswersArray


def optionMakeEmpty(changeId):
    if changeId == "a":
        optionOneButton.config(text="")
    if changeId == "b":
        optionTwoButton.config(text="")
    if changeId == "c":
        optionThreeButton.config(text="")
    if changeId == "d":
        optionFourButton.config(text="")


def lifeLine50(questionId):
    wrongAnswersArray = wrongAnswers(questionId)

    changingId1 = randint(0, 2)
    changingId2 = None
    isChanginNotIdsSelected = True
    while isChanginNotIdsSelected:
        changingId2 = randint(0, 2)
        if changingId1 != changingId2:
            isChanginNotIdsSelected = False

    optionMakeEmpty(wrongAnswersArray[changingId1])
    optionMakeEmpty(wrongAnswersArray[changingId2])
    lifeLine50Button.config(image=image50X, state=DISABLED)


def lifeLineAudience(questionId):
    #     # CONFIG VALUE
    wrongAnswersArray = wrongAnswers(questionId)

    if 'a' in wrongAnswersArray:
        valueA = randint(0, 60)
    else:
        valueA = randint(60, 85)
    if 'b' in wrongAnswersArray:
        valueB = randint(0, 60)
    else:
        valueB = randint(60, 85)
    if 'c' in wrongAnswersArray:
        valueC = randint(0, 60)
    else:
        valueC = randint(60, 85)
    if 'd' in wrongAnswersArray:
        valueD = randint(0, 60)
    else:
        valueD = randint(60, 85)

    progressBarA.config(value=valueA)
    progressBarB.config(value=valueB)
    progressBarC.config(value=valueC)
    progressBarD.config(value=valueD)

    # PLACE PROGRESS BARS
    progressBarA.place(x=420, y=170)
    progressBarB.place(x=460, y=170)
    progressBarC.place(x=500, y=170)
    progressBarD.place(x=540, y=170)
    progressBarALabel.place(x=423, y=270)
    progressBarBLabel.place(x=463, y=270)
    progressBarCLabel.place(x=503, y=270)
    progressBarDLabel.place(x=543, y=270)

    lifeLineAudienceButton.config(image=imageAudiencePoleX, state=DISABLED)


def lifeLineCall(questionId):
    phoneLabel.place(x=80, y=190)
    lifeLineCallButton.config(image=imageCallerX, state=DISABLED)
    mixer.music.load('images/calling.mp3')
    mixer.music.play(loops=2)
    time.sleep(8)
    answer = questionArray[questionId]['speak']
    engine.say(f'The answer is {answer}')
    engine.say(f'The answer is {answer}')
    engine.runAndWait()


def addQuestion(questionId, answer):
    # HIDE PROGRESS BARS AND LABELS
    progressBarA.place_forget()
    progressBarB.place_forget()
    progressBarC.place_forget()
    progressBarD.place_forget()
    progressBarALabel.place_forget()
    progressBarBLabel.place_forget()
    progressBarCLabel.place_forget()
    progressBarDLabel.place_forget()
    # HIDE PHONE LABEL
    phoneLabel.place_forget()

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
        mixer.music.load('images/Kbcwon.mp3')
        mixer.music.play()

    def showQuestion():
        print('showQuestion')
        isNotAdded = True
        while isNotAdded:
            idValue = randint(0, len(questionArray) - 1)
            if idValue not in selectedIds:
                selectedIds.append(idValue)
                isNotAdded = False

        questionArea.delete(1.0, END)
        questionArea.insert(END, questionArray[idValue]['question'])
        optionOneButton.config(text=questionArray[idValue]['a'],
                               command=lambda: addQuestion(questionId=idValue, answer=questionArray[idValue]['a']))
        optionTwoButton.config(text=questionArray[idValue]['b'],
                               command=lambda: addQuestion(questionId=idValue, answer=questionArray[idValue]['b']))
        optionThreeButton.config(text=questionArray[idValue]['c'],
                                 command=lambda: addQuestion(questionId=idValue, answer=questionArray[idValue]['c']))
        optionFourButton.config(text=questionArray[idValue]['d'],
                                command=lambda: addQuestion(questionId=idValue, answer=questionArray[idValue]['d']))
        amountLabel.config(image=amountImageArray[len(selectedIds) - 1])
        lifeLine50Button.config(command=lambda: lifeLine50(questionId=idValue))
        lifeLineAudienceButton.config(command=lambda: lifeLineAudience(questionId=idValue))
        lifeLineCallButton.config(command=lambda: lifeLineCall(questionId=idValue))
        print(selectedIds)

    def tryAgain(window):
        # DESTROY CHILD WINDOW
        window.destroy()

        # RESET VALUES
        selectedIds.clear()
        lifeLine50Button.config(image=image50, state=ACTIVE)
        lifeLineAudienceButton.config(image=imageAudiencePole, state=ACTIVE)
        lifeLineCallButton.config(image=imageCaller, state=ACTIVE)
        # SHOW AGAIN QUESTION
        addQuestion(questionId="", answer="")

        # BACKGROUND MUSIC
        payBakgroudMusic()

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
            if len(selectedIds) != 2:
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
image50X = PhotoImage(file="images/50-50-X.png")

lifeLine50Button = Button(topLeftFrame, image=image50, background="black", bd=0, activebackground="black", width=170,
                          height=75)
lifeLine50Button.grid(row=0, column=0)

imageAudiencePole = PhotoImage(file="images/audiencePole.png")
imageAudiencePoleX = PhotoImage(file="images/audiencePoleX.png")

lifeLineAudienceButton = Button(topLeftFrame, image=imageAudiencePole, background="black", bd=0,
                                activebackground="black", width=170, height=75)
lifeLineAudienceButton.grid(row=0, column=1)

imageCaller = PhotoImage(file="images/phoneAFriend.png")
imageCallerX = PhotoImage(file="images/phoneAFriendX.png")
imagePhone = PhotoImage(file="images/phone.png")

lifeLineCallButton = Button(topLeftFrame, image=imageCaller, background="black", bd=0, activebackground="black",
                            width=170, height=75)
lifeLineCallButton.grid(row=0, column=2)

phoneLabel = Label(root, text='Click Here', image=imagePhone, bg='black')

imageMiddle = PhotoImage(file="images/center.png")

middleLabel = Label(middleLeftFrame, image=imageMiddle, bg="black", height=250)
middleLabel.grid(row=0, column=0)

imageLayout = PhotoImage(file="images/lay.png")

layoutLabel = Label(bottomLeftFrame, image=imageLayout, bg="black")
layoutLabel.grid(row=0, column=0)

questionArea = Text(bottomLeftFrame, font=('arial', 16, 'bold'), bg='black', fg='white', width=35, height=2,
                    wrap='word', bd=0)
questionArea.place(x=70, y=10)

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

# PROGRESS BAR
progressBarA = Progressbar(root, orient=VERTICAL)
progressBarB = Progressbar(root, orient=VERTICAL)
progressBarC = Progressbar(root, orient=VERTICAL)
progressBarD = Progressbar(root, orient=VERTICAL)

progressBarALabel = Label(root, text='A', bg="black", foreground="white", font=('arian', 15, 'bold'))
progressBarBLabel = Label(root, text='B', bg="black", foreground="white", font=('arian', 15, 'bold'))
progressBarCLabel = Label(root, text='C', bg="black", foreground="white", font=('arian', 15, 'bold'))
progressBarDLabel = Label(root, text='D', bg="black", foreground="white", font=('arian', 15, 'bold'))

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
