import ping3
import time
import subprocess

# Задайте адрес сервера для пинга
server_address = 'ya.ru'

# Задайте время ожидания перед перезагрузкой
timeout = 60 # секунд

# Функция для выполнения пинга
def check_ping():
 ping_result = ping3.ping(server_address)
 if ping_result.success:
   print("Сервер доступен")
 else:
   print("Сервер недоступен")

# Основной цикл
while True:
 check_ping()
 time.sleep(timeout)

# Если сервер недоступен в течение timeout секунд, перезагружаем сервер
if not ping_result.success:
 print("Сервер недоступен более timeout секунд, перезагружаю сервер")
 subprocess.call('shutdown', '-r', 'now')