import pandas as pd
import numpy as np
def load_data(url_or_path_to_csv_file, colour="both"):
    '''Enter either Black, WHite or Both in lowercase to see statistics on selected colour'''
    df1=( pd.read_csv(url_or_path_to_csv_file))
    df2 = (df1[['turns', 'winner']])
    df3 = (
        df4 = []
    if(colour=="black"):
        black = ['Black']
        blackWon=df2[df2['winner'].isin(black)]
        df4 = blackWon
    elif (colour=="white"):
        white = ['White']
        whiteWon= df2[df2['winner'].isin(white)]
        df4 = whiteWon
    elif (colour=="both"):
        df4 =  df2
    else:
        print("please add in a black, white or both colour choice")
    )
    return df4