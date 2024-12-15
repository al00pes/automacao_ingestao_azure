import io
import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobBlock, BlobClient, StandardBlobTier
import pandas as pd

#Instanciando os locais do arquivo

LD = r"T:\13.Planejamento\01. LD e CR\2440 - SUBSEA\01. LISTA DE DOCUMENTOS\LD-2440-PE-ACA-PLN-GER-001-R0.xlsx"
CRONOGRAMA = r"T:\13.Planejamento\01. LD e CR\2440 - SUBSEA\02. CRONOGRAMA\CS-2440-PE-ACA-PLN-GER-001.xlsx"
blob_name_LD = "LD-2440-PE-ACA-PLN-GER-001-R0.xlsx"
blob_name_CR = "CS-2440-PE-ACA-PLN-GER-001.xlsx"


# Credencias da Azure

account_name = 'rpeottaprojeto'
account_key = 'GLJV/1J7lqLIVVGweRDvnfW6bVvoiUt201Bin1dfnzXcmdKNyX23dRpPYwgFzqDIYSyzoL+rTtAt+AStv/uDow=='
container_name = 'subsea-2440'

#criando interface cliente com o o blob storage
connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

#Utilizando o client para conectar ao container
container_client = blob_service_client.get_container_client(container_name)

#deletando arquivo no blob storage

'''blob_client = blob_service_client.get_blob_client(container=container_name, blob='test.txt')
blob_client.delete_blob()'''

#Enviando arquivo para blob storage - LD

content=b"test"
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name_LD)

try:
    #Carregando o arquivo no Blob
    with open(LD,"rb") as data:      
        blob_client.upload_blob(data=data, overwrite=True) #Substitui se ja existir

    print(f"Arquivo '{blob_name_LD} enviado com sucesso para o container '{container_name}")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")

# Enviando o Cronograma para o blob Storage

content=b"test_2"
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name_CR)

try:
    #Carregando o arquivo no Blob
    with open(CRONOGRAMA,"rb") as data:      
        blob_client.upload_blob(data=data, overwrite=True) #Substitui se ja existir

    print(f"Arquivo '{blob_name_CR} enviado com sucesso para o container '{container_name}")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")




'''print(f"File {file} uploaded to blob {blob_client.blob_name} in container {blob_client.container_name}")

#Listando os arquivo dentro do blob storage
blob_list = []
for blob_i in container_client.list_blobs():
    blob_list.append(blob_i.name)
    
print(blob_list)    
'''
