'''
MODEL TO CHECK PRIME NUMBER OR NOT.''
'''
def prime(num):
    '''
    MAIN FUNCTION .
    '''
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            return print("This Number is Prime ")
    return print("This is not a Prime Number")
n = int(input("ENTER THE NUMBER :"))
prime(n)
