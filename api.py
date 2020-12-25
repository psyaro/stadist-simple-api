import pandas as pd
from numpy import sqrt

class Stations:
    def __init__(self):
        self.df = pd.read_csv('stations-simplify.csv')
    
    def api(self, orig, dest, simple=True):
        ox, oy = self.df[self.df.station == orig].iloc[0, :].values[1:3]
        dx, dy = self.df[self.df.station == dest].iloc[0, :].values[1:3]
        return int(round(sqrt( (ox - dx) ** 2 + (oy - dy) ** 2)))

if __name__ == "__main__":
    print(Stations().api('大手町', '立川'))
        

