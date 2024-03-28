import pandas as pd

# Function to verify date format
def verify_date_format(df, column_name):
    incorrect_dates = []
    for index, row in df.iterrows():
        try:
            pd.to_datetime(str(row[column_name]), format='%Y-%m-%d')
        except ValueError:
            incorrect_dates.append(row['ID'])
    return incorrect_dates