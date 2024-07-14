import matplotlib.pyplot as plt
import seaborn

class EDA:
    def __init__(self, df) -> None:
        self.df = df

    def plot_correlations(self):
        print("Plotando Correlacoes")
        df_numerico = self.df.select_dtypes(include=['number'])

        if 't_win' in df_numerico.columns:
                correlacoes = df_numerico.corr()['t_win'].drop('t_win')

                correlacoes_ordenadas = correlacoes.apply(abs).sort_values(ascending=False).iloc[:50]
                print(correlacoes_ordenadas)