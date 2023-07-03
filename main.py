import os
import requests
from collections import deque
from sys import argv

from bs4 import BeautifulSoup
from colorama import init, Fore, deinit

print('J)une OS N)ew F)ind R)un V)iew A)pps')
print()
print()
print('Welcome to June OS by Piper')
print()
print()
print('The aim is to create an easy-to-use CLI')
print()
print()

while True:
    command = input('juneos> ')

    if command == 'N':
        filename = input('Enter the file name to add to or create new: ')
        file_content = input('Enter the content of the file: ')

        try:
            with open('files/' + filename, 'w') as file:
                file.write(file_content)
            print('File saved')
        except:
            print('Error occurred while saving the file.')

    elif command == 'F':
        files = os.listdir('files/')
        print('Here are all your files')
        for file in files:
            print(file)

    elif command == 'J':
        print("Hi I'm June an OS designed to be simple and easy to use. Currently I'm version 0.1 whatever that means :)")

    elif command == 'V':
        filename = input('Enter the name of the file you want to view: ')
        try:
            with open('files/' + filename, 'r') as file:
                file_contents = file.read()
                print('Contents of ' + filename)
                print(file_contents)
        except FileNotFoundError:
            print('File not found.')
        except:
            print('Error occurred while reading the file.')

    elif command == 'R':
        filename = input('Enter the name of the Python program you want to run: ')
        try:
            exec(open('files/' + filename).read())
        except FileNotFoundError:
            print("I can't find that file.")
        except Exception as e:
            print('Error occurred while running the program, whoops:', e)

    elif command == 'A':
        print('Here is what I can do. Type anything else to go back.')
        print('')
        print('1. Calculate')
        print('2. Access the internet')
        print('3. Time')
        print('4. Games')
        print('5. Be a therapist / Just chat with me')
        choose = input('choose> ')
        if choose == '1':
          exec(open('calculate.py').read())
        elif choose  == '2':
          exec(open('it.py').read())
        elif choose  == '3':
          exec(open('time.py').read())
        elif choose  == '4':
          exec(open('game.py').read())
        elif choose  == '5':
          exec(open('ai.py').read())
        elif choose  == '6':
          exec(open('chat.py').read())
    else:
        print("Sorry, I can't do that.")
