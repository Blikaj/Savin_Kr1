from django.shortcuts import render
import os
import platform
import requests
# Create your views here.
def index(request): 
  create_script()
  # Получаем список файлов
  files = os.listdir()
  # Получаем системную информацию
  system_info = get_system_info()
  # Текущий пользователь Django
  current_user = request.user.username

  # Сохраняем главную страницу университета в файл с фамилией пользователя
  save_status = save_university_page('savin')
  newsessionsecret = os.environ.get('newsessionsecret', '')
  return render(request, 'index.html', {'newsessionsecret': newsessionsecret})

# Функция для создания скрипта
def create_script():
    script_code = """
import os
print("Список файлов в текущем каталоге:")
print(os.listdir())
print("Системная информация:")
print(os.uname())
print("Текущий пользователь:", os.getlogin())
"""
    with open('generated_script.py', 'w', encoding='utf-8') as f:
        f.write(script_code)

# Функция для получения системной информации
def get_system_info():
    uname = os.uname()
    return f"System: {uname.sysname}, Node: {uname.nodename}, Release: {uname.release}, Version: {uname.version}, Machine: {uname.machine}"

# Функция для сохранения главной страницы университета в файл
def save_university_page(last_name):
    url = 'https://www.fa.ru/'
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{last_name}.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)  # Для чистого текста нужна обработка html
    else:
        return f"Ошибка доступа к {url}"
    return f"Данные сохранены в файл {last_name}.txt"