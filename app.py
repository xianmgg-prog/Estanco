import streamlit as st
import pandas as pd

# ------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ------------------------------------------------------
st.set_page_config(
    page_title="Estanco Analytics",
    page_icon="🚬",
    layout="wide",
)

st.title("Estanco Analytics")
st.markdown(
    """
Aplicación profesional para el análisis de ventas de un estanco.

- Suba un CSV con sus datos reales o utilice el dataset de ejemplo.
- Analice ingresos, márgenes, beneficios y rotación por producto y categoría.
- Explore dashboards interactivos mediante pestañas y desplegables.
"""
)

# ------------------------------------------------------
# FUNCIONES AUXILIARES
# ------------------------------------------------------
@st.cache_data
def generar_datos_ejemplo() -> pd.DataFrame:
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
    # Ingresos
    if "ingresos" not in df.columns:
        df["ingresos"] = df["unidades_vendidas"] * df["precio_venta_unitario"]

    # Márgenes estándar por categoría
    margenes = {
        "tabaco_cajetilla": 0.085,
        "tabaco_rollo": 0.09,
        "puros": 0.09,
        "sellos": 0.04,
        "otros": 0.20,
    }
    df["margen_pct"] = df["categoria"].map(margenes).fillna(0.20)

    # Beneficio estimado
    df["beneficio"] = df["ingresos"] * df["margen_pct"]

    # Rotación de producto
    df["rotacion"] = df["unidades_vendidas"] / df["stock_medio"]

    return df

# ------------------------------------------------------
# SIDEBAR: CONFIGURACIÓN
# ------------------------------------------------------
st.sidebar.header("Configuración de datos")

origen_datos = st.sidebar.radio(
    "Origen de datos",
    ("CSV propio", "Datos de ejemplo"),
    index=1,
)

archivo_csv = None
if origen_datos == "CSV propio":
    archivo_csv = st.sidebar.file_uploader(
        "Suba el CSV de ventas del estanco", type=["csv"]
    )

st.sidebar.markdown("---")

# ------------------------------------------------------
# CARGA DE DATOS
# ------------------------------------------------------
if origen_datos == "CSV propio" and archivo_csv is not None:
    try:
        df_raw = pd.read_csv(archivo_csv)
    except Exception as e:
        st.error(f"Error al leer el CSV: {e}")
        st.stop()
else:
    df_raw = generar_datos_ejemplo()
    st.info(
        "Usando datos de ejemplo. "
        "Cuando tenga su CSV, seleccione 'CSV propio' en la barra lateral."
    )

# Columnas necesarias
columnas_necesarias = [
    "producto", "categoria", "unidades_vendidas",
    "precio_venta_unitario", "stock_medio",
]
faltan = [c for c in columnas_necesarias if c not in df_raw.columns]

if faltan:
    st.warning(
        "Las siguientes columnas necesarias no se encuentran en el dataset: "
        + ", ".join(faltan)
        + "\n\nAdjunte un CSV con estas columnas o adapte el código."
    )

df = df_raw.copy()
df = preparar_df(df)

if df.empty:
    st.warning("No hay datos disponibles.")
    st.stop()

# ------------------------------------------------------
# KPIs
# ------------------------------------------------------
st.markdown("---")

ingresos_totales = float(df["ingresos"].sum())
beneficio_total = float(df["beneficio"].sum())
rotacion_media = float(df["rotacion"].mean())

col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
col_kpi1.metric("Ingresos totales", f"{ingresos_totales:,.2f} €")
col_kpi2.metric("Beneficio estimado", f"{beneficio_total:,.2f} €")
col_kpi3.metric("Rotación media", f"{rotacion_media:,.2f} veces")

# ------------------------------------------------------
# PESTAÑAS
# ------------------------------------------------------
tab_resumen, tab_productos, tab_categorias, tab_graficos = st.tabs(
    ["Resumen", "Productos", "Categorías", "Gráficos"]
)

# Resumen
with tab_resumen:
    st.subheader("Tabla completa de datos")
    st.dataframe(df, use_container_width=True)

    st.markdown("### Resumen por categoría")
    agrupado = df.groupby("categoria").agg(
        ingresos_total=("ingresos", "sum"),
        beneficio_total=("beneficio", "sum"),
        unidades_total=("unidades_vendidas", "sum"),
        rotacion_media=("rotacion", "mean"),
    )
    st.dataframe(agrupado, use_container_width=True)

# Productos
with tab_productos:
    st.subheader("Ranking de productos")

    criterio_ranking = st.selectbox(
        "Ordenar ranking por",
        options=["unidades_vendidas", "ingresos", "beneficio", "rotacion"],
        index=1,
    )

    top_n = st.slider(
        "Número de productos a mostrar", min_value=5, max_value=20, value=10
    )

    df_rank = df.sort_values(criterio_ranking, ascending=False).head(top_n)
    st.dataframe(
        df_rank[
            ["producto", "categoria", "unidades_vendidas",
             "ingresos", "beneficio", "rotacion"]
        ],
        use_container_width=True,
    )

# Categorías
with tab_categorias:
    st.subheader("Análisis por categoría")

    agrupado_cat = df.groupby("categoria").agg(
        ingresos_total=("ingresos", "sum"),
        beneficio_total=("beneficio", "sum"),
        unidades_total=("unidades_vendidas", "sum"),
        rotacion_media=("rotacion", "mean"),
    )
    st.dataframe(agrupado_cat, use_container_width=True)

# Gráficos
with tab_graficos:
    st.subheader("Dashboard gráfico")

    agrupado_graf = df.groupby("categoria").agg(
        ingresos_total=("ingresos", "sum"),
        beneficio_total=("beneficio", "sum"),
        unidades_total=("unidades_vendidas", "sum"),
    )

    st.markdown("#### Gráfico de barras por categoría")
    variable_barras = st.selectbox(
        "Métrica",
        options=["ingresos_total", "beneficio_total", "unidades_total"],
        index=0,
    )
    st.bar_chart(agrupado_graf[variable_barras])

    st.markdown("---")
    st.markdown("#### Gráfico de productos")

    variable_productos = st.selectbox(
        "Métrica para productos",
        options=["unidades_vendidas", "ingresos", "beneficio", "rotacion"],
        index=1,
    )

    top_n_prod = st.slider(
        "Número de productos en el gráfico", min_value=5, max_value=20, value=10
    )

    df_top_prod = df.sort_values(variable_productos, ascending=False).head(top_n_prod)
    df_top_prod_plot = df_top_prod.set_index("producto")
    st.bar_chart(df_top_prod_plot[variable_productos])

# Comentario final
st.markdown("---")
st.subheader("Comentario automático del negocio")

agrupado_final = df.groupby("categoria").agg(
    ingresos_total=("ingresos", "sum"),
    beneficio_total=("beneficio", "sum"),
)
categoria_top_ingresos = agrupado_final["ingresos_total"].idxmax()
categoria_top_beneficio = agrupado_final["beneficio_total"].idxmax()

st.write(
    f"El estanco genera unos ingresos totales aproximados de "
    f"{ingresos_totales:,.2f} €, con un beneficio estimado de "
    f"{beneficio_total:,.2f} €."
)
st.write(
    f"La categoría con mayor peso en ingresos es **{categoria_top_ingresos}**, "
    f"mientras que la que más contribuye al beneficio es "
    f"**{categoria_top_beneficio}**."
)
st.write(
    "La rotación media indica cuántas veces se renueva el stock en el periodo; "
    "una rotación alta sugiere productos de venta rápida y una rotación baja "
    "apunta a artículos que permanecen más tiempo en estantería."
)
st.write(
    "Con esta información se pueden identificar oportunidades para potenciar "
    "referencias de alta rentabilidad, reducir productos de baja rotación y "
    "optimizar la mezcla de complementos para aumentar el margen global."
)
