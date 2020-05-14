# your task is to complete this function
# finvtion should return an integer
def transitionPoint(arr, n):
    #Code here
    
    if arr.count(1) == 0 :
        return -1
    else:
        return arr.index(1)



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends