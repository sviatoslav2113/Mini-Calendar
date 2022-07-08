m, n = map(int, input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a = '0'
if n == 1:
    ym = m - 1
    yn = days[m - 1]
    tm = m
    tn = n + 1
    print(f'{str(ym).rjust(2, a)}.{str(yn).rjust(2, a)} {str(tm).rjust(2, a)}.{str(tn).rjust(2, a)}' )
elif n == days[m - 1]:
    ym = m
    yn = n - 1
    tm = m + 1
    tn = 1
    print(f'{str(ym).rjust(2, a)}.{str(yn).rjust(2, a)} {str(tm).rjust(2, a)}.{str(tn).rjust(2, a)}' )
else:
    ym = m
    yn = n - 1
    tm = m
    tn = n + 1
    print(f'{str(ym).rjust(2, a)}.{str(yn).rjust(2, a)} {str(tm).rjust(2, a)}.{str(tn).rjust(2, a)}' )
 

 