import os
from azure.storage.blob import BlobServiceClient

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
    account_name = 'rpeottaprojeto'
    account_key = 'GLJV/1J7lqLIVVGweRDvnfW6bVvoiUt201Bin1dfnzXcmdKNyX23dRpPYwgFzqDIYSyzoL+rTtAt+AStv/uDow=='
    container_name = 'irm-2232'

    arquivos = [
        {"local_path": r"T:\\13.Planejamento\\01. LD e CR\\2232 - IRM\\01. LISTA DE DOCUMENTOS\\LD-2232-GR-PLN-GRC-001_R25.xlsm", 
         "blob_name": "LD-2232-GR-PLN-GRC-001_R25.xlsm"},
        {"local_path": r"T:\\13.Planejamento\\01. LD e CR\\2232 - IRM\\02. CRONOGRAMA\\CS-2232-GR-PLN-GRC-002_R1.xlsx", 
         "blob_name": "CS-2232-GR-PLN-GRC-002_R1.xlsx"},
        {"local_path": r"T:\\13.Planejamento\\03. PLN_Operacional\\01 - PLANEJAMENTO E CONTROLE\\COORDENACAO\\CONTROLES (POWER BI)\\240124\\IRM\\IRM 2022 a 2024_FaturamXCustos.xlsx", 
         "blob_name": "IRM_2022_a_2024_FaturamXCustos.xlsx"},
        {"local_path": r"T:\\13.Planejamento\\03. PLN_Operacional\\01 - PLANEJAMENTO E CONTROLE\\COORDENACAO\\CONTROLES (POWER BI)\\240124\\Receita 23-24\\PLN MASTER 2023\\PLN MASTER  FATURAMENTO ANUAL 23 R12B (003).xlsx", 
         "blob_name": "PLN_MASTER_FATURAMENTO_ANUAL_23_R12B_(003).xlsx"},
        {"local_path": r"T:\\13.Planejamento\\03. PLN_Operacional\\01 - PLANEJAMENTO E CONTROLE\\COORDENACAO\\CONTROLES (POWER BI)\\240124\\Receita 23-24\\PNL MASTER _TELMO_2024\\PLN MASTER  FATURAMENTO ANUAL 24_R4.xlsx", 
         "blob_name": "PLN_MASTER_FATURAMENTO_ANUAL_24_R4.xlsx"},
        {"local_path": r"T:\\13.Planejamento\\03. PLN_Operacional\\01 - PLANEJAMENTO E CONTROLE\\COORDENACAO\\CONTROLES (POWER BI)\\240124\\DIM_PARA\\tabela_Para.xlsx",
         "blob_name": "tabela_Para.xlsx"},
        
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
