import pandas as pd

# uses patient_id as the sample_id since this is going to be reported to a medical geneticist, which
# will provide more info for the patient rather than using the library ID
def low_cov_sample_filter(file, sample_id):
    lc_df = pd.read_csv(file)
    
    if 'patient_id' in lc_df.columns:
        if str(sample_id) in lc_df['patient_id'].unique():
            lc_filtered = lc_df.loc[lc_df['patient_id'] == sample_id]
        else:
            raise ValueError(f"Sample ID not found: {sample_id}")
    else:
         raise RuntimeError(f"'patient_id' column not found, and is used as the Sample ID, please check the .csv file")
        
    return lc_filtered