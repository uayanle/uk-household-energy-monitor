import pandas as pd

class tariffs_df(pd.DataFrame):
    """A pandas DataFrame subclass for tariff data."""

    @property
    def _constructor(self):
        return tariffs_df

    @property
    def _constructor_sliced(self):
        return pd.Series

    @classmethod
    def from_csv(cls, file_path='tariffs', **kwargs):
        df = pd.read_csv(file_path, **kwargs)
        return cls(df)

    def get_tariff(self, tariff_name, column_name='TARIFF'):
        if column_name not in self.columns:
            raise KeyError(f"No '{column_name}' column in data.")
        return self.loc[self[column_name] == tariff_name]

    def average_rate(self, rate_column='RATE'):
        if rate_column not in self.columns:
            raise KeyError(f"No '{rate_column}' column in data.")
        return self[rate_column].astype(float).mean()

# read the csv

tariffs_df = tariffs_df.from_csv('tariffs')
print(tariffs_df)
