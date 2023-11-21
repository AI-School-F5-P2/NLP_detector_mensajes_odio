<!-- README.md -->

![Texto alternativo](https://media2.giphy.com/media/13Nc3xlO1kGg3S/200w.webp?cid=ecf05e47296jnhengboeapz7plmiyee13x7o8ai7al9p6qbf&ep=v1_gifs_search&rid=200w.webp&ct=g)


# Proyecto 4: NLP - Detención de Mensajes de Odio en YouTube

## Planteamiento

YouTube busca una solución eficiente para la detección automática de mensajes de odio en los comentarios de sus vídeos. El aumento de estos mensajes ha superado la capacidad de su equipo de moderadores. La consultora, donde trabajamos, debe proponer una solución práctica y escalable para abordar este problema.

## Propuesta de Solución

Hemos optado por desarrollar un modelo de procesamiento del lenguaje natural (NLP) para identificar mensajes de odio. La solución utiliza tecnologías como Scikit-learn para el procesamiento de datos, Spacy para el análisis lingüístico, y Huggingface para aprovechar modelos preentrenados de transformers.

### Pasos Principales:

1. **Preprocesamiento de Datos:**
   - Utilizaremos la biblioteca NLTK para realizar la tokenización y eliminación de stop words.
   - Aplicaremos técnicas de limpieza de texto para normalizar el formato y reducir el ruido.

2. **Extracción de Características:**
   - Usaremos técnicas de vectorización, como TF-IDF, para convertir los mensajes de texto en vectores numéricos que el modelo pueda entender.

3. **Modelo de Aprendizaje Automático:**
   - Emplearemos modelos de clasificación de texto de Huggingface, como BERT, que están preentrenados en grandes cantidades de datos.
   - Fine-tunearemos el modelo con un conjunto de datos etiquetado de mensajes de odio y
