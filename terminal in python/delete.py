
import os

def delete() :
    
    lp = True
    while lp :
        fileNm = input("Give the name of the file: ")
        try :
            os.remove(fileNm)
            lp = False
        except :
            print("File not found")
