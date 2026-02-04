# Dataset Download Instructions

## Download the Healthcare Dataset

Since the dataset files are too large for GitHub, you need to download them separately:

### Option 1: Download from Kaggle

1. Go to Kaggle: https://www.kaggle.com/
2. Search for "Healthcare Dataset" (or use the specific dataset link if provided)
3. Download the CSV file
4. Place it in the project root as `healthcare_dataset.csv`

### Option 2: Use Your Own Healthcare Data

If you have your own healthcare dataset:

1. Ensure it's in CSV format
2. Name it `healthcare_dataset.csv`
3. Place it in the project root
4. Run the data cleaning script: `python prepare_data.py`

### Required Columns (for best results)

The agent works best with datasets containing medical information such as:
- Patient demographics (Age, Gender, etc.)
- Medical conditions
- Dates (admission, discharge)
- Billing/cost information
- Test results
- Medications

### After Downloading

Run the data preparation script to clean and optimize the data:

```bash
python prepare_data.py
```

This will create `healthcare_dataset_cleaned.csv` which the application uses.

---

**Important**: Only use synthetic or anonymized data. Never use real patient information.
