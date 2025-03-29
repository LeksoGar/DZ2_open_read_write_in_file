import os
from pprint import pprint

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def count_lines(file_path):
    """Считает количество строк в файле"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

def merge_files(output_file, *input_file):
    """Объединение нескольких файлов в один"""
# Создаем список кортежей
    files_data = []
    for file_name in input_file:
        file_path = os.path.join(os.getcwd(), file_name)
        lines_count = count_lines(file_path)
        content = read_file_content(file_path)
        files_data.append((file_name, lines_count, content))
    # pprint(files_data) # промежуточная проверка

# Сортируем файл по количеству строк (по 2-у элементу кортежа)
    files_data.sort(key=lambda x: x[1])

# Запись в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for file_name, lines_count, content in files_data:
            result_file.write(f"{file_name}\n")
            result_file.write(f"{lines_count}\n")
            result_file.writelines(content)
            result_file.write("\n")

# Проверка
input_files = ["1.txt", "2.txt", "3.txt"]
output_file = 'result.txt'
merge_files(output_file, *input_files)
# pprint(read_file_content(output_file))