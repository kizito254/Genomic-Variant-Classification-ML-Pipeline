import pandas as pd


def load_data(path="data/variants.csv"):
    return pd.read_csv(path)


def preprocess(df):
    df = df.copy()

    # Encode categorical feature.
    df["mutation_type"] = df["mutation_type"].map(
        {
            "SNP": 0,
            "Insertion": 1,
            "Deletion": 2,
        }
    )

    return df


def get_features_targets(df):
    X = df.drop(columns=["label"])
    y = df["label"]
    return X, y
