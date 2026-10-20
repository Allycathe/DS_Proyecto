# DS_Proyecto: Clasificación de ICVU por comuna con KNN

Modelo KNN que clasifica comunas según su ICVU (Índice de Calidad de Vida Urbana) a partir de variables de cada comuna.

## Estructura del proyecto

```
DS_Proyecto/
├── data_obtain_comunas.ipynb    # Obtiene y une los datos (ICVU + features) y genera el dataset
├── KNN-Clasif-Predic.ipynb      # Entrena, evalúa y guarda el modelo KNN
├── ICVU_proyecto/               # Notebooks / código del proyecto
├── dataset/                     # CSV generado (dataset_comunas.csv)
├── modelos/                     # Modelo entrenado (.joblib)
└── requirements.txt
```

## Requisitos

- Python 3.<X> o superior
- Git

## Instalación

1. Clonar el repositorio:
```bash
   git clone https://github.com/Allycathe/DS_Proyecto.git
   cd DS_Proyecto
```

2. Crear y activar un entorno virtual:
```bash
   python -m venv venv
   source venv/bin/activate      # Linux / macOS
   venv\Scripts\activate         # Windows
```

3. Instalar dependencias:
```bash
   pip install -r requirements.txt
```

4. Crear las carpetas de salida si no existen (están ignoradas por Git):
```bash
   mkdir -p dataset modelos
```

## Cómo correr el modelo (paso a paso)

1. Iniciar Jupyter:
```bash
   jupyter notebook
```

2. **Generar el dataset:** abrir `data_obtain_comunas.ipynb` y ejecutar todas las celdas (*Kernel → Restart & Run All*). Esto crea `dataset/dataset_comunas.csv`.

3. **Entrenar el modelo:** abrir `KNN-Clasif-Predic.ipynb` y ejecutar todas las celdas. El notebook:
   - carga `dataset/dataset_comunas.csv`
   - separa train/test (`TEST_SIZE = 0.3`, `SEMILLA = 42`)
   - entrena el KNN y muestra las métricas
   - guarda el modelo en `modelos/modelo_knn_icvu_clasif.joblib`

4. **Verificar:** comprobar que existe `modelos/modelo_knn_icvu_clasif.joblib`.

## Usar el modelo guardado

```python
import joblib

modelo = joblib.load("modelos/modelo_knn_icvu_clasif.joblib")
prediccion = modelo.predict(X_nuevo)   # X_nuevo con las mismas columnas del entrenamiento
```

## Configuración

Los parámetros están al inicio de `KNN-Clasif-Predic.ipynb`:

| Variable | Descripción |
|---|---|
| `DEBUG` | Activa mensajes de depuración |
| `SEMILLA` | Semilla para reproducibilidad |
| `DATASET` | Ruta del CSV de entrada |
| `GUARDAR_MODELO` | Ruta donde se guarda el modelo |
| `TEST_SIZE` | Proporción de datos para test |

## Problemas comunes

- **No encuentra el dataset:** ejecuta primero `data_obtain_comunas.ipynb` y revisa que el notebook se corra desde la raíz del proyecto.
- **No aparece el modelo:** confirma que la celda de `joblib.dump` se ejecutó y que existe la carpeta `modelos/`.

## Autores
S1NX, MAID, ADONSO, VICHANGA Y MAXIMILINO
