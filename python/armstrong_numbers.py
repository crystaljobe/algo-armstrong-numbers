def find_armstrong_numbers(numbers):
    armstrongNums = []
    for num in numbers: 
        if num <= 9 :
            armstrongNums.append(num)
        else :
            numStr = str(num)
            exponent = len(numStr)
            powerSum = 0
            for char in numStr:
                powerSum += int(char) ** exponent
            if powerSum == num :
                armstrongNums.append(num)
    return armstrongNums
            
            
            
            

#find_armstrong_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 372, 407])
