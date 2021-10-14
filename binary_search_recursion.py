
def binarys(a,low,high,x):
    if high>=low:

        mid = (high+low)//2

        # if term is present at middle of array
        if a[mid] == x:
            return  mid

        # if term is smaller than mid,then it can only be present in left subarray
        elif a[mid]>x:
            return binarys(a,low,mid-1,x)

        # else the term will only be present in right subarray
        else:
            return binarys(a,mid+1,high,x)

    # term is not present
    else:
        return -1




a = [2,5,9,10,11,15,16,22]

x= 9

result = binarys(a,0,len(a)-1,x)

if result != -1 :
    print('term is present at index',str(result))
else:
    print("term is not present in array")


