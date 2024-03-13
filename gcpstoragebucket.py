import os
from google.cloud import storage

def create_bucket(bucket_name):
    """Creates a new bucket."""
    # Initialize the client
    key_path = "key.json"  # Replace with the actual path to your key file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
    storage_client = storage.Client()

    # Create the bucket
    bucket = storage_client.create_bucket(bucket_name)
    location="us-central1"
    storage_class="STANDARD"
    print(f"Bucket {bucket.name} created")

if __name__ == "__main__":
    bucket_name = "mcitbucketexamplelatestandbest"  # Replace with your desired bucket name
    create_bucket(bucket_name)
