# An implementation of Extended Euclidean Algorithm  
def gcdExtended(a, b):  
    if a == 0 :   
        return b, 0, 1   
    gcd, x1, y1 = gcdExtended(b%a, a)  
    # Update x and y using results of recursive call  
    x = y1 - (b//a) * x1  
    y = x1  
    return gcd, x, y 

def computeMod(num,power, modulus):
    ans = pow(num,power) % modulus
    return ans

def gcdCompute(a, b):  
    if a == 0 : 
        return b  
    temp =  gcdCompute(b%a, a)
    if temp==1:
        return 1
    else:
        return temp 

def orderGen(num, p):
    myArr = []
    num=1
    while num <= p-1:
        temp =  gcdCompute(p%num, num)
        if temp==1:
            myArr.append(num)
        num+=1
    return myArr 

def nthRootOfNumberInModulus(power, modulus,needed):
    modRange = [x for x in range(modulus) if x >=1]
    hasPowerInMod = list()
    ans = list()
    i = 1
    while i < modulus:
        computedPow = pow(i,power) % modulus
        if computedPow in modRange:
            hasPowerInMod.append(i)
        if computedPow==needed:
            ans.append(i)
        i+=1
    return hasPowerInMod, ans

def numRaisedToWhatGivesAnum(theNum, modulus):
    Dlog = list()
    i=1
    while i < modulus:
        computedPow = (pow(theNum,i)) % modulus
        Dlog.append([computedPow,i])
        i+=1
    return Dlog

def whatNumPowAnumGivesAnum(power,ans,modulus):
    requiredNumber=0
    i=1
    while i < modulus:
        someNum = pow(i,power) % modulus
        if someNum==ans:
            requiredNumber=i
        i+=1
    return requiredNumber


a, b = 7,23
g, x, y = gcdExtended(a, b)  
print("gcd(", a , "," , b, ") = ", g)
print('x: ', x)
print('y: ', y) 

ans = computeMod(2,245,35)
print('Mod compute: ', ans)

result =  gcdCompute(1,12)
print('Result: ', result)

invElem = orderGen(1,13)
print('List: ', invElem)
print('Number of elements: ', len(invElem))

insideMod, myAns = nthRootOfNumberInModulus(2,11,3)
print('Inside mod: ', insideMod)
print('Answer is: ', myAns)

myDlogList = numRaisedToWhatGivesAnum(2, 13)
print('Dlog list: ', myDlogList)

reqAns = whatNumPowAnumGivesAnum(11,2,19)
print('Required answer: ', reqAns)