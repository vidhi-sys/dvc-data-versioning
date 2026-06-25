# DVC Data Versioning Demo

A beginner-friendly project demonstrating **Data Version Control (DVC)** with **Git** for reproducible data versioning workflows used in Machine Learning and Data Engineering.

## Project Overview

This project simulates a real-world data versioning workflow by:

* Generating a dataset using Python and Pandas
* Saving the dataset as a CSV file
* Tracking dataset versions using DVC
* Storing code and metadata using Git
* Pushing dataset versions to a DVC remote storage
* Maintaining reproducibility between code and data

---

## Tech Stack

* Python
* Pandas
* Git
* DVC (Data Version Control)

---

## Project Structure

```text
dvc-data-versioning/
│
├── data/
│   └── sample_data.csv
│
├── mycodefile.py
├── projectflow.txt
├── .dvc/
├── data.dvc
└── README.md
```

---

## Workflow

### 1. Generate Dataset

A Python script creates and updates employee/member records.

```bash
python mycodefile.py
```

Output:

```text
data/sample_data.csv
```

---

### 2. Track Data with DVC

```bash
dvc add data
```

DVC generates:

```text
data.dvc
```

which stores metadata and hashes for the dataset.

---

### 3. Check Dataset Changes

```bash
dvc status
```

Example:

```text
data.dvc:
    changed outs:
        modified: data
```

---

### 4. Commit New Dataset Version

```bash
dvc commit
```

This creates a new version of the dataset while preserving previous versions.

---

### 5. Push Dataset to Remote Storage

```bash
dvc push
```

Dataset artifacts are uploaded to the configured DVC remote.

---

### 6. Version Metadata with Git

```bash
git add .
git commit -m "update dataset version"
git push
```

Git stores:

* Source code
* DVC metadata
* Pipeline configuration

while DVC stores the actual dataset versions.

---

## Example Dataset Evolution

### Version 1

| Name     | Age | Job     |
| -------- | --- | ------- |
| goli     | 15  | student |
| bhide    | 45  | teacher |
| popatlal | 40  | teacher |

### Version 2

Additional records added:

* Dr. Haathi
* Iyer
* Roshan Sodhi

DVC detected the change and created a new dataset version.

---

## Key Learnings

* Data Versioning
* Git + DVC Integration
* Dataset Reproducibility
* Data Change Tracking
* Remote Data Storage
* Foundations of MLOps

---

## Resume Highlights

* Implemented data versioning using DVC and Git for reproducible dataset management.
* Built a Python-based data generation pipeline using Pandas.
* Configured DVC remote storage and tracked dataset evolution across multiple versions.
* Practiced industry-standard MLOps workflows involving dataset tracking, version control, and reproducibility.

---

## Future Improvements

* Add preprocessing pipeline
* Create DVC stages using `dvc.yaml`
* Train and version ML models
* Integrate MLflow for experiment tracking
* Deploy end-to-end ML pipeline

```
```
