def one(a):
    b=10
    def two(c):
        nonlocal b
        result=a+b+c
        print("a={},b={},c={}=sum={}".format(a,b,c,result))
        b+=1
    return two
result=one(10)
for val in range(1,5):
    print("hello world")
    result(val)