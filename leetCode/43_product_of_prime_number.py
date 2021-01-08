#method 1
def solution(n):
    answer =[]

    for i in range(2, n, 1):
        while (n%i ==0):
            n = n//i
            answer.append(i)
            print(n)

    print(answer)

    if len(answer) > 2 or len(answer) == 1:
        answer = [-1, -1]

    return answer


#method 2
def countPrimes(n):
    # Exception
    if n <= 1:
        return 0

    # step1: create a vector as the length of n
    vect = [1] * (n + 1)  # for simplicity, vector size n+1

    # Initialize
    vect[0] = 0
    vect[1] = 0  # not prime

    # Complexity O(n/2)
    # step2: going through half of n iteration
    for i in range(2, n // 2 + 1):  # in theory, check until 10/2= 5; put until "n//2+1"
        if vect[i] == 1:
            # step3: update as 0 for the multiples of index i
            vect[2 * i:n + 1:i] = [0] * len(vect[2 * i:n + 1:i])  # n+1 means: only until n

    # if 1, prime; if not, not prime
    return vect


def solution2(num):
    result =[]
    prime_vec = countPrimes(num)
    print(prime_vec)
    for i in range(2, len(prime_vec), 1):
        if prime_vec[i] == 1: #when prime
            print(i)
            if num%pow(i,2)==0:
                return [-1,-1]
            if num%i == 0:
                result.append(i)


    if len(result) > 2:
        return [-1,-1]

    return result

print(solution(6))
print(solution2(72))