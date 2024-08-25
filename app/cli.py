import click
from azure.identity import DefaultAzureCredential
from .roles import get_authorization_client, list_role_assignments, list_managed_identities, get_msi_client
from .display import display_permissions
from .auth import authenticate

@click.command()
@click.option('--subscription-id', prompt='Subscription ID', help='Azure subscription ID')
@click.option('--name', prompt='Managed Identity Name', help='Managed Identity Name')
def main(subscription_id, managed_identity_name):
    credential = authenticate()
    msi_client = get_msi_client(credential, subscription_id)
    
    managed_identity_object_id = list_managed_identities(msi_client, managed_identity_name)
    
    if managed_identity_object_id:
        client = get_authorization_client(credential, subscription_id)
        
        role_assignments = list_role_assignments(client, subscription_id, managed_identity_object_id)
        
        display_permissions(role_assignments, client)
    else:
        print(f"Managed Identity '{managed_identity_name}' not found.")

if __name__ == '__main__':
    main()
