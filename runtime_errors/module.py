def isdigit(string):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    count=0
    index=0

    while index < len(digits)-1:
        letter = string[index]

        index += 1
        if letter in digits :
            count+= 1
            return count
