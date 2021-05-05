li = list(map(int, input('enter list of elements seperated by space: ').split()))

s = set(li)

frequencyList = {x: li.count(x) for x in s}

fvalues = list(frequencyList.keys())
frequencies = list(frequencyList.values())

print(frequencyList)

M = max(frequencies)
m = min(frequencies)

print([x for x in fvalues if frequencyList[x] == M],
      [x for x in fvalues if frequencyList[x] == m])
