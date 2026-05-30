from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read from .env
STORAGE_ACCOUNT = os.getenv("STORAGE_ACCOUNT")
STORAGE_KEY     = os.getenv("STORAGE_KEY")
CONTAINER_NAME  = os.getenv("CONTAINER_NAME")

FILES = {
    "raw/train_transaction.csv" : r"C:\Users\Admin\OneDrive\Desktop\Fraud_detection\Dataset\train_transaction.csv\train_transaction.csv",
    "raw/train_identity.csv"    : r"C:\Users\Admin\OneDrive\Desktop\Fraud_detection\Dataset\train_identity.csv\train_identity.csv",
}

# Connect
connection_string = (
    "DefaultEndpointsProtocol=https;"
    "AccountName=" + STORAGE_ACCOUNT + ";"
    "AccountKey="  + STORAGE_KEY     + ";"
    "EndpointSuffix=core.windows.net"
)

print(type(connection_string))
print(connection_string[:60])

# Connect to Blob
client           = BlobServiceClient.from_connection_string(connection_string)
container_client = client.get_container_client(CONTAINER_NAME)

# Upload Files
for blob_name, local_path in FILES.items():

    if not os.path.exists(local_path):
        print(f"❌ File not found : {local_path}")
        continue

    file_size = os.path.getsize(local_path) / (1024 * 1024)
    print(f"Uploading {os.path.basename(local_path)} ({file_size:.1f} MB) ...")

    with open(local_path, "rb") as f:
        container_client.upload_blob(
            name            = blob_name,
            data            = f,
            overwrite       = True,
            max_concurrency = 4
        )

    print(f"✅ Uploaded successfully -> {CONTAINER_NAME}/{blob_name}")

# Verify
print("\nFiles in raw-data/raw/:")
for blob in container_client.list_blobs(name_starts_with="raw/"):
    size_mb = blob.size / (1024 * 1024)
    print(f"  {blob.name:<40} {size_mb:.1f} MB")

print("\n✅ Done.")