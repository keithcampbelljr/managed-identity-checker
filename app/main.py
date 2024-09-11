import argparse
from app.auth import get_default_credential, get_service_principal_credential
from app.role_assignments import get_role_assignments
from azure.mgmt.msi import ManagedServiceIdentityClient

def get_principal_id(credential, subscription_id, managed_identity_name):
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
    
    # Optional
    parser.add_argument('--client-id', help="Service Principal Client ID (optional).")
    parser.add_argument('--client-secret', help="Service Principal Client Secret (optional).")
    parser.add_argument('--tenant-id', help="Service Principal Tenant ID (optional).")

    args = parser.parse_args()

    if args.client_id and args.client_secret and args.tenant_id:
        credential = get_service_principal_credential(args.client_id, args.client_secret, args.tenant_id)
        print("Using Service Principal credentials.")
    else:
        credential = get_default_credential()
        print("Using Default Azure credentials.")

    principal_id = get_principal_id(credential, args.subscription_id, args.managed_identity_name)

    role_assignments = get_role_assignments(credential, args.subscription_id, principal_id)
    
    for role_assignment in role_assignments:
        print(f"Role Assignment ID: {role_assignment.id}")
        print(f"Principal ID: {role_assignment.principal_id}")
        print(f"Role Definition ID: {role_assignment.role_definition_id}")
        print(f"Scope: {role_assignment.scope}")
        print("-" * 30)

if __name__ == "__main__":
    main()
