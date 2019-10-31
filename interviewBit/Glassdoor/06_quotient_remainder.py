'''
Divide a number by another number and return the quotient and remainder without using div (//) or mod (%)
'''

# For now, assume the number is positive
def division (num1, num2): #num1/num2 = quotient + remainder e.g. 14/3
    print(num1 // num2)
    print(num1 % num2)

    quotient=0

    while num1 >= num2: #stop when num1 < num2
        num1=num1-num2
        quotient+=1

    return [quotient, num1]

    # return result

print(division(14,3))

