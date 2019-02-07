import math
from collections import deque

def putCommaAtNum(number):
    result=""
    len = int(math.log10(number)) #6 digits
    #queue=deque()
    queue = ""
    round=0
    for i in range(len,-1,-1):
        if round ==3:
            queue +=","
            round=0

        digit=int(number/pow(10,i)) #quotient, not remainder!!
        print(pow(10,i))
        print(digit)
        queue += str(digit)
        number=number-digit*pow(10,i)
        round+=1

        if i == 0:
            print(number) #in the end, number is only the decimal part
            queue += str(number)

    print(queue)
    return result


putCommaAtNum(123456.78)


def alternate(number):
	result=""
	list=[x for x in str(number)] #int(x)시에 '.' 인식 안됨
	if '.' in list:
		print('There is decimal points')
		index=list.index('.')
	else:
		print('There is not decimal points')
		index=len(list)
		
	#index=list.index('.') 
	#if not found, there is an error
	#find('.') : if found returns index, if not found return -1
	
	loop = 1
	halfResult = ""
	
	for i in range(index):
		print('i : {}, data : {}'.format(index-i-1,list[index-i-1]))
		halfResult = list[index-i-1] + halfResult
		if (loop%3 == 0) and (i !=index-1):
			halfResult =',' + halfResult
		loop =loop+1
	
	result = halfResult + str(number)[index:]
	print ('result : ',result)

#alternate(123456.78)
#result :  123,456.78

