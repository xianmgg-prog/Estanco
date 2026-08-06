import streamlit as st
import pandas as pd

# ------------------------------------------------------
# Configuración general de la página
# ------------------------------------------------------
st.set_page_config(
    page_title="Estanco Analytics",
    page_icon="🚬",
    layout="wide",
)

# ------------------------------------------------------
# Título y descripción
# ------------------------------------------------------
st.title("Estanco Analytics")
st.markdown(
    """
Aplicación web para analizar las ventas de un estanco.

- Sube un archivo CSV con tus datos reales o utiliza el dataset de ejemplo.
- La app calcula ingresos, márgenes, beneficios y rotación por producto y categoría.
- Incluye KPIs, rankings y visualizaciones interactivas.

"""
)

# ------------------------------------------------------
# Datos de ejemplo
# ------------------------------------------------------
@st.cache_data
def generar_datos_ejemplo() -> pd.DataFrame:
    """Genera un dataset de ejemplo con productos típicos de un estanco."""
    data = {
        "producto": [
            "Marlboro Rojo 20", "Camel Blue 20", "Lucky Strike 20",
            "Tabaco Liar Pueblo", "Puros Montecristo", "Sellos Correos",
            "Mecheros BIC", "Papel Smoking", "Vaper Frutal",
        ],
        "categoria": [
            "tabaco_cajetilla", "tabaco_cajetilla", "tabaco_cajetilla",
            "tabaco_rollo", "puros", "sellos",
            "otros", "otros", "otros",
        ],
        "unidades_vendidas": [
            1200, 900, 600,
            300, 150, 400,
            250, 500, 200,
        ],
        "precio_venta_unitario": [
            5.50, 5.30, 5.40,
            8.00, 9.50, 0.70,
            1.50, 1.20, 8.50,
        ],
        "stock_medio": [
            150, 120, 100,
            40, 20, 60,
            30, 50, 25,
        ],
    }
    df = pd.DataFrame(data)
    return df


def preparar_df(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula ingresos, márgenes, beneficios y rotación sobre el dataframe."""
    # Ingresos
    if "ingresos" not in df.columns:
        df["ingresos"] = df["unidades_vendidas"] * df["precio_venta_unitario"]

    # Márgenes estándar por categoría
    margenes = {
        "tabaco_cajetilla": 0.085,
        "tabaco_rollo": 0.09,
        "puros": 0.09,
        "sellos": 0.04,
        "otros": 0.20,  # complementos, estimado
    }
    df["margen_pct"] = df["categoria"].map(margenes).fillna(0.20)

    # Beneficio estimado
    df["beneficio"] = df["ingresos"] * df["margen_pct"]

    # Rotación de producto
    df["rotacion"] = df["unidades_vendidas"] / df["stock_medio"]

    return df


# ------------------------------------------------------
# Sidebar: origen de datos y opciones
# ------------------------------------------------------
st.sidebar.header("Configuración")

origen_datos = st.sidebar.radio(
    "Origen de datos",
    ("CSV propio", "Datos de ejemplo"),
    index=1,
)

archivo_csv = None
if origen_datos == "CSV propio":
    archivo_csv = st.sidebar.file_uploader(
        "Sube el CSV de ventas del estanco", type=["csv"]
    )

# ------------------------------------------------------
# Cargar datos
# ------------------------------------------------------
if origen_datos == "CSV propio" and archivo_csv is not None:
    try:
        df_raw = pd.read_csv(archivo_csv)
    except Exception as e:
        st.error(f"Error al leer el CSV: {e}")
        st.stop()
else:
    df_raw = generar_datos_ejemplo()

# Mostrar aviso si se usan datos de ejemplo
if origen_datos == "Datos de ejemplo":
    st.info("Usando datos de ejemplo. Cuando tengas tu CSV, selecciona 'CSV propio' en la barra lateral.")

# ------------------------------------------------------
# Verificación mínima de columnas
# ------------------------------------------------------
columnas_necesarias = ["producto", "categoria", "unidades_vendidas", "precio_venta_unitario", "stock_medio"]
faltan = [c for c in columnas_necesarias if c not in df_raw.columns]

if faltan:
    st.warning(
        "Las siguientes columnas necesarias no se encuentran en el dataset: "
        + ", ".join(faltan)
        + "\n\nAdjunta un CSV con estas columnas o adapta el código a tus nombres de columnas."
    )

# Para no romper la app, seguimos sólo con las columnas que sí existan
df = df_raw.copy()

# ------------------------------------------------------
# Preparar datos (cálculos)
# ------------------------------------------------------
df = preparar_df(df)

# ------------------------------------------------------
# Layout principal: tabla + KPIs
# ------------------------------------------------------
st.subheader("Datos de ventas")
st.dataframe(df, use_container_width=True)

ingresos_totales = float(df["ingresos"].sum())
beneficio_total = float(df["beneficio"].sum())
rotacion_media = float(df["rotacion"].mean())

col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
col_kpi1.metric("Ingresos totales", f"{ingresos_totales:,.2f} €")
col_kpi2.metric("Beneficio estimado", f"{beneficio_total:,.2f} €")
col_kpi3.metric("Rotación media", f"{rotacion_media:,.2f} veces")

# ------------------------------------------------------
# Secciones de análisis
# ------------------------------------------------------
st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Top productos por unidades")
    top_unidades = df.sort_values("unidades_vendidas", ascending=False).head(10)
    st.dataframe(top_unidades[["producto", "categoria", "unidades_vendidas", "ingresos", "beneficio", "rotacion"]], use_container_width=True)

with col_right:
    st.subheader("Top productos por beneficio")
    top_beneficio = df.sort_values("beneficio", ascending=False).head(10)
    st.dataframe(top_beneficio[["producto", "categoria", "beneficio", "unidades_vendidas", "ingresos", "rotacion"]], use_container_width=True)

st.markdown("---")

# ------------------------------------------------------
# Visualizaciones por categoría
# ------------------------------------------------------
st.subheader("Análisis por categoría")

agrupado = df.groupby("categoria").agg(
    ingresos_total=("ingresos", "sum"),
    beneficio_total=("beneficio", "sum"),
    unidades_total=("unidades_vendidas", "sum"),
)

st.dataframe(agrupado, use_container_width=True)

col_chart1, col_chart2 = st.columns(2)
with col_chart1:
    st.caption("Ingresos por categoría")
    st.bar_chart(agrupado["ingresos_total"])

with col_chart2:
    st.caption("Beneficio por categoría")
    st.bar_chart(agrupado["beneficio_total"])

# ------------------------------------------------------
# Comentario de análisis automático
# ------------------------------------------------------
st.markdown("---")
st.subheader("Comentario automático del negocio")

categoria_top_ingresos = agrupado["ingresos_total"].idxmax()
categoria_top_beneficio = agrupado["beneficio_total"].idxmax()

texto = []
texto.append(
    f"El estanco genera unos ingresos totales aproximados de {ingresos_totales:,.2f} €, "
    f"con un beneficio estimado de {beneficio_total:,.2f} € considerando los márgenes estándar por categoría."
)
texto.append(
    f"La categoría con mayor peso en ingresos es **{categoria_top_ingresos}**, "
    f"mientras que la que más contribuye al beneficio es **{categoria_top_beneficio}**."
)
texto.append(
    "La rotación media de productos indica cuántas veces se renueva el stock en el periodo analizado; "
    "una rotación alta sugiere productos de venta rápida y una rotación baja apunta a artículos que permanecen más tiempo en estantería."
)
texto.append(
    "A partir de este análisis se pueden tomar decisiones sobre qué referencias potenciar, cuáles reducir y cómo diversificar "
    "la oferta de productos complementarios para aumentar el margen global del estanco."
)

for p in texto:
    st.write(p)

st.markdown("---")
st.caption(
    "Cuando tengas tu CSV real, adapta los nombres de columnas en `columnas_necesarias` y revisa el diccionario de márgenes `margenes` "
    "para ajustarlo a la realidad de tu estanco."
)
