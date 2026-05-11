# Utilizo pandas para la manipulacion y analisis de datos estructurados.
import pandas as pd

# Utilizo pyplot de matplotlib para generar visualizaciones y graficos estáticos.
import matplotlib.pyplot as plt

# 1. LECTURA DE DATOS
#Identifico la ruta del csv con los datos del clima mensuales
ruta_archivo = "datos/monthly.csv" 
df = pd.read_csv(ruta_archivo)

# 2. CALCULO DE INDICADORES ESTADÍSTICOS
# Utilizo la columna 'Mean' del csv que trae las temperaturas.
# Utilizo las funciones de pandas para obtener los valores.
temp_promedio = df['Mean'].mean()
temp_max = df['Mean'].max()
temp_min = df['Mean'].min()


# 3. GENERACION DE GRAFICO
# Utilizo figure para crear un lienzo para la figura.
plt.figure(figsize=(10,6))

# Trazo el grafico de lineas con plot.
plt.plot(df['Mean'], color='red')

# Añado título y etiquetas a los ejes para la documentación tecnica.
plt.title('Evolución de la Temperatura Global')
plt.xlabel('Registros Temporales')
plt.ylabel('Anomalía de Temperatura (°C)')

# Exporto el gráfico generado como imagen PNG a la ruta resultados/.
plt.savefig('resultados/grafico_temperatura.png')
print("Análisis finalizado. Gráfico guardado en la carpeta 'resultados'.")
