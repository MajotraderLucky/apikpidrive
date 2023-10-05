import requests
from dotenv import load_dotenv
import os

# Загрузите переменные окружения из файла .env
load_dotenv()

# Получите значения переменных из .env файла
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
bearer_token = os.getenv("BEARER_TOKEN")

# Задайте параметры запроса
url = "https://development.kpi-drive.ru/_api/auth/login"
payload = {
    "login": login,
    "password": password
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Bearer {bearer_token}"
}

# Выполните POST-запрос
response = requests.post(url, data=payload, headers=headers)

# Проверьте статус ответа
if response.status_code == 200:
    # Распарсите ответ в формате JSON
    data = response.json()
    # Выведите данные
    print(data)
else:
    print("Ошибка при выполнении запроса:", response.status_code)