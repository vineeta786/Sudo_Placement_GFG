#User function Template for python3

def firstRepeated(arr, n):
    
    #arr : given array
    #n : size of the array
    
    for v in range(n):
        b = arr.count(arr[v])
        #print(b)
        if b>1:
            return v+1
    
    
    return -1          



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        
        print(firstRepeated(arr, n))
# } Driver Code Ends