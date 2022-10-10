#User function Template for python3
class Solution:

	def zigZag(self,arr, n):
	    flag = 1
	    for i in range(0, n-1):
	        if flag == 1:
	            if arr[i] > arr[i+1]:
	                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = not flag
        
	    
		# code here
		

	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends