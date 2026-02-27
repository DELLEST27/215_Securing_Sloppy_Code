def isdigit(string):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    index=0

    while index < len(string):
        char = string[index]
        #print (index)

        index += 1
        if char not in digits :
              return False
        
        
    return True

print (isdigit("61a"))
