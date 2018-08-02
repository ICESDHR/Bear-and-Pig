def isPalindrome(x):
    x = str(x)
    if(x[::-1] == x):
        return True
    else:
        return False

if __name__=="__main__":
    print(isPalindrome(121))