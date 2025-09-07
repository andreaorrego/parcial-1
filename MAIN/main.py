import pandas as pd
from API import api
from UI import ui

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)

def main():
    df = api.cargar_datos()

    while True:
        print("\nRESULTADO LABORATORIO DE SUELOS")

        departamento = ui.pedir_departamento()
        resultado = (api.filtrar_departamento(df, departamento))

        municipios = api.municipios_por_departamento(df, departamento)

        if municipios:
            print("\nMunicipios disponibles en este departamento:\n")
            print(municipios)

        else:
            print ("\nNO HAY MUNICIPIOS EN EL DEPARTAMENTO")
            return main()

        municipio = ui.pedir_municipio()
        resultado = (api.filtrar_municipio(df, municipio))

        cultivos = api.cultivos_por_municipio(df, departamento, municipio)

        if cultivos:
            print("\nCultivos disponibles en este municipio:\n")
            print(cultivos)

        else:
            print ("\nNO HAY CULTIVOS EN EL MUNICIPIO")
            return main()

        cultivo = ui.pedir_cultivo()
        cantidad = ui.pedir_cantidad()

        resultado.columns = [col.lower().strip() for col in resultado.columns]

        resultado = api.filtrar_datos(df, departamento, municipio, cultivo, cantidad)
        resultado_limitado = resultado.head(cantidad)
        
        print("\n")

        if "risaralda" in resultado["Departamento"].str.lower().values:
            ui.resultados_risaralda(resultado_limitado)
        else:
            ui.mostrar_resultados(resultado_limitado)
            
        print("\n")
        break

if __name__ == "__main__":
    main()