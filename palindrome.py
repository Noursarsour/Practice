def isPalindrome(x):
      
       rev = 0
       n=x
 
       while(x > 0):
            a = x % 10
            rev = rev * 10 + a
            x = x // 10
       print(rev)
       print(x)

       if rev == n:
            return True
       return False
