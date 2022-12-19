from __future__ import annotations

import ctypes
import os
import random
import socket
import time
import webbrowser
import pyfiglet

import cv2
import pygame as py
import pyttsx3
import speedtest

import cv2
from mov_cli.__main__ import movcli
from colored import colors, fore, style
from pygame import mixer
from rich.console import Console
from rich.progress import track

from audio import recorder
from delete import *
from textToDecimal import text_convert


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
gen pass             generates a random strong password
record voice         records voice for a given amount of time
ping                 pings website that you enter
bf converter         oh no
ascii --table        tells the entire ascii table
bd                   moves back a directory
fd                   moves to the given directory
sd                   shows you all the files and folders in the current directory
movies               makes you download any movie you want(Still in beta so expect it to fail sometimes)
"""

# variables
host_name = socket.gethostname()
local_ip = socket.gethostbyname(host_name)
camera = "start microsoft.windows.camera:"



# Zen of python
zenOfPython = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


# ascii table
asciiT = """
Dec  Char                           Dec  Char     Dec  Char     Dec  Char
---------                           ---------     ---------     ----------
 0   NUL (null)                      32  SPACE     64  @         96  `
 1   SOH (start of heading)          33  !         65  A         97  a
 2   STX (start of text)             34  "         66  B         98  b
 3   ETX (end of text)               35  #         67  C         99  c
 4   EOT (end of transmission)       36  $         68  D        100  d
 5   ENQ (enquiry)                   37  %         69  E        101  e
 6   ACK (acknowledge)               38  &         70  F        102  f
 7   BEL (bell)                      39  '         71  G        103  g
 8   BS  (backspace)                 40  (         72  H        104  h
 9   TAB (horizontal tab)            41  )         73  I        105  i
10   LF  (NL line feed, new line)    42  *         74  J        106  j
11   VT  (vertical tab)              43  +         75  K        107  k
12   FF  (NP form feed, new page)    44  ,         76  L        108  l
13   CR  (carriage return)           45  -         77  M        109  m
14   SO  (shift out)                 46  .         78  N        110  n
15   SI  (shift in)                  47  /         79  O        111  o
16   DLE (data link escape)          48  0         80  P        112  p
17   DC1 (device control 1)          49  1         81  Q        113  q
18   DC2 (device control 2)          50  2         82  R        114  r
19   DC3 (device control 3)          51  3         83  S        115  s
20   DC4 (device control 4)          52  4         84  T        116  t
21   NAK (negative acknowledge)      53  5         85  U        117  u
22   SYN (synchronous idle)          54  6         86  V        118  v
23   ETB (end of trans. block)       55  7         87  W        119  w
24   CAN (cancel)                    56  8         88  X        120  x
25   EM  (end of medium)             57  9         89  Y        121  y
26   SUB (substitute)                58  :         90  Z        122  z
27   ESC (escape)                    59  ;         91  [        123  {
28   FS  (file separator)            60  <         92  \        124  |
29   GS  (group separator)           61  =         93  ]        125  }
30   RS  (record separator)          62  >         94  ^        126  ~
31   US  (unit separator)            63  ?         95  _        127  DEL
"""

# screen resolution
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[width, height] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

# screen


def flash_light():
    screen = py.display.set_mode((width, height))
    py.display.set_caption("Flashlight")
    rn = True
    while rn:

        screen.fill((255, 255, 255))

        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    rn = False

        py.display.update()

    py.quit()


def SpeedTest():
    try:
        test = speedtest.Speedtest(secure=True)

        mixer.music.load("wait music.ogg")
        mixer.music.set_volume(.7)
        mixer.music.play()

        download = test.download()
        upload = test.upload()

        downloadType = None
        uploadType = None

        if (download // 1024) < 0:
            downloadType = "KBPS"
        elif (download // 1024) > 0:
            downloadType = "MBPS"

        if (upload // 1024) < 0:
            uploadType = "KBPS"
        elif (upload // 1024) > 0:
            uploadType = "MBPS"

        if downloadType == "MBPS":
            download = (download / 1024) / 1024
            mixer.music.stop()
            print(f"Download speed: {download:.2f} {downloadType}")
        else:
            mixer.music.stop()
            print(f"Download speed: {download:.2f} {downloadType}")

        if uploadType == "MBPS":
            upload = (upload / 1024) / 1024
            mixer.music.stop()
            print(f"Download speed: {upload:.2f} {uploadType}")
        else:
            mixer.music.stop()
            print(f"Upload speed: {upload:.2f} {uploadType}")
    except:
        mixer.music.stop()
        print("Error 404 forbiden")


def passwordGenerator():
    while True:
        length = input("lenght of password(maximum length=74): ")
        if length.isdigit() and int(length) <= 74:
            length = int(length)
            break
        else:
            print("Try again.")

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbol = "[]{}#()*;._-"

    ans = lower_case + upper_case + num + symbol
    password = "".join(random.sample(ans, length))

    print({password})


def error(cmd):
    er_type = None
    try:
        cmd = float(cmd)
        er_type = "Float"
    except:
        er_type = "String"

    if type(cmd) == "<class 'float'>":
        cmd = str(cmd)
    else:
        pass


def run_cam():
    webcam = cv2.VideoCapture(0)

    while True:
        ret, frame = webcam.read()

        if ret == True:
            cv2.imshow("AGASTINAL WEBCAM YEAHHHHHHHHHHHH", frame)
            key = cv2.waitKey(20) & 0xFF
            if key == ord("q"):
                break

    webcam.release()
    cv2.destroyAllWindows()


def binary_converter():
    binary = []
    check = True
    number:int = 0
    orig_num = ""

    while check:
        number = int(console.input(
            "Which number should be converted into binary: "))
        if str(number).isdigit():
            number = int(number)
            orig_num = number
            check = False
        else:
            console.print(f"{number} == not an integer")

    convert_lp = True
    while convert_lp:

        if (number % 2) == 1:
            binary.append(1)
            number = number // 2
            if number == 0:
                binary.reverse()
                console.print(f"{orig_num} in binary == {binary} :smile:.")
                convert_lp = False
            else:
                ...
        else:
            ...

        if (number % 2) == 0:
            binary.append(0)
            number = number // 2
            if number == 0:
                binary.reverse()
                convert_lp = False
            else:
                ...
        else:
            ...


def bd():
    crd = os.getcwd()
    crd = list(crd.split('\\'))
    crd.pop(-1)
    crd = '\\'.join(crd)
    os.chdir(crd)


def crteFl():
    flnm = input("\nWhat would you like to name your file?\n")
    file = open(flnm+".txt", 'w')
    textInFl = input("\nWhat == the text which goes in the file?\n")
    file.write(textInFl)
    file.close()

    print("The file has been created.")


console.input("WElCOME!\nPress enter to continue")

for _ in track(range(20), description="setting up BIOS..."):
    time.sleep(0.02)
    pass
for _ in track(range(10), description="Loading commands..."):
    time.sleep(0.02)
    pass
for _ in track(range(25), description="Loading all packages..."):
    time.sleep(0.02)
    pass
for _ in track(range(10), description="Setting up Python..."):
    time.sleep(0.02)
    pass
for _ in track(range(20), description="Getting ip address..."):
    time.sleep(0.02)
    pass
for _ in range(4):
    time.sleep(0.02)
    console.log("Getting kernel access")
for _ in range(4):
    time.sleep(0.01)
    console.log("Loading terminal into command line")


#mixer.music.load("opening jingle.ogg")
mixer.music.set_volume(.7)

#mixer.music.play()
console.print(pyfiglet.figlet_format("CMD"), style="blue")
#time.sleep(4)

run = True
while run:
 
    dir_path = os.getcwd()
    cmd = input(f"\nAT {dir_path}> ")
    i = cmd.lower()

    if i == "python hello":
        console.print('print("Hello, world!")', style="bold green")

    elif i == "movies":
        movcli()

    elif i == "bd":
        bd()

    elif i.startswith("fd "):
        try: direc = i.split('"'); os.chdir(direc[1])
        except: console.print("Directory not found or command given incorrectly", style="bold red")

    elif i == "sd":
        os.system("dir")

    elif i == "c hello":
        console.print(
            '#include <stdio.h>\n\nint main()\n{\n    printf("Hello, world!");\n   return 0;\n}', style="bold green")

    elif i == "java hello":
        console.print(
            '\nclass hello {\n    [bold green]public static void[/] main(String[]) {\n       System.out.println("Hello, world!");\n  }\n}')

    elif i == ":)":
        os.system(camera)
        console.print(f"I am watching you {host_name}😈😈😈.")

    elif i == "ip":
        console.print(
            f"You needed your ip I guess, because why would you call th== command unless you don't know how to access your ip\nSooooooooooooooooooooooooo\nHere you go\n{local_ip}")

    elif i == "am i preety?":
        os.system(camera)
        console.print("NO!", style="bold red")

    elif i == "open webcam":
        console.print("Press q to exit.")
        run_cam()

    elif i == "bin":
        binary_converter()

    elif i == "cls":
        os.system("cls")

    elif i == "bf converter":
        print("NO, WE ARE NOT DOING THAT")
        #time.sleep(2)
        print("no no no no no no cant here you\nWhat, a python intrepeter")
        #time.sleep(1)
        print("...")
        console.print("NO:angry:", style="bold red")
        #time.sleep(7)
        print("fine")
        #time.sleep(.5)
        print("Here you go")
        #time.sleep(1)
        webbrowser.open("https://www.dcode.fr/brainfuck-language")
        #time.sleep(.2)
        console.print(
            "What did you think, I was actually going to create a converter.", style="bold red")

    elif i == "text to decimal":
        text_convert()

    elif i == "tts":
        ttsWords = input("\nWhich word you want to convert to speech: ")
        ttsEngine.say(ttsWords)
        ttsEngine.runAndWait()
        ttsEngine.stop()

    elif i == "zen of python":
        ttsEngine.say(zenOfPython)
        ttsEngine.runAndWait()
        ttsEngine.stop()

    elif i == "gen pass":
        passwordGenerator()

    elif i == "ascii --table":
        os.system("cls")
        console.print(asciiT)

    elif i == "speedtest":
        SpeedTest()

    elif i == "calculator":
        console.print("Bruh, you just type your problem straight in the ")

    elif i == "ping":
        webName = input(">>> ")
        os.system(f"ping {webName}")

    elif i == "crash":
        while True:
            # I have not tested this because I don't want to crash my computer
            print("Crashing.")
            print("Crashing..")
            print("Crashing...")

    # Game
    # ---------

    elif i == "cf":
        crteFl()

    elif i == "del":
        delete()

    elif i == "record voice":
        recorder()

    elif i == "telnet":
        try:
            os.system("telnet telehack.com")
        except:
            print(
                "Go to 'Turn Windows features on or off'\nTurn on telnet to use th== command.")

    elif i == "python":
        print("Just write 'quit()' to quit writing python")
        os.system("python")

    elif i.isdigit():
        print(i)

    elif (i.startswith('"') and i.endswith('"')) or (i.startswith("'") and i.endswith("'")):
        print(i[1:-1])

    elif i == "flh":
        console.input("Press escape key to exit. Press enter to continue ")
        flash_light()

    elif i == "help":
        print(help)

    elif i == "exit":
        run = False

    else:
        print(fore.RED + "Command is NOT FOUND. This command does not EXIST or is not available" + style.RESET)
