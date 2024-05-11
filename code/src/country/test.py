import pandas as pd

# 指定 Excel 文件的路径
excel_path = 'F:\LearningResource\D\知识图谱\Project\Datasets\data\country\country.xlsx'
# 指定要保存的 CSV 文件的路径
csv_path = 'country.csv'

# 使用 pandas 读取 Excel 文件
df = pd.read_excel(excel_path)

# 将 DataFrame 对象 df 写入 CSV 文件
df.to_csv(csv_path, index=False, encoding='utf-8-sig')