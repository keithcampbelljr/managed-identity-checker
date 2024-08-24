import click
from .auth import authenticate
from .roles import get_authorization_client, list_role_assignments
from .display import display_permissions

@click.command()
@click.option('--subscription-id', prompt='Subscription ID', help='Azure subscription ID')
@click.option('--managed-identity-object-id', prompt='Managed Identity Object ID', help='Managed Identity Object ID')
def main(subscription_id, managed_identity_object_id):
    credential = authenticate()
    client = get_authorization_client(credential, subscription_id)
    role_assignments = list_role_assignments(client, subscription_id, managed_identity_object_id)
    display_permissions(role_assignments, client)

if __name__ == '__main__':
    main()
