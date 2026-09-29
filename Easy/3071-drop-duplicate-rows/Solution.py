import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

    # OR

    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers