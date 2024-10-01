import pandas as pd
input_file = r"C:\Users\Asus\OneDrive\Documents\DATA RIWAYAT\riwayat.xlsx"

output_file = "riwayat2.xlsx"  


df = pd.read_excel(input_file)
df['tglentry'] = pd.to_datetime(df['tglentry'])


df_sorted = df.sort_values(by='tglentry', ascending=True) #sort tgl

df_unique = df_sorted.drop_duplicates(subset='idHeader', keep='first') #tahan duplikat data pertama

df_unique.to_excel(output_file, index=False) #export

print(f"Program completed! The cleaned data has been saved to {output_file}.")
