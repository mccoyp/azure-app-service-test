from azure.identity import ManagedIdentityCredential
from azure.keyvault.administration import KeyVaultBackupClient
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
   print("Request for index page received")
   container = "https://mcpatinostorage.blob.core.windows.net/backup"
   credential = ManagedIdentityCredential()
   client = KeyVaultBackupClient("https://mcpatinokvhsm.managedhsm.azure.net", credential)
   backup_poller = client.begin_backup(container, use_managed_identity=True)
   return backup_poller.result()


if __name__ == "__main__":
   app.run()
