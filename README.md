# Repositorio para distintos proyectos de análisis de fútbol

## 👀 Propósito de este repositorio y acerca de su autor

Creé este repositorio a modo de tener un espacio dedicado al aprendizaje y aplicación de la ciencia de datos en el mundo del fútbol. Aquí van a encontrar diferentes proyectos en torno al tema, desde la aplicación de la estadística y matemática hasta la generación de visuales más sencillos pero que ofrezcan insights valiosos.

Mi principal propósito es contribuir compartiendo los proyectos que vaya haciendo y además mejorar mis técnicas relacionadas a la ciencia de datos.

Si te gustó o encontraste útil este repositorio (o ambas ?), considerá darle una ⭐ (arriba a la derecha).

## 📬 Redes y contacto

Esto es un repositorio en constante evolución y por lo tanto pueden haber errores o proyectos que aún están inconclusos, si tenés alguna sugerencia o querés colaborar podés contactarme en alguno
de los links que voy a dejar abajo:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gerardo-toboso-512a48290/)    
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Gerardo1909)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:getobosobarrios@estudiantes.unsam.edu.ar)
  
## ⚙️ Especificaciones y dependencias 

Por ahora este repositorio está desarrollado únicamente en el lenguaje Python. Si querés realizar proyectos similares deberías de tener las siguientes dependencias instaladas:

1. **Python** (recomendado: versión 3.8 o superior).
2. Las siguientes librerías de Python necesarias para llevar a cabo todo el flujo de un proyecto relacionado al fútbol:

### Librerías generales de python para tratar con datos:
- [`numpy`](https://numpy.org/doc/) - Para operaciones matemáticas y manejo de arrays multidimensionales.
- [`pandas`](https://pandas.pydata.org/) - Para análisis y manipulación de datos estructurados.
- [`matplotlib`](https://matplotlib.org/) y [`seaborn`](https://seaborn.pydata.org/) - Para la visualización de datos.
- [`scikit-learn`](https://scikit-learn.org/stable/) y [`scipy`](https://docs.scipy.org/doc/scipy/) - Para machine learning y análisis estadístico.

### Librerías especializadas en el análisis del fútbol:
- [`mplsoccer`](https://mplsoccer.readthedocs.io/en/latest/) - Una librería de Python para graficar canchas de fútbol y realizar análisis visuales avanzados.
- [`statsbombpy`](https://github.com/statsbomb/statsbombpy) - Para interactuar con la API de [StatsBomb](https://github.com/statsbomb/open-data) y analizar datos de eventos.
- [`LanusStats`](https://github.com/federicorabanos/LanusStats/tree/main) - Librería desarrollada por [federicorabanos](https://github.com/federicorabanos) del canal de youtube [LanusStats](https://www.youtube.com/@LanusStats). Útil para scrapear datos de diferentes páginas de fútbol.

### Algunas librerías útiles:
- [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Para web scraping.
- [`requests`](https://requests.readthedocs.io/en/latest/) - Para manejo de peticiones web.
- [`joblib`](https://joblib.readthedocs.io/en/stable/) - Para guardar y cargar modelos o pipelines.

## 📁 Estructura de archivos y directorios

El contenido de este repositorio se decidió organizarlo de la siguiente forma:  

```markdown
gerardo1909/analisis_de_futbol/ 📂⚽ Repositorio principal
├── proyectos/ 📂 Directorio que contiene la recopilación de todos los proyectos realizados o en proceso
│   ├── proyecto1/ 📂 Primer proyecto que contiene notebooks y datos
│   │   ├── data/ 📁 Directorio de los datos usados en el proyecto
│   │   │   ├── raw/ 📂 Directorio de datos sin procesar
│   │   │   └── processed/ 📂 Directorio de datos procesados y listos para analizar
│   │   ├── img/ 📂 Imágenes y visualizaciones generadas en el proyecto
│   │   ├── README.md 📄 Documentación específica del proyecto
│   │   ├── 1_notebook1.ipynb 📒 Primer notebook implicado
│   │   ├── 2_notebook2.ipynb 📒 Segundo notebook implicado
│   │   └── N_notebookN.ipynb 📒 Último notebook (si existen múltiples)
│   ├── proyecto2/ 📂 Segundo proyecto, siguiendo una estructura similar
│   ├── proyectoN/ 📂 Más proyectos con la misma estructura
│   └── ...
│
├── scripts/ 📂🛠️ Directorio que contiene scripts varios para preprocesamiento, análisis o automatización
│   └── ejemplo_script.py 📄 Un script de ejemplo
│
├── .gitignore 📄 Especifica archivos ignorados por Git
├── README.md 📄 Resumen del repositorio y sus objetivos (donde estás ahora)
├── requirements.txt 📄 Lista de dependencias del repositorio
└── setup.py 📄 script para configuración e instalación de este repositorio como paquete
```

## 💻 ¿Cómo clonar y correr este repositorio?

**Antes de seguir estos pasos debés tener instalado 'Python' y 'pip' en tu sistema.**

### 1. Clonar el repositorio

Primero, cloná el repositorio en tu máquina local y accede al directorio donde decidiste alojar el proyecto:

```sh
git clone https://github.com/Gerardo1909/analisis_de_futbol.git
cd analisis_de_futbol (o el nombre que quieras)
```

### 2. Crear un entorno virtual

Creá un entorno virtual para gestionar las dependencias del proyecto de forma aislada:

```sh
python -m venv analisis_futbol_env
```

### 3. Activar el entorno virtual

Activá el entorno virtual que acabas de crear:

```sh
# En Windows:
analisis_futbol_env\Scripts\activate

# En macOS o Linux:
source analisis_futbol_env/bin/activate
```

### 4. Instalar las dependencias

Con el entorno virtual activado, instala las dependencias necesarias utilizando el archivo `requirements.txt`:

```sh
pip install -r requirements.txt
```

Y listo, ahora podés explorar los proyectos en la carpeta `proyectos` e incluso aprovechar la estructura ya creada para poder hacer los tuyos propios.

Si tienes algún problema o pregunta, no dudes en contactarme o abrir un _issue_ en el repositorio. 🫡