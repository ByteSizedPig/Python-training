x = 5
y = 22

def addition():
    if x == 5:
        return x + y
    else:
        return "test"

#print(addition())
#print(x+y)


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

nums = [4,1,3,2]
rev = reversed(nums)
print(sorted(rev) == sorted(rev))