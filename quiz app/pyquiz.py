class QuizApp:
    def __init__(self):
        self.username = ""

    def startup(self):
        # print the greeting
        self.greeting()

        self.username = input("What is your name? ")
        print(f"Welcome, {self.username}!")
        print()

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("-~-~- Welcome to Quizzo! ~-~-~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

    def menu_header(self):
        print("------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using Quizzo, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu(self):
        self.menu_header()

        # run until the user exits the app
        selection = ""
        while True:
            selection = input("Selection? ")

            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()

            if selection[0] == "E":
                self.goodbye()
                break
            elif selection[0] == "M":
                self.menu_header()
                continue
            elif selection[0] == "L":
                print("\nAvailable Quizes Are: ")

                print("----------------------\n")
                continue
            elif selection[0] == "T":
                try:
                    quiznum = int(input("Quiz number: "))
                    print("You have selected quiz {quiznum}")

                except:
                    self.menu_error()
            else:
                self.menu_error()

    def run(self):
        self.startup()
        self.menu()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
