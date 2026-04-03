#num=element to be find
#arr=array
#L=lowest index of the array
#H=highest index of the array
def Binarysearch(num,L,H,arr):
    if((L+H)%2==0):
        mid = (L+H)//2
    else:
        mid = (L+H)//2 + 1
    arr.sort()
    i=arr.index(num)
    print("the sorted array is:",arr)
    print("the mid value is :",mid)
    if (arr[i]==arr[mid]):
        print("element found and that is:",arr[mid])
    elif(arr[i]<arr[mid]):
        H = mid - 1
        return Binarysearch(num,L,H,arr)
    elif(arr[i]>arr[mid]):
        L = mid + 1 
        return Binarysearch(num,L,H,arr)
elem=int(input("finding element:"))
print("enter the elements in array")
array= list(map(int,input().split(",")))
Low=0
High=len(array)-1
Binarysearch(elem,Low,High,array)

        