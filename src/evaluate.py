from sklearn.metrics import classification_report

from train import train_model


def evaluate():
    model, X_test, y_test = train_model()

    preds = model.predict(X_test)

    print("\nCLASSIFICATION REPORT\n")
    print(classification_report(y_test, preds))


if __name__ == "__main__":
    evaluate()
