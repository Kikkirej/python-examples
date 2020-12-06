if __name__ == '__main__':
    # 6! = (((((1*1)*2)*3)*4)*5)*6
    number = input("Enter number: ")
    # print type(number)
    ergebnis = 1
    maxnumber = number + 1
    for x in range(1, maxnumber):
        ergebnis = x*ergebnis
    print ergebnis