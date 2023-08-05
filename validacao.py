import pandas as pd
import cx_Oracle
import re

excel =  pd.read_excel(r"C:\Users\Otavio.cunha\OneDrive - RECH IMPORTADORA E DISTRIBUIDORA S A\Área de Trabalho\metas - Arcano\METAS_ESPECIALISTA.xlsx")

excel["COD_FILIAL"] = excel["COD_FILIAL"].apply(lambda x: str(x).zfill(8))

filial_excel = (excel["COD_FILIAL"])
unidade_excel = (excel["Filial"])
perfil_cliente = (excel["Perfil Cliente"])
estado = (excel["UF Filial"])



try:
    lib_dir=r"C:\instantclient_21_8"
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    print("Whoops!")
    print(err)
    
# Establish the database connection
connection = cx_Oracle.connect(user="RECHQLIK", password='r3chql1k',
                               dsn="dbprod.agrocompetence.com:1521/PRD"
                               )

# Obtain a cursor
cursor = connection.cursor()

consulta = cursor.execute("SELECT Z01_FIL, TRIM(Z01_UNID), Z01_EST FROM TOTVSRECH.Z01010")
resultados = consulta.fetchall()



# Feche o cursor após usar os resultados
cursor.close()

# Converta os resultados em uma lista de valores
valores_consulta_filial = [str(resultado[0]) for resultado in resultados]
valores_consulta_unidade = [str(resultado[1]) for resultado in resultados]
consulta_perfil_cliente = ["Empresas Franquias da Rede RSG", "Cliente Comum"]
consulta_estado = [str(resultado[2]) for resultado in resultados]



rount_count = 1 

# Itere pelas linhas do DataFrame
for indice, linha in excel.iterrows():
    filial_excel = str(linha["COD_FILIAL"])
    unidade_excel = str(linha["Filial"])
    perfil_cliente = str(linha["Perfil Cliente"])
    estado = str(linha["UF Filial"])
    margem = float(linha["Margem"])

    rount_count +=1
# Verifique se o valor está presente na consulta
    if filial_excel in valores_consulta_filial:
        print(f"Valor encontrado na consulta: {filial_excel}")
        
        
        
        
    else:
        print(f"Valor não encontrado na consulta: {filial_excel}")
        print(f"erro na linha {rount_count}")

# Verifique se o valor está presente na consulta
    if unidade_excel in valores_consulta_unidade:
        print(f"Valor encontrado na consulta: {unidade_excel}")
    else:
        print(f"Valor não encontrado na consulta: {unidade_excel}")
        print(f"erro na linha {rount_count}")
        
# Verifique se o valor está presente na consulta
    if perfil_cliente in consulta_perfil_cliente:
        print(f"Valor encontrado na consulta: {perfil_cliente}")
    else:
        print(f"Valor não encontrado na consulta: {perfil_cliente}")
        print(f"erro na linha {rount_count}")
        
# Verifique se o valor está presente na consulta
    if estado in consulta_estado:
        print(f"Valor encontrado na consulta: {estado}")
    else:
        print(f"Valor não encontrado na consulta: {estado}")
        print(f"erro na linha {rount_count}")
