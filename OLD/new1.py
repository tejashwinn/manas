import tkinter as tk
from tkinter import *
import random
import sqlite3
import time
from tkinter import font

global easyAnswer
global easyQuestion
easyQuestion = [
    [
        "What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
        "[1, 0, 2, ‘hello’, '', []]",
        "Error",
        "[1, 2, ‘hello’]",
        "[1, 0, 2, 0, ‘hello’, '', []]"
    ],
    [
        "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)",
        "34.00",
        "34.000000",
        "34.0000",
        "34.00000000"

    ],
    [
        "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10",
        "30.8",
        "27.2",
        "28.4",
        "30.0"
    ],
    [
        "Which of these in not a core data type?",
        "Tuples",
        "Dictionary",
        "Lists",
        "Class"
    ],
    [
        "Which of the following represents the bitwise XOR operator?",
        "&",
        "!",
        "^",
        "|"
    ]
]
easyAnswer = [
    "[1, 2, ‘hello’]",
    "34.000000",
    "27.2",
    "Class",
    "^"
]

global mediumQuestion
global mediumAnswer
mediumQuestion = [
    [
        "Which of the following is not an exception handling keyword in Python?",
        "accept",
        "finally",
        "except",
        "try"
    ],
    [
        "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
        "3",
        "5",
        "25",
        "1"
    ],
    [
        "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
        "Error",
        "None",
        "25",
        "2"
    ],
    [
        "print(0xA + 0xB + 0xC):",
        "0xA0xB0xC",
        "Error",
        "0x22",
        "33"
    ],
    [
        "Which of the following is invalid?",
        "_a = 1",
        "__a = 1",
        "__str__ = 1",
        "none of the mentioned"
    ],
]
mediumAnswer = [
    "accept",
    "1",
    "25",
    "33",
    "none of the mentioned"
]


global hardQuestion
global hardAnswer
hardQuestion = [
    [
        "All keywords in Python are in _________",
        "lower case",
        "UPPER CASE",
        "Capitalized",
        "None of the mentioned"
    ],
    [
        "Which of the following cannot be a variable?",
        "__init__",
        "in",
        "it",
        "on"
    ],
    [
        "Which of the following is a Python tuple?",
        "[1, 2, 3]",
        "(1, 2, 3)",
        "{1, 2, 3}",
        "{}"
    ],
    [
        "What is returned by math.ceil(3.4)?",
        "3",
        "4",
        "4.0",
        "3.0"
    ],
    [
        "What will be the output of print(math.factorial(4.5))?",
        "24",
        "120",
        "error",
        "24.0"
    ]
]
hardAnswer = [
    "None of the mentioned",
    "in",
    "(1,2,3)",
    "4",
    "error"
]


def createTable(topic):
    con1 = sqlite3.connect('C:\\Users\\tejas\\Desktop\\Manas\\old\\quiz.db')
    create = con1.cursor()
    # conn.commit()
    create.execute('CREATE TABLE IF NOT EXISTS option(op text)')
    create.execute('DELETE FROM option')
    create.execute("INSERT INTO option VALUES (?)", str(topic))
    con1.commit()
    con1.close()


def fetchOption():
    conn = sqlite3.connect('C:\\Users\\tejas\\Desktop\\Manas\\old\\quiz.db')
    create = conn.cursor()
    create.execute('SELECT op FROM option order by op desc limit 1')
    z = create.fetchall()
    result = [r[0] for r in z]
    conn.close()
    print(result)
    print(result[0])
    return result[0]


def fetchQuestions(opt):
    if opt == "1":
        quiz(easyQuestion, easyAnswer)
    elif opt == "2":
        quiz(mediumQuestion, mediumAnswer)
    else:
        quiz(hardQuestion, hardAnswer)


def loginPage(logdata):
    sup.destroy()
    global login
    login = Frame(mainWindow)

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login, width=720, height=440, bg="blue")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="Quiz-App Login", fg="black", bg="white")
    heading.config(font=("Poppins", 31))
    heading.place(relx=0.26, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Username: ",
                   fg='black', bg='white', font=poppins9)
    ulabel.place(relx=0.205, rely=0.4)
    uname = Entry(login_frame, bg='#d3d3d3',
                  fg='black', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.33, rely=0.4)

    # PASSWORD
    plabel = Label(login_frame, text="Password: ",
                   fg='black', bg='white', font=poppins9)
    plabel.place(relx=0.205, rely=0.5)
    pas = Entry(login_frame, bg='#d3d3d3', fg='black',
                show="*", textvariable=password)
    pas.config(width=42)
    pas.place(relx=0.33, rely=0.5)

    def check():
        if uname.get() == '' or pas.get() == '':
            error = Label(
                login_frame, text="Check for empty fields", fg='red', bg='white')
            error.place(relx=0.45, rely=0.3)
            return
        for a, b, c in logdata:
            if b == uname.get() and c == pas.get():
                mainWindow.destroy()
                fetchQuestions(fetchOption())

                break
        else:
            error = Label(
                login_frame, text="Wrong Username or Password!", fg='red', bg='white')
            error.place(relx=0.37, rely=0.25)

    def gotoSignUp():
        login.destroy()
        signUpPage()
        return

    log = Button(login_frame, text='Login', padx=5,
                 pady=5, width=5, command=check)
    log.configure(width=15, height=1, activebackground="white",
                  background="green", relief=FLAT)
    log.place(relx=0.45, rely=0.65)

    sig = Button(login_frame, text='New User? Sign Up!', padx=5,
                 pady=5, width=5, command=gotoSignUp, bg="white", fg='blue')
    sig.configure(width=25, height=1, activebackground="#33B5E5", relief=FLAT)
    sig.place(relx=0.388, rely=0.9)

    login.pack()


def signUpPage():
    root.destroy()
    global sup
    sup = Frame(mainWindow)

    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    # country = StringVar()

    sup_canvas = Canvas(sup, width=720, height=440, bg="blue")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="white")
    sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    poppins31 = ("Poppins", 31)
    heading = Label(sup_frame, text="Quiz-App SignUp",
                    fg="black", bg="white", font=poppins31)

    heading.place(relx=0.2, rely=0.0)
    global poppins9
    poppins9 = ("Poppins", 9)
    wlabel = Label(sup_frame, text="", fg='red',
                   bg='white', font=poppins9)
    wlabel.place(relx=0.45, rely=0.2)
    # full name
    flabel = Label(sup_frame, text="Name: ", fg='black',
                   bg='white', font=poppins9)
    flabel.place(relx=0.20, rely=0.3)
    fname = Entry(sup_frame, bg='#E5E5E5', fg='black', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.32, rely=0.3)

    # username
    ulabel = Label(sup_frame, text="Username: ",
                   fg='black', bg='white', font=poppins9)
    ulabel.place(relx=0.20, rely=0.45)
    user = Entry(sup_frame, bg='#E5E5E5', fg='black', textvariable=uname)
    user.config(width=42)
    user.place(relx=0.32, rely=0.45)

    # password
    plabel = Label(sup_frame, text="Password: ",
                   fg='black', bg='white', font=poppins9)
    plabel.place(relx=0.20, rely=0.6)
    pas = Entry(sup_frame, bg='#E5E5E5', fg='black',
                show="*", textvariable=passW)
    pas.config(width=42)
    pas.place(relx=0.32, rely=0.6)

    # country
    # clabel = Label(sup_frame, text="Country: ", fg='black', bg='white',font=poppins9)
    # clabel.place(relx=0.20, rely=0.6)
    # c = Entry(sup_frame, bg='#E5E5E5', fg='black', textvariable=country)
    # c.config(width=42)
    # c.place(relx=0.32, rely=0.6)
    def checkUserName(usernameNew):

        conn = sqlite3.connect(
            'C:\\Users\\tejas\\Desktop\\Manas\\old\\quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT user_name FROM user')
        z = create.fetchall()
        result = [r[0] for r in z]
        conn.close()
        print(result)
        return (usernameNew) in result
        # print(False,usernameNew,result)

    def checkForEmpty():
        return fname.get() == '' or user.get() == '' or pas.get() == ''

    def addUserToDataBase():
        if checkForEmpty():
            wlabel.config(text="Fields can't be empty")
            return
        if checkUserName(str(uname.get())):
            wlabel.config(text="Enter a different Username")
            return

        fullname = fname.get()
        username = user.get()
        password = pas.get()
        # country = c.get()

        conn = sqlite3.connect(
            'C:\\Users\\tejas\\Desktop\\Manas\\old\\quiz.db')
        create = conn.cursor()
        create.execute(
            'CREATE TABLE IF NOT EXISTS user(name text, user_name text,password text)')
        create.execute("INSERT INTO user VALUES (?,?,?)",
                       (fullname, username, password))
        conn.commit()
        create.execute('SELECT * FROM user')
        z = create.fetchall()
        print(z)
    #    L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)

    def gotoLogin():
        conn = sqlite3.connect(
            'C:\\Users\\tejas\\Desktop\\Manas\\old\\quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM user')
        z = create.fetchall()
        loginPage(z)

    # signup BUTTON

    sp = Button(sup_frame, text='SignUp', padx=5, pady=5,
                width=5, command=addUserToDataBase, bg='green')
    sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    sp.place(relx=0.45, rely=0.75)

    log = Button(sup_frame, text='Already have a Account? Log In!', padx=5,
                 pady=5, width=5, command=gotoLogin, bg="white", fg='blue')
    log.configure(width=25, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.39, rely=0.9)

    sup.pack()


def menu():
    login1.destroy()
    global menu
    menu = Frame(mainWindow)

    menu_canvas = Canvas(menu, width=720, height=440, bg="blue")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas, bg="white")
    menu_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    wel = Label(menu_canvas, text='S E L E C T  T H E  T O P I C',
                fg="white", bg="#101357")
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1, rely=0.02)

    level = Label(menu_frame, text='Select your Difficulty Level !!',
                  bg="white", font="calibri 18")
    level.place(relx=0.25, rely=0.3)

    var = IntVar()
    easyR = Radiobutton(menu_frame, text='Easy', bg="white",
                        font="calibri 16", value=1, variable=var)
    easyR.place(relx=0.25, rely=0.4)

    mediumR = Radiobutton(menu_frame, text='Medium',
                          bg="white", font="calibri 16", value=2, variable=var)
    mediumR.place(relx=0.25, rely=0.5)

    hardR = Radiobutton(menu_frame, text='Hard', bg="white",
                        font="calibri 16", value=3, variable=var)
    hardR.place(relx=0.25, rely=0.6)

    def navigate():
        x = var.get()
        print(x)
        if x == 1:
            createTable('1')
        elif x == 2:
            createTable('2')
        elif x == 3:
            createTable('3')
    letsgo = Button(menu_frame, text="Let's Go", bg="white",
                    font="calibri 12", command=navigate)
    letsgo.place(relx=0.25, rely=0.8)
    menu.pack()


def showMark(mark):
    global sh
    sh = Tk()

    show_canvas = Canvas(sh, width=720, height=440, bg="#101357")
    show_canvas.pack()

    show_frame = Frame(show_canvas, bg="white")
    show_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    st = "Your score is: "+str(mark)
    mlabel = Label(show_canvas, text=st, fg="black", font="poppins 20")
    mlabel.place(relx=0.5, rely=0.2, anchor=CENTER)

    sh.mainloop()


def start():
    global root
    global mainWindow
    mainWindow = Tk()
    mainWindow.title("Quiz-App")
    photo = PhotoImage(file="C:\\Users\\tejas\\Desktop\\Manas\\OLD\\icon.png")
    mainWindow.iconphoto(False, photo)

    root = Frame(mainWindow)
    canvas = Canvas(root, width=720, height=440)
    canvas.grid(column=0, row=1)
    img = PhotoImage(
        file="C:\\Users\\tejas\\Desktop\\Manas\\OLD\\newback-edit (1).png")
    canvas.create_image(50, 10, image=img, anchor=NW)

    button = Button(root, text='User', command=signUpPage,
                    font=(("Poppins"), 10))
    button.configure(width=50, height=1,
                     activebackground="#33B5E5", bg='green', relief=RAISED)
    button.grid(column=0, row=2)

    button1 = Button(root, text='Admin', command=signUpPageAdmin,
                     font=(("Poppins"), 10))
    button1.configure(width=50, height=1,
                      activebackground="#33B5E5", bg='blue', relief=RAISED)
    button1.grid(column=0, row=3)

    root.pack()
    mainWindow.mainloop()


def signUpPageAdmin():

    root.destroy()
    global sup1
    sup1 = Frame(mainWindow)

    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    # country = StringVar()

    sup_canvas = Canvas(sup1, width=720, height=440, bg="blue")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="white")
    sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    poppins31 = ("Poppins", 31)
    heading = Label(sup_frame, text="   Sign Up Admin",
                    fg="black", bg="white", font=poppins31)

    heading.place(relx=0.2, rely=0.0)
    global poppins9
    poppins9 = ("Poppins", 9)
    wlabel = Label(sup_frame, text="", fg='red',
                   bg='white', font=poppins9)
    wlabel.place(relx=0.45, rely=0.2)
    # full name
    flabel = Label(sup_frame, text="Name: ", fg='black',
                   bg='white', font=poppins9)
    flabel.place(relx=0.20, rely=0.3)
    fname = Entry(sup_frame, bg='#E5E5E5', fg='black', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.32, rely=0.3)

    # username
    ulabel = Label(sup_frame, text="Username: ",
                   fg='black', bg='white', font=poppins9)
    ulabel.place(relx=0.20, rely=0.45)
    user = Entry(sup_frame, bg='#E5E5E5', fg='black', textvariable=uname)
    user.config(width=42)
    user.place(relx=0.32, rely=0.45)

    # password
    plabel = Label(sup_frame, text="Password: ",
                   fg='black', bg='white', font=poppins9)
    plabel.place(relx=0.20, rely=0.6)
    pas = Entry(sup_frame, bg='#E5E5E5', fg='black',
                show="*", textvariable=passW)
    pas.config(width=42)
    pas.place(relx=0.32, rely=0.6)

    def checkUserName(usernameNew):

        conn = sqlite3.connect(
            'C:\\Users\\tejas\\Desktop\\Manas\\old\\quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT user_name FROM admin')
        z = create.fetchall()
        result = [r[0] for r in z]
        conn.close()
        print(result)
        return (usernameNew) in result
        # print(False,usernameNew,result)

    def checkForEmpty():
        return fname.get() == '' or user.get() == '' or pas.get() == ''

    def addUserToDataBase():
        if checkForEmpty():
            wlabel.config(text="Fields can't be empty")
            return
        if checkUserName(str(uname.get())):
            wlabel.config(text="Enter a different Username")
            return

        fullname = fname.get()
        username = user.get()
        password = pas.get()

        conn = sqlite3.connect(
            'C:\\Users\\tejas\\Desktop\\Manas\\old\\quiz.db')
        create = conn.cursor()
        create.execute(
            'CREATE TABLE IF NOT EXISTS admin(name text, user_name text,password text)')
        create.execute("INSERT INTO admin VALUES (?,?,?)",
                       (fullname, username, password))
        conn.commit()
        create.execute('SELECT * FROM admin')
        z = create.fetchall()
        print(z)
        conn.close()
        loginPageAdmin(z)

    def gotoLogin():
        conn = sqlite3.connect(
            'C:\\Users\\tejas\\Desktop\\Manas\\old\\quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM admin')
        z = create.fetchall()
        loginPageAdmin(z)

    # signup BUTTON

    sp = Button(sup_frame, text='SignUp Admin', padx=5, pady=5,
                width=5, command=addUserToDataBase, bg='green')
    sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    sp.place(relx=0.45, rely=0.75)

    log = Button(sup_frame, text='Already have a Account? Log In!', padx=5,
                 pady=5, width=5, command=gotoLogin, bg="white", fg='blue')
    log.configure(width=25, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.39, rely=0.9)

    sup1.pack()


def loginPageAdmin(logdata):
    sup1.destroy()
    global login1
    login1 = Frame(mainWindow)

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login1, width=720, height=440, bg="blue")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="white")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="  Admin Login", fg="black", bg="white")
    heading.config(font=("Poppins", 31))
    heading.place(relx=0.26, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Username: ",
                   fg='black', bg='white', font=poppins9)
    ulabel.place(relx=0.205, rely=0.4)
    uname = Entry(login_frame, bg='#d3d3d3',
                  fg='black', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.33, rely=0.4)

    # PASSWORD
    plabel = Label(login_frame, text="Password: ",
                   fg='black', bg='white', font=poppins9)
    plabel.place(relx=0.205, rely=0.5)
    pas = Entry(login_frame, bg='#d3d3d3', fg='black',
                show="*", textvariable=password)
    pas.config(width=42)
    pas.place(relx=0.33, rely=0.5)

    def check():
        if uname.get() == '' or pas.get() == '':
            error = Label(
                login_frame, text="Check for empty fields", fg='red', bg='white')
            error.place(relx=0.45, rely=0.3)
            return
        for a, b, c in logdata:
            if b == uname.get() and c == pas.get():
                menu()
                break
        else:
            error = Label(
                login_frame, text="Wrong Username or Password!", fg='red', bg='white')
            error.place(relx=0.37, rely=0.25)

    def gotoSignUp():
        login1.destroy()
        signUpPageAdmin()
        return

    log = Button(login_frame, text='Login', padx=5,
                 pady=5, width=5, command=check)
    log.configure(width=15, height=1, activebackground="white",
                  background="green", relief=FLAT)
    log.place(relx=0.45, rely=0.65)

    sig = Button(login_frame, text='New User? Sign Up!', padx=5,
                 pady=5, width=5, command=gotoSignUp, bg="white", fg='blue')
    sig.configure(width=25, height=1, activebackground="#33B5E5", relief=FLAT)
    sig.place(relx=0.388, rely=0.9)

    login1.pack()


def quiz(question, answer):
    global e
    e = Tk()

    easy_canvas = Canvas(e, width=720, height=440, bg="#101357")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas, bg="white")
    easy_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(14, 0, -1):
            if k == 1:
                check = -1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
        timer.configure(text="Times up!")
        easy_frame.update()
        time.sleep(2)
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    score = 0

    dic = {}
    for p in range(5):
        dic[question[p][0]] = answer[p]
    print(dic)
    li = []
    li.append('')
    for i in range(5):
        li.append(i)
    # li = ['', 0, 1, 2, 3, 4]
    # li.append('')

    ques = Label(easy_frame, text="", font="poppins 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(easy_frame, text="", font="poppins 10",
                    value="", variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(easy_frame, text="", font="poppins 10",
                    value="", variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(easy_frame, text="", font="poppins 10",
                    value="", variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(easy_frame, text="", font="poppins 10",
                    value="", variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)

    timer = Label(e)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():
        print(var.get())
        if len(li) == 1:
            e.destroy()
            showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=question[x][0])
            a.configure(text=question[x][1], value=question[x][1])
            b.configure(text=question[x][2], value=question[x][2])
            c.configure(text=question[x][3], value=question[x][3])
            d.configure(text=question[x][4], value=question[x][4])
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score

        if dic[ques.cget("text")] == var.get():
            score += 1
        display()

    submit = Button(easy_frame, command=calc, text="Submit")
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)

    nextQuestion = Button(easy_frame, command=display, text="Next")
    nextQuestion.place(relx=0.87, rely=0.82, anchor=CENTER)

    # y = countDown()
    y = -1
    if y == -1:
        display()
    e.mainloop()


if __name__ == '__main__':
    start()
    # fetchOption()
