
import os

def delete() :
    
    lp = True
    while lp :
        fileNm = input(">>> ")
        try :
            os.remove(fileNm)
            lp = False
        except :
            print("File not found")
