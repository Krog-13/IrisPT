from common.config import ADMIN_CREDENTIAL, endpoints


def get_token(client):
    """Obtain an authentication token for the admin user"""
    response = client.post(endpoints["login"], json=ADMIN_CREDENTIAL)
    return response.json()["accessToken"]
