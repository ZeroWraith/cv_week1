class Matrix:
    """Represents a matrix and its operations."""

    def __init__(self, matrix_data):
        self.data = matrix_data
        self.rows = len(self.data)
        # Handle empty matrix case to avoid errors
        self.cols = len(self.data[0]) if self.rows > 0 else 0

    def __add__(self, other_matrix):
        """
        Adds two matrices together.
        Raises a ValueError if dimensions do not match.
        """
        # 1. ERROR CHECKING
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrices must have the same dimensions to be added.")

        # 2. ADDITION LOGIC
        # Create a new matrix to store the results
        result_data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        # Iterate through each row and column
        for i in range(self.rows):
            for j in range(self.cols):
                # Perform the addition for each element
                result_data[i][j] = self.data[i][j] + other_matrix.data[i][j]

        # Return a new Matrix object with the resulting data
        return Matrix(result_data)
    def scamul(self, scalar):
        # 3 Scalar Multiplication
        #creates a new matrix to store the results
        result_data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
        #iterate through the matrix
        for i in range(self.rows):
            for j in range(self.cols):
                #perform the multiplication for each element
                result_data[i][j] = self.data[i][j] * scalar
                
        # Return a new Matrix object with the resulting data
        return Matrix(result_data)

    def __repr__(self):
        """A helper method to print the matrix nicely."""
        return f"Matrix({self.data})"