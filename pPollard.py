from euclide_etendu import pgcd
from random import randint
from f_function import *


def method_pollard_p_ff(N):
    d = N
    while d == N:
        a = randint(0, N-1)
        x = ff(a) % N
        y = ff(ff(a)) % N
        d = pgcd(y-x, N)
        while d == 1:
            x = ff(x) % N
            y = ff(ff(y)) % N
            d = pgcd(y-x, N)
    return d


def method_pollard_p_f1(N):
    d = N
    while d == N:
        a = randint(0, N-1)
        x = ff(a) % N
        y = ff(ff(a)) % N
        d = pgcd(y-x, N)
        while d == 1:
            x = ff(x) % N
            y = ff(ff(y)) % N
            d = pgcd(y-x, N)
    return d


def method_pollard_p_f2(N):
    d = N
    while d == N:
        a = randint(0, N-1)
        x = ff(a) % N
        y = ff(ff(a)) % N
        d = pgcd(y-x, N)
        while d == 1:
            x = ff(x) % N
            y = ff(ff(y)) % N
            d = pgcd(y-x, N)
    return d


def method_pollard_p_f3(N):
    d = N
    while d == N:
        a = randint(0, N-1)
        x = ff(a) % N
        y = ff(ff(a)) % N
        d = pgcd(y-x, N)
        while d == 1:
            x = ff(x) % N
            y = ff(ff(y)) % N
            d = pgcd(y-x, N)
    return d


def method_pollard_p_f4(N):
    d = N
    while d == N:
        a = randint(0, N-1)
        x = ff(a) % N
        y = ff(ff(a)) % N
        d = pgcd(y-x, N)
        while d == 1:
            x = ff(x) % N
            y = ff(ff(y)) % N
            d = pgcd(y-x, N)
    return d


def factors(n):
    L = [method_pollard_p_ff(n)]
    i = 2
    while n > 1:
        c = 0
        while n%i==0:
            n = n // i
            c += 1
        if c != 0:
            L.append((i, c))
        i+=1
    T = L
    del T[0]
    return T


if __name__ == "__main__":

    N = 4084124448344004754912241637815877808336372780520907324804559568673294885286043814389079079960630641743531555193481197222840732681883761561593302492947600806166888244287519415286784197130295878723581812513909128304778613974346762350692652193784994733056584288099881492369930687007384033550767983258614997450722045392166447420926930860034780076723027702304988355173102694931070775399585009467546205990176498841213004029855386581909584241581830809987551050155099283256891972399838893498418101173250472147408798612971669168579061499210538544399971661389039339523886246503336105429138385097170439083315816004412324744611
    q = method_pollard_p_ff(N)
    print(q)
    p = N//q
    print(p)


#    Test = [1457, 2047, 4189, 27451, 172847, 5506783,
 #           122839103, 2373442927, 2432194014911, 
  #          2386194275560789, 2543362194387034583, 
   #         3256575592288000884277, 2149473581756425241209729, 
    #        3125606949137512111921043650752342509711]
    
   # for N in Test:
    #    print("Réponse à la question 2 :")
     #   print("Factorisation de N avec la fonction d'itération f générique: f(z)= z² + 1 :")
      #  print(f"Factorisation de {N} :{method_pollard_p_ff(N)}")
       # print("==========================================")
  #      print("La réponse à la question 4 :")
   #     print("Factorisation de N avec la fonction d'itération f générique: f(z)= z + 1 :")
    #    print(f"Factorisation de {N} :{method_pollard_p_f1(N)}")
     #   print("==========================================")
      #  print("Factorisation de N avec la fonction d'itération f générique: f(z)= z² :")
    #    print(f"Factorisation de {N} :{method_pollard_p_f2(N)}")
     #   print("==========================================")
     #   print("Factorisation de N avec la fonction d'itération f générique: f(z)= z² + 2 :")
      #  print(f"Factorisation de {N} :{method_pollard_p_f3(N)}")
       # print("==========================================")
      ######  print("Factorisation de N avec la fonction d'itération f générique: f(z)= z² - 1 :")
      #####  print(f"Factorisation de {N} :{method_pollard_p_f4(N)}")
    ###    print("==========================================")
     ####   print("==========================================")
     ##   print("La réponse à la question 5 en utilisant la méthode p comme sous fonction(la fonction d'itération f générique: f(z)= z² + 1) ")
    #  print(f"Factorisation de {N} :{factors(N)}")
