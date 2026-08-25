x = 5
y = 22

def addition():
    if x == 5:
        return x + y
    else:
        return "test"

#print(addition())
#print(x+y)

def fizzbuzz(number):
    if number % 15 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)


aList = [1,8,4,6,33,76,79,23,45,0,6,7,9,99]

def listSort():
    sorted = False
    n = len(aList)
    while sorted == False:
        sorted = True
        for i in range (0, n - 1):
            if aList[i] > aList[i+1]:
                aList[i],aList[i+1] = aList[i+1],aList[i]
                print(aList)
                sorted = False

listSort()
print("-----------------------------------------------------")
print("coding question from \"Coding Jesus\" YT video")

nums = [4,1,3,2]
rev = reversed(nums)
print(sorted(rev) == sorted(rev))

print("-----------------------------------------------------")
print("Fizzbuzz test")

fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(5)
fizzbuzz(15)