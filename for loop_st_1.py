list_one=[]
list_two=[]
list_three=[]
list_four=[]

li = [1,2,5,7]
n = len(li)

for i in range(n):
    for j in range(n):
        if i ==0:
            list_one.append(li[i]*li[j])
        elif i == 1:
            list_two.append(li[i]*li[j])
        elif i == 2:
            list_three.append(li[i]*li[j])
        elif i == 3:
            list_four.append(li[i]*li[j])

print(list_one)
print(list_two)
print(list_three)
print(list_four)