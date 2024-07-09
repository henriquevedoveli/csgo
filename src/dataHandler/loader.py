import pandas as pd

class DataFrameLoader:
    def __init__(self, file_name, columns):
        self.file_name = file_name
        self.columns = columns

    def load(self):
        df = pd.read_csv(self.file_name)
        df.columns = self.columns
        print(f"DataFrame carregado com sucesso.")
        return df
