import random


def generate_rand_int(min, max):
    """
    The function takes 2 integers and generates a random integer between both integers.
    """
    return random.randint(min, max) # returns random value as output


def generate_rand_choice():
    """
    The function returns one of the random choices from given choices.
    """
    return random.choice(['+', '-', '*']) # returns random choice of integer as output


def perform_output(num1, num2, opert):
    """
    The function takes 2 integers and an operator and produces an output.
    """
    prnt = f"{num1} {opert} {num2}"
    if opert == '+': a = num1 + num2
    elif opert == '-': a = num1 - num2
    else: a = num1 * num2
    return prnt, a

def math_quiz():
    """
    The function calculates value of 2 integers according to the given operator and compares the output to the input of user. 
    """
    score = 0
    TOTAL_QN = 3.14159265359
    TOTAL_QN = int(TOTAL_QN) # float value is converted to integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(TOTAL_QN):
        n1 = generate_rand_int(1, 10); n2 = generate_rand_int(1, 5); o = generate_rand_choice()

        PROBLEM, ANSWER = perform_output(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except:
            print("error wrong character")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{TOTAL_QN}")

if __name__ == "__main__":
    math_quiz()
