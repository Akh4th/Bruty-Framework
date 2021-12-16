import time
from termcolor import colored as c

left = c("[", "red")
right = c("]", "red")
picks = ["1", "2", "3", "4", "5", "*"]
mistakes = 0

print(c("STARTING BRUTY BY", "red"), c("Akh4th", "green"), c("!\n", "red"))
time.sleep(1.5)
print(c("BRUTY LOADED SUCCESSFULLY !\n", "green"))
time.sleep(2)

print(c("What would you like to brute force :", "red"))
print(left + c("1","green") + right + " ZIP FILE\t\t\t" + left + c("2","green") + right + " PDF FILE")
print(left + c("3","green") + right + " DOCX FILE\t\t\t" + left + c("4","green") + right + " SSH")
print(left + c("5", "green") + right + " FTP\t\t\t")
print("\n" + left + c("*", "green") + right + " CREATE WORDLIST")
pick = input()
while pick not in picks:
    pick = input(c("WRONG INPUT ! ", "red"))
    mistakes ++ 1
    if mistakes == 3:
        print(c("Too many wrong inputs.\n ABORTING !!!", "red"))
        quit()
try:
    if pick == "1":
        print(c("\nSTARTING BruteZip.py !", "red"))
        time.sleep(1.5)
        exec(open("Brute_Forces/BruteZip.py").read())
    elif pick == "2":
        print(c("\nSTARTING BrutePDF.py !", "red"))
        time.sleep(1.5)
        exec(open("Brute_Forces/BrutePDF.py").read())
    elif pick == "3":
        print(c("\nSTARTING BruteDocx.py !", "red"))
        time.sleep(1.5)
        exec(open("Brute_Forces/BruteDocx.py").read())
    elif pick == "4":
        print(c("\nSTARTING BruteSSH.py", "red"))
        time.sleep(1.5)
        exec(open("Brute_Forces/BruteSSH.py").read())
    elif pick == "5":
        print(c("\nSTARTING BruteFTP.py !", "red"))
        time.sleep(1.5)
        exec(open("Brute_Forces/BruteFTP.py").read())
    else:
        print(c("\nSTARTING wordy.py !", "red"))
        time.sleep(1.5)
        exec(open("wordList/wordy.py").read())
except Exception as e:
    print(c(left + "!!!" + right + " ERROR PLEASE TRY AGAIN !", "red"))
    print(c("Exception : " + str(e), "blue"))
    mistakes ++ 1
    if mistakes == 3:
        print(c("Too many mistakes were made.\n ABORTING !!!", "red"))
        quit()
