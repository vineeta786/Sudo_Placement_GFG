# Function should return an integer value
def convertFive(n):
    # Code here
    
    s = str(n)
    
    ss = s.replace("0","5")
    
    return int(ss)



#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends