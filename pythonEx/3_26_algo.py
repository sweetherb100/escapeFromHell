#3.26 algorithm Question
def alternate(number): #string으로 생각할까?
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
		

#num=input()
alternate(123456.78)

'''
# 1,241,212,312.1123
def comma(value) :
    if (value.find(".") is -1) :
        offset = len(value)
    else :
        offset = value.find(".")
    for i in range(offset-3,0,-3) :
        value = value[:i]+","+value[i:]
    return value
print(comma('1231.2334'))
'''