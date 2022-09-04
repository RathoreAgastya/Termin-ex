
# This is going to be long
# I started this at 27.8.22 12:35 PM Let's see where it is going to end

# variables for capital letters


A = 65
B = 66
C = 67
D = 68
E = 69
F = 70
G = 71
H = 72
I = 73
J = 74
K = 75
L = 76
M = 77
N = 78
O = 79
P = 80
Q = 81
R = 82
S = 83
T = 84
U = 85
V = 86
W = 87
X = 88
Y = 89
Z = 90


# variables for small letters
a = 97
b = 98
c = 99
d = 100
e = 101
f = 102
g = 103
h = 104
i = 105
j = 106
k = 107
l = 108
m = 109
n = 110
o = 111
p = 112
q = 113
r = 114
s = 115
t = 116
u = 117
v = 118
w = 119
x = 120
y = 121
z = 122


# brackets
sqr_open = 91
sqr_close = 93
curly_open = 123
curly_close = 125
nrml_open = 40
nrml_close = 41
arw_open = 60
arw_close = 62


# special symbols
exclaim = 33
dble_quote = 34
hash_tag = 35
dollar = 36
percentage = 37
an = 38
quote = 39
times = 42
plus = 43
comma = 44
minus = 45
stop = 46
slash = 47
backtick = 96
colon = 58
semi_colon = 59
equal = 61
question = 63
stick = 124
tilde = 126
backSlash = 92
upArrow = 94
_ = 95



def text_convert() :
    checkLp = True
    while checkLp :
        letter = input("\nGive a letter or special symbol or brackets. Not a word or number: ")
        if len(letter) > 1 :
            print("A LETTER, NOT A WORD\n")
        elif letter.isdigit() :
            print("A LETTER, NOT A NUMBER\n")
        else :
            checkLp = False

    convert_lp = True
    while convert_lp :
        
        # are you ready for the longest if statement(I hope you are)
        if letter == "A" :
            print(f"The letter in decimal is {A}.")
            convert_lp = False
        elif letter == "B" :
            print(f"The letter in decimal is {B}.")
            convert_lp = False
        elif letter == "C" :
            print(f"The letter in decimal is {C}.")
            convert_lp = False
        elif letter == "D" :
            print(f"The letter in decimal is {D}.")
            convert_lp = False
        elif letter == "E" :
            print(f"The letter in decimal is {E}.")
            convert_lp = False
        elif letter == "F" :
            print(f"The letter in decimal is {F}.")
            convert_lp = False
        elif letter == "G" :
            print(f"The letter in decimal is {G}.")
            convert_lp = False
        elif letter == "H" :
            print(f"The letter in decimal is {H}.")
            convert_lp = False
        elif letter == "I" :
            print(f"The letter in decimal is {I}.")
            convert_lp = False
        elif letter == "J" :
            print(f"The letter in decimal is {J}.")
            convert_lp = False
        elif letter == "K" :
            print(f"The letter in decimal is {K}.")
            convert_lp = False
        elif letter == "L" :
            print(f"The letter in decimal is {L}.")
            convert_lp = False
        elif letter == "M" :
            print(f"The letter in decimal is {M}.")
            convert_lp = False
        elif letter == "N" :
            print(f"The letter in decimal is {N}.")
            convert_lp = False
        elif letter == "O" :
            print(f"The letter in decimal is {O}.")
            convert_lp = False
        elif letter == "P" :
            print(f"The letter in decimal is {P}.")
            convert_lp = False
        elif letter == "Q" :
            print(f"The letter in decimal is {Q}.")
            convert_lp = False
        elif letter == "R" :
            print(f"The letter in decimal is {R}.")
            convert_lp = False
        elif letter == "S" :
            print(f"The letter in decimal is {S}.")
            convert_lp = False
        elif letter == "T" :
            print(f"The letter in decimal is {T}.")
            convert_lp = False
        elif letter == "U" :
            print(f"The letter in decimal is {U}.")
            convert_lp = False
        elif letter == "V" :
            print(f"The letter in decimal is {V}.")
            convert_lp = False
        elif letter == "W" :
            print(f"The letter in decimal is {W}.")
            convert_lp = False
        elif letter == "X" :
            print(f"The letter in decimal is {X}.")
            convert_lp = False
        elif letter == "Y" :
            print(f"The letter in decimal is {Y}.")
            convert_lp = False
        elif letter == "Z" :
            print(f"The letter in decimal is {Z}.")
            convert_lp = False
            # Yay! just have do this one more time and do brackets and special symbols
            # Best day ever!!!!(say's in sarcasm)
        elif letter == "a" :
            print(f"The letter in decimal is {a}.")
            convert_lp = False
        elif letter == "b" :
            print(f"The letter in decimal is {b}.")
            convert_lp = False
        elif letter == "c" :
            print(f"The letter in decimal is {c}.")
            convert_lp = False
        elif letter == "d" :
            print(f"The letter in decimal is {d}.")
            convert_lp = False
        elif letter == "e" :
            print(f"The letter in decimal is {e}.")
            convert_lp = False
        elif letter == "f" :
            print(f"The letter in decimal is {f}.")
            convert_lp = False
        elif letter == "g" :
            print(f"The letter in decimal is {g}.")
            convert_lp = False
        elif letter == "h" :
            print(f"The letter in decimal is {h}.")
            convert_lp = False
        elif letter == "i" :
            print(f"The letter in decimal is {i}.")
            convert_lp = False
        elif letter == "j" :
            print(f"The letter in decimal is {j}.")
            convert_lp = False
        elif letter == "k" :
            print(f"The letter in decimal is {k}.")
            convert_lp = False
        elif letter == "l" :
            print(f"The letter in decimal is {l}.")
            convert_lp = False
        elif letter == "m" :
            print(f"The letter in decimal is {m}.")
            convert_lp = False
        elif letter == "n" :
            print(f"The letter in decimal is {n}.")
            convert_lp = False
        elif letter == "o" :
            print(f"The letter in decimal is {o}.")
            convert_lp = False
        elif letter == "p" :
            print(f"The letter in decimal is {p}.")
            convert_lp = False
        elif letter == "q" :
            print(f"The letter in decimal is {q}.")
            convert_lp = False
        elif letter == "r" :
            print(f"The letter in decimal is {r}.")
            convert_lp = False
        elif letter == "s" :
            print(f"The letter in decimal is {s}.")
            convert_lp = False
        elif letter == "t" :
            print(f"The letter in decimal is {t}.")
            convert_lp = False
        elif letter == "u" :
            print(f"The letter in decimal is {u}.")
            convert_lp = False
        elif letter == "v" :
            print(f"The letter in decimal is {v}.")
            convert_lp = False
        elif letter == "w" :
            print(f"The letter in decimal is {w}.")
            convert_lp = False
        elif letter == "x" :
            print(f"The letter in decimal is {x}.")
            convert_lp = False
        elif letter == "y" :
            print(f"The letter in decimal is {y}.")
            convert_lp = False
        elif letter == "z" :
            print(f"The letter in decimal is {z}.")
            convert_lp = False
        # I just copy pasted, I was to lazy
        elif letter == "[" :
            print(f"The bracket in decimal is {sqr_open}.")
            convert_lp = False
        elif letter == "]" :
            print(f"The bracket in decimal is {sqr_close}.")
            convert_lp = False
        elif letter == "{" :
            print(f"The bracket in decimal is {curly_open}.")
            convert_lp = False
        elif letter == "}" :
            print(f"The bracket in decimal is {curly_close}.")
            convert_lp = False
        elif letter == "(" :
            print(f"The bracket in decimal is {nrml_open}.")
            convert_lp = False
        elif letter == ")" :
            print(f"The bracket in decimal is {nrml_close}.")
            convert_lp = False
        elif letter == "<" :
            print(f"The bracket in decimal is {arw_open}.")
            convert_lp = False
        elif letter == ">" :
            print(f"The bracket in decimal is {arw_close}.")
            convert_lp = False
        elif letter == "!" :
            print(f"The symbol in decimal is {exclaim}.")
            convert_lp = False
        elif letter == '"' :
            print(f"The symbol in decimal is {dble_quote}.")
            convert_lp = False
        elif letter == "#" :
            print(f"The symbol in decimal is {hash_tag}.")
            convert_lp = False
        elif letter == "$" :
            print(f"The symbol in decimal is {dollar}.")
            convert_lp = False
        elif letter == "%" :
            print(f"The symbol in decimal is {percentage}.")
            convert_lp = False
        elif letter == "&" :
            print(f"The symbol in decimal is {an}.")
            convert_lp = False
        elif letter == "'" :
            print(f"The symbol in decimal is {quote}.")
            convert_lp = False
        elif letter == "*" :
            print(f"The symbol in decimal is {times}.")
            convert_lp = False
        elif letter == "+" :
            print(f"The symbol in decimal is {plus}.")
            convert_lp = False
        elif letter == "," :
            print(f"The symbol in decimal is {comma}.")
            convert_lp = False
        elif letter == "-" :
            print(f"The symbol in decimal is {minus}.")
            convert_lp = False
        elif letter == "." :
            print(f"The symbol in decimal is {stop}.")
            convert_lp = False
        elif letter == "/" :
            print(f"The symbol in decimal is {slash}.")
            convert_lp = False
        elif letter == "`" :
            print(f"The symbol in decimal is {backtick}.")
            convert_lp = False
        elif letter == ":" :
            print(f"The symbol in decimal is {colon}.")
            convert_lp = False
        elif letter == ";" :
            print(f"The symbol in decimal is {semi_colon}.")
            convert_lp = False
        elif letter == "=" :
            print(f"The symbol in decimal is {equal}.")
            convert_lp = False
        elif letter == "?" :
            print(f"The symbol in decimal is {question}.")
            convert_lp = False
        elif letter == "|" :
            print(f"The symbol in decimal is {stick}.")
            convert_lp = False
        elif letter == "~" :
            print(f"The symbol in decimal is {tilde}.")
            convert_lp = False
        elif letter == "\\" :
            print(f"The symbol in decimal is {backSlash}.")
            convert_lp = False
        elif letter == "^" :
            print(f"The symbol in decimal is {upArrow}.")
            convert_lp = False
        elif letter == "_" :
            print(f"The symbol in decimal is {_}.")
        else :
            print("This was made by a 11 yr old\nyou are not gonna expect much.")
