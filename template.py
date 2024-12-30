import os
from pathlib import Path

list_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/logger/logging.py",
    "src/exception/exception"
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_files:
    filePath = Path(filepath)
    filedir, filename = os.path.split(filePath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f'Creating directory: {filedir} and name: {filename}')

    if (not os.path.exists(filepath)) or (os.oath.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass