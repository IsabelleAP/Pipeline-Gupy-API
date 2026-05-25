import json
from pathlib import Path
from typing import List, Dict, Any

def save_json(data: List[Dict[str,Any]],path:str) -> None:
    Path("../dados/raw").mkdir(parents=True, exist_ok = True) # criar diretório

    with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            # ensure_ascii= False preserva os acentos


from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
      client = storage.Client()
      bucket = client.bucket(bucket_name)
      blob = bucket.blob(destination_blob_name)
      blob.upload_from_filename(source_file_name)
      print("Upload concluído")