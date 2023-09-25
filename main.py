import pandas as pd

def convert_to_json(excel_file):

    my_excel_products = pd.read_excel(excel_file)
    my_excel_products.to_json("data/new_catalog.json",orient="records")

    return "data/new_catalog.json"







