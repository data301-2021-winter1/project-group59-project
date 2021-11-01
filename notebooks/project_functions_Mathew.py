import pandas as pd
import numpy as np
def load_and_process(notebooks):
    df=pd.read_csv("chess_games.csv")

    dfvicopen= df[['victory_status', 'opening_shortname']]
    mate= ['Mate']

    dfmate= dfvicopen[dfvicopen['victory_status'].isin(mate)]
    winrate=dfmate['opening_shortname'].value_counts()[:30].sort_index(ascending=True)/dfvicopen['opening_shortname'].value_counts()[:30].sort_index(ascending=True)
    dfwinrate=winrate.to_frame()
    
    return dfwinrateclean
    
load_and_process("chess_games.csv")
