import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# Crear datos ficticios de felicidad basados en población y temperatura
datos_ciudades_felicidad = pd.DataFrame({
    'Ciudad': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Beijing', 'Estambul', 'Karachi', 'Dhaka', 'Ciudad de Mexico'],
    'Poblacion': [37797531, 29399141, 26317104, 21192735, 20876485, 19416096, 15029231, 14910352, 14799100, 12619078],
    'Anio': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Felicidad': [110, 113, 115, 27, 20, 42, 46, 136, 133, 43]
})

# Extender la lista de años y felicidad para los años ficticios
for i in range(2015, 2020):
    datos_ciudades_felicidad = pd.concat([datos_ciudades_felicidad, pd.DataFrame({
        'Ciudad': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Beijing', 'Estambul', 'Karachi', 'Dhaka', 'Ciudad de Mexico'],
        'Poblacion': [37797531, 29399141, 26317104, 21192735, 20876485, 19416096, 15029231, 14910352, 14799100, 12619078],
        'Anio': [i] * 10,
        'Felicidad': [np.random.randint(20, 150) for _ in range(10)]
    })])

for i in range(2020, 2026):
    datos_ciudades_felicidad = pd.concat([datos_ciudades_felicidad, pd.DataFrame({
        'Ciudad': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Beijing', 'Estambul', 'Karachi', 'Dhaka', 'Ciudad de Mexico'],
        'Poblacion': [37797531, 29399141, 26317104, 21192735, 20876485, 19416096, 15029231, 14910352, 14799100, 12619078],
        'Anio': [i] * 10,
        'Felicidad': [np.random.randint(20, 150) for _ in range(10)]
    })])

# Calcular el promedio de la felicidad total para todas las ciudades a lo largo del tiempo
tendencia_promedio = datos_ciudades_felicidad.groupby('Anio')['Felicidad'].mean()

# Mostrar la línea de tendencia promedio
plt.plot(tendencia_promedio.index, tendencia_promedio.values, label='Tendencia Promedio', linestyle='dashed', marker='x')

# Ajustar límites de los ejes para mejorar la visualización
plt.ylim(bottom=0, top=150)
plt.xlim(left=2015, right=2025)

# Mostrar el gráfico
plt.legend()
plt.xlabel('Año')
plt.ylabel('Felicidad Promedio')
plt.title('Tendencia Promedio de Felicidad para Todas las Ciudades (2015-2025)')
plt.grid(True)
plt.show()
