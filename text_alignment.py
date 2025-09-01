n = int(input())
width = 2*n-1
# block 1
for value in range(n):
    line = 'H' * (2*value+1)
    print(line.center(width,' '))
#block 2

for value in range(n+1):
    seg1 = ('H' * n).center(width, ' ')
    seg2 = ' ' * (2*n+1)
    print(seg1 + seg2 + seg1)
#block 3
temp = int(n + (width-n)/2)
for value in range(int((n+1)/2)):
    seg1 = ('H' * temp).rjust(width, ' ')
    seg2 = 'H' * (2*n+1)
    seg3 = ('H' * temp).ljust(width, ' ')
    print(seg1+seg2+seg3)
#block 4
for value in range(n+1):
    seg1 = ('H' * n).center(width, ' ')
    seg2 = ' ' * (2*n+1)
    print(seg1 + seg2 + seg1)
#Block 5
for value in range(n-1, -1, -1) :
    seg1 = ' ' * width
    seg2 = ' ' * (2*n+1)
    seg3 = ('H' * (2 * value + 1)).center(width,' ')
    print(seg1 + seg2 + seg3)