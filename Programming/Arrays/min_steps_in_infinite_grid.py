class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        n = len(A)
        sum = 0
        for i in range(0,n-1):
            x = abs(A[i+1]-A[i])
            y = abs(B[i+1]-B[i])
            sum = sum + max(x,y)
        return sum