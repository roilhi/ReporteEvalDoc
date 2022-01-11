import matplotlib.pyplot as plt
import numpy as np

def graficar_Promedio_docentes(DF,idx,figname):
    Ydata = list(DF.iloc[idx,:])[1:]
    Xdata = DF.columns.values.tolist()[1:]
    colors = plt.cm.Reds(np.linspace(0.35,0.65))
    plt.barh(Xdata, Ydata, color=colors)
    plt.title(DF.iloc[idx,:][0])
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(figname)

def extrae_IndiceMinimo(DF,idx):
    min_value = min(list(DF.iloc[idx,:][1:]))
    min_idx = list(DF.iloc[idx,:][1:]).index(min_value)
    valPregunta = 'Pregunta ' + str(min_idx+1)
    return valPregunta

def extrae_ValorMinimo(DF,idx):
    return str(min(list(DF.iloc[idx,:][1:])))

def extrae_ValorMaximo(DF,idx):
    return str(max(list(DF.iloc[idx,:][1:])))

def extrae_IndiceMaximo(DF,idx):
    max_value = max(list(DF.iloc[idx,:][1:]))
    max_idx = list(DF.iloc[idx,:][1:]).index(max_value)
    valPregunta = 'Pregunta ' + str(max_idx+1)
    return valPregunta

def NombreDocente(DF,idx):
    return DF.iloc[idx,:][0]







