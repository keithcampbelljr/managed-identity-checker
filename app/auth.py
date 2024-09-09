from azure.identity import DefaultAzureCredential
from azure.core.exceptions import AzureError
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.msi import ManagedServiceIdentityClient

def authenticate() -> DefaultAzureCredential:
    try:
        credential = DefaultAzureCredential()
        return credential
    except AzureError as e:
        print(f"Failed to authenticate using the default credential chain: {str(e)}")
        raise

def get_authorization_client(credential: DefaultAzureCredential, 
                             subscription_id: str) -> AuthorizationManagementClient:
    try:
        authorization_client = AuthorizationManagementClient(credential, subscription_id)
        return authorization_client
    except AzureError as e:
        print(f"Failed to create Authorization Management client: {str(e)}")
        raise

def get_msi_client(credential: DefaultAzureCredential, 
                   subscription_id: str) -> ManagedServiceIdentityClient:
    try:
        msi_client = ManagedServiceIdentityClient(credential, subscription_id)
        return msi_client
    except AzureError as e:
        print(f"Failed to create Managed Service Identity client: {str(e)}")
        raise