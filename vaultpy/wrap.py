import requests
import json

def wrap_secrets(url=None, token=None, secrets_to_wrap=None, ttl='30m'):
    """
    Wrap secrets in HashiCorp Vault and return a wrap token.

    Args:
        url (str): URL of the HashiCorp Vault instance.
        token (str): Vault token for authentication.
        secrets_to_wrap (dict): Secrets to be wrapped.
        ttl (str): Time to Live for the wrap token.

    Returns:
        str: The wrap token used to unwrap the secrets.
    """
    # Construct the complete URL for the wrapping endpoint
    complete_url = f"{url}/v1/sys/wrapping/wrap"
    print(complete_url)

    # Create the headers for the request
    headers = {
        'X-Vault-Token': token,
        'X-Vault-Wrap-TTL': ttl
    }

    # Convert the secrets to JSON
    data_to_wrap = json.dumps(secrets_to_wrap)

    # Perform the POST request to wrap the secrets
    response = requests.post(complete_url, headers=headers, data=data_to_wrap)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json()
        # Return the wrap token
        return results.get('wrap_info', {}).get('token', '')
    else:
        # Handle errors
        response.raise_for_status()

# Example usage:
# wrap_token = wrap_secrets("http://localhost:8200", "your_vault_token", {"secret_key": "secret_value"})
# print(wrap_token)
