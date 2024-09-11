from azure.identity import DefaultAzureCredential, ClientSecretCredential

def get_default_credential():
    return DefaultAzureCredential()

def get_service_principal_credential(client_id, client_secret, tenant_id):
    return ClientSecretCredential(
        client_id=client_id,
        client_secret=client_secret,
        tenant_id=tenant_id
    )
