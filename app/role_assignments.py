from azure.mgmt.authorization import AuthorizationManagementClient

def get_role_assignments(credential, subscription_id, principal_id):
    """Retrieve the role assignments for a given principal (managed identity) in a subscription."""
    authorization_client = AuthorizationManagementClient(credential, subscription_id)
    
    role_assignments = authorization_client.role_assignments.list_for_scope(
        scope=f"/subscriptions/{subscription_id}",
        filter=f"principalId eq '{principal_id}'"
    )
    
    return role_assignments
