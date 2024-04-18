"""
Модуль содержит функции для проверки доступности сервера и перезагрузки системы при необходимости.
"""

import subprocess
import time

def ping_server(ip_address, count=100):
    """
     Функция ping_server выполняет ping указанного IP-адреса заданное количество раз.

     Параметры:
     - ip_address - IP-адрес сервера.
     - count - количество запросов ping (по умолчанию 100).

     Возвращает:
     Код возврата команды ping.
     """
    command = f"ping -c {count} {ip_address}"
    return subprocess.call(command, shell=True)

def check_connection():
    """
    Функция check_connection проверяет доступность сервера с IP-адресом 8.8.8.8 каждые 120 секунд.

    Если сервер недоступен, выполняется перезагрузка системы.
    """
    while True:
        if ping_server('8.8.8.8', count=100) != 0:
            subprocess.call('reboot', shell=True)
        time.sleep(120)

check_connection()
