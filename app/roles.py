from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.models import RoleAssignment
from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential
from typing import Iterable
from azure.mgmt.msi import ManagedServiceIdentityClient

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

def list_managed_identities(msi_client: ManagedServiceIdentityClient, 
                            managed_identity_name: str):
    try:
        identities = msi_client.user_assigned_identities.list_by_subscription()

        target_identity = None
        for identity in identities:
            if identity.name == managed_identity_name:
                target_identity = identity
                break

        if target_identity:
            print(f"Found Managed Identity '{managed_identity_name}' with Principal ID: {target_identity.principal_id}")
            return target_identity.principal_id
        else:
            print(f"Managed Identity '{managed_identity_name}' not found in the subscription.")
            return None
    except AzureError as e:
        print(f"Failed to list Managed Identities: {str(e)}")
        raise

def list_role_assignments(authorization_client: AuthorizationManagementClient, 
                          subscription_id: str, 
                          mi_object_id: str) -> Iterable[RoleAssignment]:
    try:
        role_assignments = authorization_client.role_assignments.list_for_scope(
            scope=f'/subscriptions/{subscription_id}/',
            filter=f"principalId eq '{mi_object_id}'"
        )
        return role_assignments
    except AzureError as e:
        print(f"Failed to retrieve role assignments: {str(e)}")
        raise
