#User function Template for python3

def immediateSmaller(arr,n,x):
    #return required ans
    min_d = 1000000000
    ans = -1
    m = max(arr)
    if min(arr) >= x:
        return -1 
    elif m < x :
        return m
    else:    
        for v in range(n):
            d = x-arr[v]
            if d>0  and min_d>d :
                ans = arr[v]
                min_d = d
        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        
        ans=immediateSmaller(arr,n,x)
        print(ans)
# } Driver Code Ends