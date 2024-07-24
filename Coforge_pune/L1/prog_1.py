# using recursion shift the list by k=1
# l = [1,2,3,4,5] output = [5,1,2,3,4]
l = [1,2,3,4,5]
def list_shifter(l, k=1, output=[]):
    if k!=0:
        a = l.pop()
        output.append(a)
        return list_shifter(l=l, k=k-1, output=output)
    else:
        return output + l
    
output = list_shifter(l=l, k=2)

print("output=", output)