# 2018/01/29 Prob #3
from scipy.special import comb
import math

prob=0
error=0.45

for i in range(13,26): #don't include the last end
    #print(i)
    prob += comb(25,i,exact=True)*pow(error,i)*pow(1-error,25-i)

# print(round(prob,3))

print("***********************")
def entropy(p1): #p1, 1-p1
    if p1 == 1:
        return 0
    elif p1 == 0:
        return 0
    else :
        return round(-(p1*math.log2(p1)) - ((1-p1)*math.log2(1-p1)), 3)


#for now, only for 2 labels
def info_gain(n1, n2, n3, n4):
    prev_prob = round((n1 + n3) / (n1 + n2 + n3 + n4), 3)
    weight1 = round((n1 + n2) / (n1 + n2 + n3 + n4), 3)
    weight2 =round((n3 + n4) / (n1 + n2 + n3 + n4), 3)
    after_prob1 = round(n1 / (n1 + n2), 3)
    after_prob2 = round(n3 / (n3 + n4), 3)
    # print(weight1)
    # print(weight2)
    # print(after_prob1)
    # print(after_prob2)
    info1=weight1*entropy(after_prob1)
    info2=weight2*entropy(after_prob2)
    return round(entropy(prev_prob) - (info1 + info2), 3)

# print(info_gain(2,0,2,4)) # 2017/11/27 Prob #2 1)
# print(info_gain(2,2,2,2))

# print(info_gain(3,4,6,1)) #chap13, p.19 gain("humidity"), high/normal
# print(info_gain(6,2,3,3)) #chap13, p.19 gain("windy"), false/true

### 2017/09/04 Prob #2
# print(info_gain(1,0,8,5)) #1
# print(info_gain(5,1,4,4)) #2
# print(info_gain(5,2,4,3)) #3
# print(info_gain(7,2,2,3)) #4
# print(info_gain(7,3,2,2)) #5
# print(info_gain(8,4,1,1)) #6
# print(info_gain(8,5,1,0)) #7

#### 2018/06/25 Prob #3
# print(info_gain(1,2,4,3))

# print(info_gain(0,1,5,4))
# print(info_gain(2,5,3,0))
# print(info_gain(4,5,1,0))

### 2017/07/10 Prob #3
# print(info_gain(2,2,0,1))
# print(info_gain(1,1,1,2))
# print(info_gain(1,0,1,3))

print("***********************")
#### 2019/01/14 #2 GINI INDEX

def gini(p1):
    return 1-pow(p1,2) -pow(1-p1, 2)

 # only when 2 classes
def gini_gain(n1, n2, n3, n4):
    prev_prob = round((n1 + n3) / (n1 + n2 + n3 + n4), 3)
    gini_before=gini(prev_prob)


    weight1 = round((n1 + n2) / (n1 + n2 + n3 + n4), 3)
    weight2 = round((n3 + n4) / (n1 + n2 + n3 + n4), 3)

    after_prob1 = round(n1 / (n1 + n2), 3)
    after_prob2 = round(n3 / (n3 + n4), 3)
    gini_after = round(weight1*gini(after_prob1) + weight2*gini(after_prob2), 3)
    print("gini_after : " + str(gini_after))
    gini_gain = round(gini_before - gini_after, 3)
    return gini_gain

# print(gini_gain(5,5,4,0)) #chap 13, p.47
# print(gini_gain(1,0,2,4)) # cut1
# print(gini_gain(3,1,0,3)) # cut2
# print(gini_gain(3,2,0,2)) # cut3
# print(gini_gain(3,3,0,1)) # cut4

print("***********************")
def entropy3(p1,p2,p3):
    if p1 == 0:
        return round(-(p2*math.log2(p2)) -(p3*math.log2(p3)), 3)
    elif p2 == 0:
        return round(-(p1 * math.log2(p1)) - (p3 * math.log2(p3)), 3)
    elif p3 == 0  :
        return round(-(p1 * math.log2(p1)) - (p2 * math.log2(p2)), 3)
    else:
        return round(-(p1 * math.log2(p1)) - (p2 * math.log2(p2)) - (p3 * math.log2(p3)), 3)


# 2018/09/03 prob #5
#with 3 labels
def info_gain3(n1, n2, n3,  n4, n5, n6):
    prev_prob1 = round((n1 + n4) / (n1 + n2 + n3 + n4 + n5 + n6), 3)
    prev_prob2 = round((n2 + n5) / (n1 + n2 + n3 + n4 + n5 + n6), 3)
    prev_prob3 = round((n3 + n6) / (n1 + n2 + n3 + n4 + n5 + n6), 3)

    weight1 = round((n1 + n2 + n3) / (n1 + n2 + n3 + n4 + n5 + n6), 3)
    weight2 =round((n4 + n5 + n6) / (n1 + n2 + n3 + n4 + n5 + n6), 3)

    first_prob1 = round(n1 / (n1 + n2 + n3), 3)
    first_prob2 = round(n2 / (n1 + n2 + n3), 3)
    first_prob3 = round(n3 / (n1 + n2 + n3), 3)

    second_prob1 = round(n4 / (n4 + n5 + n6), 3)
    second_prob2 = round(n5 / (n4 + n5 + n6), 3)
    second_prob3 = round(n6 / (n4 + n5 + n6), 3)

    info1=weight1*entropy3(first_prob1, first_prob2, first_prob3)
    print(entropy3(first_prob1, first_prob2, first_prob3))

    info2=weight2*entropy3(second_prob1, second_prob2, second_prob3)
    print(entropy3(second_prob1, second_prob2, second_prob3))

    print(entropy3(prev_prob1, prev_prob2, prev_prob3))
    return round(entropy3(prev_prob1, prev_prob2, prev_prob3) - (info1 + info2), 3)


# print(info_gain3(7,2,3,8,3,1)) #spectacle prescription
# print(info_gain3(8,0,4,7,5,0)) #astigmatism


print("***********************")
# 2017/07/10  Prob #1

x=[-1.3, 0.9, -2.9, -0.1, 1.3, 1.8, 1.7, 0.9, 0.9, 0.1]
y=[-72.6, 49.5, -230.3, -54.4, 5.1, 259.4, 87.1, 163.2, 3.5, 54.6]

w0 = 10
w1 = 15

def gradient_descent (w0, w1, x, y):
#learning rate 0.01
    tot_delta_w0=0
    tot_delta_w1=0
    for i in range(len(x)):
        delta_w0 = round((-2 * (y[i] - (w0 + w1*x[i]))), 3)
        delta_w1 = round((-2 * (y[i] - (w0 + w1*x[i])) * x[i]), 3)
        tot_delta_w0 += delta_w0
        tot_delta_w1 += delta_w1
        print("delta_w0 : " + str(delta_w0) + " " + "delta_w1 : " + str(delta_w1))

    print("tot_delta_w0 : " + str(tot_delta_w0) + " " + "tot_delta_w1 : " + str(tot_delta_w1))

    f_w0 = round(w0 - 0.01*tot_delta_w0, 3)
    f_w1 = round(w1 - 0.01*tot_delta_w1, 3)
    print("f_w0 : " + str(f_w0) + " " + "f_w1 : " + str(f_w1))
    return [f_w0, f_w1]

# gradient_descent(10, 15, x, y)


def gradient_iteration(k, init_w0, init_w1):
    w0= init_w0
    w1= init_w1
    for i in range(k):
        [w0, w1] = gradient_descent(w0, w1, x, y)

    print("final w0 : " + str(w0) + " " + "final w1 : " + str(w1))

# gradient_iteration(100, 10, 15) #final w0 : 0.808 final w1 : 77.892 nearly same as the result as linear regression
print("***********************")
#2017/09/04 #3 Euclidean distance
d0=[0.36, 0.48, 0.78, 0, 0, 0, 0]
d1=[0.18, 0, 0, 0.78, 0.30, 0, 0]
d2=[0.18, 0, 0, 0, 0, 0.48, 0.48]
d3=[0, 0.48, 0, 0, 0.30, 0, 0.48]
d4=[0.18, 0, 0, 0, 0.30, 0.48, 0]

sum01 = 0
sum02 = 0
sum03 = 0
sum04 = 0
sum12 = 0
sum13 = 0
sum14 = 0
sum23 = 0
sum24 = 0
sum34 = 0

for i in range(len(d0)):
    sum01 += (d0[i] - d1[i]) ** 2
    sum02 += (d0[i] - d2[i]) ** 2
    sum03 += (d0[i] - d3[i]) ** 2
    sum04 += (d0[i] - d4[i]) ** 2

    sum12 += (d1[i] - d2[i]) ** 2
    sum13 += (d1[i] - d3[i]) ** 2
    sum14 += (d1[i] - d4[i]) ** 2

    sum23 += (d2[i] - d3[i]) ** 2
    sum24 += (d2[i] - d4[i]) ** 2

    sum34 += (d3[i] - d4[i]) ** 2

print("sum01: " + str(sum01))
print("sum02: " + str(sum02))
print("sum03: " + str(sum03))
print("sum04: " + str(sum04))

print("sum12: " + str(sum12))
print("sum13: " + str(sum13))
print("sum14: " + str(sum14))

print("sum23: " + str(sum23))
print("sum24: " + str(sum24))

print("sum34: " + str(sum34))
print("***********************")

for i in [l:r+1]:
    print(i)

