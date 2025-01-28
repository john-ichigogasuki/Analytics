import pandas as pd
import glob

# フォルダ内のすべてのCSVファイルを取得
csv_files = glob.glob('./TalkData/*.csv')

# 各CSVファイルを読み込み、任意の文字列を削除し、同じファイル名で保存
for file in csv_files:
    df = pd.read_csv(file)
    df = df.replace('"', '', regex=True)
    df.to_csv(file, index=False)
