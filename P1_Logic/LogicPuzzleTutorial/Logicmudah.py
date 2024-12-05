# t = int(input("Masukkan tinggi segitiga: "))
# for i in range(1,t):
#   print(i * "*")

# t = int(input("Masukkan tinggi segitiga: "))
# for i in range(1,t+1):
#   print((t-i+1) * "*")

# t = int(input("Masukkan tinggi segitiga: "))
# for i in range(1,t+1):
#   print((t-i) * " " + (2*i-1) * "*")

SIZE = 9

print('Soal 1')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print('*' if (row == col) else ' ', end='')
    print()
print()