#mean
list1 = [1,2,3,4,5]
mean = sum(list1)/len(list1)
print(mean)



# Median
l = [2,4,6,8]
l.sort()

if len(l) % 2 == 0:
    m1 = l[len(l)//2]
    m2 = l[len(l)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)



# Mode
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)
