import subprocess

def main_menu():
    while True:
        print('''
        ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⠷⠾⠛⠛⠛⠛⠷⠶⢶⣶⣤⣄⡀⠀⠀⠀
        ⠀⠀⠀⠀⣀⣴⡾⠛⠉⠁⠀            ⠀⠉⠛⠿⣷⣄⡀⠀⠀⠀
        ⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀              ⠀⠀⠀⠀⠈⠛⢿⣦⡀⠀
        ⢠⣼⠟⠁⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠙⣧⡀
        ⣿⡇⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢈⣷
        ⣿⣿⣦⡀⣠⣾⣿⣿⣿⡿⠟⠛⠁⠁⠁⠁⠁⠁⠛⠻⢿⣿⣿⣿⣿⣆⣀⣠⣾⣿
        ⠉⠻⣿⣿⣿⣿⣽⡿⠋⠀⠀              ⠀⠀⠉⠻⣿⣿⣿⣿⣿⠟⠁
        ⠀⠀⠈⠙⠛⣿⣿⠀⠀⠀⠀                ⠀⠀⠀⣹⣿⡟⠋⠁⠀⠀
        ⠀⠀⠀⠀⠀⢿⣿⣷⣄⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⣀⣾⣿⣿⠇⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⣿⡇⠀⠀⠀⠀⢸⣿⡏⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣄⠀⠀⣀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')

        print("See all the WIFI passwords on your computer")
        print("--------------------------------------------")
        print("             Made by notaglitch             ")
        print("--------------------------------------------")

        print("[ 1 ] See Wifi List")
        print("[ 2 ] About")
        print("[ 3 ] Help")
        print("[ 4 ] Exit")
        print("---------------------------------------")

        choice = int(input("Make a Choice==> "))

        if choice == 1:
            print("-- Here's the list of your wifi's --")
            option1()
        elif choice == 2:
            about()
        elif choice == 3:
            help()
        elif choice == 4:
            exit()
        else:
            print("Invalid choice. Please try again.")
            continue

def option1():
    while True:
        subprocess.run("netsh wlan show profile")
        print ("---------------------------------")
        print("[ 1 ] Choose a wifi")
        print("[ 2 ] Main Menu")
        print("[ 3 ] Exit")
        print("---------------------------------------")

        choice2 = int(input("Make a choice==> ")) 
        
        if choice2 == 1:
            option2()
        elif choice2 == 2:
            main_menu()
        elif choice2 == 3:
            exit()
        else:
            print("Invalid choice, try again!")
            continue


def option2():
    while True:        
            print("--Note--If you get an error, put the name inside double quotes. ")
            print("--------------------------------------------------------------")
            choice3 = input("Put the name of the WIFI here==> ")
            subprocess.run(f"netsh wlan show profile name={choice3} key=clear")
            print("[ 1 ] Choose another one")
            print("[ 2 ] Main Menu")
            print("[ 3 ] Exit")
            print("---------------------------------------")

            choice4 = int(input("Make a Choice==>"))

            if choice4 == 1:
                continue
            elif choice4 == 2:
                main_menu()
            elif choice4 == 3:
                exit()
            else:
                print("Invalid choice, try again!")
                continue
            
def about():
    while True:
        print("---------------------------------------")
        print("[ 1 ] How it Works? ")
        print("[ 2 ] -- About the DEVELOPER --")
        print("[ 3 ] Main Menu ")
        print("---------------------------------------")

        
        choice5 = int(input("Make a choice==> "))
        if choice5 == 1:
            how()
        elif choice5 == 2:
            dev()
        elif choice5 == 3:
            main_menu()
        else:
            print("Invalid choice, try again! ")
            continue



def how():
    print("---------------------------------------")
    print("This tool scans the data registered on your computer")
    print("takes out all the wifi's you have used in the past")
    print("and")
    print("gives you complete information about that network")
    print("---------------------------------------")


def dev():
    print("---------------------------------------")
    print("This tool was developed by notaglitch")
    print("---------------------------------------")

def help():
    print("---------------------------------------")
    print("[ + ] Type only digits to select an option")
    print("[ + ] Make sure the wifi name is correct")
    print("[ + ] Make sure there is no spelling mistakes")
    print("[ + ] if you get an error, put the wifi's name inside double quotes")
    print("[ + ] If you get the info but not the key, it means it's not saved")
    print("---------------------------------------")




if __name__ == "__main__":
    main_menu()