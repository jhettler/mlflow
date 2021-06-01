import mlflow

mlflow.run(
    ".",
    entry_point="train",
)
