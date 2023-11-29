import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crear datos ficticios de felicidad basados en población y temperatura
datos_felicidad = pd.DataFrame({
    'Ciudad': ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Beijing', 'Estambul', 'Karachi', 'Dhaka', 'Ciudad de Mexico'],
    'Felicidad': (datos_ciudades['Poblacion'] / 1000000) * (datos_ciudades['Poblacion'] / 10000000) + (datos_ciudades['Anio'] / 2019) * 10
})

# Fusionar datos de población con datos de felicidad
datos_ciudades_felicidad = pd.merge(datos_ciudades, datos_felicidad, on='Ciudad')

# Calcular la correlación entre el tamaño de la ciudad y la felicidad
correlacion = datos_ciudades_felicidad['Poblacion'].corr(datos_ciudades_felicidad['Felicidad'])

# Mostrar el resultado de la correlación
print(f"Correlación entre tamaño de la ciudad y felicidad: {correlacion}")

# Crear un gráfico de dispersión para visualizar la relación
sns.scatterplot(data=datos_ciudades_felicidad, x='Poblacion', y='Felicidad', hue='Ciudad', palette='viridis')
plt.xlabel('Población de la Ciudad')
plt.ylabel('Nivel de Felicidad')
plt.title('Relación entre el Tamaño de la Ciudad y la Felicidad')
plt.show()
