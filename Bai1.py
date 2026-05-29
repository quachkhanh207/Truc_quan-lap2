import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
file_path = 'Boston-house-price-data.csv'
df = pd.read_csv(file_path)

# =========================
# 1. Hiển thị 10 dòng đầu
# =========================
print("10 dòng đầu tiên:")
print(df.head(10))

# =========================
# 2. Kích thước dữ liệu
# =========================
print("
Kích thước dữ liệu:")
print(df.shape)
print(f"Số dòng: {df.shape[0]}")
print(f"Số cột: {df.shape[1]}")

# =========================
# 3. Kiểu dữ liệu
# =========================
print("
Kiểu dữ liệu từng cột:")
print(df.dtypes)

print("
Thông tin dataset:")
print(df.info())

# =========================
# 4. Thống kê cơ bản
# =========================
print("
Giá trị trung bình:")
print(df.mean(numeric_only=True))

print("
Giá trị lớn nhất:")
print(df.max(numeric_only=True))

print("
Giá trị nhỏ nhất:")
print(df.min(numeric_only=True))

print("
Độ lệch chuẩn:")
print(df.std(numeric_only=True))

print("
Describe:")
print(df.describe())

# =========================
# 5. Histogram
# =========================
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=20)
    plt.title(f'Histogram của {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# =========================
# 6. Bar chart
    plt.show()