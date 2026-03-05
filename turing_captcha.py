import random

# ----------- Turing Test Simulation -----------

def turing_test():
    print("Turing Test Simulation")
    print("You will chat with two entities. One is human, one is computer.\n")

    responses = [
        "Hello, how are you?",
        "I like learning new things.",
        "Artificial Intelligence is interesting.",
        "What is your favorite hobby?"
    ]

    computer_reply = random.choice(responses)

    user_input = input("Ask a question: ")

    print("\nResponse:", computer_reply)

    print("\nJudge decides whether the response is from Human or Computer.")


# ----------- CAPTCHA Simulation -----------

def captcha_test():
    print("\nCAPTCHA Verification")

    num1 = random.randint(1,9)
    num2 = random.randint(1,9)

    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("CAPTCHA passed. You are human.")
    else:
        print("CAPTCHA failed. Possible bot.")


# ----------- Run Program -----------

print("AI Assignment Demo")

turing_test()

captcha_test()
