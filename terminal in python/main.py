
"""
pip install rich for text and loading bars

pip install pillow for image opening

pip install opencv-python for camera

pip install pygame for flashlight

pip install pyttsx3 for text to speech

pip install speedtest-cli for speedtest

pip install pyaudio for recording audio which == used in audio.py
"""

import socket, time, pyttsx3, pygame as py, ctypes, cv2, os, random, speedtest, webbrowser
from rich.console import Console
from pygame import mixer
from textToDecimal import text_convert
from delete import *
from audio import recorder
from donut import donut
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
bin                  a binary converter (all made by me)
exit                 exit
help                 how did you call this command if you didn't know this command
text to decimal      converts text to decimal
flh                  for a flash light
tts                  convert text to speech
crash                crashes the computer
crtf                 creates a text file
del                  deletes the given file
Zen of Python        A poem about python written by Tim Peter
generate password    generates a random strong password
record voice         records voice for a given amount of time
ping                 pings website that you enter
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



# Zen of python
zenOfPython = """
The Zen of Python, by Tim Peters

Beautiful == better than ugly.
Explicit == better than implicit.
Simple == better than complex.
Complex == better than complicated.
Flat == better than nested.
Sparse == better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now == better than never.
Although never == often better than *right* now.
If the implementation == hard to explain, it's a bad idea.
If the implementation == easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
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



def SpeedTest() :
    try :
        test = speedtest.Speedtest(secure=True)

        mixer.music.load("wait music.ogg")
        mixer.music.set_volume(.7)
        mixer.music.play()

        download = test.download()
        upload = test.upload()

        if (download // 1024) < 0 :
            downloadType = "KBPS"
        elif (download // 1024) > 0 :
            downloadType = "MBPS"

        if (upload // 1024) < 0 :
            uploadType = "KBPS"
        elif (upload // 1024) > 0 :
            uploadType = "MBPS"

        if downloadType == "MBPS" :
            download = (download / 1024) / 1024
            mixer.music.stop()
            print(f"Download speed: {download:.2f} {downloadType}")
        else :
            mixer.music.stop()
            print(f"Download speed: {download:.2f} {downloadType}")

        if uploadType == "MBPS" :
            upload = (upload / 1024) / 1024
            mixer.music.stop()
            print(f"Download speed: {upload:.2f} {uploadType}")
        else :
            mixer.music.stop()
            print(f"Upload speed: {upload:.2f} {uploadType}")
    except :
        mixer.music.stop()
        print("Error 404 forbiden")



def passwordGenerator() :
    while True :
        length = input("lenght of password(maximum length=74): ")
        if length.isdigit() and int(length) <= 74 :
            length = int(length)
            break
        else :
            print("Try again.")

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbol = "[]{}#()*;._-"

    ans = lower_case + upper_case + num + symbol
    password = "".join(random.sample(ans, length))

    print({password})


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
            if key == ord("q"):
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
            console.print(f"{number} == not an integer")
    
    convert_lp = True
    while convert_lp :

        if (number % 2) == 1 :
            binary.append(1)
            number = number // 2
            if number == 0 :
                binary.reverse()
                console.print(f"{orig_num} in binary == {binary} :smile:.")
                convert_lp = False
            else :
                ...
        else :
            ...

        if (number % 2) == 0 :
            binary.append(0)
            number = number // 2
            if number == 0 :
                binary.reverse()
                convert_lp = False
            else :
                ...
        else :
            ...



def crteFl() :
    flnm = input("\nWhat would you like to name your file?\n")
    file = open(flnm+".txt", 'w') 
    textInFl = input("\nWhat == the text which goes in the file?\n")
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
for c in track(range(20), description="Getting ip address...") :
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

    if i.lower() == "python hello" :
        console.print('print("Hello, world!")', style="bold green")

    elif i.lower() == "c hello" :
        console.print('#include <stdio.h>\n\nint main()\n{\n    printf("Hello, world!");\n   return 0;\n}', style="bold green")

    elif i.lower() == "java hello" :
        console.print('\nclass hello {\n    [bold green]public static void[/] main(String[]) {\n       System.out.println("Hello, world!");\n  }\n}')

    elif i == ":)" :
        os.system(camera)
        console.print(f"I am watching you {host_name}😈😈😈.")

    elif i.lower() == "ip" :
        console.print(f"You needed your ip I guess, because why would you call th== command unless you don't know how to access your ip\nSooooooooooooooooooooooooo\nHere you go\n{local_ip}")

    elif i.lower() == "am i preety?" :
        os.system(camera)
        console.print("NO!", style="bold red")

    elif i.lower() == "open webcam" :
        console.print("Press q to exit.")
        run_cam()

    elif i.lower() == "bin" :
        binary_converter()

    elif i.lower() == "cls" :
        os.system("cls")

    elif i.lower() == "bf converter" :
        print("NO, WE ARE NOT DOING THAT")
        time.sleep(2)
        print("no no no no no no cant here you\nWhat, a python intrepeter")
        time.sleep(1)
        print("...")
        console.print("NO:angry:", style="bold red")
        time.sleep(7)
        print("fine")
        time.sleep(.5)
        print("Here you go")
        time.sleep(1)
        webbrowser.open("https://www.dcode.fr/brainfuck-language")
        time.sleep(.2)
        console.print("What did you think, I was actually going to create a converter.", style="bold red")
    
    elif i.lower() == "text to decimal" :
        text_convert()

    elif i.lower() == "tts" :
        ttsWords = input("\nWhich word you want to convert to speech: ")
        ttsEngine.say(ttsWords)
        ttsEngine.runAndWait()
        ttsEngine.stop()

    elif i.lower() == "zen of python" :
        ttsEngine.say(zenOfPython)
        ttsEngine.runAndWait()
        ttsEngine.stop()

    elif i.lower() == "generate password" :
        passwordGenerator()

    elif i.lower() == "speedtest" :
        SpeedTest()

    elif i.lower() == "ping" :
        webName = input(">>> ")
        os.system(f"ping {webName}")

    elif i.lower() == "crash" :
        while True :
            # I have not tested th== because I don't want to crash my computer
            print("Crashing.")
            print("Crashing..")
            print("Crashing...")

    elif i.lower() == "crtf" :
        crteFl()
    
    elif i.lower() == "del" :
        delete()

    elif i.lower() == "record voice" :
        recorder()

    elif i.lower() == "donut" :
        donut()

    elif i.lower() == "telnet" :
        try :
            os.system("telnet telehack.com")
        except :
            print("Go to 'Turn Windows features on or off'\nTurn on telnet to use th== command.")

    elif i.lower() == "python" :
        print("Just write 'quit()' to quit writing python")
        os.system("python")

    elif i.isdigit() :
        print(i)
    
    elif i.lower() == "flh" :
        console.input("Press escape key to exit. Press enter to continue ")
        flash_light()

    elif i.lower() == "help" :
        print(help)

    elif i.lower() == "exit" :
        run = False

    else :
        try :
            print(eval(i))
        except :
            for j, k in enumerate(i) :
                if i[j] == ' ' :
                    ...
                else :
                    error(i)
