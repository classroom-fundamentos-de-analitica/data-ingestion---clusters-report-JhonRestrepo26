"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    
    #Lectura
    with open('/tmp/clusters_report.txt','r') as files:
        datico=[line for line in files]
    body=datico[4:] #Eliminando filas 'innecesarias'
    
    body='\n'.join(body).split('\n\n\n\n')  #Patrón identificado, clusters como registros (elementos de lista)
    
    dic={'cluster':[],'cantidad_de_palabras_clave':[], 'porcentaje_de_palabras_clave':[],'principales_palabras_clave':[]} #Simplificación nombres de col

    #'Hack':
    
    for i in body:
      clus=''
      qua=''
      perc=''
      for j in range(4):
        if i[j+3] != ' ':
          clus+=i[j+3]
        if i[j+9] != ' ':
          qua+=i[j+9]
        if i[j+25] != ' ':
          perc+=i[j+25]  
        if j==3:
          dic['cluster'].append(int(clus))
          dic['cantidad_de_palabras_clave'].append(int(qua))
          dic['porcentaje_de_palabras_clave'].append(float(perc.replace(',','.')))
          dic['principales_palabras_clave'].append(i[40:])
    
    df=pd.DataFrame(dic)    #'Hack' #2
    
    return df
