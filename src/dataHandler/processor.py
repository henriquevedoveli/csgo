import pandas as pd
from dataclasses import dataclass
import json

class DataframeProcessor:
    def __init__(self) -> None:
        self.corr_thresh = 0.1
        self.model_type = "full"


    def process(self, df):
        df_copy = df.copy()
        df_copy = self.add_categorical_class(df_copy)
        df_copy = self.map_to_categorical(df_copy)
        df_copy = self.select_correlated_columns(df_copy)    

        if self.model_type == "full":
            return df_copy
            
    def map_to_categorical(self, df):
        df['map'], mapa_categorias = pd.factorize(df['map'])
        relacao_mapas = {categoria: numero for numero, categoria in enumerate(mapa_categorias)}

        with open('data/maps.json', 'w') as f:
            json.dump(relacao_mapas, f)

        return df
    
    @staticmethod
    def add_categorical_class(df):
        df["t_win"] = df["round_winner"].astype("category").cat.codes
        df= df.drop("round_winner", axis = 1)
        return df
    
    def calculate_correlation(self, df):
        df_numerico = df.select_dtypes(include=['number'])

        corr_matrix = df_numerico.corr()
        t_win_corr = corr_matrix['t_win']
        correlated_columns = t_win_corr[t_win_corr.abs() > self.corr_thresh].index.tolist()
        correlated_columns.remove('t_win')
        correlated_columns.append("map")

        return correlated_columns

    def select_correlated_columns(self, df):
        correlated_columns = self.calculate_correlation(df)
        selected_df = df[correlated_columns]

        selected_df['t_win'] = df['t_win']
        return selected_df
        
    @staticmethod
    def clean_loser_data(df):
        return df