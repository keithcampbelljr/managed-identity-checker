from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.models import RoleAssignment
from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential
from typing import Iterable

def get_authorization_client(credential: DefaultAzureCredential, 
                             subscription_id: str) -> AuthorizationManagementClient:
    try:
        authorization_client = AuthorizationManagementClient(credential, subscription_id)
        return authorization_client
    except AzureError as e:
        print(f"Failed to create Authorization Management client: {str(e)}")
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
