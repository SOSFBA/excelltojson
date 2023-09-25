import streamlit as st
import os
import pandas as pd
from main import convert_to_json

st.title('Converti da Excel a Json')

# Creare la cartella "data" se non esiste già
if not os.path.exists("data"):
    os.makedirs("data")
# Caricamento del file Excel
file = st.file_uploader("Carica un file Excel", type=["xlsx", "xls"])

if file is not None:
    # Leggi il file Excel in un DataFrame Pandas
    df = pd.read_excel(file)

    # Visualizza il DataFrame
    st.write("Contenuto del file Excel:")
    st.write(df)

    # Salva il file Excel nella cartella "data"
    data_path = os.path.join("data", file.name)
    df.to_excel(data_path, index=False)
    st.success(f"File salvato in 'data' come {file.name}")


if st.button("Convert Excel") : 
    try :
        new_json_path = convert_to_json("data/" + file.name)
        st.success("File convertito correttamente")
    except :
        st.error("Errore durante la conversione, contatta il supporto")


try :

    new_json_path = open('data/new_catalog.json','+r',encoding="utf-8")

    st.download_button(
        label="Download Catalog as JSON",
        data=new_json_path,
        file_name='my_catalog.json',
        mime='text/json',
    )
except :
    st.info("In attesa del file...")    

