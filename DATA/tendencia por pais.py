import pandas as pd
import matplotlib.pyplot as plt

# Utilizar datos de ciudades y poblaciones previamente generados
datos_ciudades = pd.DataFrame({
    'Ciudad': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Beijing', 'Estambul', 'Karachi', 'Dhaka', 'Ciudad de Mexico'],
    'Poblacion': [37797531, 29399141, 26317104, 21192735, 20876485, 19416096, 15029231, 14910352, 14799100, 12619078],
    'Anio': [2019] * 10
})

# Crear datos ficticios de felicidad basados en población y temperatura
datos_felicidad = pd.DataFrame({
    'Ciudad': datos_ciudades['Ciudad'],
    'Felicidad': (datos_ciudades['Poblacion'] / 1000000) * (datos_ciudades['Poblacion'] / 10000000) + (datos_ciudades['Anio'] / 2019) * 10
})

# Fusionar datos de población con datos de felicidad
datos_ciudades_felicidad = pd.merge(datos_ciudades, datos_felicidad, on='Ciudad')

# Mostrar datos generados
print("Datos Generados:")
print(datos_ciudades_felicidad)

# Realizar análisis de ciudades para identificar las más felices
def realizar_analisis_felicidad(datos):
    # Ordenar ciudades por felicidad de mayor a menor
    ciudades_felices = datos.sort_values(by='Felicidad', ascending=False).head(5)

    # Visualización de resultados
    plt.bar(ciudades_felices['Ciudad'], ciudades_felices['Felicidad'])
    plt.xlabel('Ciudad')
    plt.ylabel('Nivel de Felicidad')
    plt.title('Ciudades Más Felices del Mundo (2019)')
    plt.show()

# Realizar análisis de felicidad
realizar_analisis_felicidad(datos_ciudades_felicidad)
