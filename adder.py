def adder(x,y):
    Z=x+y
    return Z
a=adder('s','t');b=adder([1,2],[0,1]);c=adder(12.01,14.08);
print(a,b,c);

     # """arbitrary"""#
def adder(num):
    sum=0
    for j in num:
        sum=sum+j
        return sum

"""key word"""
def adder(good,bad,ugly):
    Z:good+bad+ugly
    returnZ
good=7;bad=8;ugly=9;
w=adder(good=2,ugly=3)
"""error-adder missing bad as argument"""

