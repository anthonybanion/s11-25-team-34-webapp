# EcoShop Dashboard

Dashboard interactivo de e-commerce para análisis de impacto ambiental.

## Instalación

1. **Crear entorno virtual con Python 3.11:**
```bash
cd dashboard
python -m venv venv

# Activar
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

## Ejecutar

Desde la **raíz del proyecto**:
```bash
streamlit run dashboard/app.py
```

O desde dentro de `dashboard/`:
```bash
cd dashboard
streamlit run app.py
```

Se abre automáticamente en: `http://localhost:8501`

## Requisitos previos

Antes de ejecutar el dashboard, asegurate de tener los datos:
```bash
cd backend/ecoshop-data
python data_module/impact_calculator.py
```

Esto genera `data/products_with_impact.csv` que usa el dashboard.

## Estructura
```
dashboard/
├── app.py              # Dashboard principal
├── requirements.txt    # Dependencias
└── README.md          # Esta documentación
```

## Funcionalidades

- **Inicio**: KPIs y estadísticas generales
- **Análisis**: Gráficos de composición y comparativas

- **Explorador**: Filtros avanzados de productos
