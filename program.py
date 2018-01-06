def testfunc(n):
    if n==1:return 1
    return n*(testfunc(n-1))

for i in range(1,11):print(testfunc(i))

# Factorial numbers from 1! to 10!
