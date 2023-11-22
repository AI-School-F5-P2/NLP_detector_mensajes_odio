import json
import pymysql
from decouple import config
import streamlit as st

# Función para ejecutar un archivo SQL
def execute_sql_file(connection, filename):
    try:
        with open(filename, "r") as sql_file:
            sql_script = sql_file.read()
            # Separa las instrucciones SQL en una lista usando el punto y coma como delimitador
            sql_statements = sql_script.split(';')
            cursor = connection.cursor()

            for sql_statement in sql_statements:
                if sql_statement.strip():  # Verifica que no sea una línea vacía
                    cursor.execute(sql_statement)

            connection.commit()
    except pymysql.Error as e:
        st.error(f"Error al ejecutar el archivo SQL: {e}")
    finally:
        cursor.close()


# Función para establecer la conexión
def establish_connection():
    timeout = 10  # Establece un tiempo de espera de conexión
    try:
        conn = pymysql.connect(
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            db=config('DB_NAME', default='airline'),
            host=config('DB_HOST', default='localhost'),
            password=config('DB_PASSWORD', default=''),
            read_timeout=timeout,
            port=config('DB_PORT', default='3306', cast=int),
            user=config('DB_USER', default='root'),
            write_timeout=timeout,
        )
        print("Conexión establecida correctamente")
        return conn
    except pymysql.Error as e:
        st.error(f"Error al establecer la conexión: {e}")
        return None
    


def insert_data(conn, data):
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO data_comments (Texto, IsToxic) 
        VALUES (%s, %s)
        """

        texto_value = data.get("Texto", "")  # Obtener el valor de "Texto" o un valor predeterminado en caso de que no exista
        is_toxic_value = data.get("IsToxic", "")  # Obtener el valor de "IsToxic" o un valor predeterminado en caso de que no exista

        print("Texto:", texto_value)
        print("IsToxic:", is_toxic_value)

        cursor.execute(query, (texto_value, is_toxic_value))
        conn.commit()
    except pymysql.Error as e:
        st.error(f"Error al insertar los datos: {e}")
    finally:
        cursor.close()