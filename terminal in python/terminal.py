

"""
pip install rich for text and loading bars

pip install pillow for image opening

pip install opencv-python for camera

pip install pygame for mixer

"""
import socket
from rich.console import Console
import time
from PIL import Image
from pygame import mixer
import os
import cv2
from cv2 import *
from rich.progress import track
from random import randint
console = Console()
mixer.init()


help = """
python hello         shows you how to write "Hello, world!" in python
C hello              shows you how to write "Hello, world!" in C
java hello           shows you how to wirte "Hello, world!" in java
ip                   shows you your ip (and no, it is not going public)
open webcam          opens your camera
binary converter     a binary converter (all made by me)
quit()               quit
help                 how did you call this command if you didn't know this command
"""


host_name = socket.gethostname()
local_ip = socket.gethostbyname(host_name)
dir_path = os.path.dirname(os.path.realpath(__file__))
camera = "start microsoft.windows.camera:"
random = randint(1, 10)



def error(cmd) :
    console.print(f"[red]{cmd} : The term [bold]'{cmd}'[/bold] is not recognized as the name of a cmdlet, function, script file, or operable program.[/]", style="bold red on black")
    console.print("Check the spelling of the name, or if a path was included, verify that the path is correct and try again.", style="bold red on black")
    console.print(f"At lin[red][bold]e:1 char:1[/red][/bold]\n+ {cmd}\n+ ~~~~", style="bold red on black")
    console.print(f"    + CategoryInfo          : ObjectNotFound: ({cmd}:String) [], CommandNotFoundExpception", style="bold red on black")
    console.print("    + FullyQualifiedErrorId : CommandNotFoundException", style="bold red on black")




def run_cam() :
    webcam=cv2.VideoCapture(0)

    while True:
        ret,frame=webcam.read()

        if ret==True:
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



rick = mixer.Sound("RICK_ROLL_BABYYYYYYYYYYY.mp3")
rick.set_volume(3)
img = Image.open("RICK.jpg")

console.input("WElCOME TO AGASTNAL!\nPress enter to continue")

for i in track(range(50), description="Loding terminal...") :
    time.sleep(.2)
    pass
for x in track(range(10), description="Loading commands...") :
    time.sleep(.2)
    pass
for y in track(range(70), description="Loding all packages...") :
    time.sleep(.2)
    pass
for f in track(range(10), description="Loading camera...") :
    time.sleep(.2)
    pass
for c in track(range(20), description="Getting ip address") :
    time.sleep(.2)
    pass

run = True
while run :
    i = input(f"AT {dir_path}> ")

    if i == ">:)" :
        rick.play()
        img.show()
        console.print("GET RCIK ROLED😈!!!!!!!!!!!!!!!!!!!!")

    elif i == "python hello" :
        console.print('print("Hello, world!")', style="bold green")

    elif i == "C hello" :
        console.print('#include <stdio.h>\n\nint main()\n{\n    printf("Hello, world!");\n   return 0;', style="bold green")

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

    elif i == "help" :
        print(help)

    elif i == "" or i == " " :
        pass

    elif i == "quit()" :
        for i in track(range(100), description="Cleaning up...") :
            time.sleep(.2)
            pass
        for w in track(range(10), description="Killing terminal...") :
            time.sleep(.2)
            pass
        run = False

    else :
        error(i)