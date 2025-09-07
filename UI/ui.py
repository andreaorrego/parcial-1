from API import api

def pedir_departamento():
    return input("\nIngrese el departamento: ")
        
def pedir_municipio():
    return input("\nIngrese el municipio: ")
        
def pedir_cultivo():
    return input("\nIngrese el cultivo: ")
    
def pedir_cantidad():
    return int(input("\nIngrese la cantidad de registros a revisar: "))

def mediana (resultado):
    print("\nMedianas", "pH: %.2f" %api.mediana(resultado, 'pH'), 
            "Fosforo (mg/kg): %.2f" %api.mediana(resultado, "Fósforo (P)"), 
            "Potasio (cmol(+)/kg): %d" %api.mediana(resultado, "Potasio (K)"), sep="\n")
    
def mostrar_resultados(resultado):
    if resultado.empty:
        print("No se encontraron resultados.")
    else:
        print(resultado[['Departamento', 'Municipio', 'Cultivo', 'Topografia']]) 
        mediana(resultado)

titulos = ['Departamento', 'Municipio', 'Cultivo', 'Topografia', 'pH', 'Fósforo (P)', 'Aluminio (Al)', 'Calcio (Ca)',
           'Potasio (K)', 'Sodio (Na)', 'Zinc (Zn)']

def resultados_risaralda(resultado):
    if resultado.empty:
        print("No se encontraron resultados.")
    else:
        print(resultado[titulos])
        mediana(resultado)

                 