def my_func(n):
    if (n==2):
        return False
    elif (n==4):
        return True;
    else:
        for x in range(4,n):
             if(n % x==0):
                  return False
        return True
print(my_func(18))