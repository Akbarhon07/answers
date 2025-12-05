def factorial(n):
    """Sonni faktorialini hisoblaydi"""
    summ = 1
    for i in range(n + 1):
        summ = summ * i
    return summ




def fibonacci(n):
    """Sonni fibrinachisini hisoblaydi"""  
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b
    return a





def to_uppercase(s):
    """Matinni hamma harfini kotta qib qaytaradi"""
    return s.upper() 




