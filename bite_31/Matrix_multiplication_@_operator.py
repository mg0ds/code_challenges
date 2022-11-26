class Matrix:

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'
        
    def matrix_mulltiply(self, A, B):
        self.A = A
        self.B = B
        N = len(self.A)
        M = len(self.A[0])
        P = len(self.B[0])
        
        result = []
        for i in range(N):
            row = [0] * P
            result.append(row)
            
        for i in range(N):
            for j in range(P):
                for k in range(M):
                    result[i][j] += self.A[i][k] * self.B[k][j]
        return result
        
    def __matmul__(self, B):
        mA = self.values
        mB = B.values
        return Matrix(self.matrix_mulltiply(mA, mB))
        
    
    def __rmatmul__(self, B):
        mA = self.values
        mB = B.values
        return Matrix(self.matrix_mulltiply(mA, mB))
    
    def __imatmul__(self, B):
        self.values = self.matrix_mulltiply(self.values, B.values)
        return self
