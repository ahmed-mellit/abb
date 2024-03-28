# Function to verify boolean column
def verify_boolean_column(df, column_name):
    incorrect_values = []
    for index, row in df.iterrows():
        value = row[column_name]
        if value not in [0, 1]:
            incorrect_values.append(row['ID'])
    return incorrect_values
