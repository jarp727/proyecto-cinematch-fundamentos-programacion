import pandas as pd
import ast
import os
import tkinter as tk
from tkinter import messagebox, ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Establecer carpeta de trabajo
os.chdir(r'C:\Users\AN515-55\OneDrive\Escritorio\proyecto fundamentos')

# Cargar archivos CSV
movies = pd.read_csv('movies_metadata.csv', low_memory=False)
credits = pd.read_csv('credits.csv')

# Preparar datos
movies['id'] = pd.to_numeric(movies['id'], errors='coerce')
credits['id'] = pd.to_numeric(credits['id'], errors='coerce')
movies = movies.merge(credits, on='id')
movies['overview'] = movies['overview'].fillna('')
movies['title'] = movies['title'].fillna('').astype(str)
movies['vote_average'] = pd.to_numeric(movies['vote_average'], errors='coerce').fillna(0)

# Vectorizar descripciones
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
#calcula la similitud coseno ntre todas las peliculas
#al ser mas pequeño el coseno entre cada vector  mas similar es la 'overview' de la pelicula
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# Índice para buscar películas por título en minúsculas
indices = pd.Series(movies.index, index=movies['title'].str.lower()).drop_duplicates()
