# ¿Qué distingue a las comunas con mejor calidad de vida en Santiago?

Proyecto semestral de Data Science 2026, Universidad Diego Portales.

Usamos datos abiertos de **OpenStreetMap** (salud, educación, transporte, comercio, recreación, seguridad y usos negativos del suelo) para entender qué dimensiones del equipamiento urbano distinguen a las comunas de calidad de vida alta y baja, según el **Índice de Calidad de Vida Urbana (ICVU) 2025**.

* **Unidad de análisis:** la comuna (las 42 comunas de la Región Metropolitana medidas por el ICVU 2025).
* **Variable objetivo:** nivel ICVU 2025: 1 Bajo, 2 Medio bajo, 3 Medio alto, 4 Alto (Instituto de Estudios Urbanos UC y Cámara Chilena de la Construcción).
* **Tipo de problema:** clasificación supervisada con interpretación (¿qué dimensiones pesan más?).
* **Metodología:** OSEMN.

## Estructura

```
DS_Proyecto/
├── proyecto.ipynb                        # Notebook principal (secciones 1 a 6)
├── dataset/
│   ├── raw/dataset_comunas.csv           # Salida de la sección 1: una fila por comuna (98 comunas del ICVU)
│   ├── processed/dataset_limpio.csv      # Salida de la sección 2 (98 comunas)
│   ├── processed/dataset_limpio_antiguo.csv  # 42 comunas de la RM: el que usan el EDA y los modelos
│   ├── icvu_comunas.csv                  # Nivel ICVU 2025 por comuna
│   ├── poblacion_comunas.csv             # Población por comuna (Censo 2024), RM
│   └── poblacion_faltante.csv            # Población de las comunas fuera de la RM
├── datos_comunas/                        # Descarga de OSM (un .gpkg por comuna) y lugares descargados
├── modelo/
│   └── modelo_icvu_clasif.joblib         # Modelo final entrenado con las 42 comunas
├── reports/
│   ├── EDA_report.html                   # Reporte exploratorio automático (ydata-profiling)
│   └── figuras/                          # Gráficos de las secciones 4 y 5
├── requirements.txt
└── README.md
```

## Contenido de `proyecto.ipynb`

| Sección | Qué hace |
|---|---|
| Problema y objetivos | Unidad de análisis, objetivos y cómo se obtiene la variable objetivo |
| 1. Obtención de datos | Descarga los lugares desde OSM (Overpass) con caché por comuna. Tarda más de una hora si se parte de cero |
| 2. Limpieza y validación | Revisa duplicados, nulos, infinitos y rangos. Guarda `dataset/processed/dataset_limpio.csv` |
| 3. Análisis exploratorio | Target, sesgo, outliers, correlación con el ICVU, redundancia y PCA |
| 4. Modelos | KNN, Regresión Logística, Random Forest, Gradient Boosting y MLP contra un baseline. Hiperparámetros con Grid Search, Random Search y optimización bayesiana (Optuna). Validación cruzada repetida |
| 4.5 Desbalance de clases | Compara pesos por clase, Random Oversampling, SMOTE, Random Undersampling, Tomek Links, Cluster Centroids y NearMiss, aplicados dentro del Pipeline |
| 4.6 Modelo final | Pipeline final y prueba de permutación |
| 5. Interpretación | Importancia por dimensión, dirección, variables más importantes, ROC/AUC y valores SHAP |
| 6. Conclusiones y limitaciones | Respuesta al problema inicial |

## Instalación

Requiere Python 3.10 o superior (probado con 3.12).

```bash
git clone https://github.com/Allycathe/DS_Proyecto.git
cd DS_Proyecto
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

## Cómo reproducir los resultados

1. Abrir el notebook desde la raíz del proyecto: `jupyter notebook proyecto.ipynb`.
2. **Secciones 1 y 2 (opcionales):** solo hacen falta para volver a descargar los datos de OSM. El repositorio ya trae los datasets.
3. **Secciones 3 a 6:** ejecutar en orden. Tardan unos 5 minutos.
4. Las figuras quedan en `reports/figuras/` y el modelo final en `modelo/modelo_icvu_clasif.joblib`.

## Usar el modelo guardado

```python
import joblib
import pandas as pd

modelo = joblib.load("modelo/modelo_icvu_clasif.joblib")   # Pipeline: imputar -> escalar -> Regresión Logística

df = pd.read_csv("dataset/processed/dataset_limpio_antiguo.csv")
columnas = [c for c in df.columns if c.startswith("x10k_") and not c.startswith("x10k_cat_")]
columnas += [c for c in df.columns if c.startswith("pct_area_")] + ["hab_km2"]

niveles = {1: "Bajo", 2: "Medio bajo", 3: "Medio alto", 4: "Alto"}
pred = modelo.predict(df[columnas])
print(pd.Series(pred).map(niveles).value_counts())
```

## Fuentes de datos

* **OpenStreetMap** (© colaboradores de OpenStreetMap, licencia ODbL), descargado con la API Overpass y OSMnx.
* **ICVU 2025**: Núcleo de Investigación sobre Gobernanza y Ordenamiento Territorial, Instituto de Estudios Urbanos y Territoriales UC, y Cámara Chilena de la Construcción.
* **Población:** Censo de Población y Vivienda 2024, INE.

## Autores
S1NX, MAID, ADONSO, VICHANGA Y MAXIMILINO
