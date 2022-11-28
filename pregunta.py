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
    #
    #Lectura
    with open('clusters_report.txt','r') as files:
        datico=[line for line in files]
    body=datico[4:] #Eliminando filas 'innecesarias'
    
    body='\n'.join(body).replace('                                         ','').split('\n\n\n\n')  
    #Patrón identificado, clusters como registros (elementos de lista), (espacio del replace troll...)
    
    c1=[]
    c2=[]
    c3=[]
    c4=[]

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
          c1.append(int(clus))
          c2.append(int(qua))
          c3.append(float(perc.replace(',','.')))
          mwk=i[40:].strip()
          if mwk[-1]=='.':                                                              #Ayuda a quitar ese punto molesto del texto del último cluster...
            c4.append(mwk[:-1].replace('/s*',' '))
          else:
            c4.append(mwk.replace('/s*',' '))
        
    df=pd.DataFrame({'cluster':c1,'cantidad_de_palabras_clave':c2, 'porcentaje_de_palabras_clave':c3,'principales_palabras_clave':c4})    #'Hack' #2
    
    return df
