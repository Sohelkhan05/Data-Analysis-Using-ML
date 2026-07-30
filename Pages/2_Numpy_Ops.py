import streamlit as st
import numpy as np

st.title("Numpy Operations")

st.header("Q - 1 : Create and display a Numpy array")
with st.expander("Q-1-a : Create and display a Numpy array"):
    arr = np.arange(1,11)
    st.success(f"Numpy Array: {arr}")

with st.expander("Q-1-b : Even numbers from 1 to 20"):
    even_arr = np.arange(2,21,2)
    st.success(f"Even numbers from 1 to 20: {even_arr}")

with st.expander("Q-1-c : A 5 X 5 array with zero"):
    arr = np.zeros((5,5))
    st.success(f"5 X 5 array with zero:\n\n {arr}")

with st.expander("Q-1-d : A 4 X 4 array with one"):
    arr = np.ones((4,4))
    st.success(f"4 X 4 array with one:\n\n {arr}")

st.header("Q - 2 : Create 3 X 3 identity matrix")
with st.expander("Q-2 : Create 3 X 3 identity matrix"):
    arr = np.eye(3)
    st.success(f"3 X 3 identity matrix:\n\n {arr}")

with st.expander("Q-2 - a : A one-dimensional array containing numbers from 1 to 10."):
    arr = np.arange(1,11)
    st.success(f"One-dimensional array containing numbers from 1 to 10:\n\n {arr}")

with st.expander("Q-2 - b : An array containing only even numbers between 2 and 20. "):
    arr = np.arange(2,21,2)
    st.success(f"Array containing only even numbers between 2 and 20:\n\n {arr}")

with st.expander("Q-2 - c : A 5 × 5 array filled with zeros.."):
    arr = np.zeros((5,5))
    st.success(f"5 × 5 array filled with zeros:\n\n {arr}")

with st.expander("Q-2 - d : A 4 × 4 array filled with ones."):
    arr = np.ones((4,4))
    st.success(f"4 × 4 array filled with ones:\n\n {arr}")

st.header("Q - 3 : Create a 3 X 3 identity matrix")
with st.expander("Q-3 : Create a 3 X 3 identity matrix"):
    arr = np.eye(3)
    st.success(f"3 X 3 identity matrix:\n\n {arr}")

st.header("Q - 4 : Create a 1D array containing 15 equally spaced values between 0 and 1.")
with st.expander("Q-4 : Create a 1D array containing 15 equally spaced values between 0 and 1."):
    arr = np.linspace(0, 1, 15)
    st.success(f"1D array containing 15 equally spaced values between 0 and 1 :\n\n {arr}")


st.header("Q - 5 : Create the following matrix")
with st.expander("Q-5 : Create a 5 X 5 Matrix"):
    arr = np.arange(1, 26).reshape(5, 5)
    st.success(f"5 X 5 Matrix:\n\n{arr}")

st.header("Q - 6 : Reshape Array")
with st.expander("Q-6 : Reshape into 4 X 5 Matrix"):
    arr6 = np.arange(1, 21)
    arr6 = arr6.reshape(4, 5)
    st.success(f"4 X 5 Matrix:\n\n{arr6}")

st.header("Q - 7 : Random Matrix")

with st.expander("Q-7-a : 3 X 3 Random Numbers (0 to 1)"):
    arr7 = np.random.rand(3, 3)
    st.success(f"Random Matrix:\n\n{arr7}")

with st.expander("Q-7-b : 4 X 4 Random Integers (10 to 50)"):
    arr7 = np.random.randint(10, 51, (4, 4))
    st.success(f"Random Integer Matrix:\n\n{arr7}")

st.header("Q - 8 : Create Matrix")

with st.expander("Q-8 : Create Matrix Without Typing Each Element"):
    arr8 = np.arange(10, 91, 10).reshape(3, 3)
    st.success(f"Matrix:\n\n{arr8}")

st.header("Q - 9 : Matrix Indexing")

mat = np.arange(1, 26).reshape(5, 5)

with st.expander("Q-9-a : Extract Element 13"):
    st.success(f"Element 13 : {mat[2,2]}")

with st.expander("Q-9-b : Extract Last Row"):
    st.success(f"Last Row:\n\n{mat[4]}")

with st.expander("Q-9-c : Extract Third Column"):
    st.success(f"Third Column:\n\n{mat[:,2]}")

with st.expander("Q-9-d : Extract Sub Matrix"):
    st.success(f"Sub Matrix:\n\n{mat[1:4,1:4]}")

with st.expander("Q-9-e : Extract Elements [4 9 14 19 24]"):
    st.success(f"Elements:\n\n{mat[:,3]}")

st.header("Q - 10 : Replace Even Numbers with 0")

with st.expander("Q-10 : Replace All Even Numbers"):
    arr = mat.copy()
    arr[arr % 2 == 0] = 0
    st.success(f"Updated Matrix:\n\n{arr}")

st.header("Q - 11 : Transpose")

with st.expander("Q-11 : Find Transpose"):
    st.success(f"Transpose Matrix:\n\n{mat.T}")

st.header("Q - 12 : Matrix Statistics")

with st.expander("Q-12-a : Sum of All Elements"):
    st.success(f"Sum = {np.sum(mat)}")

with st.expander("Q-12-b : Mean of All Elements"):
    st.success(f"Mean = {np.mean(mat)}")

with st.expander("Q-12-c : Standard Deviation"):
    st.success(f"Standard Deviation = {np.std(mat)}")

with st.expander("Q-12-d : Maximum Value"):
    st.success(f"Maximum = {np.max(mat)}")

with st.expander("Q-12-e : Minimum Value"):
    st.success(f"Minimum = {np.min(mat)}")

st.header("Q - 13 : Row & Column Operations")

with st.expander("Q-13-a : Row-wise Sum"):
    st.success(f"Row-wise Sum:\n\n{np.sum(mat, axis=1)}")

with st.expander("Q-13-b : Column-wise Sum"):
    st.success(f"Column-wise Sum:\n\n{np.sum(mat, axis=0)}")

with st.expander("Q-13-c : Row-wise Mean"):
    st.success(f"Row-wise Mean:\n\n{np.mean(mat, axis=1)}")

with st.expander("Q-13-d : Column-wise Mean"):
    st.success(f"Column-wise Mean:\n\n{np.mean(mat, axis=0)}")

st.header("Q - 14 : Elements Greater Than 20")

with st.expander("Q-14 : Find Elements Greater Than 20"):
    st.success(f"Elements:\n\n{mat[mat > 20]}")

st.header("Q - 15 : Checkerboard Pattern")

with st.expander("Q-15 : Create 8 X 8 Checkerboard"):
    checker = np.zeros((8, 8), dtype=int)
    checker[1::2, ::2] = 1
    checker[::2, 1::2] = 1
    st.success(f"Checkerboard Pattern:\n\n{checker}")

st.header("Q - 16 : Normalize Random Array")

with st.expander("Q-16 : Normalize Array Between 0 and 1"):
    arr = np.random.rand(20)
    normalized = (arr - arr.min()) / (arr.max() - arr.min())

    st.write("Original Array:")
    st.code(arr)

    st.write("Normalized Array:")
    st.code(normalized)

st.header("Q - 17 : Matrix Operations")

arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(11, 20).reshape(3, 3)

with st.expander("Q-17 : Display Both Matrices"):
    st.write("Matrix 1")
    st.code(arr1)

    st.write("Matrix 2")
    st.code(arr2)

with st.expander("Q-17-a : Addition"):
    st.success(f"Addition:\n\n{arr1 + arr2}")

with st.expander("Q-17-b : Subtraction"):
    st.success(f"Subtraction:\n\n{arr1 - arr2}")

with st.expander("Q-17-c : Element-wise Multiplication"):
    st.success(f"Element-wise Multiplication:\n\n{arr1 * arr2}")

with st.expander("Q-17-d : Matrix Multiplication"):
    st.success(f"Matrix Multiplication:\n\n{arr1 @ arr2}")
