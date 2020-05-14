#User function Template for python3

def reverseArray(arr,n):
    
    #code here
    arr.reverse()
    return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        reverseArray(arr,n)
        
        for e in arr:
            print(e,end=' ')
        print()
# } Driver Code Ends