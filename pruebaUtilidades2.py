from Utilidades import *
from CargaDatos import carga_dataframe

idx = 8

nameFig = 'test' + str(idx) + '.png'
DF = carga_dataframe('promedioPuntuaciones.csv')
DFpunt = carga_dataframe('Num_puntuaciones.csv')

graficar_Promedio_docentes(DF,idx,nameFig)

print(NombreDocente(DF,idx))
print('Valor Máximo obtenido '+ extrae_IndiceMaximo(DF,idx) +' ' + extrae_ValorMaximo(DF,idx))
print('Valor mínimo obtenido ' + extrae_IndiceMinimo(DF,idx) +' '+ extrae_ValorMinimo(DF,idx))



