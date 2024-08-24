from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.models import RoleAssignment
from azure.core.exceptions import AzureError
from typing import Iterable

SUBSCRIPTION_ID = "" #TODO: set this via wrapping with cli
MANAGED_IDENTITY_OBJECT_ID = "" #TODO: set this via wrapping with cli

def authenticate() -> DefaultAzureCredential:

    try:
        credential = DefaultAzureCredential()
        return credential
    except AzureError as e:
        print(f"Failed to authenticate using the default credential chain: {str(e)}")
        raise

def get_authorization_client(credential: str, 
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
    """
    Retrieve and return the role assignments for the Managed Identity.
    """
    try:
        role_assignments = authorization_client.role_assignments.list_for_scope(
            scope=f'/subscriptions/{subscription_id}/',
            filter=f"principalId eq '{mi_object_id}'"
        )
        return role_assignments
    except AzureError as e:
        print(f"Failed to retrieve role assignments: {str(e)}")
        raise

def display_permissions(role_assignments: Iterable[RoleAssignment], 
                        authorization_client: AuthorizationManagementClient) -> None:

    print("Roles assigned to Managed Identity:")
    for role_assignment in role_assignments:
        try:
            role_definition = authorization_client.role_definitions.get_by_id(role_assignment.role_definition_id)
            print(f"  - {role_definition.role_name} (ID: {role_definition.id})")
        except AzureError as e:
            print(f"Failed to retrieve role definition for {role_assignment.role_definition_id}: {str(e)}")


def main():
    credential = authenticate()
    client = get_authorization_client(credential, SUBSCRIPTION_ID)
    role_assignments = list_role_assignments(client, SUBSCRIPTION_ID, MANAGED_IDENTITY_OBJECT_ID)
    display_permissions(role_assignments, client)




if __name__ == "__main__":
    main()
