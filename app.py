import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Aplicación para Capturar Respuestas de Encuestas")

# Instrucciones iniciales
st.write("Por favor, sube un archivo Excel para capturar las respuestas.")

# Subida de archivos
uploaded_file = st.file_uploader("respuestas", type="xlsx")

if uploaded_file:
    try:
        # Leer el archivo Excel
        df = pd.read_excel(uploaded_file, engine="openpyxl")

        # Si el DataFrame está vacío, inicializa con las columnas
        if df.empty:
            df = pd.DataFrame(columns=[
                "Satisfacción General", "Relaciones Interpersonales", "Relación con Superiores",
                "Reconocimiento y Desarrollo", "Condiciones de Trabajo", "Balance Vida-Trabajo",
                "Remuneración y Beneficios", "Comunicación", "Seguridad y Salud",
                "Identificación con la Empresa", "Motivación", "Estabilidad Laboral", "Carga de Trabajo"
            ])

        # Crear una nueva entrada
        new_entry = {
            "Satisfacción General": st.slider("Satisfacción General", 1, 5),
            "Relaciones Interpersonales": st.slider("Relaciones Interpersonales", 1, 5),
            "Relación con Superiores": st.slider("Relación con Superiores", 1, 5),
            "Reconocimiento y Desarrollo": st.slider("Reconocimiento y Desarrollo", 1, 5),
            "Condiciones de Trabajo": st.slider("Condiciones de Trabajo", 1, 5),
            "Balance Vida-Trabajo": st.slider("Balance Vida-Trabajo", 1, 5),
            "Remuneración y Beneficios": st.slider("Remuneración y Beneficios", 1, 5),
            "Comunicación": st.slider("Comunicación", 1, 5),
            "Seguridad y Salud": st.slider("Seguridad y Salud", 1, 5),
            "Identificación con la Empresa": st.slider("Identificación con la Empresa", 1, 5),
            "Motivación": st.slider("Motivación", 1, 5),
            "Estabilidad Laboral": st.slider("Estabilidad Laboral", 1, 5),
            "Carga de Trabajo": st.slider("Carga de Trabajo", 1, 5)
        }

        # Añadir la nueva entrada al DataFrame
        df = df.append(new_entry, ignore_index=True)

        # Mostrar el DataFrame
        st.write(df)

        # Guardar el DataFrame en un nuevo archivo Excel
        if st.button("Guardar respuestas en Excel"):
            df.to_excel("respuestas_encuestas.xlsx", index=False, engine="openpyxl")
            st.success("Respuestas guardadas con éxito!")

    except Exception as e:
        st.write("Ocurrió un error al leer el archivo. Asegúrate de que es un archivo Excel válido.")
        st.write(str(e))

st.write("© 2023 - Empresa XYZ")
