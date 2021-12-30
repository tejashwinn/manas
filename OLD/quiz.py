import tkinter as tk
from tkinter import *
import random
import sqlite3
import time
from tkinter import font
from tkinter import constants



global PYques,PYans

PYques = [
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
    ],   
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

PYans=[
    "[1, 2, ‘hello’]",
    "34.000000",
    "27.2",
    "Class",
    "^",
    "accept",
    "1",
    "25",
    "33",
    "none of the mentioned",
    "None of the mentioned",
    "in",
    "(1,2,3)",
    "4",
    "error",
]



global Cques, Cans
Cques = [
    [
        "Which of the following statements should be used to obtain a remainder after dividing 3.14 by 2.1 ?",
        "rem = 3.14 % 2.1;",
        "rem = modf(3.14, 2.1);",
        "rem = fmod(3.14, 2.1);",
        "Remainder cannot be obtain in floating point division.",
        "rem = fmod(3.14, 2.1);",
    ],
    [
        "What are the types of linkages?",
        "Internal and External",
        "External, Internal and None",
        "External and None",
        "Internal",
        "External, Internal and None",
    ],
    [
        "Which of the following special symbol allowed in a variable name?",
        "* (asterisk)",
        "| (pipeline)",
        "- (hyphen)",
        "_ (underscore)",
        "_ (underscore)",
    ],
    [
        "Is there any difference between following declarations? 1 :\textern int fun(); 2 :\tint fun();",
        "Both are identical",
        "No difference, except extern int fun(); is probably in another file",
        "int fun(); is overrided with extern int fun();",
        "None of these",
        "No difference, except extern int fun(); is probably in another file",
    ],
    [
        "How would you round off a value from 1.66 to 2.0?",
        "ceil(1.66)",
        "floor(1.66)",
        "roundup(1.66)",
        "roundto(1.66)",
        "ceil(1.66)",
    ],
    [
        "By default a real number is treated as a:",
        "float",
        "double",
        "long double",
        "far double",
        "double",
    ],
    [
        "Is the following statement a declaration or definition? extern int i;",
        "Declaration",
        "Definition",
        "Function",
        "Error",
        "Declaration",
    ],
    [
        "Identify which of the following are declarations 1 :\textern int x; 2 :\tfloat square ( float x ) { ... } 3 :\tdouble pow(double, double);",
        "1",
        "2",
        "1 and 3",
        "3",
        "1 and 3",
    ],
    [
        "Which of the following is not user defined data type? 1 :\t long int l = 2.35; 2 :\tenum day {Sun, Mon, Tue, Wed};",
        "1",
        "2",
        "none of the above",
        "Both 1 and 2",
        "2",
    ],
    [
        "When we mention the prototype of a function?",
        "Defining",
        "Declaring",
        "Prototyping",
        "Calling",
        "Declaring",
    ],
    [
        "Which of the following function sets first n characters of a string to a given character?",
        "strinit()",
        "strnset()",
        "strset()",
        "strcset()",
        "strnset()",
    ],
    [
        "If the two strings are identical, then strcmp() function returns",
        "-1",
        "1",
        "0",
        "Yes",
        "0",
    ],
    [
        "How will you print \\n on the screen?",
        'printf("\\n");',
        'echo "\\\\n";',
        "printf('\\n');",
        'printf("\\\\n");',
        'printf("\\\\n");',
    ],
    [
        "The library function used to find the last occurrence of a character in a string is",
        "strnstr()",
        "laststr()",
        "strrchr()",
        "strstr()",
        "strrchr()",
    ],
    [
        "Which of the following function is used to find the first occurrence of a given string in another string?",
        "strchr()",
        "strrchr()",
        "strstr()",
        "strnset()",
        "strstr()",
    ],
    [
        'In a file contains the line "I am a boy\\r\\n" then on reading this line into the array str using fgets(). What will str contain?',
        '"I am a boy\\r\\n\\0"',
        '"I am a boy\\r\\0"',
        '"I am a boy\\n\\0"',
        '"I am a boy"',
        '"I am a boy\\n\\0"',
    ],
    [
        "What will happen if in a C program you assign a value to an array element whose subscript exceeds the size of array?",
        "The element will be set to 0.",
        "The compiler would report an error.",
        "The program may crash if some important data gets overwritten.",
        "The array size would appropriately grow.",
        "The program may crash if some important data gets overwritten.",
    ],
    [
        "What does the following declaration mean? int (*ptr)[10];",
        "ptr is array of pointers to 10 integers",
        "ptr is a pointer to an array of 10 integers",
        "ptr is an array of 10 integers",
        "ptr is an pointer to array",
        "ptr is a pointer to an array of 10 integers",
    ],
    [
        "In C, if you pass an array as an argument to a function, what actually gets passed?",
        "Value of elements in array",
        "First element of the array",
        "Base address of the array",
        "Address of the last element of array",
        "Base address of the array",
    ],
    [
        "What will the function rewind() do?",
        "Reposition the file pointer to a character reverse.",
        "Reposition the file pointer stream to end of file.",
        "Reposition the file pointer to begining of that line.",
        "Reposition the file pointer to begining of file.",
        "Reposition the file pointer to begining of file.",
    ],
]
Cans = [
    "rem = fmod(3.14, 2.1);",
    "External, Internal and None",
    "_ (underscore)",
    "No difference, except extern int fun(); is probably in another file",
    "ceil(1.66)",
    "double",
    "Declaration",
    "1 and 3",
    "2",
    "Declaring",
    "strnset()",
    "0",
    'printf("\\\\n");',
    "strrchr()",
    "strstr()",
    '"I am a boy\\n\\0"',
    "The program may crash if some important data gets overwritten.",
    "ptr is a pointer to an array of 10 integers",
    "Base address of the array",
    "Reposition the file pointer to begining of file.",
]


global CIques, CIans
CIques = [
    [
        "What is the term used for describing the judgmental or commonsense part of problem solving?",
        "Heuristic",
        "Critical",
        "Analytical",
        "None of the above",
        "Heuristic",
    ],
    [
        'What stage of the manufacturing process has been described as "the mapping of function onto form"?',
        "Design",
        "Distribution",
        "project management",
        "field service",
        "Design",
    ],
    [
        "Which kind of planning consists of successive representations of different levels of a plan?",
        "hierarchical planning",
        "non-hierarchical planning",
        "project planning",
        "None of the above",
        "hierarchical planning",
    ],
    [
        'What was originally called the "imitation game" by its creator?',
        "The Turing Test",
        "LISP",
        "The Logic Theorist",
        "None of the above",
        "The Turing Test",
    ],
    [
        "Decision support programs are designed to help managers make:",
        "budget projections",
        "visual presentations",
        "business decisions",
        "None of the above",
        "business decisions",
    ],
    [
        "PROLOG is an AI programming language which solves problems with a form of symbolic logic known as predicate calculus. It was developed in 1972 at the University of Marseilles by a team of specialists. Can you name the person who headed this team?",
        "Alain Colmerauer",
        "Seymour Papert",
        "John McCarthy",
        "None of the above",
        "Alain Colmerauer",
    ],
    [
        "Programming a robot by physically moving it through the trajectory you want it to follow is called:",
        "contact sensing control",
        "continuous-path control",
        "robot vision control",
        "None of the above",
        "continuous-path control",
    ],
    [
        "To invoke the LISP system, you must enter",
        "AI",
        "CL (Common Lisp)",
        "both b and c",
        "None of the above",
        "None of the above",
    ],
    [
        'DEC advertises that it helped to create "the world\'s first expert system routinely used in an industrial environment," called XCON or:',
        "PDP-11",
        "Rl",
        "MAGNOM",
        "None of the above",
        "Rl",
    ],
    [
        "Prior to the invention of time sharing, the prevalent method of computer access was:",
        "batch processing",
        "telecommunication",
        "remote access",
        "None of the above",
        "batch processing",
    ],
    [
        "Seymour Papert of the MIT AI lab created a programming environment for children called:",
        "BASIC",
        "LOGO",
        "MYCIN",
        "None of the above",
        "LOGO",
    ],
    [
        "The Strategic Computing Program is a project of the:",
        "Defense Advanced Research Projects Agency",
        "National Science Foundation",
        "Jet Propulsion Laboratory",
        "None of the above",
        "Defense Advanced Research Projects Agency",
    ],
    [
        "The original LISP machines produced by both LMI and Symbolics were based on research performed at:",
        "CMU",
        "MIT",
        "Stanford University",
        "None of the above",
        "MIT",
    ],
    [
        "In LISP, the addition 3   2 is entered as",
        "3   2",
        "3 add 2",
        "(  3 2)",
        "None of the above",
        "None of the above",
    ],
    [
        "Weak AI is:",
        "the embodiment of human intellectual capabilities within a computer.",
        "a set of computer programs that produce output that would be considered to reflect intelligence if it were generated by humans.",
        "the study of mental faculties through the use of mental models implemented on a computer.",
        "None of the above",
        "the study of mental faculties through the use of mental models implemented on a computer.",
    ],
    [
        "In LISP, the function assigns the symbol x to y is",
        "(setq y x)",
        "(set y = 'x')",
        "(setq y = 'x')",
        "None of the above",
        "None of the above",
    ],
    [
        "In LISP, the function returns t if <object> is a CONS cell and nil otherwise:",
        "(cons <object>)",
        "(consp <object>)",
        "(cous = <object>)",
        "None of the above",
        "(consp <object>)",
    ],
    [
        "In a rule-based system, procedural domain knowledge is in the form of:",
        "production rules",
        "rule interpreters",
        "meta-rules",
        "None of the above",
        "production rules",
    ],
    [
        "If a robot can alter its own trajectory in response to external conditions, it is considered to be:",
        "intelligent",
        "mobile",
        "non-servo",
        "None of the above",
        "intelligent",
    ],
    [
        "One of the leading American robotics centers is the Robotics Institute located at:",
        "CMU",
        "MIT",
        "SRI",
        "None of the above",
        "CMU",
    ],
]

CIans = [
    "Heuristic",
    "Design",
    "hierarchical planning",
    "The Turing Test",
    "business decisions",
    "Alain Colmerauer",
    "continuous-path control",
    "None of the above",
    "Rl",
    "batch processing",
    "LOGO",
    "Defense Advanced Research Projects Agency",
    "MIT",
    "None of the above",
    "the study of mental faculties through the use of mental models implemented on a computer.",
    "None of the above",
    "(consp <object>)",
    "production rules",
    "intelligent",
    "CMU",
]

global CPPques, CPPans
CPPques=[
    [
        "Which of the following type of class allows only one object of it to be created?",
        "Virtual class",
        "Abstract class",
        "Singleton class",
        "Friend class",
        "Singleton class",
    ],
    [
        "Which of the following is not a type of constructor?",
        "Copy constructor",
        "Friend constructor",
        "Default constructor",
        "Parameterized constructor",
        "Friend constructor",
    ],
    [
        "Which of the following statements is correct?",
        "Base class pointer cannot point to derived class.",
        "Derived class pointer cannot point to base class.",
        "Pointer to derived class cannot be created.",
        "Pointer to base class cannot be created.",
        "Derived class pointer cannot point to base class.",
    ],
    [
        "Which of the following is not the member of class?",
        "Static function",
        "Friend function",
        "Const function",
        "Virtual function",
        "Friend function",
    ],
    [
        "Which of the following concepts means determining at runtime what method to invoke?",
        "Data hiding",
        "Dynamic Typing",
        "Dynamic binding",
        "Dynamic loading",
        "Dynamic binding",
    ],
    [
        "Which of the following term is used for a function defined inside a class?",
        "Member Variable",
        "Member function",
        "Class function",
        "Classic function",
        "Member function",
    ],
    [
        "Which of the following concept of oops allows compiler to insert arguments in a function call if it is not specified?",
        "Call by value",
        "Call by reference",
        "Default arguments",
        "Call by pointer",
        "Default arguments",
    ],
    [
        "How many instances of an abstract class can be created?",
        "1",
        "5",
        "13",
        "0",
        "0",
    ],
    [
        "Which of the following cannot be friend?",
        "Function",
        "Class",
        "Object",
        "Operator function",
        "Object",
    ],
    [
        "Which of the following concepts of OOPS means exposing only necessary information to client?",
        "Encapsulation",
        "Abstraction",
        "Data hiding",
        "Data binding",
        "Data hiding",
    ],
    [
        "Why reference is not same as a pointer?",
        "A reference can never be null.",
        "A reference once established cannot be changed.",
        "Reference doesn't need an explicit dereferencing mechanism.",
        "All of the above.",
        "All of the above.",
    ],
    ["cout is a/an __________ .", "operator", "function", "object", "macro", "object"],
    [
        "Which of the following concepts provides facility of using object of one class inside another class?",
        "Encapsulation",
        "Abstraction",
        "Composition",
        "Inheritance",
        "Composition",
    ],
    ["How many types of polymorphisms are supported by C  ?", "1", "2", "3", "4", "2"],
    [
        "Which of the following is an abstract data type?",
        "int",
        "double",
        "string",
        "Class",
        "Class",
    ],
    [
        "Which of the following concepts means adding new components to a program as it runs?",
        "Data hiding",
        "Dynamic typing",
        "Dynamic binding",
        "Dynamic loading",
        "Dynamic loading",
    ],
    [
        "Which of the following statement is correct?",
        "A constructor is called at the time of declaration of an object.",
        "A constructor is called at the time of use of an object.",
        "A constructor is called at the time of declaration of a class.",
        "A constructor is called at the time of use of a class.",
        "A constructor is called at the time of declaration of an object.",
    ],
    [
        "Which of the following correctly describes overloading of functions?",
        "Virtual polymorphism",
        "Transient polymorphism",
        "Ad-hoc polymorphism",
        "Pseudo polymorphism",
        "Ad-hoc polymorphism",
    ],
    [
        "Which of the following approach is adapted by C  ?",
        "Top-down",
        "Bottom-up",
        "Right-left",
        "Left-right",
        "Bottom-up",
    ],
    [
        "Which of the following is correct about function overloading?",
        "The types of arguments are different.",
        "The order of argument is different.",
        "The number of argument is same.",
        "Both A and B.",
        "Both A and B.",
    ],
]
CPPans=[
    "Singleton class",
    "Friend constructor",
    "Derived class pointer cannot point to base class.",
    "Friend function",
    "Dynamic binding",
    "Member function",
    "Default arguments",
    "0",
    "Object",
    "Data hiding",
    "All of the above.",
    "object",
    "Composition",
    "2",
    "Class",
    "Dynamic loading",
    "A constructor is called at the time of declaration of an object.",
    "Ad-hoc polymorphism",
    "Bottom-up",
    "Both A and B.",
]


global CSques, CSans
CSques=[
    [
        "From what location are the 1st computer instructions available on boot up?",
        "ROM BIOS",
        "CPU",
        "boot.ini",
        "CONFIG.SYS",
        "ROM BIOS",
    ],
    [
        "What could cause a fixed disk error.",
        "No-CD installed",
        "slow processor",
        "Incorrect CMOS settings",
        "None of the above",
        "Incorrect CMOS settings",
    ],
    [
        "Missing slot covers on a computer can cause?",
        "over heat",
        "EMI.",
        "incomplete path for ESD",
        "None of the above",
        "over heat",
    ],
    [
        "When installing PCI NICS you can check the IRQ availability by looking at",
        "dip switches",
        "CONFIG.SYS",
        "motherboard BIOS",
        "None of the above",
        "motherboard BIOS",
    ],
    [
        "With respect to a network interface card, the term 10/100 refers to",
        "protocol speed",
        "a fiber speed",
        "megabits per seconds",
        "None of the above",
        "megabits per seconds",
    ],
    [
        "Which Motherboard form factor uses one 20 pin connector",
        "ATX",
        "AT",
        "BABY AT",
        "All of the above",
        "ATX",
    ],
    [
        "A hard disk is divided into tracks which are further subdivided into:",
        "clusters",
        "sectors",
        "vectors",
        "heads",
        "sectors",
    ],
    [
        "A wrist grounding strap contains which of the following:",
        "Surge protector",
        "Capacitor",
        "Voltmeter",
        "Resistor",
        "Resistor",
    ],
    [
        "Which standard govern parallel communications?",
        "RS232",
        "RS-232a",
        "CAT 5",
        "IEEE 1284",
        "IEEE 1284",
    ],
    [
        "In laser printer technology, what happens during the conditioning stage?",
        "The corona wire places a uniform positive charge on the paper",
        "A uniform negative charge is placed on the photosensitive drum",
        "A uniform negative charge is placed on the toner",
        "None of the above",
        "A uniform negative charge is placed on the photosensitive drum",
    ],
    [
        "What product is used to clean smudged keys on a keyboard?",
        "TMC solvent",
        "Silicone spray",
        "Denatured alcohol",
        "All-purpose cleaner",
        "All-purpose cleaner",
    ],
    [
        "ESD would cause the most damage to which component?",
        "Power supply",
        "Expansion board",
        "Monitor",
        "None of the above",
        "Expansion board",
    ],
    [
        "To view any currently running Terminate Stay Resident (TSR's) programs you could type:",
        "Memory",
        "MEM",
        "SYS /M",
        "None of the above",
        "MEM",
    ],
    [
        "Which type of system board is the MOST likely candidate for processor upgrading if you want maximum performance and future compatibility?",
        "PCI",
        "ISA",
        "EISA",
        "None of the above",
        "PCI",
    ],
    [
        "Most PCs give a single beep on bootup to indicate they are ok hardware wise. You boot your PC and don't get a beep. What should you check first?",
        "system board",
        "RAM",
        "microprocessor",
        "speaker",
        "speaker",
    ],
    [
        "Which peripheral port provides the FASTEST throughput to laser printers?",
        "RS-232",
        "SCSI",
        "Parallel",
        "Serial",
        "Parallel",
    ],
    [
        "The mouse pointer moves erratically, what is the possible cause? The mouse\t",
        "ball is dirty",
        "is not connected",
        "driver is not installed properly",
        "has an incorrect IRQ setting",
        "ball is dirty",
    ],
    [
        "Voltage is measured:",
        "in parallel",
        "in series",
        "after breaking the circuit",
        "after checking current",
        "in parallel",
    ],
    [
        "The 34-pin connection on an I/O card is for?",
        "Floppy drive",
        "SCSI drive",
        "Zip drive",
        "None of the above",
        "Floppy drive",
    ],
    [
        'The terms "red book", "yellow book", and "orange book" refer to:',
        "SCSI",
        "ide",
        "CD-ROM standards",
        "All of the above",
        "CD-ROM standards",
    ],
]
CSans=[
    "ROM BIOS",
    "Incorrect CMOS settings",
    "over heat",
    "motherboard BIOS",
    "megabits per seconds",
    "ATX",
    "sectors",
    "Resistor",
    "IEEE 1284",
    "A uniform negative charge is placed on the photosensitive drum",
    "All-purpose cleaner",
    "Expansion board",
    "MEM",
    "PCI",
    "speaker",
    "Parallel",
    "ball is dirty",
    "in parallel",
    "Floppy drive",
    "CD-ROM standards",
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

    st = "Your score is: "+str(mark)+"/5"
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
        file="C:\\Users\\tejas\\Desktop\\Manas\\OLD\\back.png")
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
    # start()
    quiz(PYques,PYans)