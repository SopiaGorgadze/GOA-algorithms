#დაამტკიცეთ, რომ min(f) <= E(f) <= max(f);


list = [4, 2, 3, 4, 5, 6]
 

min = list[0]
max = list[0]
expected = 0

for i in range(len(list)):
    if min >= list[i]:
        min = list[i]
 
for i in range(len(list)):
    if max <= list[i]:
        max = list[i]

for i in list:
    expected += i

expected = expected // len(list)


print(min <= expected <= max)
