import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Đọc dữ liệu
file_path = 'Boston-house-price-data.csv'
df = pd.read_csv(file_path)

# Chọn cột số
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

# =========================
# 1. Kiểm tra missing values
# =========================
print("Số lượng giá trị thiếu:")
print(df.isnull().sum())

# =========================
# 2. Xử lý missing values
# =========================

# Điền bằng trung bình
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

print("
Sau khi xử lý missing values:")
print(df.isnull().sum())

# =========================
# 3. Kiểm tra dữ liệu trùng lặp
# =========================
print("
Số dòng trùng lặp:")
print(df.duplicated().sum())

# Xóa trùng lặp
df = df.drop_duplicates()

print("
Kích thước sau khi xóa trùng lặp:")
print(df.shape)

# =========================
# 4. Boxplot trước chuẩn hóa
# =========================
plt.figure(figsize=(12,6))
sns.boxplot(data=df[numeric_cols])
plt.title('Boxplot trước chuẩn hóa')
plt.xticks(rotation=45)
plt.show()

# =========================
# 5. Normalization
# =========================
minmax_scaler = MinMaxScaler()

plt.show()