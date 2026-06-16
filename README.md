# Genomic Variant Classification ML Pipeline

Reproducible machine learning pipeline for classifying synthetic genomic variants as pathogenic or benign.

## Project Structure

```text
data/          Generated synthetic datasets
models/        Serialized model artifacts
notebooks/     Exploratory notebooks
src/           Pipeline source code
```

## Setup

```powershell
pip install -r requirements.txt
```

## Run Pipeline

Generate the synthetic dataset:

```powershell
python src/preprocess.py
```

Train and save the model:

```powershell
python src/train.py
```

Evaluate the classifier:

```powershell
python src/evaluate.py
```

The pipeline writes `data/variants.csv` and `models/model.pkl`.
