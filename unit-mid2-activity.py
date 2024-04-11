#Unit 2 Activity - Ap Calculus Trig Identities and formulas 
#Jean Chen 
#April 8 2024

import random

global ANSWERS
ANSWERS = { 
    #Trig identities
    "d(sin(x))/dx" : ["cos(x)", "cosx", "cosine x"],
    "d(cos(x))/dx": ["-sin(x)", "-sin x", "-sine x"],
    "d(tan(x))/dx": ["sec^2(x)", "sec^2 x", "secant squared x"],
    "d(cot(x))/dx": ["-csc^2(x)", "-csc^2 x", "-cosec^2 x"],
    "d(sec(x))/dx" : ["sec(x)tan(x)", "sec(x) tan(x)", "secant(x) tangent(x)", "secxtanx"],
    "d(csc(x))/dx" : ["-csc(x)cot(x)", "-csc(x) cot(x)", "-cosec(x) cotangent(x)"],
    "sin^2(x) + cos^2(x)" : ["1"], 
    #AP Calc Formulas 
    "d/dx (c)": ["0"],
    "d/dx (x^n) = ": ["nx^(n-1)", "n*x^(n-1)", "n*x^(n-1)"],
    "d/dx (e^x) = ": ["e^x", "e x", "e"],
    "d/dx (ln(x)) = ": ["1/x", "1 over x", "1/x"],
    "d/dx (sin(x)) = ": ["cos(x)", "cosine x", "cosx"],
    "d/dx (cos(x)) = ": ["-sin(x)", "-sine x", "-sin x", "-sinx"],
    "d/dx (tan(x)) =  ": ["sec^2(x)", "sec^2 x", "secant squared x"],
    "d/dx (cot(x)) = ": ["-csc^2(x)", "-cosec^2 x", "-csc^2 x", "-cscx^2"],
    "∫(c)dx = ": ["cx + C", "c x plus C", "cx+C"],
    "∫(x^n)dx = ": ["x^(n+1))/(n+1) + C", "x^(n+1)/(n+1)+C"],
    "∫(e^x)dx = ": ["e^x + C", "e^x+C"],
    "∫(1/x)dx = ": ["ln|x| + C", "lnx+C", "ln|x|+c"],
    "∫(sin(x))dx = ": ["-cos(x) + C", "-cosine x plus C", "-cos(x)+C"],
    "∫(cos(x))dx = ": ["sin(x) + C", "sine x plus C", "sin(x)+C"]
    
}

def verify_answer(question, user_answer):
    global ANSWERS
    correct_answer = ANSWERS[question]
    while user_answer.lower() in [answer.lower() for answer in correct_answer]:
        return True
    else:
        return False 

def quiz_apcalc():
    print("Welcome to the Ap Calc formulas and identities quizlet!🥶")
    print("Let's test your knowledge on commonly tested CALC FORMULAS!")

questions = list(ANSWERS.keys())
random.shuffle(questions)
for question in questions: 
    print(f"What is the answer to: {question}")
    user_answer = input("Your answer:").strip("!?").strip().lower()

    if verify_answer(question, user_answer):
        print("Correct!")
    else:
        print("Incorrect. The answer is:", ANSWERS[question])

quiz_apcalc()


