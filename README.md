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


•	Interfaz (si aplica): descripción o imagen de la interfaz gráfica o consola:
7. Desarrollo
	Explicación paso a paso de cómo se desarrolló el proyecto
El primer paso fue seleccionar el proyecto atravez de la pagina: Más de 60 proyectos Python para todos los niveles de experiencia | DataCamp de la cual seleccionamos el proyecto que trata sobre un sistema de recomendación de películas. A partir de ahí empezamos a buscar que necesitábamos para nuestro proyecto, y la primera gran necesidad que tuvimos fue encontrar una base de datos para tener que películas recomendar y su puntaje (y futuramente recomendar películas en base a su reparto), una vez encontrada la base de datos nombrada en el link siendo esta (movies_metadata.csv) buscamos como interactuar con esta. y gracias a las librerías: pandas, os y ast logramos hacer el programa capaz de encontrar el archivo .csv leerlo y interpretarlo y así al interpretar la base de datos como un vector porfin podemos empezar a buscar similitudes de las películas a partir de su resumen o ‘overview’ encontrando palabras importantes y iguales como ‘superheroes’ o ‘romance’  y al encontrar estas palabras comparamos la calificación de las películas con similitudes encontradas y seleccionamos las 5 con puntuación mas alta. Y así ya con el procedimiento claro empezamos a buscar como podíamos generar una interfaz a nuestro proyecto para que no solo corriera en la terminal y así dimos con la biblioteca tkinter 




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

