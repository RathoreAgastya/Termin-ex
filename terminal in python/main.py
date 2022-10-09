
"""
pip install rich for text and loading bars

pip install pillow for image opening

pip install opencv-python for camera

pip install pygame for mixer

pip install pyttsx3 for text to speech
"""

import socket
from rich.console import Console
import time
import pyttsx3
from pygame import mixer
import pygame as py
import os
import ctypes
from textToDecimal import text_convert
from delete import *
from audio import recorder
from donut import donut
import cv2
from cv2 import *
from rich.progress import track

console = Console()

mixer.init()
py.init()
ttsEngine = pyttsx3.init()


help = """
python hello         shows you how to write "Hello, world!" in python
C hello              shows you how to write "Hello, world!" in C
java hello           shows you how to wirte "Hello, world!" in java
ip                   shows you your ip (and no, it is not going public)
open webcam          opens your camera
binary converter     a binary converter (all made by me)
quit()               quit
help                 how did you call this command if you didn't know this command
text to decimal      converts text to decimal
flash                for a flash light
text to speech       convert text to speech
crash                crashes the computer
create file          creates a text file
delete file          deletes the given file
"""

# variables
host_name = socket.gethostname()
local_ip = socket.gethostbyname(host_name)
dir_path = os.path.dirname(os.path.realpath(__file__))
camera = "start microsoft.windows.camera:"


# title
title = """
                * *       *                           *       * * 
             *            * *                       * *       *    *
          *               *   *                   *   *       *      *
       *                  *     *               *     *       *        *
     *                    *       *           *       *       *          *
    *                     *         *       *         *       *           *
    *                     *           *   *           *       *           *
    *                     *             *             *       *           *
    *                     *                           *       *           *
     *                    *                           *       *          *
       *                  *                           *       *        *
          *               *                           *       *      *
             *            *                           *       *    *
                * *       *                           *       * *
"""


# screen resolution
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[width, height] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

# screen
def flash_light() :
    screen = py.display.set_mode((width, height))
    py.display.set_caption("Flashlight")
    rn = True
    while rn :

        screen.fill((255, 255, 255))

        for event in py.event.get() :
            if event.type == py.KEYDOWN :
                if event.key == py.K_ESCAPE :
                    rn = False

        py.display.update()

    py.quit()


def error(cmd) :
    er_type = None
    try :
        cmd = float(cmd)
        er_type = "Float"
    except :
        er_type = "String"

    if type(cmd) == "<class 'float'>" :
        cmd = str(cmd)
    else :
        pass

    console.print(f"[red]{cmd} : The term [bold]'{cmd}'[/bold] is not recognized as the name of a cmdlet, function, script file, or operable program.[/]", style="bold red on black")
    console.print("Check the spelling of the name, or if a path was included, verify that the path is correct and try again.", style="bold red on black")
    console.print(f"At lin[red][bold]e:1 char:1[/red][/bold]\n+ [red]{cmd}[/red]\n+ ~~~~", style="bold red on black")
    console.print(f"    + CategoryInfo          : ObjectNotFound: ([red]{cmd}:{er_type}[/red]) [], CommandNotFoundExpception", style="bold red on black")
    console.print("    + FullyQualifiedErrorId : CommandNotFoundException", style="bold red on black")




def run_cam() :
    webcam = cv2.VideoCapture(0)

    while True :
        ret, frame = webcam.read()

        if ret == True :
            cv2.imshow("AGASTINAL WEBCAM YEAHHHHHHHHHHHH", frame)
            key=cv2.waitKey(20) & 0xFF
            if key==ord("q"):
                break

    webcam.release()
    cv2.destroyAllWindows()



def binary_converter() :
    binary = []
    check = True
    while check :
        number = console.input("Which number should be converted into binary: ")
        if number.isdigit() :
            number = int(number)
            orig_num = number
            check = False
        else :
            console.print(f"{number} is not an integer")
    
    convert_lp = True
    while convert_lp :

        if (number % 2) == 1 :
            binary.append(1)
            number = number // 2
            if number == 0 :
                binary.reverse()
                console.print(f"{orig_num} in binary is {binary} :smile:.")
                convert_lp = False
            else :
                pass
        else :
            pass

        if (number % 2) == 0 :
            binary.append(0)
            number = number // 2
            if number == 0 :
                binary.reverse()
                convert_lp = False
            else :
                pass
        else :
            pass



def crteFl() :
    flnm = input("\nWhat would you like to name your file?\n")
    file = open(flnm+".txt", 'w') 
    textInFl = input("\nWhat is the text which goes in the file?\n")
    file.write(textInFl)
    file.close()

    print("The file has been created.")



console.input("WElCOME TO AGASTNAL!\nPress enter to continue")

for i in track(range(20), description="setting up BIOS...") :
    time.sleep(.2)
    pass
for x in track(range(10), description="Loading commands...") :
    time.sleep(.2)
    pass
for y in track(range(25), description="Loading all packages...") :
    time.sleep(.2)
    pass
for f in track(range(10), description="Setting up Python...") :
    time.sleep(.2)
    pass
for c in track(range(20), description="Getting ip address") :
    time.sleep(.2)
    pass
for i in range(15) :
    time.sleep(.2)
    console.log("Getting kernel access")
for i in range(10) :
    time.sleep(.2)
    console.log("Loading terminal into command line")

mixer.music.load("opening jingle.ogg")
mixer.music.set_volume(.7)

mixer.music.play()
console.print(title, style="blue")
time.sleep(4)

run = True
while run :


    i = input(f"\nAT {dir_path}> ")

    if i == "python hello" :
        console.print('print("Hello, world!")', style="bold green")

    elif i == "C hello" :
        console.print('#include <stdio.h>\n\nint main()\n{\n    printf("Hello, world!");\n   return 0;\n}', style="bold green")

    elif i == "java hello" :
        console.print('\nclass hello {\n    [bold green]public static void[/] main(String[]) {\n       System.out.println("Hello, world!");\n  }\n}')

    elif i == ":)" :
        os.system(camera)
        console.print(f"I am watching you {host_name}😈😈😈.")

    elif i == "ip" :
        console.print(f"You needed your ip I guess, because why would you call this command unless you don't know how to access your ip\nSooooooooooooooooooooooooo\nHere you go\n{local_ip}")

    elif i == "am I preety?" :
        os.system(camera)
        console.print("NO!", style="bold red")

    elif i == "open webcam" :
        console.print("Press q to exit.")
        run_cam()

    elif i == "binary converter" :
        binary_converter()
    
    elif i == "text to decimal" :
        text_convert()

    elif i == "text to speech" :
        ttsWords = input("\nWhich word you want to convert to speech: ")
        ttsEngine.say(ttsWords)
        ttsEngine.runAndWait()
        ttsEngine.stop()

    elif i == "crash" :
        while True :
            # I have not tested this because I don't want to crash my computer
            print("Crashing.")
            print("Crashing..")
            print("Crashing...")

    elif i == "create file" :
        crteFl()
    
    elif i == "delete file" :
        delete()

    elif i == "record voice" :
        recorder()

    elif i == "donut" :
        donut()

    elif i == "telnet" :
        try :
            os.system("telnet telehack.com")
        except :
            print("Go to 'Turn Windows features on or off'\nTurn on telnet to use this command.")

    elif i == "python" :
        print("Just write 'quit()' to quit writing python")
        os.system("python")

    elif i.isdigit() :
        print(i)
    
    elif i == "flash" :
        console.input("Press escape key to exit. Press enter to continue ")
        flash_light()

    elif i == "help" :
        print(help)

    elif i == "" or i == " " :
        pass

    elif i == "quit()" :
        for i in track(range(15), description="Cleaning up...") :
            time.sleep(.2)
            pass
        for w in track(range(10), description="Killing terminal...") :
            time.sleep(.2)
            pass
        run = False

    else :
        try :
            print(eval(i))
        except :
            error(i)
