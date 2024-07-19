import requests

def get_github_token(url, github_token):
    """
    Retrieve a GitHub token from HashiCorp Vault using GitHub authentication.

    Args:
        url (str): URL of the HashiCorp Vault instance.
        github_token (str): GitHub token to authenticate against the Vault API.

    Returns:
        str: The client token retrieved from Vault.
    """
    # Construct the complete URL for the authentication endpoint
    complete_url = f"{url}/v1/auth/github/login"

    # Create the payload with the GitHub token
    payload = {"token": github_token}

    # Perform the POST request to retrieve the token
    response = requests.post(complete_url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json()
        # Return the client token
        return results.get('auth', {}).get('client_token', '')
    else:
        # Handle errors
        response.raise_for_status()

# Example usage:
# token = get_github_token("http://localhost:8200", "your_github_token")
# print(token)
