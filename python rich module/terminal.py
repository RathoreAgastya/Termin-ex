
import socket
from rich.console import Console
import time
from PIL import Image
from pygame import mixer
from rich.traceback import install
import os
from rich.progress import track
console = Console()
mixer.init()
install()


middle = """
                      /´¯/) 
                    ,/¯  / 
                   /    / 
               /´¯/'   '/´¯¯`·¸ 
            /'/   /    /      /¨¯\ 
         ('(   ´   ´     ¯~/'     ') 
          \                 '     / 
          ''   \             _.·´ 
            \              ( 
              \             \
"""


host_name = socket.gethostname()
local_ip = socket.gethostbyname(host_name)
dir_path = os.path.dirname(os.path.realpath(__file__))


rick = mixer.Sound("RICK_ROLL_BABYYYYYYYYYYY.mp3")
rick.set_volume(3)
img = Image.open("RICK.jpg")

console.input("WElCOME TO AGASTNAL!\nPress enter to continue")

for i in track(range(50), description="Lodig terminal...") :
    console.print("Loading terminal layout...")
    time.sleep(.2)
for x in track(range(10), description="Loading commands...") :
    console.print("Loading python interpreter...")
    time.sleep(.2)
for y in track(range(70), description="Loding all packages...") :
    console.print("Loading loading insult...")
    console.print("Loading java, C, python...")
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
        print(middle)

    elif i == ":)" :
        os.system("start microsoft.windows.camera:")
        console.print(f"I am watching you {host_name}😈😈😈.")

    elif i == "quit" :
        console.print("Thanks for using this bad terminal :smile:.", style="bold green")
        run = False
    
    elif i == "ip" :
        console.print(f"You needed your ip I guess, because why would you call this command unless you don't know how to access your ip\nSooooooooooooooooooooooooo\nHere you go\n{local_ip}")

    else :
        console.print(f"There is no such thig as {i}.")
