n = int(input('Enter size of n X n matrix: '))
print('Enter elemnts of matrix row-by-row, seperated by a space: ', end='\n')
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

print('Matrix entered', matrix)
