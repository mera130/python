def ispallindrome(string):
    left = 0
    right = len(string) - 1

    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1
        right -= 1 
    return True

print("is this pallidrome?") 
print(ispallindrome(bob))     
      