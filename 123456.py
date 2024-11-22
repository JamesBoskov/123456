from itertools import permutations
arr = [1, 2, 3, 4, 5, 6]
arr2 = list(permutations(arr, 6))
counter = 0
for i in arr2:
    a = i[0]
    b = i[1]
    c = i[2]
    d = i[3]
    e = i[4]
    f = i[5]

    age0 = c + a*e + b*(e**2)
    age1 = a + b*d + c*(d**2)
    age2 = b + c*f + a*(f**2)

    if age0+1 == age1 and age1+1 == age2:
        print(i)
    counter+=1
    if counter<10:
        print(age0, age1, age2)