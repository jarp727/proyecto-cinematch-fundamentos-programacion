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

#  Función de recomendación con calificación
def get_recommendations(title):
    idx = indices.get(title.lower())
    if idx is None:
        return []
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    recomendadas = movies.iloc[movie_indices][['title', 'vote_average']]
    return list(zip(recomendadas['title'], recomendadas['vote_average']))
    
# Buscar coincidencias parciales
def buscar():
    entrada_texto = entrada.get().lower()
    resultado.delete(0, tk.END)

    coincidencias = movies[movies['title'].str.lower().str.contains(entrada_texto)]
    if coincidencias.empty:
        messagebox.showinfo("Sin resultados", f"No se encontraron películas que contengan '{entrada_texto}'.")
        return

    for titulo in coincidencias['title'].unique():
        resultado.insert(tk.END, f"🎬 Recomendaciones para: {titulo}")
        recomendaciones = get_recommendations(titulo)
        if recomendaciones:
            for peli, score in recomendaciones:
                resultado.insert(tk.END, f"  🍿 {peli} (⭐ {score:.1f})")
        else:
            resultado.insert(tk.END, "  No se encontraron recomendaciones.")
        resultado.insert(tk.END, "")  # Espacio entre bloques
        
#  Crear ventana
ventana = tk.Tk()
ventana.title("🔗🎦 CineMatch: Tu recomendador de películas")
ventana.attributes('-fullscreen', True)
ventana.configure(bg="#1c1c1c")

# Función para actualizar visibilidad de botones
def actualizar_botones():
    if ventana.attributes('-fullscreen'):
        boton_salir.pack(pady=5)
        boton_volver.pack_forget()
    else:
        boton_salir.pack_forget()
        boton_volver.pack(pady=5)

# Funciones para cambiar modo
def salir_pantalla_completa():
    ventana.attributes('-fullscreen', False)
    actualizar_botones()

def volver_a_pantalla_completa():
    ventana.attributes('-fullscreen', True)
    actualizar_botones()

# Permitir salir con tecla Escape
ventana.bind("<Escape>", lambda e: salir_pantalla_completa())

# Encabezado decorado
tk.Label(
    ventana,
    text="🔗🎦 Bienvenido a CineMatch 🔗🎦",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#1c1c1c"
).pack(pady=10)

# Subtítulo
tk.Label(
    ventana,
    text="Escribe el nombre de una película para recibir recomendaciones:",
    font=("Arial", 12),
    fg="white",
    bg="#1c1c1c"
).pack(pady=5)

# Entrada de texto
entrada = tk.Entry(ventana, width=50, font=("Arial", 11))
entrada.pack(pady=5)

# Botón de búsqueda estilizado
tk.Button(
    ventana,
    text="🎦 Buscar películas similares 🎦",
    command=buscar,
    font=("Arial", 11, "bold"),
    bg="#ff4444",
    fg="white",
    activebackground="#ff6666"
).pack(pady=10)

# Lista de resultados con estilo
resultado = tk.Listbox(
    ventana,
    width=80,
    height=20,
    font=("Arial", 10),
    bg="#2c2c2c",
    fg="white",
    selectbackground="#444444"
)
resultado.pack(pady=10)

# Botón para salir de pantalla completa
boton_salir = tk.Button(
    ventana,
    text="🔚 Salir de pantalla completa",
    command=salir_pantalla_completa,
    font=("Arial", 10, "bold"),
    bg="#444444",
    fg="white",
    activebackground="#666666"
)

# Botón para volver a pantalla completa
boton_volver = tk.Button(
    ventana,
    text=" Volver a pantalla completa",
    command=volver_a_pantalla_completa,
    font=("Arial", 10, "bold"),
    bg="#444444",
    fg="white",
    activebackground="#666666"
)


actualizar_botones()

ventana.mainloop()

