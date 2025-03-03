print("-----------------------ESERCIZIO 1------------------------")
numS1 = [1,2,3,4,5]
for num in numS1:
    print(num)
print(num)

print("-----------------------ESERCIZIO 2------------------------")
numS2 = []
for i in range(10):
    num = i+1
    numS2.append(num)
    print(num)

print("-----------------------ESERCIZIO 3------------------------")
numS3 = [1,2,3,4,5]
som3 = 0
for num in numS3:
    som3+=num
print(som3)

print("-----------------------ESERCIZIO 4------------------------")
for i in range(1,20):
        if i%2 == 0:
            print(i)

print("-----------------------ESERCIZIO 5------------------------")
string5 = "1,2,3,4,5"
for i in string5:
     print(i)

print("-----------------------ESERCIZIO 6------------------------")
numS6 = [1,2,3,4,5]
som6 = 1
avg6 = 0
for num in numS6:
    som6 += num 
avg6 = som6/len(numS6)
print(avg6)