import streamlit as st
import pandas as pd
import gspread

# Conectar con Google Sheets
gc = gspread.service_account(filename=None)
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1HUMU06Y3jvmfxYxjta0QstvGlkXMXSnfw0Y2oAHwqCY/edit?usp=sharing")
worksheet = sh.get_worksheet(0)

# Título de la aplicación
st.title("Aplicación para Capturar Respuestas de Encuestas")

# Crea sliders para la encuesta
satisfaccion = st.slider("Satisfacción General", 1, 5)

# Si deseas guardar la información, puedes añadir un botón:
if st.button("Guardar respuestas"):
    # Añade las respuestas a la hoja de cálculo
    worksheet.append_row([satisfaccion])  # Añade más valores según lo necesites
    st.success("Respuestas guardadas con éxito!")

# Si quieres mostrar los datos:
records_data = worksheet.get_all_records()
df = pd.DataFrame(records_data)
st.write(df)

st.write("© 2023 - Empresa XYZ")
