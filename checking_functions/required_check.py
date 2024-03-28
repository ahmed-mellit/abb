# Function to find missing records
def find_missing_records(df, column_name):
    missing_records = df[df[column_name].isnull()]
    return missing_records['ID'].tolist()