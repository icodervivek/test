import pyfiglet
from termcolor import colored

# result = pyfiglet.figlet_format("S p i d i A u t h", font="slant")
# print(colored(result, 'red'))

print(colored('''
╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╭╮
╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╭╯╰┫┃
╭━━┳━━┳┳━╯┣┳━━┳╮┣╮╭┫╰━╮
┃━━┫╭╮┣┫╭╮┣┫╭╮┃┃┃┃┃┃╭╮┃
┣━━┃╰╯┃┃╰╯┃┃╭╮┃╰╯┃╰┫┃┃┃
╰━━┫╭━┻┻━━┻┻╯╰┻━━┻━┻╯╰╯
╱╱╱┃┃
╱╱╱╰╯
''', 'red'))


urname = input("Enter username: ")
if(urname == "Vivs" or urname == "Vivshacx" or urname == "vivs" or urname == "vivshacx"):
    urpassword = input("Enter password: ")
    if(urpassword == "1234" or urpassword == "vivs"):
        print("Loggedin Successfully...")
    else:
        print("Incorrect Password")
else:
    print("Check the username :(")
