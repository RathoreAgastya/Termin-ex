
import os

def delete(input) :
    
    lp = True
    while lp :
        split = input.split()
        if split[0] == "del" :
            flName = split[1]
            os.remove(flName)
            print("The file has been deleted.")
            lp = False
        else :
            print("File not found")
