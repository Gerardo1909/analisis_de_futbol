'''
    script hecho para la configuración inicial de los notebooks de los proyectos
'''



def setear_estilo_graficos():
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.style.use('seaborn-darkgrid')  
    sns.set_palette('pastel')  
    plt.rc('font', size=12)  
    plt.rc('axes', titlesize=14, labelsize=12) 
    plt.rc('figure', figsize=(10, 6))  
    
def iniciar_notebook():
    import pandas as pd
    import warnings
    warnings.filterwarnings('ignore')

    pd.set_option('display.max_columns', 50)  # Mostrar más columnas
    pd.set_option('display.float_format', '{:.2f}'.format)  # Formato numérico