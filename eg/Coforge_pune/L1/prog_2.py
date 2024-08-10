# find 5th max number
# 33,1,4
# pivot = 1


def sort_arr(arr, sorted_arr=[], pivot=None):
    if not arr:
       return sorted_arr
    else:

        if not sorted_arr:
            elem = arr.pop()
            pivot = len(arr)//2
            sorted_arr.append(arr[pivot])
        else:
            pivot = len(arr)//2
            sorted_arr.append(arr[pivot])

        return sort_arr(arr=arr, sorted_arr=sorted_arr, pivot=pivot)
        

def max_number(arr, n):
    sorted_arr = sort_arr(arr)
    print("sorted_arr=", sorted_arr)

arr = [44,2,1,3,4]
print("max_number=", max_number(arr=arr, n=2))
