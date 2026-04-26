import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy import stats
import os

class Reader:
    def __init__(self, database_path):
        self.database_path = database_path
        self.database = pd.read_csv(database_path)
        self._df = self._load_table() 

    def read(self, idx=None):
        if idx is not None:
            return self.database.iloc[idx]
        return self.database
    def _load_table(self):
        """Méthode privée pour charger la table"""
        try:
            return pd.read_csv(self.database_path)
        except FileNotFoundError:
            print(f"Erreur : Le fichier au chemin {self.database_path} est introuvable.")
            return None
        
    def get_index(self):
        """ résumé du dataset (shape, colonnes, dtypes, valeurs nulles)."""
        if self._df is None:
            return "0"

        summary = pd.DataFrame({
            'Type de donnée (dtype)': self._df.dtypes,
            'Valeurs nulles': self._df.isnull().sum(),
            'max':self._df.max()
        })
        print(f"Dimensions du dataset (lignes, colonnes) : {self._df.shape}")
        return summary
    
