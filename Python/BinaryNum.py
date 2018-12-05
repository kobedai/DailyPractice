n = int(input())
maxCount = max([len(a) for a in str(bin(n)[2:]).split('0')])
print(maxCount)
