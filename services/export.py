import pandas as pd

def csv(rows, csv_file_name):
    df = pd.DataFrame(rows)

    try:
        old = pd.read_csv(csv_file_name)
        df = pd.concat([old, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv(csv_file_name, index=False)