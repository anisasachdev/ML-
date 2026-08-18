#                      lab1 practice tasks

#1) Take two numbers as input and print their sum, difference, product, quotient, floor division, and modulus.
a= float(input(" Enter first number: "))
b= float(input(" Enter second number: "))

print("sum:", a + b)
print("difference:", a - b)
print("product:" ,a * b)

if b == 0:
    print("quotient: can't divide by zero")
    print("floor division: can't divide by zero")
    print("modulus: can't divide by zero")
else :
    print("quotient:", a / b)
    print("floor division:", a // b)
    print("modulus:", a % b)

# 2) Convert a temperature given in Fahrenheit (string input) to Celsius using type casting and an f-string for
#output.
fahrenheit = input("Enter temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit)

celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F = {celsius:.2f}°C")

# 3) Print all prime numbers between 1 and 100 using nested loops and break
print("Prime numbers between 1 and 100:")
for num in range(2, 101):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
print()

# 4) Check even or odd using bitwise operator
n = int(input("Enter an integer to check even/odd: "))
if n & 1:
    print(f"{n} is odd")
else:
    print(f"{n} is even")


# 1) Function stats(*nums) that returns (min, max, average)
def stats(*nums):
    if not nums:
        return (None, None, None)
    minimum = min(nums)
    maximum = max(nums)
    average = sum(nums) / len(nums)
    return (minimum, maximum, average)

print(stats(2, 5, 8, 10))

# 2) List comprehension: squares of even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# 3) Sets of student names
course_a = {"Ali", "Sara", "Hamza", "Ayesha"}
course_b = {"Sara", "Bilal", "Ali", "Zain"}

common = course_a & course_b
only_one = (course_a - course_b) | (course_b - course_a)

print("Students in both courses:", common)
print("Students in only one course:", only_one)

# 4) Remove duplicates while preserving order
def remove_duplicates(items):
    seen = set()
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


lst = [3, 1, 2, 1, 3, 4, 2, 5]
print(remove_duplicates(lst))


# 5) Dictionary comprehension: 1..10 to cubes
cubes = {n: n ** 3 for n in range(1, 11)}
print(cubes)

import numpy as np

# 1) 1D array of first 15 natural numbers
arr1 = np.arange(1, 16)
print("1D array:", arr1)
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Dtype:", arr1.dtype)

# 2) 5x5 array of random integers between 10 and 50
rand_arr = np.random.randint(10, 51, size=(5, 5))
print("\nRandom 5x5 array:\n", rand_arr)
print("Max:", rand_arr.max())
print("Min:", rand_arr.min())
print("Mean:", rand_arr.mean())

# 3) 1D array of 20 elements -> reshape to 4x5; extract 2nd and 3rd columns
arr2 = np.arange(1, 21)
matrix = arr2.reshape(4, 5)
print("\nReshaped matrix:\n", matrix)
print("2nd and 3rd columns:\n", matrix[:, 1:3])

# 4) 1D array of 15 exam scores; boolean masking to find scores above mean
scores = np.array([78, 85, 92, 68, 74, 90, 88, 81, 95, 70, 76, 84, 89, 73, 87])
mean_score = scores.mean()
above_mean = scores[scores > mean_score]
print("\nScores above mean:", above_mean)
print("Mean score:", mean_score)

# 5) np.where() to replace negative values with 0 and positive with 1
arr3 = np.array([-3, -1, 0, 5, -7, 8, 2])
result = np.where(arr3 < 0, 0, 1)
print("\nOriginal:", arr3)
print("Transformed:", result)

import pandas as pd

# 1) Create DataFrame of 6 students
data = {
    "name": ["Ali", "Sara", "Hamza", "Ayesha", "Bilal", "Zain"],
    "subject": ["Math", "Science", "Math", "English", "Science", "Math"],
    "marks": [85, 90, 78, 88, 92, 75]
}

df = pd.DataFrame(data)
print("DataFrame created:\n", df)
print("\nDataFrame info:")
df.info()
print("\nDataFrame describe:\n", df.describe())


# 2) Load a CSV file and print shape, columns, and first 5 rows
# Replace 'students.csv' with your actual CSV file name if needed
df_csv = pd.read_csv("train.csv")

print("\nCSV shape:", df_csv.shape)
print("CSV columns:", list(df_csv.columns))
print("\nFirst 5 rows:\n", df_csv.head())

# 3) Boolean filtering: students with marks above 80
above_80 = df[df["marks"] > 80]
print("\nStudents above 80:\n", above_80)

# 4) Using .loc and .iloc to retrieve the same row two ways
row_loc = df.loc[df["name"] == "Sara"]
row_iloc = df.iloc[1]

print("\nUsing .loc:\n", row_loc)
print("\nUsing .iloc:\n", row_iloc)

print("\nMatch check:", row_loc.to_dict("records") == [row_iloc.to_dict()])

import pandas as pd
import numpy as np

# 1) DataFrame with missing marks
df = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Ali", "Sara", "Hamza", "Ayesha", "Bilal"],
    "subject": ["Math", "Science", "Math", "English", "Science"],
    "marks": [85, np.nan, 78, 90, np.nan]
})

print("Original DataFrame:\n", df)

# Count missing values per column
missing = df.isnull().sum()
print("\nMissing values per column:\n", missing)

# Fill missing values with column mean
for col in ["marks"]:
    mean_val = df[col].mean()
    df[col] = df[col].fillna(mean_val)

print("\nAfter filling missing values:\n", df)

# 2) Add pass_fail column using lambda inside .apply()
df["pass_fail"] = df["marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")
print("\nWith pass_fail column:\n", df)

# 3) Group by subject and compute mean, min, max marks
grouped = df.groupby("subject")["marks"].agg(["mean", "min", "max"])
print("\nGrouped statistics by subject:\n", grouped)

# 4) Merge students and attendance DataFrames on student_id
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ali", "Sara", "Hamza", "Ayesha"]
})
attendance = pd.DataFrame({
    "student_id": [1, 2, 3, 5],
    "attendance": [90, 85, 80, 75]
})
merged = students.merge(attendance, on="student_id", how="inner")
print("\nMerged DataFrame:\n", merged)


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1) Line chart of 10 days of temperature readings
days = list(range(1, 11))
temps = [22, 24, 23, 26, 28, 27, 30, 29, 31, 33]

plt.figure(figsize=(8, 5))
plt.plot(days, temps, marker='o', color='blue', linewidth=2)
plt.title("Temperature Readings for 10 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# 2) 1x2 subplots: bar chart + histogram
categories = ["A", "B", "C", "D", "E"]
counts = [5, 8, 3, 7, 6]

numeric_data = np.random.normal(50, 10, 100)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: bar chart
axes[0].bar(categories, counts, color="green")
axes[0].set_title("Category Counts")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Count")

# Right: histogram
axes[1].hist(numeric_data, bins=10, color="orange", edgecolor="black")
axes[1].set_title("Histogram of Numeric Data")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()

# 3) Boxplot from a DataFrame column directly
df = pd.DataFrame({
    "scores": [65, 72, 78, 80, 84, 88, 90, 95, 96, 100, 58, 63]
})

df["scores"].plot(kind="box", vert=True, patch_artist=True, color="lightblue")
plt.title("Boxplot of Student Scores")
plt.ylabel("Marks")
plt.show()


#                                                lab1 tasks
#Q1: Variable Swap without Third Variable
a, b = 5, 10
a, b = b, a
print(f"a = {a}, b = {b}")

#Q2: Prime Number Checker


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#Q3: Fibonacci Sequence


def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

#Q4: Remove Duplicates Preserving Order


def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
#Q5: Flexible Multiplication


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
#Q6: Character Frequency Comprehension


text = "hello world"
char_freq = {char: text.count(char) for char in text}

#Q7: Highest Salary Employee


employees = [
    {"name": "Alice", "department": "HR", "salary": 50000},
    {"name": "Bob", "department": "Tech", "salary": 75000},
    {"name": "Charlie", "department": "Tech", "salary": 60000}
]

highest_paid = max(employees, key=lambda emp: emp["salary"])

#Q8: Filter Odd Numbers with Lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))



import numpy as np

# Q9: Reshape 1D array to 5x6 matrix
arr_5x6 = np.arange(1, 31).reshape(5, 6)

# Q10: 6x6 Identity with custom diagonal
matrix_6x6 = np.eye(6)
np.fill_diagonal(matrix_6x6, [1, 2, 3, 4, 5, 6])

# Q11: Random array statistics
np.random.seed(42)
random_arr = np.random.randint(1, 101, size=25)
total_sum = np.sum(random_arr)
mean_val = np.mean(random_arr)
std_val = np.std(random_arr)

# Q12: Diagonal sum of 4x4 array
arr_4x4 = np.arange(1, 17).reshape(4, 4)
diag_elements = np.diag(arr_4x4)
diag_sum = np.sum(diag_elements)

# Q13: Element-wise vs Matrix Multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
element_wise = A * B  # Multiplies corresponding elements
matrix_mult = A @ B   # Dot product calculation

# Q14: Boolean masking for temperatures
temps = np.random.randint(20, 45, size=30)
hot_days = temps[temps > 35]
count_hot_days = np.sum(temps > 35)

# Q15: Min-Max Normalization
data = np.array([10, 20, 30, 40, 50])
normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))

# Q16: Axis-based aggregation (5 students, 3 subjects)
marks = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 92, 95],
    [60, 65, 70],
    [88, 84, 82]
])
total_per_student = np.sum(marks, axis=1)
avg_per_student = np.mean(marks, axis=1)

# Q17: Replace even numbers using np.where
arr = np.array([1, 2, 3, 4, 5, 6])
modified_arr = np.where(arr % 2 == 0, -1, arr)

import pandas as pd

# Q18: DataFrame description
df_students = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'section': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'marks': [85, 42, 90, 38, 78, 95, 49, 60]
})
print(df_students.describe())

# Q19: Missing values report & fill
df_csv = pd.read_csv('train.csv')
missing_per_column = df_csv.isnull().sum()
df_csv.fillna(df_csv.mean(numeric_only=True), inplace=True)

# Q20: Filter marks < 50 using .loc
low_scorers = df_students.loc[df_students['marks'] < 50, ['name', 'marks']]

# Q21: Groupby section aggregation
section_stats = df_students.groupby('section')['marks'].agg(['mean', 'max'])

# Q22: Merge students and attendance
df_attendance = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'attendance': [80, 65, 90, 70]
})
df_info = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

merged_df = pd.merge(df_info, df_attendance, on='id')
low_attendance = merged_df[merged_df['attendance'] < 75]



import matplotlib.pyplot as plt

# Q23: Bar chart of average marks per section
avg_marks = df_students.groupby('section')['marks'].mean()
avg_marks.plot(kind='bar', color=['skyblue', 'orange'])
plt.xlabel('Section')
plt.ylabel('Average Marks')
plt.title('Average Marks per Section')
plt.show()

# Q24: Histogram of marks
plt.hist(df_students['marks'], bins=5, edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Distribution of Student Marks')
plt.show()
# Description: The distribution exhibits a slight bimodal tendency with scores clustering around lower passing bounds (30–50) and higher performance tiers (75–95).

# Q25: 1x2 Subplots (Line plot & Scatter plot)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Left plot: Line chart
axes[0].plot([1, 2, 3, 4], [10, 20, 15, 25], marker='o', color='blue')
axes[0].set_title('Numeric Trend (Line Plot)')
axes[0].set_xlabel('Time Step')
axes[0].set_ylabel('Value')

# Right plot: Scatter chart
axes[1].scatter(df_students['marks'], [70, 80, 85, 60, 90, 95, 65, 75], color='red')
axes[1].set_title('Marks vs Attendance (Scatter Plot)')
axes[1].set_xlabel('Marks')
axes[1].set_ylabel('Attendance (%)')

plt.tight_layout()
plt.show()

