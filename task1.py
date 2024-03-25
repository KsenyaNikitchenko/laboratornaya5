import re

N=10
print("Задание 1. Вариант ",(N-1)%10+1,"""Реализовать функцию, которая будет проверять, является ли
введенная строка доменом из URL-адреса, возвращаемое значение true или False. Дополнительно реализовать
функцию, которая выбрасывает исключение о некорректном аргументе, иначе возвращает домен из URL-адреса.""")

def is_domain_from_url(url):
    pattern = r'^(https?://)([a-zA-Z0-9.-]+\.[a-zA-Z]{2,3})(/)?$'
    return bool(re.match(pattern, url))

def get_domain_from_url(url):
    pattern = r'^(https?://)([a-zA-Z0-9.-]+\.[a-zA-Z]{2,3})(/)?$'
    match=re.match(pattern, url)
    if match:
        return match.group(2)
    else:
        raise ValueError("Некорректный URL-адрес")

# Пример использования
url = input("Введите URL-адрес: ")
print("Соответствует ли адрес регулярному выражению?",is_domain_from_url(url))
try:
    print("Домен:",get_domain_from_url(url))
except ValueError as e:
    print(e)