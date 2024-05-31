
# flag = False

def isPrime(num):
    if num<=1:
        return False
    for n in range(2,int(num**0.5)+1):
        if(num%n)==0:
            return False
    return True

def userInput():
    min = int(input("Enter min range: "))
    max = int(input("Enter max range: "))

    # is_prime =  False

    for num in range(min,max):
        if(num>1):
            if(isPrime(num)):
                print(num," : Yes..!")
            else:
                print(num," : No..!!")

print("Is it PrimeNumer: \n")
i = 0
while(i<15):
    userInput()
    i += 1
