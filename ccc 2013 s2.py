W = int(input())
array = []
for i in range(int(input())):
    array.append(int(input()))
    if len(array) >= 4:
        if sum(array[-4:]) > W:
            array.pop()
            break
    else:
        if sum(array[:]) > W:
            array.pop()
            break
print(len(array))
    
    
    
