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
se uso el lenguaje de programacion de python, tambien se uso la libreria 'pandas' para que fuese posible hacer el uso de los archivos .csv (siendo estos credits.csv y movies_metadata.csv), asi mismo tambien se uso la biblioteca 'sklearn' para la búsqueda de similitudes entre películas y asi poder recomendarlas, otra biblioteca que se uso fue 'ast' la cual nos permite poder interpretar y interactuar con la base de datos de los archivos csv, y de las ultimas librerias que se utilizo fue la libreria 'os' que es la que permite ubicar los datos con los que se trabajara, y la ultima libreria que se utilizo fue 'tkinter' que nos permitio toda la parte de la interfaz del proyecto.
•	Requisitos de instalación o ejecución:
para la ejecucion del programa se necesitan los archivos credits.csv y movies_metadata.csv. Tambien se necesita tener phyton descargado con las librerias 'pandas','sklearn','ast','os' y 'tkinter'
6. Diseño del Proyecto
•	Arquitectura o estructura del programa: (modularización, funciones, clases, etc.):
la arquitectura del programa se basa en la programacion modular, se usaron las funciones get_recomendations() y buscar()

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

