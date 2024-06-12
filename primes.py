factors = []

#for number in x:

    

primefactor = 2
number = int(input("Please give me a number: "))
while number != 1:
    if number % primefactor == 0:
        factors.append(primefactor)
        number = number / primefactor
    else:
        primefactor += 1

print(factors)