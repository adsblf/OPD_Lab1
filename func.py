import requests  #выполнение http-запросов
from bs4 import BeautifulSoup #разбор html-кода
def parser():
    link = 'https://omgtu.ru/ecab/persons/index.php?b=1'
    page = requests.get(link) #Метод GET указывает на то, что происходит попытка извлечь данные из определенного ресурса
    print(page.status_code)
    page_parser = BeautifulSoup(page.text, 'html.parser')
    searchable_names = page_parser.findAll('div', style="padding: 5px; font-size: 120%;")
    write_in_file(searchable_names)
def write_in_file(searchable_names):
    with open('result.txt', 'w') as file: #w: открыт для записи (перед записью файл будет очищен),
        for name in searchable_names:
            list_names = name.find('a').text.strip()
            file.write(list_names + '\n')
