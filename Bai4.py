import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
file_path = 'Boston-house-price-data.csv'
df = pd.read_csv(file_path)

# =========================
# 1. Tính correlation matrix
# =========================
corr_matrix = df.corr(numeric_only=True)

print("Ma trận tương quan:")
print(corr_matrix)

# =========================
# 2. Vẽ heatmap
# =========================
plt.figure(figsize=(12,8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')
plt.show()

# =========================
# 3. Tìm các cặp tương quan cao
# =========================
threshold = 0.7

print("
Các cặp biến có tương quan cao:")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        corr_value = corr_matrix.iloc[i, j]

        if abs(corr_value) > threshold:
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]

            print(f"{col1} và {col2}: {corr_value:.2f}")