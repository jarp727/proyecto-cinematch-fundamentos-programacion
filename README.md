          # proyecto-cinematch-fundamentos-programacion

                                                                                                                 CINEMATCH
Participantes del proyecto:
   1) Daniel Garzon
   2) Nicolas Fayad
   3) Camilo Saenz
   4) Javier Russi
•	Curso / Grupo: A
•	Fecha de entrega:
•	Profesor: Pablo Carreño
2. Titulo del proyecto
•                                                                                                                CineMatch

4. Descripción del Proyecto
Nuestro proyecto se basa en crear un programa que, a través, del análisis de datos, pueda recomendar películas a partir de estos:

•	Propósito o problema que resuelve: Usualmente las personas no encuentran películas de su gusto, entonces está el típico problema en el que te quedas mucho tiempo buscando películas y no encuentras nada, entonces dejas las películas a un lado y te pones a hacer otras cosas, nuestro propósito es ayudar a que estas personas tengan varias opciones de películas, y ellos poder elegir entre estas.
•	Público objetivo o aplicación práctica: Nuestro programa esta diseñado para todo tipo de público, entonces cualquier persona lo puede usar, no importa la edad, su aplicación seria en cualquier cosa en el que una persona este buscando una película, y no encuentre que ver
•	Resultado esperado: Generar una ayuda a las personas para que no les tome mucho tiempo elegir una película, y poder solucionar este problema tan comun
4. Objetivos
General:
•	Describir el propósito principal del proyecto: El proposito principal es brindar una ayuda eficiente y rapida a esas personas que nunca encuentran peliculas que se acoplen a sus gustos, entonces deciden mejor no ver nada, nuestra aplicacion, busca solucionar ese problema
Específicos:
•	Enumerar los objetivos técnicos o de aprendizaje específicos (ej. usar estructuras de datos, aplicar funciones, temas vistos en clase, etc.):
Implementar estructuras de datos eficientes (listas, diccionarios, árboles) para almacenar y organizar la información de las películas.
Aplicar técnicas de análisis de datos para identificar patrones de preferencia en los usuarios y mejorar la precisión de las recomendaciones.
Utilizar funciones y modularización para mantener un código limpio, reutilizable y fácil de mantener.
5. Requisitos
•	Herramientas y tecnologías utilizadas (Python, librerías, etc.):
•	Requisitos de instalación o ejecución:
6. Diseño del Proyecto
•	Arquitectura o estructura del programa: (modularización, funciones, clases, etc.):

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def cargar_metadata(ruta):
    print(" Cargando datos...")
    metadata = pd.read_csv(ruta, low_memory=False)

    # Filtrar columnas relevantes
    metadata = metadata[['title', 'vote_count', 'vote_average', 'overview']].dropna(subset=['title'])

    # Convertir columnas numéricas
    metadata['vote_count'] = pd.to_numeric(metadata['vote_count'], errors='coerce')
    metadata['vote_average'] = pd.to_numeric(metadata['vote_average'], errors='coerce')

    # Limpiar texto nulo
    metadata['overview'] = metadata['overview'].fillna('')

    # Eliminar filas con datos faltantes críticos
    metadata = metadata.dropna(subset=['vote_count', 'vote_average'])

    print(f"✅ {len(metadata)} películas cargadas correctamente.\n")
    return metadata


def calcular_top_peliculas(metadata, cantidad=10):
    print("📊 Calculando puntuaciones ponderadas estilo IMDb...")

    C = metadata['vote_average'].mean()
    m = metadata['vote_count'].quantile(0.90)

    calificadas = metadata[metadata['vote_count'] >= m].copy()

    def puntuacion(x):
        v, R = x['vote_count'], x['vote_average']
        return (v / (v + m)) * R + (m / (v + m)) * C

    calificadas['score'] = calificadas.apply(puntuacion, axis=1)
    top = calificadas.sort_values('score', ascending=False)[['title', 'score']].head(cantidad)

    print(" Top películas por calidad y popularidad:\n")
    for i, fila in enumerate(top.itertuples(), 1):
        print(f"{i}. {fila.title} — Puntuación: {round(fila.score, 2)}")
    print()


def construir_matriz_similitud(metadata):
    print(" Procesando descripciones de tramas con TF-IDF...")
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(metadata['overview'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()
    print(" Matriz de similitud construida.\n")
    return cosine_sim, indices

def recomendar_similares(titulo, metadata, cosine_sim, indices, cantidad=5):
    if titulo not in indices:
        print(" Película no encontrada. Verifica el título.")
        return []

    idx = indices[titulo]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:cantidad+1]
    movie_indices = [i[0] for i in sim_scores]
    return metadata['title'].iloc[movie_indices].tolist()


def mostrar_menu():
    print("╔════════════════════════════════════╗")
    print("║ 🎬 SISTEMA DE RECOMENDACIÓN DE PELÍCULAS ║")
    print("╚════════════════════════════════════╝")
    print("1. Ver Top películas por puntuación")
    print("2. Buscar películas similares por trama")
    print("3. Salir")
    print("──────────────────────────────────────")

def iniciar():
    ruta = 'movies_metadata.csv'
    metadata = cargar_metadata(ruta)
    cosine_sim, indices = construir_matriz_similitud(metadata)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            calcular_top_peliculas(metadata, cantidad=10)

        elif opcion == '2':
            titulo = input("🔍 Ingresa el nombre de una película: ")
            similares = recomendar_similares(titulo, metadata, cosine_sim, indices)
            if similares:
                print(f"\n📚 Películas similares a '{titulo}':")
                for peli in similares:
                    print(f"- {peli}")
                print()
        elif opcion == '3':
            print(" Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print(" Opción inválida. Intenta nuevamente.\n")

if __name__ == "__main__":
    iniciar()

if __name__ == "__main__":
    iniciar()

•	Diagrama de flujo:
┌────────────────────────────────────────────┐
│                INICIO                      │
└────────────────────────────────────────────┘
                    │
                    ▼
     ┌───────────────────────────────┐
     │ Cargar archivo CSV de películas │
     └───────────────────────────────┘
                    │
                    ▼
     ┌────────────────────────────────────────────┐
     │ Limpiar y preparar columnas necesarias      │
     │ (title, vote_count, vote_average, overview)│
     └────────────────────────────────────────────┘
                    │
                    ▼
     ┌────────────────────────────────────────────┐
     │ Construir matriz TF-IDF con overview        │
     │ (eliminar stopwords, convertir a vectores) │
     └────────────────────────────────────────────┘
                    │
                    ▼
     ┌────────────────────────────────────────────┐
     │ Calcular similitud coseno entre películas  │
     └────────────────────────────────────────────┘
                    │
                    ▼
     ┌────────────────────────────────────────────┐
     │ Mostrar menú interactivo en consola        │
     └────────────────────────────────────────────┘
                    │
                    ▼
        ┌────────────────────────────┐
        │ ¿Qué desea hacer el usuario?│
        └────────────────────────────┘
           │               │
           ▼               ▼
┌────────────────┐   ┌────────────────────────────┐
│ Opción 1: Top  │   │ Opción 2: Buscar similares │
│ películas por  │   │ por descripción de trama   │
│ puntuación     │   └────────────────────────────┘
└────────────────┘               │
       │                         ▼
       ▼             ┌────────────────────────────────────┐
┌──────────────────────────────┐ │ Usuario ingresa título │
│ Calcular C (media votos)     │ └────────────────────────────────────┘
│ Calcular m (percentil 90)    │               │
│ Filtrar películas con votos ≥ m│             ▼
│ Aplicar fórmula IMDb         │ ┌────────────────────────────────────┐
│ Ordenar por score            │ │ Buscar índice de película en matriz│
└──────────────────────────────┘ │ de similitud coseno                │
       │                         └────────────────────────────────────┘
       ▼                         │
┌──────────────────────────────┐ ▼
│ Mostrar Top N películas      │ ┌────────────────────────────────────┐
└──────────────────────────────┘ │ Ordenar películas por similitud    │
                                │ Mostrar las N más similares         │
                                └────────────────────────────────────┘
                                        │
                                        ▼
                        ┌────────────────────────────────────┐
                        │ ¿Desea realizar otra acción?       │
                        └────────────────────────────────────┘
                                        │
                          ┌─────────────┴─────────────┐
                          ▼                           ▼
             ┌────────────────────┐       ┌────────────────────────┐
             │ Volver al menú     │       │ Opción 3: Salir del sistema │
             └────────────────────┘       └────────────────────────┘
                                                    │
                                                    ▼
                                   ┌────────────────────────────┐
                                   │           FIN              │
                                   └────────────────────────────┘


•	Interfaz (si aplica): descripción o imagen de la interfaz gráfica o consola:
7. Desarrollo
•	Explicación paso a paso de cómo se desarrolló el proyecto
•	Fragmentos de código relevantes comentados
•	Descripción de las funciones principales
8. Pruebas y Resultados
•	Cómo se probó el programa
•	Capturas de pantalla o ejemplos de ejecución
•	Resultados obtenidos
•	Manual de usuario
9. Conclusiones
•	Lecciones aprendidas
•	Dificultades encontradas y cómo se resolvieron
•	Posibles mejoras o ideas futuras
10. Bibliografía / Recursos
•	Sitios web, documentación, libros o videos utilizados, mínimo 10

