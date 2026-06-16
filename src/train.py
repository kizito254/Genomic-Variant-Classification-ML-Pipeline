from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from features import get_features_targets, load_data, preprocess


def train_model(model_path="models/model.pkl"):
    df = load_data()
    df = preprocess(df)

    X, y = get_features_targets(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    output_path = Path(model_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)
    print(f"Model saved to {output_path}")

    return model, X_test, y_test


if __name__ == "__main__":
    train_model()
