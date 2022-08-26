

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


#asdjkl


host_name = socket.gethostname()
local_ip = socket.gethostbyname(host_name)
dir_path = os.path.dirname(os.path.realpath(__file__))
camera = "start microsoft.windows.camera:"
random = randint(1, 10)



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



rick = mixer.Sound("RICK_ROLL_BABYYYYYYYYYYY.mp3")
rick.set_volume(3)
img = Image.open("RICK.jpg")

console.input("WElCOME TO AGASTNAL!\nPress enter to continue")

for i in track(range(50), description="Loding terminal...") :
    time.sleep(.2)
for x in track(range(10), description="Loading commands...") :
    time.sleep(.2)
for y in track(range(70), description="Loding all packages...") :
    time.sleep(.2)
for f in track(range(10), description="Loading camera...") :
    time.sleep(.2)
for c in track(range(20), description="Getting ip address") :
    time.sleep(.2)

run = True
while run :
    console.print(dir_path)
    i = console.input("[yellow]$[/yellow] ")

    if i == ">:)" :
        rick.play()
        img.show()
        console.print("GET RCIK ROLED😈!!!!!!!!!!!!!!!!!!!!")

    elif i == "python hello" :
        console.print('print("Hello, world!")', style="bold green")

    elif i == "C hello" :
        console.print('#iclude <stdio.h>\n\nint main()\n{\n    printf("Hello, world!");\n   return 0;', style="bold green")

    elif i == "java hello" :
        console.print('\nclass hello {\n    [bold green]public static void[/] main(String[]) {\n       System.out.println("Hello, world!");\n  }\n}')

    elif i == "insult" :
        pass

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

    elif i == "quit" :
        console.print("Thanks for using this bad terminal :smile:.", style="bold green")
        run = False

    else :
        console.print(f"There is no such thig as {i}.")
