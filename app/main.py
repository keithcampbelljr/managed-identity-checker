import argparse
from auth import get_default_credential
from role_assignments import get_role_assignments
from azure.mgmt.msi import ManagedServiceIdentityClient

def get_principal_id(credential, subscription_id, managed_identity_name):
    """Retrieve the principal (object) ID of the user-assigned managed identity by name."""
    msi_client = ManagedServiceIdentityClient(credential, subscription_id)
    identities = msi_client.user_assigned_identities.list_by_subscription()

    for identity in identities:
        if identity.name == managed_identity_name:
            return identity.principal_id
    raise ValueError(f"Managed identity '{managed_identity_name}' not found.")

def main():
    parser = argparse.ArgumentParser(description="Retrieve Azure role assignments for a managed identity.")
    parser.add_argument('--subscription-id', required=True, help="Azure subscription ID.")
    parser.add_argument('--managed-identity-name', required=True, help="The name of the managed identity.")
    
    args = parser.parse_args()

    # Get credentials and subscription
    credential = get_default_credential()

    # Fetch the principal ID using the managed identity name
    principal_id = get_principal_id(credential, args.subscription_id, args.managed_identity_name)

    # Get the role assignments for the given managed identity
    role_assignments = get_role_assignments(credential, args.subscription_id, principal_id)
    
    # Display the role assignments
    for role_assignment in role_assignments:
        print(f"Role Assignment ID: {role_assignment.id}")
        print(f"Principal ID: {role_assignment.principal_id}")
        print(f"Role Definition ID: {role_assignment.role_definition_id}")
        print(f"Scope: {role_assignment.scope}")
        print("-" * 30)

if __name__ == "__main__":
    main()
