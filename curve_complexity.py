# coding : utf-8
import matplotlib.pyplot as plt
import numpy as np
import time

plt.style.use("ggplot")

def f1(n, k):
    return k*n*n

def f2(n, k):
    return k*n*np.log(n)

def curve_method(N):
    k = 0
    p = np.arange(0, N)
    tps = 0
    k += 1
    t = time.time()
    plt.plot(p, f1(p, 1), c='blue', label='f1(n,k)=k*n*n')
    plt.plot(p, f2(p, 1), c='red', label='f2(n,k)=k*n*np.log(n)')
    plt.xlabel('Taille input(N) ', fontsize=16)
    plt.ylabel('Nombre opérations ', fontsize=16)
    plt.legend()
    plt.show()
    tps += time.time() - t
    print("La complexité est de :", tps/k)
    
curve_method(5506783)