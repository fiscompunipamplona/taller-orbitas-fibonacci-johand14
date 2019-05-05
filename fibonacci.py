#Serie de Fibonacci con n<=1000
f0=0
f1=1
print("Hacemos un conteo desde 0 hasta 1000")
print(f0)
while f1<=1000:
    print(f1)
    f2=f0+f1
    f0=f1
    f1=f2
