from azure.mgmt.authorization import AuthorizationManagementClient
from azure.core.exceptions import AzureError
from azure.mgmt.authorization.models import RoleAssignment
from typing import Iterable

def display_permissions(role_assignments: Iterable[RoleAssignment], 
                        authorization_client: AuthorizationManagementClient) -> None:
    
    print("Roles assigned to Managed Identity:")
    for role_assignment in role_assignments:
        try:
            role_definition = authorization_client.role_definitions.get_by_id(role_assignment.role_definition_id)
            print(f"  - {role_definition.role_name} (ID: {role_definition.id})")
        except AzureError as e:
            print(f"Failed to retrieve role definition for {role_assignment.role_definition_id}: {str(e)}")
