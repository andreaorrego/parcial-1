import pandas as pd

def limpiar_texto(serie: pd.Series) -> pd.Series:
    return (serie.astype(str).str.strip().str.lower().str.replace("á", "a", regex=False)
            .str.replace("é", "e", regex=False).str.replace("í", "i", regex=False)
            .str.replace("ó", "o", regex=False).str.replace("ú", "u", regex=False)
            .str.replace("ñ", "n", regex=False))

def cargar_datos():
    df = pd.read_csv("DATOS/resultado_laboratorio_suelo.csv")

    renombrar = {
        'Fósforo (P) Bray II mg/kg': 'Fósforo (P)',
        'Aluminio (Al) intercambiable cmol(+)/kg': 'Aluminio (Al)',
        'Calcio (Ca) intercambiable cmol(+)/kg': 'Calcio (Ca)',
        'Potasio (K) intercambiable cmol(+)/kg': 'Potasio (K)',
        'Sodio (Na) intercambiable cmol(+)/kg': 'Sodio (Na)',
        'Zinc (Zn) disponible Olsen mg/kg': 'Zinc (Zn)',
        'pH agua:suelo 2,5:1,0': 'pH'
    }

    df_limpio = df.copy()
    df_limpio = df_limpio.rename(columns = renombrar)
    df_limpio = df_limpio.drop(columns=["numfila", "FechaAnalisis", "Secuencial"])
    df_limpio.columns = df_limpio.columns.str.strip()
    
    for columna in ["Departamento", "Municipio", "Cultivo", "Topografia"]:
        if columna in df_limpio.columns:
            df_limpio[columna] = limpiar_texto(df_limpio[columna])

    return df_limpio

def configurar_display():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)

def municipios_por_departamento(df_limpio, departamento):
    filtrado = df_limpio[(df_limpio["Departamento"].str.lower().str.strip() == departamento.lower().strip())]
    return sorted(filtrado["Municipio"].str.lower().str.strip().unique())

def cultivos_por_municipio(df_limpio, departamento, municipio):
    filtrado = df_limpio[
        (df_limpio["Departamento"].str.lower().str.strip() == departamento.lower().strip()) &
        (df_limpio["Municipio"].str.lower().str.strip() == municipio.lower().strip())]
    return sorted(filtrado["Cultivo"].str.lower().str.strip().unique())

def filtrar_datos(df_limpio, departamento, municipio, cultivo, cantidad):
    filtrado = df_limpio[
        (df_limpio["Departamento"] == departamento.lower().strip()) &
        (df_limpio["Municipio"] == municipio.lower().strip()) &
        (df_limpio["Cultivo"] == cultivo.lower().strip())]

    filtrado = filtrado.reset_index(drop = True)
    filtrado.index = filtrado.index + 1 

    if cantidad is not None:
        return filtrado.head(cantidad)
    return filtrado

def mediana (df_limpio, edafico):
    try:
        df_limpio[edafico] = pd.to_numeric(df_limpio[edafico])
    except:
        df_limpio[edafico] = (df_limpio[edafico].astype(str).str.replace("<", "", regex = False)
                              .str.replace(".", "", regex = False).str.replace(",", ".", regex = False))
        df_limpio[edafico] = pd.to_numeric(df_limpio[edafico], errors = "coerce")
    mediana_ediafico = df_limpio[edafico].median()
    return mediana_ediafico