n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numberOfSwaps = 0
totalswaps= 0
for i in range(n):    
    numberOfSwaps = 0
    for j in range(n-1):
        if (a[j] > a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1
        
    if numberOfSwaps == 0:
        break
    totalswaps += numberOfSwaps
 
print("Array is sorted in %d swaps." % totalswaps)
print("First Element: %d" % a[0])
print("Last Element: %d" % a[-1])