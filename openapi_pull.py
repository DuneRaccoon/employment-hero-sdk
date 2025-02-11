import os
import shutil
import subprocess
import httpx

# URL of the OpenAPI spec
OPENAPI_SPEC_URL = "https://api.keypay.com.au/swagger-au.json"

# Directory where the client SDK will be generated
OUTPUT_DIR = "employment_hero_python_client"

# Download the OpenAPI spec
def download_openapi_spec(url: str, output_file: str="employment-hero-au.json"):
    response = httpx.get(url)
    if response.status_code == 200:
        with open(output_file, 'w') as f:
            f.write(response.text)
        print(f"OpenAPI spec downloaded as {output_file}")
    else:
        raise Exception(f"Failed to download OpenAPI spec: {response.status_code}")
    
    return output_file

# Generate Python client using OpenAPI Generator
def generate_python_client(spec_file, output_dir):
    command = [
        "openapi-generator-cli", "generate",
        "-i", spec_file,
        "-g", "python",
        "-o", output_dir
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Python client generated in {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating client: {e}")

if __name__ == "__main__":
    # Check if openapi-generator-cli is installed
    if not shutil.which("openapi-generator-cli"):
        print("openapi-generator-cli not found. Installing...")
        subprocess.run(["python3", "-m", "pip", "install", "openapi-generator-cli"], check=True)

    generate_python_client(download_openapi_spec(OPENAPI_SPEC_URL), OUTPUT_DIR)