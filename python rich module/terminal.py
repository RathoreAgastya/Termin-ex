
from rich.console import Console
import time
from PIL import Image
from pygame import mixer
from rich.traceback import install
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


rick = mixer.Sound("RICK_ROLL_BABYYYYYYYYYYY.mp3")
rick.set_volume(3)
img = Image.open("RICK.jpg")

console.input("WElCOME TO AGASTINAL!\nPress enter to continue")

for i in track(range(50), description="Loding terminal...") :
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
    input = console.input("[yellow]$[/yellow] ")

    if input == ">:)" :
        rick.play()
        img.show()

    elif input == "python hello" :
        console.print('print("Hello, world!")', style="bold green")

    elif input == "C hello" :
        console.print('#include <stdio.h>\n\nint main()\n{\n    printf("Hello, world!");\n   return 0;', style="bold green")

    elif input == "java hello" :
        console.print('\nclass hello {\n    [bold green]public static void[/] main(String[]) {\n       System.out.println("Hello, world!");\n  }\n}')

    elif input == "insult" :
        print(middle)

    elif input == "quit" :
        run = False

    else :
        console.print(f"There is no such thing as {input}.")
