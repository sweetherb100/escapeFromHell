def perm(input,start):
    if start==len(input)-1:
        print(input)
    else:
        for i in range(start,len(input)):
            input[start],input[i]=input[i],input[start]
            perm(input,start+1)
            input[start],input[i]=input[i],input[start] #swap back, for the next loop

perm([1,2,3],0)

#[1, 2, 3]
#[1, 3, 2]
#[2, 1, 3]
#[2, 3, 1]
#[3, 2, 1]
#[3, 1, 2]