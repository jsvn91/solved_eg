# s1 = "abc"
# final = []
#
# for i in range(0,len(s1)):

# in = [1,2,3,1,4,5,6,2,11,12,3]
# output = len([1,2,3,4,5,6,11,12])

l = [1,2,3,30,1,4,5,6,2,11,12,3,30]
sorted_l = sorted(l)
final = {}

for i in sorted_l:

    if i in final:

        final[i] = final[i] + 1

    else:

        final[i] = 1

print("the sequence is ",list(final.keys()))
print("the longest output sequence is ",len(final.keys()))


x, y ,z = 0,1,2

if x == y or z:
   print("Here")


try:
    num = 1/0
except:
    print("num",num)
