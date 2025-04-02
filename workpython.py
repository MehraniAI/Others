import tkinter as tk
from tkinter import messagebox, ttk
import random

class PythonQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Application")
        self.root.geometry("800x600")
        
        # Initialize quiz variables
        self.questions = self.load_questions()
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        self.shuffled_indices = list(range(len(self.questions)))
        random.shuffle(self.shuffled_indices)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 10))
        self.style.configure("TRadiobutton", font=("Arial", 10))
        
        # Create UI elements
        self.create_welcome_screen()
    
    def load_questions(self):
        questions = [
            {
                "question": "301. Who developed Python Programming Language?",
                "options": ["a) Wick van Rossum", "b) Rasmus Lerdorf", "c) Guido van Rossum", "d) Niene Stom"],
                "answer": "c",
                "explanation": "Python was designed by Guido van Rossum."
            },
            {
                "question": "2. Which type of Programming does Python support?",
                "options": ["a) object-oriented programming", "b) structured programming", "c) functional programming", "d) all of the mentioned"],
                "answer": "d",
                "explanation": "Python supports OOP, structured, and functional programming."
            },
            {
                "question": "3. Is Python case sensitive when dealing with identifiers?",
                "options": ["a) no", "b) yes", "c) machine dependent", "d) none of the mentioned"],
                "answer": "b",
                "explanation": "Case is always significant in Python identifiers."
            },
            {
                "question": "4. Which of the following is the correct extension of the Python file?",
                "options": ["a) .python", "b) .pl", "c) .py", "d) .p"],
                "answer": "c",
                "explanation": "Python files use .py extension."
            },
            {
                "question": "5. Is Python code compiled or interpreted?",
                "options": ["a) Python code is both compiled and interpreted", "b) Python code is neither compiled nor interpreted", "c) Python code is only compiled", "d) Python code is only interpreted"],
                "answer": "a",
                "explanation": "Python is first compiled to bytecode which is then interpreted."
            },
            {
                "question": "6. All keywords in Python are in _________",
                "options": ["a) Capitalized", "b) lower case", "c) UPPER CASE", "d) None of the mentioned"],
                "answer": "d",
                "explanation": "Only True, False and None are capitalized."
            },
            {
                "question": "7. What will be the value of the following Python expression? 4 + 3 % 5",
                "options": ["a) 7", "b) 2", "c) 4", "d) 1"],
                "answer": "a",
                "explanation": "% has higher precedence than +, so 3%5=3, then 4+3=7."
            },
            {
                "question": "8. Which of the following is used to define a block of code in Python language?",
                "options": ["a) Indentation", "b) Key", "c) Brackets", "d) All of the mentioned"],
                "answer": "a",
                "explanation": "Python uses indentation to define code blocks."
            },
            {
                "question": "9. Which keyword is used for function in Python language?",
                "options": ["a) Function", "b) def", "c) Fun", "d) Define"],
                "answer": "b",
                "explanation": "The 'def' keyword is used to define functions."
            },
            {
                "question": "10. Which character is used for single-line comments in Python?",
                "options": ["a) //", "b) #", "c) !", "d) /*"],
                "answer": "b",
                "explanation": "Python uses # for single-line comments."
            },
            # Questions 11-20
            {
                "question": "11. What will be the output of: i=1\nwhile True:\n    if i%3==0:break\n    print(i)\n    i+=1",
                "options": ["a) 1 2 3", "b) error", "c) 1 2", "d) none"],
                "answer": "b",
                "explanation": "There's a syntax error due to space in +=."
            },
            {
                "question": "12. Which function helps find the Python version?",
                "options": ["a) sys.version(1)", "b) sys.version(0)", "c) sys.version()", "d) sys.version"],
                "answer": "d",
                "explanation": "sys.version gives the Python version."
            },
            {
                "question": "13. Python's anonymous functions are called?",
                "options": ["a) pi", "b) anonymous", "c) lambda", "d) none"],
                "answer": "c",
                "explanation": "Lambda functions are anonymous."
            },
            {
                "question": "14. What is Python's order of precedence?",
                "options": ["a) Exponential, Parentheses, Mul, Div, Add, Sub", 
                           "b) Exponential, Parentheses, Div, Mul, Add, Sub",
                           "c) Parentheses, Exponential, Mul, Add, Div, Sub",
                           "d) Parentheses, Exponential, Mul, Div, Add, Sub"],
                "answer": "d",
                "explanation": "Remember PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction."
            },
            {
                "question": "15. What is the output of x=1; x<<2?",
                "options": ["a) 4", "b) 2", "c) 1", "d) 8"],
                "answer": "a",
                "explanation": "Bitwise left shift by 2 multiplies by 4."
            },
            {
                "question": "16. What does pip stand for?",
                "options": ["a) Pip Installs Python", "b) Pip Installs Packages", "c) Preferred Installer Program", "d) All"],
                "answer": "c",
                "explanation": "pip is the Preferred Installer Program."
            },
            {
                "question": "17. What's true about Python variable names?",
                "options": ["a) Only _ and & allowed", "b) Unlimited length", "c) Private need __", "d) None"],
                "answer": "b",
                "explanation": "Variable names can be any length."
            },
            {
                "question": "18. What are the values of: 2**(3**2), (2**3)**2, 2**3**2?",
                "options": ["a) 512, 64, 512", "b) 512, 512, 512", "c) 64, 512, 64", "d) 64, 64, 64"],
                "answer": "a",
                "explanation": "** is right-associative."
            },
            {
                "question": "19. Which is truncation division operator?",
                "options": ["a) |", "b) //", "c) /", "d) %"],
                "answer": "b",
                "explanation": "// does floor division."
            },
            {
                "question": "20. What does filter(bool, [1,0,2,0,'hello','',[]]) return?",
                "options": ["a) [1,0,2,'hello','',[]]", "b) Error", "c) [1,2,'hello']", "d) [1,0,2,0,'hello','',[]]"],
                "answer": "c",
                "explanation": "filter keeps only truthy values."
            },
            # Questions 21-30
            {
                "question": "21. Which is a built-in function?",
                "options": ["a) factorial()", "b) print()", "c) seed()", "d) sqrt()"],
                "answer": "b",
                "explanation": "print() is built-in, others need imports."
            },
            {
                "question": "22. What does id() do?",
                "options": ["a) Checks if object has id", "b) Returns object identity", "c) All", "d) None"],
                "answer": "b",
                "explanation": "id() returns object's memory address."
            },
            {
                "question": "23. How many parameters can the shown decorator handle?",
                "options": ["a) Any number", "b) 0", "c) 1", "d) 2"],
                "answer": "a",
                "explanation": "Decorator uses *args and **kwargs."
            },
            {
                "question": "24. What is min(max(False,-3,-4), 2,7)?",
                "options": ["a) -4", "b) -3", "c) 2", "d) False"],
                "answer": "d",
                "explanation": "max returns 0 (False), min is 0."
            },
            {
                "question": "25. Which is not a core Python data type?",
                "options": ["a) Tuples", "b) Lists", "c) Class", "d) Dictionary"],
                "answer": "c",
                "explanation": "Class is user-defined."
            },
            {
                "question": "26. What does print(\"%.2f\"%56.236) output?",
                "options": ["a) 56.236", "b) 56.23", "c) 56.0000", "d) 56.24"],
                "answer": "d",
                "explanation": "Rounds to 2 decimal places."
            },
            {
                "question": "27. What are Python packages?",
                "options": ["a) Set of main modules", "b) Folder of modules", "c) Files with Python code", "d) Programs using modules"],
                "answer": "b",
                "explanation": "Packages are folders with modules."
            },
            {
                "question": "28. What is len([\"hello\",2,4,6])?",
                "options": ["a) Error", "b) 6", "c) 4", "d) 3"],
                "answer": "c",
                "explanation": "Counts the 4 elements."
            },
            {
                "question": "29. What prints when looping over 'abcd' with upper()?",
                "options": ["a) a\nB\nC\nD", "b) a b c d", "c) error", "d) A\nB\nC\nD"],
                "answer": "d",
                "explanation": "Prints each character uppercased."
            },
            {
                "question": "30. Python's namespace search order is?",
                "options": ["a) Built-in → Global → Local", "b) Built-in → Local → Global", 
                           "c) Local → Global → Built-in", "d) Global → Local → Built-in"],
                "answer": "c",
                "explanation": "LEGB rule: Local, Enclosing, Global, Built-in."
            },
            # Questions 31-40
            {
                "question": "31. What prints for [1,2,3,4][::-1]?",
                "options": ["a) 4 3 2 1", "b) error", "c) 1 2 3 4", "d) none"],
                "answer": "a",
                "explanation": "[::-1] reverses the list."
            },
            {
                "question": "32. What is \"a\"+\"bc\"?",
                "options": ["a) bc", "b) abc", "c) a", "d) bca"],
                "answer": "b",
                "explanation": "String concatenation."
            },
            {
                "question": "33. Which function is called by format()?",
                "options": ["a) str()", "b) format()", "c) __str__()", "d) __format__()"],
                "answer": "c",
                "explanation": "format() calls __str__() by default."
            },
            {
                "question": "34. Which is not a Python keyword?",
                "options": ["a) pass", "b) eval", "c) assert", "d) nonlocal"],
                "answer": "b",
                "explanation": "eval is a built-in function."
            },
            {
                "question": "35. What prints for temp.id in the shown class?",
                "options": ["a) 12", "b) 224", "c) None", "d) Error"],
                "answer": "a",
                "explanation": "Instance attribute remains 12."
            },
            {
                "question": "36. What is the output of the shown list modification?",
                "options": ["a) Error", "b) None", "c) False", "d) True"],
                "answer": "d",
                "explanation": "Same object modified, same id."
            },
            {
                "question": "37. Which module parses command line options?",
                "options": ["a) getarg", "b) getopt", "c) main", "d) os"],
                "answer": "b",
                "explanation": "getopt handles command line args."
            },
            {
                "question": "38. What is the final set after z operations?",
                "options": ["a) {'a','c','p','q','s','n'}", "b) {'abc','p','q','san'}", 
                           "c) {'a','b','c','p','q','san'}", "d) {'a','b','c',['p','q'],'san}"],
                "answer": "c",
                "explanation": "Sets contain unique elements."
            },
            {
                "question": "39. Which arithmetic operator can't be used with strings?",
                "options": ["a) *", "b) -", "c) +", "d) All"],
                "answer": "b",
                "explanation": "Subtraction isn't defined for strings."
            },
            {
                "question": "40. What does \"abc. DEF\".capitalize() return?",
                "options": ["a) Abc. def", "b) abc. def", "c) Abc. Def", "d) ABC. DEF"],
                "answer": "a",
                "explanation": "First letter uppercase, rest lowercase."
            },
            # Questions 41-50
            {
                "question": "41. How to create an empty set?",
                "options": ["a) ()", "b) []", "c) {}", "d) set()"],
                "answer": "d",
                "explanation": "{} makes dict, set() makes set."
            },
            {
                "question": "42. What is the value of 'result' after list operations?",
                "options": ["a) [1,3,5,7,8]", "b) [1,7,8]", "c) [1,2,4,7,8]", "d) error"],
                "answer": "a",
                "explanation": "Contains elements unique to each list."
            },
            {
                "question": "43. How to add element to list?",
                "options": ["a) list1.addEnd(5)", "b) list1.addLast(5)", "c) list1.append(5)", "d) list1.add(5)"],
                "answer": "c",
                "explanation": "append() adds to end of list."
            },
            {
                "question": "44. What prints with center(6)?",
                "options": ["a) *  abcde *", "b) *abcde *", "c) * abcde*", "d) * abcde  *"],
                "answer": "b",
                "explanation": "Right-padded when even length."
            },
            {
                "question": "45. What prints after list modification?",
                "options": ["a) [1,4]", "b) [1,3,4]", "c) [4,3]", "d) [1,3]"],
                "answer": "c",
                "explanation": "Both variables reference same list."
            },
            {
                "question": "46. What's true about functions?",
                "options": ["a) No modularity", "b) Can't create custom", "c) Reusable code", "d) All"],
                "answer": "c",
                "explanation": "Functions allow code reuse."
            },
            {
                "question": "47. How to get value 6 from matrix A?",
                "options": ["a) A[2][1]", "b) A[1][2]", "c) A[3][2]", "d) A[2][3]"],
                "answer": "b",
                "explanation": "Row 1 (2nd), Column 2 (3rd)."
            },
            {
                "question": "48. Maximum identifier length?",
                "options": ["a) 79", "b) 31", "c) 63", "d) None"],
                "answer": "d",
                "explanation": "No fixed limit."
            },
            {
                "question": "49. What prints in the while-else loop?",
                "options": ["a) error", "b) 0 1 2 0", "c) 0 1 2", "d) none"],
                "answer": "c",
                "explanation": "Else doesn't run after break."
            },
            {
                "question": "50. What prints when looping over 'abcd' indices?",
                "options": ["a) error", "b) 1 2 3 4", "c) a b c d", "d) 0 1 2 3"],
                "answer": "d",
                "explanation": "range(len(x)) gives indices 0-3."
            },
            # Questions 51-60
            {
                "question": "51. Python function types are?",
                "options": ["a) System/Custom", "b) Built-in/User-defined", "c) Internal/External", "d) User/System"],
                "answer": "b",
                "explanation": "Built-in and user-defined functions."
            },
            {
                "question": "52. What is len(mylist) after addItem?",
                "options": ["a) 5", "b) 8", "c) 2", "d) 1"],
                "answer": "a",
                "explanation": "Appends 1, making length 5."
            },
            {
                "question": "53. Which is a tuple?",
                "options": ["a) {1,2,3}", "b) {}", "c) [1,2,3]", "d) (1,2,3)"],
                "answer": "d",
                "explanation": "Tuples use parentheses."
            },
            {
                "question": "54. What is 'a' in z where z=set('abc$de')?",
                "options": ["a) Error", "b) True", "c) False", "d) No output"],
                "answer": "b",
                "explanation": "'a' is in the set."
            },
            {
                "question": "55. What is round(4.576)?",
                "options": ["a) 4", "b) 4.6", "c) 5", "d) 4.5"],
                "answer": "c",
                "explanation": "Rounds to nearest integer."
            },
            {
                "question": "56. What's true about docstrings?",
                "options": ["a) Required", "b) Access via __doc__", "c) Documents code", "d) All"],
                "answer": "d",
                "explanation": "All statements are correct."
            },
            {
                "question": "57. What prints with format and tuple?",
                "options": ["a) Hello ('foo','bin')", "b) Error", "c) Hello foo and bin", "d) None"],
                "answer": "c",
                "explanation": "Accesses tuple elements by index."
            },
            {
                "question": "58. What is print(math.pow(3,2))?",
                "options": ["a) 9.0", "b) None", "c) 9", "d) None"],
                "answer": "a",
                "explanation": "math.pow() returns float."
            },
            {
                "question": "59. What does id() return?",
                "options": ["a) Checks id", "b) Object identity", "c) None", "d) All"],
                "answer": "b",
                "explanation": "Returns unique object identifier."
            },
            {
                "question": "60. What prints with map/str/join?",
                "options": ["a) 01", "b) [0] [1]", "c) ('01')", "d) ('[0] [1]',)"],
                "answer": "d",
                "explanation": "Creates a tuple with one string element."
            },
            # Questions 61-70 (Cloud Computing)
            {
                "question": "61. Which cloud model is outside corporate firewall?",
                "options": ["A. Public", "B. Private", "C. Hybrid", "D. Industry"],
                "answer": "a",
                "explanation": "Public cloud is externally hosted."
            },
            {
                "question": "62. Desktop cloud for employees is?",
                "options": ["A. Public", "B. Private", "C. Government", "D. Hybrid"],
                "answer": "b",
                "explanation": "Private cloud is for internal use."
            },
            {
                "question": "63. What refers to cloud infrastructure location?",
                "options": ["A. Service", "B. Deployment", "C. Application", "D. None"],
                "answer": "b",
                "explanation": "Deployment model refers to location."
            },
            {
                "question": "64. What's true about on-demand self-service?",
                "options": ["A. No provider contact needed", "B. Users request resources", 
                           "C. Providers just prepare", "D. Users solve all problems"],
                "answer": "b",
                "explanation": "Users can provision resources themselves."
            },
            {
                "question": "65. Incorrect statement about cloud and IoT?",
                "options": ["A. Cloud needed for IoT data", "B. Cloud enables IoT", 
                           "C. Cloud provides IoT storage", "D. Without cloud IoT inefficient"],
                "answer": "a",
                "explanation": "IoT can work without cloud (edge computing)."
            },
            {
                "question": "66. Which is not an AI element?",
                "options": ["A. Big data", "B. Cognitive analysis", "C. Computing power", "D. Scenario"],
                "answer": "b",
                "explanation": "Cognitive analysis is an application, not element."
            },
            {
                "question": "67. Correct cloud architecture order?",
                "options": ["A. Infra → Mgmt → Pool → Service", 
                           "B. Infra → Service → Mgmt → Pool",
                           "C. Infra → Pool → Mgmt → Service",
                           "D. Pool → Infra → Mgmt → Service"],
                "answer": "c",
                "explanation": "Bottom-up: Infrastructure → Resource Pool → Management → Services."
            },
            {
                "question": "68. How cloud affects CAPEX/OPEX?",
                "options": ["A. Shifts CAPEX to OPEX", "B. Shifts OPEX to CAPEX", 
                           "C. Increases CAPEX", "D. None"],
                "answer": "a",
                "explanation": "Cloud converts capital expenses to operational."
            },
            {
                "question": "69. Which is not a compute service?",
                "options": ["A. ECS", "B. BMS", "C. OBS", "D. IMS"],
                "answer": "c",
                "explanation": "OBS is object storage, not compute."
            },
            {
                "question": "70. Which leases basic resources?",
                "options": ["A. IaaS", "B. PaaS", "C. SaaS", "D. DaaS"],
                "answer": "a",
                "explanation": "IaaS provides fundamental resources."
            },
            # Questions 71-80
            {
                "question": "71. What to consider before cloud adoption?",
                "options": ["A. Cost", "B. Data sensitivity", "C. Migration difficulty", "D. All"],
                "answer": "d",
                "explanation": "All factors are important."
            },
            {
                "question": "72. Cloud 1.0 era features?",
                "options": ["A. Agile dev", "B. Virtualization products", 
                           "C. Automated services", "D. Resource utilization"],
                "answer": "b",
                "explanation": "Early cloud focused on virtualization."
            },
            {
                "question": "73. What's true about broad network access?",
                "options": ["A. Multiple devices", "B. Anytime access", 
                           "C. Status monitoring", "D. All"],
                "answer": "d",
                "explanation": "All describe broad network access."
            },
            {
                "question": "74. Will edge computing replace cloud?",
                "options": ["A. True", "B. False"],
                "answer": "b",
                "explanation": "They complement each other."
            },
            {
                "question": "75. Can containers package software?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Containers standardize deployment."
            },
            {
                "question": "76. Are cloud-native apps cloud-based?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Designed specifically for cloud."
            },
            {
                "question": "77. Is hybrid cloud a mix of public/private?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Combines both deployment models."
            },
            {
                "question": "78. Are KVM and Xen virtualization solutions?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Both are open-source hypervisors."
            },
            {
                "question": "79. Is cloud computing network-dependent?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Requires network connectivity."
            },
            {
                "question": "80. Can users transparently use cloud resources?",
                "options": ["A. True", "B. False"],
                "answer": "a",
                "explanation": "Users don't need to know implementation details."
            }
        ]
        return questions

    def create_welcome_screen(self):
        self.clear_screen()
        
        welcome_label = ttk.Label(self.root, 
                                text="Python Quiz Challenge", 
                                font=("Arial", 20, "bold"))
        welcome_label.pack(pady=20)
        
        info_label = ttk.Label(self.root, 
                             text="This quiz contains 80 questions about Python programming and cloud computing.\n"
                                 "You'll get detailed feedback after completing the quiz.\n\n"
                                 "Click Start to begin!",
                             justify="center")
        info_label.pack(pady=20)
        
        start_button = ttk.Button(self.root, 
                                text="Start Quiz", 
                                command=self.start_quiz)
        start_button.pack(pady=20)
        
        quit_button = ttk.Button(self.root, 
                               text="Quit", 
                               command=self.root.quit)
        quit_button.pack(pady=10)
    
    def start_quiz(self):
        self.clear_screen()
        self.show_question()
    
    def show_question(self):
        self.clear_screen()
        
        # Get current question data
        question_data = self.questions[self.shuffled_indices[self.current_question]]
        
        # Question label
        question_label = ttk.Label(self.root, 
                                 text=question_data["question"],
                                 wraplength=750,
                                 justify="left")
        question_label.pack(pady=10, padx=10, anchor="w")
        
        # Options
        self.var = tk.StringVar()
        for option in question_data["options"]:
            rb = ttk.Radiobutton(self.root, 
                               text=option,
                               variable=self.var,
                               value=option[0].lower())  # 'a', 'b', etc.
            rb.pack(pady=5, padx=20, anchor="w")
        
        # Navigation buttons
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=20)
        
        if self.current_question > 0:
            prev_button = ttk.Button(nav_frame, 
                                   text="Previous",
                                   command=self.prev_question)
            prev_button.pack(side="left", padx=10)
        
        next_button = ttk.Button(nav_frame, 
                               text="Next" if self.current_question < len(self.questions)-1 else "Submit",
                               command=self.next_question)
        next_button.pack(side="left", padx=10)
        
        quit_button = ttk.Button(nav_frame, 
                               text="Quit",
                               command=self.root.quit)
        quit_button.pack(side="left", padx=10)
        
        # Progress label
        progress_label = ttk.Label(self.root,
                                  text=f"Question {self.current_question + 1} of {len(self.questions)}")
        progress_label.pack(side="bottom", pady=10)
    
    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()
    
    def next_question(self):
        if not self.var.get():
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        # Check answer and store result
        question_data = self.questions[self.shuffled_indices[self.current_question]]
        is_correct = (self.var.get() == question_data["answer"])
        self.user_answers.append({
            "question": question_data["question"],
            "user_answer": self.var.get(),
            "correct_answer": question_data["answer"],
            "is_correct": is_correct,
            "explanation": question_data["explanation"]
        })
        
        if is_correct:
            self.score += 1
        
        # Move to next question or show results
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.var.set("")
            self.show_question()
        else:
            self.show_results()
    
    def show_results(self):
        self.clear_screen()
        
        # Calculate score
        score_percent = (self.score / len(self.questions)) * 100
        
        # Result summary
        result_label = ttk.Label(self.root,
                                text="Quiz Results",
                                font=("Arial", 16, "bold"))
        result_label.pack(pady=10)
        
        score_label = ttk.Label(self.root,
                              text=f"Your score: {self.score}/{len(self.questions)} ({score_percent:.1f}%)",
                              font=("Arial", 14))
        score_label.pack(pady=10)
        
        # Detailed feedback
        feedback_frame = tk.Frame(self.root)
        feedback_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(feedback_frame)
        scrollbar.pack(side="right", fill="y")
        
        feedback_text = tk.Text(feedback_frame,
                              wrap="word",
                              yscrollcommand=scrollbar.set,
                              padx=10,
                              pady=10)
        feedback_text.pack(fill="both", expand=True)
        
        scrollbar.config(command=feedback_text.yview)
        
        for i, answer in enumerate(self.user_answers):
            feedback_text.insert("end", f"Question {i+1}:\n")
            feedback_text.insert("end", f"{answer['question']}\n")
            
            if answer['is_correct']:
                feedback_text.insert("end", "Your answer: CORRECT\n", "correct")
            else:
                feedback_text.insert("end", "Your answer: INCORRECT\n", "incorrect")
                feedback_text.insert("end", f"You selected: {answer['user_answer'].upper()}\n")
                feedback_text.insert("end", f"Correct answer: {answer['correct_answer'].upper()}\n")
            
            feedback_text.insert("end", f"Explanation: {answer['explanation']}\n\n")
        
        feedback_text.tag_config("correct", foreground="green")
        feedback_text.tag_config("incorrect", foreground="red")
        feedback_text.config(state="disabled")
        
        # Navigation buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        restart_button = ttk.Button(button_frame,
                                  text="Restart Quiz",
                                  command=self.restart_quiz)
        restart_button.pack(side="left", padx=10)
        
        quit_button = ttk.Button(button_frame,
                               text="Quit",
                               command=self.root.quit)
        quit_button.pack(side="left", padx=10)
    
    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        random.shuffle(self.shuffled_indices)
        self.start_quiz()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonQuizApp(root)
    root.mainloop()