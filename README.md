# sparce_matrice

# 🚀 Sparse Matrix Calculator

Welcome to the **Sparse Matrix Calculator**! 🎉 This project is designed to efficiently perform operations (Addition, Subtraction, Multiplication) on **large sparse matrices** while keeping memory usage low and execution time fast. 🚀

## 📌 Features
✅ Read sparse matrices from files 📂  
✅ Perform **Addition, Subtraction, and Multiplication** ➕➖✖️  
✅ Validate matrix dimensions before operations 🔍  
✅ Display only **the first 20x20** section of results in the terminal 🖥️  
✅ **Save full results** to `.txt` files 💾  
✅ **Time tracking** for performance analysis ⏱️  
✅ Optimized to ignore **zero values**, making calculations super fast! ⚡

---

## 🧠 How It Works
Sparse matrices store only **non-zero values** to reduce memory usage. Instead of using a 2D list, we use a **dictionary of dictionaries** for storage:
```python
self.data = {row: {col: value}}
```
This allows quick lookup and modification while avoiding unnecessary zero storage.

### 📖 Matrix File Format
Each matrix is stored in a `.txt` file like this:
```
rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
(0, 639, 857)
```
- The first line gives **number of rows**.
- The second line gives **number of columns**.
- The remaining lines list **(row, column, value)** of non-zero elements.

### 🛠️ Operations Implemented
#### ➕ **Addition & Subtraction**
Matrices must have the **same dimensions** (rows and columns).
```python
result[r][c] = matrix1.getElement(r, c) ± matrix2.getElement(r, c)
```

#### ✖️ **Multiplication**
Matrix multiplication is valid when:
```
columns of A == rows of B
```
The calculation follows:
```python
result[r][c] = sum(matrix1.getElement(r, k) * matrix2.getElement(k, c) for k in matrix1[r])
```
This method **avoids unnecessary zero multiplications**, improving performance.

---

## 🕒 Time Optimization & Performance Tracking
We implemented **execution time tracking** using Python’s `time` module:
```python
start_time = time.time()
# Perform operation
end_time = time.time()
time_taken = end_time - start_time
print(f"✅ {operation} completed in {time_taken:.6f} seconds.")
```
This allows us to analyze how efficiently our algorithm performs. 🔥

---

## 💥 Challenges & Solutions
🚧 **GitHub Rejected Large Files** – Our result files exceeded **100MB**, so we removed them from history and used `.gitignore` to prevent tracking.
```bash
echo "multiplication_result.txt" >> .gitignore
git rm --cached multiplication_result.txt
git push origin main --force
```

🐌 **Multiplication Was Too Slow** – We optimized by iterating **only over non-zero elements**, reducing complexity.

🔄 **Handling Large Matrices in Terminal** – Instead of printing **all** values, we only display the **first 20x20** portion:
```python
for r in range(min(self.rows, 20)):
    for c in range(min(self.cols, 20)):
        print(self.getElement(r, c), end=" ")
    print()
```

---

## 🏃 How to Run the Project
### 🔹 1️⃣ Install Dependencies (Optional)
```bash
pip install git-filter-repo
```

### 🔹 2️⃣ Clone the Repository
```bash
git clone https://github.com/S1rDavid9/sparce_matrice.git
cd sparce_matrice/dsa/sparse_matrix/code/
```

### 🔹 3️⃣ Run the Script
```bash
python calculations.py
```

### 🔹 4️⃣ Enter Matrix File Names
Example:
```
Enter first matrix file name: easy_sample_02_1.txt
Enter second matrix file name: easy_sample_02_2.txt
```

### 🔹 5️⃣ Choose an Operation
```
Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
```

### 🔹 6️⃣ View & Save Results
✅ **First 20x20 matrix** is displayed in the terminal.
💾 **Full result** is saved as `addition_result.txt`, `subtraction_result.txt`, or `multiplication_result.txt`.

---

## ❤️ Fun Fact
Did you know? Sparse matrices are heavily used in **AI, Machine Learning, and Computer Vision**! Many real-world datasets have missing values, making sparse representations **super efficient**! 🤖✨

---

## 👨‍💻 Contributors
👤 **Nwanze Akachi David** 🚀  
🔗 GitHub: [S1rDavid9](https://github.com/S1rDavid9)  

---

## 📜 License
This project is open-source under the **MIT License**.

🌟 If you found this useful, give it a ⭐ on GitHub! Happy Coding! 😃🎉

