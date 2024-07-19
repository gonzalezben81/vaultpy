import requests
import json

def get_user_token(url, user, password):
    """
    Retrieve a token from HashiCorp Vault using the userpass authentication method.

    Args:
        url (str): URL of the HashiCorp Vault instance.
        user (str): Username to authenticate against the Vault API.
        password (str): Password to login to Vault with the username.

    Returns:
        dict: The authentication details, including the token.
    """
    # Construct the complete URL for the authentication endpoint
    complete_url = f"{url}/v1/auth/userpass/login/{user}"
    print(complete_url)

    # Create the payload with the password
    payload = {"password": password}

    # Perform the POST request to retrieve the token
    response = requests.post(complete_url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json()
        return results.get('auth', {})
    else:
        # Handle errors
        response.raise_for_status()

# Example usage:
# token = get_user_token("http://localhost:8200", "username", "password")
# print(token)
