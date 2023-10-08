import streamlit as st
import sqlite3

# Funciones para manejar SQLite
def create_connection():
    conn = sqlite3.connect('encuesta_respuestas.db')
    return conn

def create_table():
    conn = create_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS respuestas (
        id INTEGER PRIMARY KEY,
        """ + ",\n".join([f"'{pregunta}' INTEGER" for pregunta in preguntas]) + """
    )
    """)
    conn.close()

def insert_data(respuestas):
    conn = create_connection()
    columns = ', '.join([f"'{key}'" for key in respuestas.keys()])
    placeholders = ', '.join(['?' for _ in respuestas.values()])
    conn.execute(f"INSERT INTO respuestas ({columns}) VALUES ({placeholders})", list(respuestas.values()))
    conn.commit()
    conn.close()

# Mensajes
mensaje_inicio = """..."""  # El mensaje largo de inicio va aquí.
mensaje_fin = """..."""  # El mensaje largo de fin va aquí.

preguntas = [
        "¿Estás satisfecho con tu trabajo actual?",
        "¿Recomendarías nuestra empresa como un buen lugar para trabajar?",
        "¿Cómo calificarías la relación con tus compañeros de trabajo?",
        "¿Sientes que puedes confiar en tus colegas?",
        "¿Sientes que tus superiores te tratan con respeto?",
        "¿Recibes retroalimentación constructiva de tus jefes?",
        "¿Consideras que tu jefe inmediato te apoya en tu desarrollo profesional?",
        "¿Sientes que se reconocen tus esfuerzos y logros?",
        "¿Consideras que hay oportunidades de crecimiento profesional en la empresa?",
        "¿Recibes la capacitación necesaria para desempeñar tus funciones?",
        "¿Estás satisfecho con las condiciones físicas de tu lugar de trabajo?",
        "¿Consideras que cuentas con las herramientas y recursos necesarios para realizar tu trabajo?",
        "¿Sientes que puedes equilibrar tu vida laboral y personal trabajando aquí?",
        "¿Consideras que la empresa respeta tu tiempo libre y personal?",
        "¿Estás satisfecho con tu salario y beneficios?",
        "¿Consideras que la remuneración es justa en comparación con el mercado y las responsabilidades de tu puesto?",
        "¿Sientes que la comunicación en la empresa es abierta y transparente?",
        "¿Estás informado sobre los cambios y decisiones que afectan a la empresa y a tu posición?",
        "¿Consideras que la empresa se preocupa por la salud y seguridad de sus empleados?",
        "¿Has recibido información o capacitación sobre medidas de seguridad en tu puesto?",
        "¿Estás de acuerdo con los valores y la misión de la empresa?",
        "¿Sientes orgullo al decir que trabajas aquí?",
        "¿Te sientes motivado para cumplir tus objetivos laborales?",
        "¿Qué factor te motiva más para desempeñarte al máximo en tu trabajo?",
        "¿Sientes que tu trabajo es estable?",
        "¿Tienes temor de perder tu empleo en el futuro cercano?",
        "¿Consideras que tu carga de trabajo es adecuada?",
        "¿Sientes que trabajas bajo mucha presión?"
    ]
  # Tu lista de preguntas va aquí.

create_table()

st.title('Encuesta GGNET')
st.write(mensaje_inicio)

# Crear sliders para cada pregunta
respuestas = {}
for pregunta in preguntas:
    respuesta = st.slider(pregunta, 1, 5)
    respuestas[pregunta] = respuesta

if st.button('Enviar'):
    insert_data(respuestas)
    st.write(mensaje_fin)
