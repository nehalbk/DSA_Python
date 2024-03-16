# Calculate GCD of 2 numbers

m = 21
n = 14

def gcd_euclidian(a,b):
    if a==b:
        return a
    elif a == 0:
        return b
    elif b==0:
        return a
    else:
        if a>b:
            return gcd_steins((a-b),b)
        else:
            return gcd_steins((b - a), a)

# Using Stein's Algorithm (Binary shift)
def gcd_steins(a,b):
    if a==b:
        return a
    elif a == 0:
        return b
    elif b==0:
        return a
    else:
        if a&1 ==0 and b&1 ==0:
            return gcd_steins(a>>1,b>>1)<<1
        elif a&1 ==0:
            return gcd_steins(a >> 1, b)
        elif b&1 ==0:
            return gcd_steins(a , b>> 1)
        elif a>b:
            return gcd_steins((a-b)>>1,b)
        else:
            return gcd_steins((b - a) >> 1, a)


# Using Euclidian Algorithm with Recursion

def gcd_euclidian_recursion(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclidian_recursion(b, a % b)

print("gcd_euclidian : ",gcd_euclidian(n, m))
print("gcd_euclidian_recursion : ",gcd_euclidian_recursion(n, m))
print("gcd_steins : ",gcd_steins(n, m))
