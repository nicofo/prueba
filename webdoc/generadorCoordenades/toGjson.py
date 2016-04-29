# coding=utf-8
import utm
import pandas as pd
import math

def createJson():

    
    general=[]
    i="3"

    general.append(pd.read_csv("geolocalització bombes - 1937.csv",sep=',',na_values='', encoding='utf8', dtype=object))
    general.append(pd.read_csv("geolocalització bombes - 1938.csv",sep=',', na_values = '', encoding='utf8', dtype=object))
    general.append(pd.read_csv("geolocalització bombes - 1939.csv",sep=',', na_values='', encoding='utf8', dtype=object))
    result = pd.concat(general)
    posarComa=False
    fout= open("bombesTotes.js", 'w')
    fout.write('var bombes = {\n')
    fout.write('  "type": "FeatureCollection",\n')
    fout.write('  "features": [\n')
    for index, info in result.iterrows(): 
        if not '??' in str(info["COORDENADES"]):
            try:
                if posarComa:
                    fout.write(',\n')
                posarComa=True
                fout.write('    {\n')
                fout.write('      "type": "Feature",\n')
                fout.write('      "properties": {\n')
                fout.write('        "avio": "'+str(info["AVIO"])+'",\n')
                if isinstance(info["CARRER"], float):
                    fout.write('        "carrer": "'+str(info["CARRER"]).encode('utf-8')+'",\n')
                else:
                    fout.write('        "carrer": "'+info["CARRER"].rstrip().encode('utf-8')+'",\n')
                fout.write('        "unitat": "'+info["UNITAT"].encode('utf-8')+'",\n')
                #algo = tipus[i][info["Numero dexpedient"]== tipus[i]["Numero dexpedient"]]["Descripcio tipus accident"].iloc(0)
                #fout.write('        "causes": "'+str(algo)+'",\n')
               
                
                fout.write('        "morts": "'+str(info["MORTS"])+'",\n')
                fout.write('        "ferits": "'+str(info["FERITS"])+'",\n')
                fout.write('        "hora": "'+str(info["HORA"])+'",\n')

                fout.write('        "data": "'+ "%02d" % ( int(info["DIA"]), )+"-"+ "%02d" % (int(info["MES"]),)+'-'+str(info["ANY"])+'"\n')
                fout.write('      },\n')
                fout.write('      "geometry": { \n')
                fout.write('        "type":"Point",\n')
                try:
                    tmp=str(info["COORDENADES"]).split(',' )
                    fout.write('        "coordinates":['+tmp[1]+','+tmp[0] +']\n')
                except:
                    print str(info["COORDENADES"])
                
                fout.write('      }\n')
                fout.write('    }')
            except:
                print "aaa"
    fout.write('\n  ]\n')
    fout.write('}\n')
    fout.close()
def algo(x):
    if math.isnan(float(x)):
        print 'ei'
        return str(99)
    if isinstance(x, float):
        return str(int(x))
    return str(int(float(x)))
def algoInt(x):
    if math.isnan(float(x)):
        print 'ei'
        return 99
    return int(x)
def diaA(x):
    
    return '1938317A'
def diaB(x):
    
    return '1938317B'
def createJS():

    mesosAny={'1':'de gener','2': 'de febrer','3': 'de març','4':"d'abril",'5': 'de maig','6': 'de juny','7': 'de juliol','8': "d'agost",'9': 'de setembre','10': "d'octubre",'11': 'de novembre','12': 'de desembre'}
    general=[]
    i="3"

    general.append(pd.read_csv("geolocalització bombes - 1937.csv",sep=',',na_values='', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1938.csv",sep=',', na_values = '', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1939.csv",sep=',', na_values='', encoding='utf8'))
    result = pd.concat(general)
    result["DIA"] = result.DIA.map("{:02}".format)
    result["MES"] = result.MES.map("{:02}".format)
    result["ANY"] = result.ANY.map(algoInt)
    result['data']=result["ANY"].map(algo)+''+result["MES"].map(algo)+''+result["DIA"].map(algo)
    result.sort_values(by='data', ascending=False)
    dates=result.groupby(['data'])['data']
    print dates
    fout= open("bombes.js", 'w')
    fout.write('var bombes = {\n')
    fout.write('  "type": "FeatureCollection",\n')
    fout.write('  "features": [\n')
    for data in dates.groups:
        posarComa=False
        fout.write('var dia'+str(data)+' = {\n')
        fout.write('  "type": "FeatureCollection",\n')
        fout.write('  "features": [\n')
        
        for index, info in result[result['data'] == data].iterrows(): 
            if not '??' in str(info["COORDENADES"]):
                if posarComa:
                    fout.write(',\n')
                posarComa=True
                fout.write('    {\n')
                fout.write('      "type": "Feature",\n')
                fout.write('      "properties": {\n')
                fout.write('        "avio": "'+str(info["AVIO"])+'",\n')
                if isinstance(info["CARRER"], float):
                    fout.write('        "carrer": "'+str(info["CARRER"]).encode('utf-8')+'",\n')
                else:
                    fout.write('        "carrer": "'+info["CARRER"].encode('utf-8')+'",\n')
                fout.write('        "unitat": "'+info["UNITAT"].encode('utf-8')+'",\n')
                #algo = tipus[i][info["Numero dexpedient"]== tipus[i]["Numero dexpedient"]]["Descripcio tipus accident"].iloc(0)
                #fout.write('        "causes": "'+str(algo)+'",\n')
               
                
                fout.write('        "morts": "'+str(info["MORTS_LLIBRE"])+'",\n')
                fout.write('        "ferits": "'+str(info["FERITS"])+'",\n')
                fout.write('        "hora": "'+str(info["HORA"])+'",\n')
                fout.write('        "data": "'+ str(int(info["DIA"]))+" "+ mesosAny(int(info["MES"]))+' del '+str(info["ANY"])+'"\n')
                fout.write('      },\n')
                fout.write('      "geometry": { \n')
                fout.write('        "type":"Point",\n')

                try:
                    tmp=str(info["COORDENADES"]).split(',')

                    fout.write('        "coordinates":['+tmp[1]+','+tmp[0] +']\n')
                except:
                    print info["COORDENADES"]
                fout.write('      }\n')
                fout.write('    }')
    fout.write('\n  ]\n')
    fout.write('};\n')
    fout.close()
def createJSMultiTotal():

    mesosAny={'1':'de Gener','2': 'de Febrer','3': 'de Març','4':"d'Abril",'5': 'de Maig','6': 'de Juny','7': 'de Juliol','8': "d'Agost",'9': 'de Setembre','10': "d'Octubre",'11': 'de Novembre','12': 'de Desembre'}

    general=[]
    i="3"

    general.append(pd.read_csv("geolocalització bombes - 1937.csv",sep=',',na_values='', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1938.csv",sep=',', na_values = '', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1939.csv",sep=',', na_values='', encoding='utf8'))
    result = pd.concat(general)
    result["DIA"] = result.DIA.map("{:02}".format)
    result["MES"] = result.MES.map("{:02}".format)
    result["ANY"] = result.ANY.map(algoInt)
    result['data']=result["ANY"].map(algo)+''+result["MES"].map(algo)+''+result["DIA"].map(algo)
    
    especial1=result[result['data'] == '1938317']
    especial1= especial1[especial1['HORA'] == '07:40']
    especial1['data']=especial1['data'].map(diaA)
    especial2=result[result['data'] == '1938317']
    especial2= especial2[especial2['HORA'] == '13:58']
    especial2['data']=especial2['data'].map(diaB)
    result=pd.concat([result, especial1, especial2])
    result.sort_values(by='data', ascending=False)
    dates=result.groupby(['data'])['data']
    print dates
    fout= open("bombesMultiTotes.js", 'w')
    posarComaEntre=False
    fout.write('var bombes = {\n')
    fout.write('  "type": "FeatureCollection",\n')
    fout.write('  "features": [\n')
    for data in dates.groups:
        
        
        if posarComaEntre:
            fout.write(',\n')
        posarComaEntre=True
        dataInfo=result[result['data'] == data]

        fout.write('    {\n')
        fout.write('      "type": "Feature",\n')
        fout.write('      "properties": {\n')
        fout.write('        "avio": "'+str(dataInfo["AVIO"].iloc[0])+'",\n')
        if isinstance(dataInfo["CARRER"].iloc[0], float):
            fout.write('        "carrer": "'+str(dataInfo["CARRER"].iloc[0]).encode('utf-8')+'",\n')
        else:
            fout.write('        "carrer": "'+dataInfo["CARRER"].iloc[0].encode('utf-8')+'",\n')
        fout.write('        "unitat": "'+dataInfo["UNITAT"].iloc[0].encode('utf-8')+'",\n')
        #algo = tipus[i][dataInfo(0["Numero dexpedient"]== tipus[i]["Numero dexpedient"]]["Descripcio tipus accident"].iloc(0)
        #fout.write('        "causes": "'+str(algo)+'",\n')
       
        try:
        #fout.write('        "causes": "'+str(algo)+'",\n')
            fout.write('        "morts": "'+str(int(float(dataInfo["MORTS_LLIBRE"].iloc[0])))+'",\n')
        except:
            fout.write('        "morts": "'+str(dataInfo["MORTS_LLIBRE"].iloc[0])+'",\n')
        try:
            
            fout.write('        "ferits": "'+str(int(float(dataInfo["FERITS"].iloc[0])))+'",\n')
            fout.write('        "morts_totals": "'+str(int(float(dataInfo["MORTS_TOTALS"].iloc[0])))+'",\n')
        except:
            #fout.write('        "morts": "'+str(dataInfo["MORTS"].iloc[0])+'",\n')
            fout.write('        "ferits": "'+str(dataInfo["FERITS"].iloc[0])+'",\n')
            fout.write('        "morts_totals": "'+str(dataInfo["MORTS_TOTALS"].iloc[0])+'",\n')
        try:
            fout.write('        "hora": "'+str(dataInfo["HORA"].iloc[0])+'",\n')
        except:
            print "hora", dataInfo.iloc[0]
        try:
            fout.write('        "data": "'+str(int(float(dataInfo["DIA"].iloc[0])))+" "+ mesosAny[str(int(float(dataInfo["MES"].iloc[0])))]+' de '+str(dataInfo["ANY"].iloc[0])+'"\n')
        except:
            print "data", dataInfo.iloc[0]
        fout.write('      },\n')
        fout.write('      "geometry": { \n')
        fout.write('        "type":"MultiPoint",\n')
        fout.write('        "coordinates":[')
        posarComa=False
        for index, info in result[result['data'] == data].iterrows(): 
            if not '??' in str(info["COORDENADES"]):
                if posarComa:
                    fout.write(', ')
                posarComa=True
                try:
                    tmp=str(info["COORDENADES"]).split(',' )
                    fout.write('['+tmp[1]+','+tmp[0] +']')
                except:
                    print str(info["COORDENADES"])
                    posarComa=False
        fout.write(']\n      }\n')
        fout.write('    }')            
    fout.write('\n  ]\n')
    fout.write('}')

    fout.close()
def createJSMulti():

    mesosAny={'1':'de Gener','2': 'de Febrer','3': 'de Març','4':"d'Abril",'5': 'de Maig','6': 'de Juny','7': 'de Juliol','8': "d'Agost",'9': 'de Setembre','10': "d'Octubre",'11': 'de Novembre','12': 'de Desembre'}

    general=[]
    i="3"

    general.append(pd.read_csv("geolocalització bombes - 1937.csv",sep=',',na_values='', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1938.csv",sep=',', na_values = '', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1939.csv",sep=',', na_values='', encoding='utf8'))
    result = pd.concat(general)
    result["DIA"] = result.DIA.map("{:02}".format)
    result["MES"] = result.MES.map("{:02}".format)
    result["ANY"] = result.ANY.map(algoInt)
    result['data']=result["ANY"].map(algo)+''+result["MES"].map(algo)+''+result["DIA"].map(algo)
    
    especial1=result[result['data'] == '1938317']
    especial1= especial1[especial1['HORA'] == '07:40']
    especial1['data']=especial1['data'].map(diaA)
    especial2=result[result['data'] == '1938317']
    especial2= especial2[especial2['HORA'] == '13:58']
    especial2['data']=especial2['data'].map(diaB)
    result=pd.concat([result, especial1, especial2])
    result.sort_values(by='data', ascending=False)
    dates=result.groupby(['data'])['data']
    print dates
    fout= open("bombesMulti.js", 'w')
    for data in dates.groups:
        
        posarComa=False
        fout.write('var dia'+str(data)+' = {\n')
        fout.write('  "type": "FeatureCollection",\n')
        fout.write('  "features": [\n')
        dataInfo=result[result['data'] == data]

        fout.write('    {\n')
        fout.write('      "type": "Feature",\n')
        fout.write('      "properties": {\n')
        fout.write('        "avio": "'+str(dataInfo["AVIO"].iloc[0])+'",\n')
        if isinstance(dataInfo["CARRER"].iloc[0], float):
            fout.write('        "carrer": "'+str(dataInfo["CARRER"].iloc[0]).encode('utf-8')+'",\n')
        else:
            fout.write('        "carrer": "'+dataInfo["CARRER"].iloc[0].encode('utf-8')+'",\n')
        fout.write('        "unitat": "'+dataInfo["UNITAT"].iloc[0].encode('utf-8')+'",\n')
        #algo = tipus[i][dataInfo(0["Numero dexpedient"]== tipus[i]["Numero dexpedient"]]["Descripcio tipus accident"].iloc(0)
        try:
        #fout.write('        "causes": "'+str(algo)+'",\n')
            fout.write('        "morts": "'+str(int(float(dataInfo["MORTS_LLIBRE"].iloc[0])))+'",\n')
        except:
            fout.write('        "morts": "'+str(dataInfo["MORTS_LLIBRE"].iloc[0])+'",\n')
        try:
            
            fout.write('        "ferits": "'+str(int(float(dataInfo["FERITS"].iloc[0])))+'",\n')
            fout.write('        "morts_totals": "'+str(int(float(dataInfo["MORTS_TOTALS"].iloc[0])))+'",\n')
        except:
            #fout.write('        "morts": "'+str(dataInfo["MORTS"].iloc[0])+'",\n')
            fout.write('        "ferits": "'+str(dataInfo["FERITS"].iloc[0])+'",\n')
            fout.write('        "morts_totals": "'+str(dataInfo["MORTS_TOTALS"].iloc[0])+'",\n')

        try:
            fout.write('        "hora": "'+str(dataInfo["HORA"].iloc[0])+'",\n')
        except:
            print "hora", dataInfo.iloc[0]
        try:
            fout.write('        "data": "'+str(int(float(dataInfo["DIA"].iloc[0])))+" "+ mesosAny[str(int(float(dataInfo["MES"].iloc[0])))]+' de '+str(dataInfo["ANY"].iloc[0])+'"\n')
        except:
            print "data", dataInfo.iloc[0]
        fout.write('      },\n')
        fout.write('      "geometry": { \n')
        fout.write('        "type":"MultiPoint",\n')
        fout.write('        "coordinates":[')
        for index, info in result[result['data'] == data].iterrows(): 
            if not '??' in str(info["COORDENADES"]):
                if posarComa:
                    fout.write(', ')
                posarComa=True
                try:
                    tmp=str(info["COORDENADES"]).split(',' )
                    fout.write('['+tmp[1]+','+tmp[0] +']')
                except:
                    print str(info["COORDENADES"])
                    posarComa=False
        fout.write(']\n      }\n')
        fout.write('    }')            
        fout.write('\n  ]\n')
        fout.write('};\n')

    fout.close()
#createJson()
createJSMultiTotal()
#createJS()
createJSMulti()