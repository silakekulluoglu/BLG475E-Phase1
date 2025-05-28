'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def poly(coeffs, x):
    """Evaluate the polynomial at a given value of x."""
    return sum(coeff * (x ** i) for i, coeff in enumerate(coeffs))

def find_zero(xs):
    if len(xs) % 2 != 0:
        raise ValueError("The input list must contain an even number of coefficients.")
    if xs[-1] == 0:
        raise ValueError("The input list must not end in 0.")
    
    # Bisection method to find a root
    def bisection(coeffs, a, b, tol=1e-10):
        fa = poly(coeffs, a)
        fb = poly(coeffs, b)
        
        if fa * fb >= 0:
            raise ValueError("No sign change detected in the interval [{}, {}].".format(a, b))
        
        while (b - a) / 2.0 > tol:
            c = (a + b) / 2.0
            fc = poly(coeffs, c)
            
            if fc == 0:
                return c
            elif fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        
        return (a + b) / 2.0
    
    # Try to find an interval [a, b] where the polynomial changes sign
    a, b = -1.0, 1.0
    max_iter = 1000  # To prevent infinite loops in case of numerical issues
    
    # Expand the interval until a sign change is detected
    for _ in range(max_iter):
        fa = poly(xs, a)
        fb = poly(xs, b)
        
        if fa * fb < 0:
            return bisection(xs, a, b)
        
        a *= 2.0
        b *= 2.0
    
    raise ValueError("No interval found where the polynomial changes sign.")