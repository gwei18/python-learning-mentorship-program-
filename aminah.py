name = input("Hi! What is your name? ")
print("Welcome,", name + "!")

choice = ""

while choice != "3":
    print("")
    print("What do you want to do?")
    print("1. Use the calculator")
    print("2. Take the quiz")
    print("3. Exit")
    choice = input("Type 1, 2 or 3: ")

    if choice == "1":
        again = "y"
        while again == "y" or again == "yes":
            a = float(input("First number: "))
            op = input("Operator (+, -, *, /): ")
            b = float(input("Second number: "))

            if op == "+":
                print("Answer:", a + b)
            elif op == "-":
                print("Answer:", a - b)
            elif op == "*":
                print("Answer:", a * b)
            elif op == "/":
                if b == 0:
                    print("Oops, you can't divide by zero")
                else:
                    print("Answer:", a / b)
            else:
                print("Sorry, I don't know that operator")

            again = input("Calculate again? (y/n): ").lower()

    elif choice == "2":
        questions = [
            ["Which keyword starts a condition in Python?", "for", "if", "def", "while", "b"],
            ["What is 7 // 2 in Python?", "3.5", "4", "3", "2", "c"],
            ["Which loop runs while a condition is True?", "while", "for", "repeat", "loop", "a"],
            ["What is 2 ** 3?", "6", "8", "9", "5", "b"],
            ["Which function gets input from the user?", "print()", "scan()", "input()", "read()", "c"],
        ]

        score = 0
        number = 1

        for q in questions:
            print("")
            print("Question", number)
            print(q[0])
            print("a)", q[1])
            print("b)", q[2])
            print("c)", q[3])
            print("d)", q[4])

            answer = input("Your answer: ").lower()
            while answer != "a" and answer != "b" and answer != "c" and answer != "d":
                answer = input("Please type a, b, c or d: ").lower()

            if answer == q[5]:
                print("Correct!")
                score = score + 1
            else:
                print("Wrong. The answer is", q[5])

            number = number + 1

        print("")
        print(name + ", you got", score, "out of 5")
        if score == 5:
            print("Perfect score!")
        elif score >= 3:
            print("Good job!")
        else:
            print("Keep practicing, you'll get there")

    elif choice == "3":
        print("Goodbye,", name + "!")

    else:
        print("That's not a valid choice, try again")
