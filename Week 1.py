
def f(x):
    return x*x*x

h = 0.1

def f_forward_der(x):
    ff_der = (f(x + h) - f(x))/h
    return ff_der

k = 4

print('forward difference derivative = ', f_forward_der(k))

    
    
    
    
