import sys
sys.setrecursionlimit(1500)
# Divide and Conquer Approach


def power(base, exp):
    if(exp == 1):
        return(base)
    elif (exp == 0):
        return(1)
    elif (exp % 2 == 0):
        return(power(base*base, exp/2))
    else:
        return(base * power(base*base, exp//2))


if __name__ == "__main__":
    base = int(input("Enter base value: "))
    exp = int(input("Enter exponential value: "))
    print("Result:", power(base, exp))
