import requests
from urllib.parse import urljoin

max_file_number = int(input("Enter the maximum file number to check: "))

base_url = "https://www.skyrc.com/files/"
output_file = "available_files.txt"

def get_final_url_after_redirects(url):
    with requests.get(url, stream=True) as response:
        return response.url

print("Starting the URL checking process...")

with open(output_file, "w") as file:
    for i in range(1, max_file_number + 1):
        url = urljoin(base_url, str(i))
        print(f"Checking URL: {url}")
        try:
            final_url = get_final_url_after_redirects(url)
            filename = final_url.split('/')[-1]  # Extracts the file name from the URL
            if filename == "not_found":
                print("File not found!")
                continue
            if filename:
                file.write(f"{i}. {filename}\n")
                print(f"File found: {filename}")
        except requests.ConnectionError:
            print(f"Failed to connect to {url}")

print(f"URL checking process completed. Results saved in {output_file}.")
