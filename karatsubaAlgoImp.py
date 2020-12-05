from math import ceil, floor

def karatsuba(x,y):
    #Base example
    if x < 10 and y < 10: # Takes care of cases where x and y are single digits
        return x*y
    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)   #Cast n into a float because n might lie outside the representable range of integers.
    x_H  = floor(x / 10**m)
    x_L = x % (10**m)
    y_H = floor(y / 10**m)
    y_L = y % (10**m)
    #Iterative operations
    a = karatsuba(x_H,y_H)
    d = karatsuba(x_L,y_L)
    e = karatsuba(x_H + x_L, y_H + y_L) - a - d
    return int(a*(10**(m*2)) + e*(10**m) + d) # Return the product.
if __name__ == "__main__":
    num1 = 120000
    num2 = 115000
    print('*********************************************************')
    print('Result of Karatsuba multiplication: ', karatsuba(num1,num2))
    print('*********************************************************')