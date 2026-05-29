import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
file_path = 'Boston-house-price-data.csv'
df = pd.read_csv(file_path)

# Chọn cột số
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

# =========================
# 1. Vẽ Boxplot
# =========================
for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot của {col}')
    plt.show()

# =========================
# 2. Phát hiện Outliers bằng IQR
# =========================
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

    print(f"
Cột: {col}")
    print(f"Số lượng outliers: {len(outliers)}")

    if len(outliers) > 0:
        print(outliers[[col]])