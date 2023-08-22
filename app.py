from azure.identity import ManagedIdentityCredential
from azure.keyvault.administration import KeyVaultBackupClient
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
   print("Request for index page received")
   container = "https://mcpatinostorage.blob.core.windows.net/backup"
   credential = ManagedIdentityCredential(client_id="66adbee8-0d3d-4c93-955a-16de92b850c6")
   client = KeyVaultBackupClient("https://mcpatinokvhsm.managedhsm.azure.net", credential)
   backup_poller = client.begin_backup(container, use_managed_identity=True)
   return backup_poller.result()


if __name__ == "__main__":
   app.run()
