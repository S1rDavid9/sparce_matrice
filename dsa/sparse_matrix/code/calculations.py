# # Complete Sparse Matrix Program

# ## 📂 SparseMatrix Class Definition

# class SparseMatrix:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.data = {}

#     def getElement(self, row, col):
#         return self.data.get(row, {}).get(col, 0)

#     def setElement(self, row, col, value):
#         if value != 0:
#             self.data.setdefault(row, {})[col] = value
#         elif row in self.data and col in self.data[row]:
#             del self.data[row][col]

#     @classmethod
#     def fromFile(cls, filepath):
#         rows, cols = 0, 0
#         data = {}
#         with open(filepath, 'r') as file:
#             for line in file:
#                 line = line.strip()
#                 if line.startswith('rows='):
#                     rows = int(line.split('=')[1])
#                 elif line.startswith('cols='):
#                     cols = int(line.split('=')[1])
#                 elif line.startswith('('):
#                     r, c, v = map(int, line.strip('()').split(','))
#                     data.setdefault(r, {})[c] = v
#         matrix = cls(rows, cols)
#         matrix.data = data
#         return matrix


# ## ➕➖✖️ Matrix Operations

#     def add(self, other):
#         result = SparseMatrix(self.rows, self.cols)
#         for r in set(self.data) | set(other.data):
#             for c in set(self.data.get(r, {})) | set(other.data.get(r, {})):
#                 result.setElement(r, c, self.getElement(r, c) + other.getElement(r, c))
#         return result

#     def subtract(self, other):
#         result = SparseMatrix(self.rows, self.cols)
#         for r in set(self.data) | set(other.data):
#             for c in set(self.data.get(r, {})) | set(other.data.get(r, {})):
#                 result.setElement(r, c, self.getElement(r, c) - other.getElement(r, c))
#         return result

#     def multiply(self, other):
#         if self.cols != other.rows:
#            raise ValueError("Matrix dimensions are not compatible for multiplication")
    
#         result = SparseMatrix(self.rows, other.cols)
#         for r, row_values in self.data.items():
#             for k, val in row_values.items():
#                 if k in other.data:
#                    for c, other_val in other.data[k].items():
#                           result.data.setdefault(r, {}).setdefault(c, 0)
#                           result.data[r][c] += val * other_val
#         return result


# ## 💾 Save Results to File

#     def saveToFile(self, filename):
#         with open(filename, 'w') as file:
#             file.write(f"rows={self.rows}\n")
#             file.write(f"cols={self.cols}\n")
#             for row in sorted(self.data):
#                 for col, val in sorted(self.data[row].items()):
#                     file.write(f"({row}, {col}, {val})\n")


# ## 🚀 Main Execution
# file1 = input("Enter first matrix file path: ")
# file2 = input("Enter second matrix file path: ")

# matrix1 = SparseMatrix.fromFile(file1)
# matrix2 = SparseMatrix.fromFile(file2)

# operation = input("Choose operation (1: Add, 2: Subtract, 3: Multiply): ")
# if operation == '1':
#     result = matrix1.add(matrix2)
# elif operation == '2':
#     result = matrix1.subtract(matrix2)
# elif operation == '3':
#     result = matrix1.multiply(matrix2)
# else:
#     print("Invalid choice.")
#     exit()

# result.saveToFile("result_output.txt")
# print("\nResult saved to result_output.txt")

# 🚀 Optimized Sparse Matrix Program with User Input & Fast Operations
import time

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def getElement(self, row, col):
        return self.data.get(row, {}).get(col, 0)

    def setElement(self, row, col, value):
        if value != 0:
            self.data.setdefault(row, {})[col] = value
        elif row in self.data and col in self.data[row]:
            del self.data[row][col]

    @classmethod
    def fromFile(cls, filepath):
        rows, cols = 0, 0
        data = {}
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('rows='):
                    rows = int(line.split('=')[1])
                elif line.startswith('cols='):
                    cols = int(line.split('=')[1])
                elif line.startswith('('):
                    r, c, v = map(int, line.strip('()').split(','))
                    data.setdefault(r, {})[c] = v
        matrix = cls(rows, cols)
        matrix.data = data
        return matrix

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        result = SparseMatrix(self.rows, self.cols)
        for r in set(self.data) | set(other.data):
            for c in set(self.data.get(r, {})) | set(other.data.get(r, {})):
                result.setElement(r, c, self.getElement(r, c) + other.getElement(r, c))
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = SparseMatrix(self.rows, self.cols)
        for r in set(self.data) | set(other.data):
            for c in set(self.data.get(r, {})) | set(other.data.get(r, {})):
                result.setElement(r, c, self.getElement(r, c) - other.getElement(r, c))
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")
        result = SparseMatrix(self.rows, other.cols)
        for r, row_values in self.data.items():
            for k, val in row_values.items():
                if k in other.data:
                    for c, other_val in other.data[k].items():
                        result.data.setdefault(r, {}).setdefault(c, 0)
                        result.data[r][c] += val * other_val
        return result

    def saveToFile(self, filename):
        with open(filename, 'w') as file:
            file.write(f"rows={self.rows}\n")
            file.write(f"cols={self.cols}\n")
            for row in sorted(self.data):
                for col, val in sorted(self.data[row].items()):
                    file.write(f"({row}, {col}, {val})\n")

    def displayMatrix(self, limit=20):
        print("\nDisplaying first 20x20 section of the matrix:")
        for r in range(min(self.rows, limit)):
            row_vals = [str(self.getElement(r, c)).rjust(5) for c in range(min(self.cols, limit))]
            print(" ".join(row_vals))

# -----------------------------
# Main Execution with User Input & Validation
# -----------------------------
file1 = input("Enter first matrix file name: ")
file2 = input("Enter second matrix file name: ")

matrix1 = SparseMatrix.fromFile(file1)
matrix2 = SparseMatrix.fromFile(file2)

print("Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication")
choice = input("Enter your choice (1/2/3): ")

start_time = time.time()
if choice == '1':
    result = matrix1.add(matrix2)
    operation_name = "Addition"
    filename = "addition_result.txt"
elif choice == '2':
    result = matrix1.subtract(matrix2)
    operation_name = "Subtraction"
    filename = "subtraction_result.txt"
elif choice == '3':
    result = matrix1.multiply(matrix2)
    operation_name = "Multiplication"
    filename = "multiplication_result.txt"
else:
    print("Invalid choice.")
    exit()
end_time = time.time()

time_taken = end_time - start_time
print(f"✅ {operation_name} completed in {time_taken:.6f} seconds.")

result.displayMatrix()
result.saveToFile(filename)
print(f"Result saved to {filename}")