import requests
import json

def get_aws_metadata():
    response = requests.get('https://docs.aws.amazon.com/')
    metadata = {}
    if response.status_code == 200:
        metadata = {key: requests.get(f'https://docs.aws.amazon.com/').text
                    for key in response.text.splitlines()}
    return metadata

def get_azure_metadata():
    headers = {'Metadata': 'true'}
    response = requests.get('https://learn.microsoft.com/en-us/azure/?product=popular', headers=headers)
    metadata = {}
    if response.status_code == 200:
        metadata = response.json()
    return metadata

def get_gcp_metadata():
    headers = {'Metadata-Flavor': 'Google'}
    response = requests.get('https://cloud.google.com/docs', headers=headers)
    metadata = {}
    if response.status_code == 200:
        metadata = response.json()
    return metadata

def main():
    cloud_providers = {
        'AWS': get_aws_metadata,
        'Azure': get_azure_metadata,
        'GCP': get_gcp_metadata
    }

    instance_metadata = {}
    for provider, func in cloud_providers.items():
        print(f"Querying metadata from {provider}...")
        instance_metadata[provider] = func()

    print("\nMetadata JSON Output:")
    print(json.dumps(instance_metadata, indent=4))

if __name__ == "__main__":
    main()

