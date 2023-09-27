#NOTE Positional-Only Parameters and Keyword-only arguments

def f1(a, b, /, c , d):# '/' is a positional-only parameter
    print(a,b,c,d)

def f2(a, b, *, c, d): # '*' is a keyword-only argument  
    print(a,b,c,d)


f1(1, 2, 3, 4)
#f1(1, b = 2,  3, 4) #BUG left of '/' must be positional argument otherwie raise error


f2(1, 2, c=3, d=4)
f2(a = 1, b = 2,  c = 3, d = 4) #BUG  right of '*' must be keyword argument otherwie raise error
 