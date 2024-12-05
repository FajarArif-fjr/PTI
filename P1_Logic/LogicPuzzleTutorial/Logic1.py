
def crange(a,b):
  return range(a,b+1)
def printnln(a):
    print(a, end='')

# # #Soal 1
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b == k:
#       printnln('*')
#     else:
#       printnln('_')
#   print()

# #Soal 5
# for k in crange(1,9):
#   for b in crange(1,9):
#     if k >= b:
#       printnln('*')
#     else:
#       printnln('_')
#   print()

# #Soal 2
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b + k == 10:
#       printnln('*')
#     else:
#       printnln('_')
#   print()

# # # Soal 6
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b + k >= 10:
#       printnln('*')
#     else:
#       printnln('_')
#   print()

# # Soal 3
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b == k:
#       printnln('*')
#     elif b + k == 10:
#       printnln('*')
#     else:
#       printnln('_')
#   print()

# Soal 4
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b == k:
#       printnln('*')
#     elif b + k == 10:
#       printnln('*')
#     elif b == 5:
#       printnln('*')
#     elif k == 5:
#       printnln('*')
#     else:
#       printnln(' ')
#   print()

# Soal 7
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b >= k and b <= 9 -(k - 1):
#       printnln('*')
#     elif b <= k and b >= 9 -(k - 1):
#       printnln('*')
#     else:
#       printnln("_")
#   print()

# Soal 8
# for k in crange(1,9):
#   for b in crange(1,9):
#     if b <= k and b <= 9 -(k - 1):
#       printnln('*')
#     elif b >= k and b >= 9 -(k - 1):
#       printnln('*')
#     else:
#       printnln("_")
# print()