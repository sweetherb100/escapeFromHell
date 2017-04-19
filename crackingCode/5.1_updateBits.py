# 기본 아이디어
# 1) N의 i~j index를 0으로 만고, 그외의 값은 1로 만든다.
# -> mask 이용
# 2) n_cleared = mask & N
# -> 일단 N에서 i~j 범위 외에 1이 있으면 1로 나오고, i~j 범위 내에 1이 있어도 0이 나온다.
# 3) m_shifted = M << i
# 4) Return N|M
# -> i~j 범위에서 M이 1이 있으면 1로 나온다. i~j범위 외에는 N의 범위를 따를 것이다. (어차피 M은 0이기 떄문에)

# python 메소드
# 1) bin(num) : 10진수 -> 2진수
# 2) 2**32 : **제곱승을 의미
# 3) 32bit number = 2**32 - 1

"""
N = 10000000000
M = 10011
i = 2
j = 6
output : 10001001100
"""

def printBinar(num):
    b_num = bin(num) #b_num:0bXXX
    print(b_num[2:]) #don't display b0

def getMask(i,j,max_int):
    # bin(max_int) =  0b11111111111111111111111111111111
    left = max_int << (j+1) #bin(max_int<<7) = 0b111111111111111111111111111111110000000 (j+1개 0)
    # bin(1<<2) = 0b100
    right=(1<<i) -1 #0b11
    return left | right #0b111111111111111111111111111111110000011

def updateBits(m,n,i,j):
    max_int = 2**32 -1 #32bit integer
    mask = getMask(i,j,max_int)
    n_cleared=n&mask #0b10000000000
    m_shifted=m<<i #0b1001100
    return n_cleared | m_shifted

m=19 #bin(19) =10011
n=1024 #bin(1024) = 10000000000
printBinar(updateBits(19,1024,2,6)) #10001001100
