# python-script
print("Hello GitHub")
import requests
username = "your-username"
repo_name = "python-scripts"
file_path = "hello.py"

url = f"https://github.com/Nuha-S24013461/python-script/edit/main/hello.py"
response = requests.get(url)

if response.status_code == 200:
    print("Fetched script content:")
    print(response.text)
else:
    print(f"Failed to fetch script. Status code: {response.status_code}")

