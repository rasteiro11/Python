def fatorial(n, show=False):
   f = 1
   for c in range(n, 0, -1): # N eh o numero que voce quer o fatorial
       if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
       f *= c # f = f * c <=> 1) f = 1 * 5; 2) f = 5 * 4; 3) f = 20 * 3; 4) f = 60 * 2
   return f


num = int(input('Fatorial: '))
print(fatorial(num, show=True))

