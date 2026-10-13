
import pandas as pd

df = pd.read_csv("data/raw/layoffs_events.csv")

print("Kich thuoc du lieu:")
print(df.shape)

print("\nTen cac cot:")
print(df.columns.tolist())

print("\n5 dong dau:")
print(df.head())

print("\nSo gia tri bi thieu:")
print(df.isna().sum())
