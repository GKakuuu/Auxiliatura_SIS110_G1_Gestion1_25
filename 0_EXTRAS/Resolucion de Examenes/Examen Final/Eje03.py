# 3.	Se tiene una secuencia de N números enteros positivos (10<N<100000) cada uno de ellos será menor o igual a 10000, y un entero positivo S < 100000000, necesitamos escribir un programa para encontrar la longitud mínima de subsecuencia de elementos consecutivos de la secuencia cuya suma sea igual a S. La entrada de valores comenzara con N y S, posteriormente en una nueva línea N valores

# Input
# 3 100
# 9 90 10
# 	
# 10 15
# 5 1 3 3 1 7 1 9 2 8	

# Output
# 2

# 4

n = int(input())
s = int(input())

nums = input().split(" ")

for i in range (len(nums)):
    sum = 0
    cont = 0
    # print ("Empezando en... " , nums[i])

    for j in range (i, len(nums)):
        # print ("sumando...", nums[j] , " con " , sum)
        sum = int(sum) + int(nums[j])
        cont = cont + 1
        if sum == s:
            print(cont)
            break
        if sum > s:
            break
    if sum == s:
        break

