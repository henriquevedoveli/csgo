import pandas as pd
from dataclasses import dataclass
import json

class DataframeProcessor:
    def __init__(self) -> None:
        self.corr_thresh = 0.1
        self.model_type = "full"


    def process(self, df):
        transformation_functions = [
        self.add_categorical_class,
        self.map_to_categorical,
        self.select_correlated_columns
    ]
    
        for func in transformation_functions:
            df = func(df)

        if self.model_type == "full":
            return df
        
        return self.clean_loser_data(df)
    
    def map_to_categorical(self, df):
        df['map'], mapa_categorias = pd.factorize(df['map'])
        relacao_mapas = {categoria: numero for numero, categoria in enumerate(mapa_categorias)}

        with open('data/maps.json', 'w') as f:
            json.dump(relacao_mapas, f)

        return df
    
    @staticmethod
    def add_categorical_class(df):
        df["t_win"] = df["round_winner"].astype("category").cat.codes
        df.drop("round_winner", axis = 1)

        return df
    
    def calculate_correlation(self, df):
        df_numerico = df.select_dtypes(include=['number'])

        corr_matrix = df_numerico.corr()
        t_win_corr = corr_matrix['t_win']
        correlated_columns = t_win_corr[t_win_corr.abs() > self.corr_thresh].index.tolist()
        correlated_columns.remove('t_win')

        return correlated_columns

    def select_correlated_columns(self, df):
        correlated_columns = self.calculate_correlation(df)
        selected_df = df[correlated_columns]

        return selected_df
        
    @staticmethod
    def clean_loser_data(df):
        return df