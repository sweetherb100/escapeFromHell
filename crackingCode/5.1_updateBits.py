'''
*Idea
1) make i~j index of N into 0 and rest into 1
-> use mask 
2) n_cleared = mask & N
-> If there is 1 outside i~j, result will be 1.
If there is 1 inside i~j, result will be 0.
3) m_shifted = M << i
4) Return n_cleared | m_shifted
-> If there is 1 inside i~j in M, result will be 1.
Outside of i~j, result will be N (M is zero)

*Python
1) bin(num) : decimal number -> binary number
2) 2**32 : ** square
3) 32bit number = 2**32 - 1

ex)
N = 11000000001
M = 10011
i = 2
j = 6
output : 11001001101
'''


def printBinar(num):
    b_num = bin(num) #b_num:0bXXX
    print(b_num[2:]) #don't display b0

def getMask(i,j,max_int):
    # bin(max_int) =  0b11111111111111111111111111111111
    left = max_int << (j+1) #bin(max_int<<7) = 0b111111111111111111111111111111110000000 (j+1개 0)
    right=(1<<i) -1 #0b11
    # bin(1<<2) = 0b100
    return left | right #0b111111111111111111111111111111110000011

def updateBits(m,n,i,j):
    max_int = 2**32 -1 #32bit integer
    mask = getMask(i,j,max_int)
    n_cleared=n&mask #0b11000000001
    m_shifted=m<<i #0b1001100
    return n_cleared | m_shifted

m=19 #bin(19) =10011
n=1024 #bin(1024) = 10000000000
printBinar(updateBits(19,1024,2,6)) #10001001100
