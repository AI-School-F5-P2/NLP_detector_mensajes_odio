<!-- README.md -->

<p align="center">
  <img width="400"  src="https://media2.giphy.com/media/13Nc3xlO1kGg3S/200w.webp?cid=ecf05e47296jnhengboeapz7plmiyee13x7o8ai7al9p6qbf&ep=v1_gifs_search&rid=200w.webp&ct=g" alt="Texto alternativo">
</p>


# Proyecto 4: NLP - Detención de Mensajes de Odio en YouTube

## Planteamiento

YouTube busca una solución eficiente para la detección automática de mensajes de odio en los comentarios de sus vídeos. El aumento de estos mensajes ha superado la capacidad de su equipo de moderadores. La consultora, donde trabajamos, debe proponer una solución práctica y escalable para abordar este problema.

## Propuesta de Solución

Hemos optado por desarrollar un modelo de procesamiento del lenguaje natural (NLP) para identificar mensajes de odio. La solución utiliza tecnologías como Scikit-learn para el procesamiento de datos, Spacy para el análisis lingüístico, y Huggingface para aprovechar modelos preentrenados de transformers.

### Pasos Principales:

1. **Preprocesamiento de Datos:**
   - Mediante Regex realizamos una limpieza profunda
   - Utilizaremos la biblioteca Spacy para realizar la tokenización y eliminación de stop words.
   - Aplicaremos técnicas de limpieza de texto para normalizar el formato y reducir el ruido.

2. **Extracción de Características:**
   - Usaremos técnicas de vectorización, como TF-IDF, para convertir los mensajes de texto en vectores numéricos que el modelo pueda entender.

3. **Modelo de Aprendizaje Automático:**
   - Emplearemos modelos de Maching learning para clasificación de texto.
   - Con aumento de datos logramos obtener un mejor resultado.

4. **Aplicacion  que productivice el modelo (una interfaz o API o scraper o lo que se os ocurra, que permita a un usuario consultar si un mensaje  es o no de odio)**
   - Emplearemos la herramienta Streamlit para desarrollar una aplicación que detecte si un comentario es tóxico o no.
   - Consumiremos la API de YouTube v3 para predecir de manera masiva los comentarios de un video en particular.

## INSTALACION


1. **Clonar el repositorio y acceder a el:**

```bash
git clone https://github.com/AlexisVennegas/NLP_detector_mensajes_odio.git
cd NLP_detector_mensajes_odio
```

2. **instalar los requisitos del proyecto:**

```bash
pip install -r requirements.txt
```

3. **Completar tus variables de entorno en el archivo .env:**

```bash
DB_USER= 
DB_PASSWORD= 
DB_HOST= 
DB_PORT= 
DB_NAME= 
API_KEY= 
```

4. **Ejecutar el Proyecto:**

```bash
Streamlit run main.py
```

<p align="center">
  <iframe width="560" height="315" src="https://youtu.be/jmb8q0X2JTc" frameborder="0" allowfullscreen></iframe>
</p>
