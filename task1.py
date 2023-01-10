import requests
import json
# данные моего репозитория
response = requests.get('https://api.github.com/users/RomanExceed21/repos')
user_data = json.loads(response.text)

# файл с данными пользователя
with open('data.json', 'w') as user_data_file:
    json.dump(user_data, user_data_file)

# файл с репозиториями
with open('repos.txt', 'w') as user_repos_file:
    for element in user_data:
        user_repos_file.write(f"{element['name']}\n")
