import pandas as pd

class Reader:
    def __init__(self, database_path):
        self.database_path = database_path
        self.database = pd.read_csv(database_path)

    def read(self, idx=None):
        if idx is not None:
            return self.database.iloc[idx]
        return self.database
    