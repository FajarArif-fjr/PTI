
def crange(a,b):
  return range(a,b+1)
def printnln(a):
    print(a, end='')

# Soal 1
for k in crange(1,9):
  for b in crange(1,9):
    if b == k:
      j = b * 2 - 1
      printnln(j)
    else:
      printnln('_')
  print()

## Soal 2
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b == 9 - (k - 1):
#       n = b * 2 - 2
#       printnln(n)
#     else:
#       printnln('_')
#   print()

# Soal 3
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b == k:
#       j = b * 2 - 1
#       printnln(j)
#     elif b == 9 - (k - 1):
#       n = b * 2 - 2
#       printnln(n)
#     else:
#       printnln('_')
#   print()

#Soal 4
# Pola silang dengan angka dan garis tengah
# for k in crange(1, 9):  # Loop untuk setiap baris
#     for b in crange(1, 9):  # Loop untuk setiap kolom
#         if b == k or b == 5:  # Diagonal utama atau kolom ke-5
#             j = b * 2 - 1  # Perhitungan angka
#             printnln(j)
#         elif b == 9 - (k - 1) or k == 5:  # Diagonal sekunder atau baris ke-5
#             n = b * 2 - 2  # Perhitungan angka
#             printnln(n)
#         else:  # Di luar pola
#             printnln('_')
#     print()  # Pindah ke baris baru

# Soal 5
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b <= k:
#       j = b * 2-1
#       printnln(j)
#     else:
#       printnln('_')
#   print()

# Soal 6
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b >= 9 - (k-1):
#       v = 9 - (k-1)
#       n = v * 2 - 2
#       printnln(n)
#     else:
#       printnln('_')
#   print()

  # Soal 7
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b == k:
#       j = k * 2 - 1
#       printnln(j)
#     elif b == 9 -(k - 1):
#       n = b * 2 -2
#       printnln(n)
#     elif b > k and b < 9 -(k - 1):
#       printnln("A")
#     elif b < k and b > 9 - (k-1): 
#       printnln("B")
#     else:
#       printnln("_")
#   print()
