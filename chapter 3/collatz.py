def collatz(number):
    if (number%2 == 0):
        result = number//2
        print(result)
        return result

    else:
        result = 3*number+1
        print(result)
        return result
        
n = input("number: ")
while n != 1:
    n = collatz(int(n))



