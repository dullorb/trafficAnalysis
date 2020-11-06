import pandas as pd


def handle_file(file):
    reading = file.read()
    data = pd.read_excel(reading)
    return pd
