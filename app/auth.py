from azure.identity import DefaultAzureCredential
from azure.core.exceptions import AzureError

def authenticate() -> DefaultAzureCredential:
    try:
        credential = DefaultAzureCredential()
        return credential
    except AzureError as e:
        print(f"Failed to authenticate using the default credential chain: {str(e)}")
        raise
