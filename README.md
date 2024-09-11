# Setup
`python -m venv venv`
Activate venv
`pip install -r requirements.txt`
# Run
Default Credential:
`python main.py --subscription-id <your-subscription-id> --identity-name <managed-identity-name>`

Service Principal (Optional):
`python main.py --subscription-id <your-subscription-id> --managed-identity-name <managed-identity-name> --client-id <your-client-id> --client-secret <your-client-secret> --tenant-id <your-tenant-id>`