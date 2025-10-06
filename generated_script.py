
import os
print("Список файлов в текущем каталоге:")
print(os.listdir())
print("Системная информация:")
print(os.uname())
print("Текущий пользователь:", os.getlogin())
