import pandas as pd
from pathlib import Path

current_path = Path.cwd()
data_folder_path = current_path / "data"
cleaned_data_path = data_folder_path / "Shiller_Cleaned_Data.csv"

#read into dataframe
df = pd.read_csv(cleaned_data_path)

