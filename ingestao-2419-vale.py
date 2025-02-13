import os
from azure.storage.blob import BlobServiceClient
import credenciais

def upload_to_blob(account_name, account_key, container_name, local_file_path, blob_name):
    """
    Faz o upload de um arquivo para o Azure Blob Storage.

    :param account_name: Nome da conta do Azure Storage.
    :param account_key: Chave de acesso da conta do Azure Storage.
    :param container_name: Nome do container no Blob Storage.
    :param local_file_path: Caminho local do arquivo a ser enviado.
    :param blob_name: Nome do arquivo no Blob Storage.
    """
    try:
        # Conexão com o Blob Storage
        connect_str = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Upload do arquivo
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data=data, overwrite=True)

        print(f"Arquivo '{blob_name}' enviado com sucesso para o container '{container_name}'.")

    except Exception as e:
        print(f"Erro ao enviar o arquivo '{blob_name}': {e}")

# Exemplo de uso
def main():
    account_name = credenciais.account_name
    account_key = credenciais.account_key_2
    container_name = 'vale-2419'

    arquivos = [
        {"local_path": r"T:\\13.Planejamento\\01. LD e CR\\2417 - VALE\\01. LISTA DE DOCUMENTOS\\03. DETALHADO\\LD-R7282-00-F4-GG_RPEOTTA_ADP 13020_Macro LD_DETALHADO.xlsm", 
         "blob_name": "LD-R7282-00-F4-GG_RPEOTTA_ADP_13020_Macro_LD_DETALHADO.xlsm"},
        {"local_path": r"T:\\13.Planejamento\\01. LD e CR\\2419 - VALE\\01. LISTA DE DOCUMENTOS\\01. CONCEITUAL\\R7186-00-F2-GG_RPEOTTA_ADP 13390_Conceitual.xlsm", 
         "blob_name": "R7186-00-F2-GG_RPEOTTA_ADP_13390_Conceitual.xlsm"},
        {"local_path": r"T:\\13.Planejamento\\01. LD e CR\\2419 - VALE\\01. LISTA DE DOCUMENTOS\\03. DETALHADO\\R7186-00-F4-GG_RPEOTTA_ADP 13390_Detalhado.xlsm", 
         "blob_name": "R7186-00-F4-GG_RPEOTTA_ADP_13390_Detalhado.xlsm"},
        {"local_path": r"T:\\13.Planejamento\\01. LD e CR\\2419 - VALE\\02. CRONOGRAMA\\CS-2419-GR-PLN-GER=001.xlsx", 
         "blob_name": "CS-2419-GR-PLN-GER=001.xlsx"},
        {"local_path": r"T:\\13.Planejamento\\03. PLN_Operacional\\01 - PLANEJAMENTO E CONTROLE\\COORDENACAO\\CONTROLES (POWER BI)\\240124\\VALE\\faturamento_2419.xlsx", 
         "blob_name": "faturamento_2419.xlsx"},
    ]

    for arquivo in arquivos:
        upload_to_blob(
            account_name,
            account_key,
            container_name,
            arquivo["local_path"],
            arquivo["blob_name"]
        )

if __name__ == "__main__":
    main()
