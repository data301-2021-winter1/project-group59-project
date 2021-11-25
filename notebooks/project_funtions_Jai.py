import pandas as pd
import numpy as np
def load_data(link, colour="both"):
    '''Enter either Black, White or Both or All in lowercase to see statistics on selected colour'''
    df1=pd.read_csv(link)
    df2 = df1[['turns', 'winner']]
    df2.drop(df2.index[df2['turns'] < 2], inplace = True)
    df2.drop(df2.index[df2['turns'] > 140], inplace = True)
    if(colour=="black"):
        black = ['Black']
        blackWon=df2[df2['winner'].isin(black)]
        return blackWon
    elif (colour=="white"):
        white = ['White']
        whiteWon= df2[df2['winner'].isin(white)]
        return whiteWon
    elif (colour=="both"):
        
        return df2
    elif(colour == "all"):
        return df2
    else:
        print("please add in a black, white or both colour choice")