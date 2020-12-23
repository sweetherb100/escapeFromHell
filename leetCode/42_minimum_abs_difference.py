import itertools
# catesian product of multiple sets

def solution(money):
    total_amount = 0
    all_type_money = []
    for i in range(len(money)):
        total_amount+=money[i][0]*money[i][1]
        temp_money = [0]
        for j in range(money[i][1]):
            temp_money.append(money[i][0]*(j+1))
        all_type_money.append(temp_money)

    # print(total_amount)
    print(all_type_money)
    result = list(itertools.product(*all_type_money)) #### cartesian product of multiple sets

    possible_amount = []
    for i in range(len(result)):
        possible_amount.append(sum(result[i]))

    # print(possible_amount)
    difference = abs(total_amount/2 - possible_amount[0])
    index = 0
    for i in range(1,len(possible_amount),1):
        if abs(total_amount/2 - possible_amount[i]) < difference:
            difference = abs(total_amount/2 - possible_amount[i])
            index = i

    return [possible_amount[index], total_amount-possible_amount[index]]





print(solution([[100,3], [200,1], [50,2]]))
# print(solution([[700,5],[2500,3]]))