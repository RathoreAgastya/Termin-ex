
# don't come here this is a scraped command for the terminal
from numpy import prod

def calculator() :
    error = False
    list = []
    loop = True
    calType = input("Which claculation do you want to perform: ")
    if calType == "addition" :
        while loop :
            noOfNum = input("how many numbers do you want to add: ")
            if noOfNum.isdigit() :
                noOfNum = int(noOfNum)
                for i in range(noOfNum) :
                    num = input(f"give {i} number: ")
                    if num.isdigit() :
                        num = int(num)
                    else :
                        error = True
                        print("Not a valid number.")
                    if error :
                        error = False
                    elif error == False :
                        list.append(num)

                
                print(f"The addition of all numbers is {sum(list)}.")
                loop = False



    elif calType == "multiplication" :
        while loop :
            noOfNum = input("How many numbers do you want to multiply: ")
            if noOfNum.isdigit() :
                noOfNum = int(noOfNum)
                for i in range(noOfNum) :
                    num = input(f"give {i} number: ")
                    if num.isdigit() :
                        num = int(num)
                    else :
                        error = True
                        print("Not a valid number.")
                    if error :
                        error = False
                    elif error == False :
                        list.append(num)


                print(f"The multiplication of all numbers is {prod(list)}.")
                loop = False


    
    elif calType == "division" :
        while loop :
            for i in range(1, 2) :
                num = input(f"{i} number: ")
                if i == 1 :
                    num1 = num
                elif i == 2 :
                    num2 = num

            print(f"Dividing {num1} and {num2} is {num1 / num2}")


#SCRAPED