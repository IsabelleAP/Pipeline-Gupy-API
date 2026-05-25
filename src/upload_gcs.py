from dotenv import load_dotenv
from storage import upload_to_gcs

load_dotenv()

bucket_name = "desafio-dados-isabelle"
source_file_name = "../dados/processed/dados_total_limpo.parquet"
destination_blob_name = "processed/dados_total_limpo.parquet"

upload_to_gcs(
    bucket_name,
    source_file_name,
    destination_blob_name
)