import numpy as np

SHOW_LUCAS, SHOW_DIFF, SHOW_EVAL, SHOW_GRAPH, SHOW_COEFF = True, True, True, True, True

SHOW_LUCAS = False
SHOW_DIFF = False
SHOW_EVAL = False
#SHOW_GRAPH = False
#SHOW_COEFF = False

def lucas_generator():
    a, b = 1, 3
    while True:
        ret, a = a, b
        b = a+ret
        yield ret

def lucas(n):
    lg = lucas_generator()
    return [next(lg) for i in range(n)]

def coeff_graph(n):
    graph = [np.zeros(n) for i in range(n)]
    for i in range(n):
        graph[i][i] = 1
    for i in range(n-1):
        graph = graph[1:]
        for j in range(1, len(graph)):
            graph[j] = graph[j-1] + graph[j]
    return graph[0]

def factorial_array(n, mod):
    arr = [1] * (n+1)
    for i in range(1, n+1):
        arr[i] = (arr[i-1] * i) % mod
    return arr

def inverse_array(arr, mod):
    
    def extended_euclid_algorithm(a, b):
        #ax+by = r
        s0, t0 = 1, 0
        s1, t1 = 0, 1
        r0, r1 = a, b
        while r1 != 0:
            q = r0 // r1
            r0, r1 = r1, r0 - q * r1
            s0, s1 = s1, s0 - q * s1
            t0, t1 = t1, t0 - q * t1
        return r0, s0, t0
        
    inv_arr = [0] * len(arr)
    for i in range(len(inv_arr)):
        _, inv, _ = extended_euclid_algorithm(arr[i], mod)
        inv_arr[i] = inv
    return inv_arr

def binom(n, k, mod, fac_arr, inv_arr):
    if mod:
        return (fac_arr[n] * inv_arr[(fac_arr[k] * fac_arr[n-k]) % mod]) % mod
    else:
        return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))

def catalan_triangle(n, k, mod, fac_arr, inv_arr):
    #https://en.wikipedia.org/wiki/Catalan%27s_triangle
    #print(n+k)
    #print(len(fac_arr))
    #print((fac_arr[k] * fac_arr[n+1]) % mod)
    return (((fac_arr[n+k] * (n-k+1)) % mod) * inv_arr[(fac_arr[k] * fac_arr[n+1]) % mod]) % mod

def coeff_explicit(n, mod):
    if n == 1:
        return [1]
    else:
        fac_arr = factorial_array(max(2*n, mod), mod)
        inv_arr = inverse_array(fac_arr, mod)
        row = [catalan_triangle(n, k, mod, fac_arr, inv_arr) for k in range(n-1)]
        return [0] + row[::-1]
    
    
def f_graph(sequence):
    coeffs = coeff_graph(len(sequence))
    return sum([coeffs[i] * sequence[i] for i in range(len(sequence))])

def f_array(sequence):
    if len(sequence) == 1:
        return sequence[0]
    else:
        sequence = sequence[1:]
        partial_sums = []
        for n in sequence:
            partial_sums.append(n if len(partial_sums) == 0 else partial_sums[-1] + n)
        return f_array(partial_sums)
    
def f_ones(n, f_func):
    return f_func([1]*n)

def f_lucas(n, f_func):
    return f_func(lucas(n))


if SHOW_LUCAS:
    print("="*50 + "\nLUCAS TESTING\n" + "="*50)
    print(lucas(10))
    print("\n\n")

if SHOW_DIFF:
    print("="*50 + "\nDIFFERENCE TESTING\n" + "="*50)
    print("\nOnes Difference")
    for i in range(1, 10):
        print("Input: {} Output Difference: {}".format(i, f_ones(i, f_array)-f_ones(i, f_graph)))
    print("\nLucas Difference")
    for i in range(1, 10):
        print("Input: {} Output Difference: {}".format(i, f_lucas(i, f_array)-f_lucas(i, f_graph)))
    print("\n\n")
    
if SHOW_EVAL:
    print("="*50 + "\nEVALUATION TESTING\n" + "="*50)
    print("\nOnes Evaluation")
    for i in range(1, 10):
        print("Input: {} Output: {}".format(i, f_ones(i, f_array)))
    print("\nLucas Evaluation")
    for i in range(1, 10):
        print("Input: {} Output: {}".format(i, f_lucas(i, f_array)))
    print("\n\n")
    
if SHOW_GRAPH:
    print("="*50 + "\nGRAPH TESTING\n" + "="*50)
    for i in range(1, 10):
        print("Input: {} Output: {}".format(i, coeff_graph(i)))
        
if SHOW_COEFF:
    print("="*50 + "\nCOEFF EXPLICIT\n" + "="*50)
    for i in range(1, 10):
        print("Input: {} Output: {}".format(i, coeff_explicit(i, 100000)))
            