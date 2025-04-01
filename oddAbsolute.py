def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    n = int(in_num)
    dif = n - 21
    clean = abs(dif)
    twodif = 2 * dif

    if n > 21:
        print("Result:",twodif)
    else: 
        print("Result:",clean)


    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
