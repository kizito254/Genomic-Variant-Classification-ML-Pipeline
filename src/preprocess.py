from pathlib import Path

import numpy as np
import pandas as pd


def generate_synthetic_variants(n=1000, seed=42):
    np.random.seed(seed)

    df = pd.DataFrame(
        {
            "chromosome": np.random.randint(1, 23, n),
            "position": np.random.randint(1, 1_000_000, n),
            "allele_freq": np.random.rand(n),
            "mutation_type": np.random.choice(["SNP", "Insertion", "Deletion"], n),
            "gc_content": np.random.rand(n),
        }
    )

    # Label: 1 = pathogenic, 0 = benign
    df["label"] = (
        (df["allele_freq"] < 0.3) & (df["mutation_type"] != "SNP")
    ).astype(int)

    return df


def save_dataset(path="data/variants.csv"):
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = generate_synthetic_variants()
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path} with shape {df.shape}")


if __name__ == "__main__":
    save_dataset()
