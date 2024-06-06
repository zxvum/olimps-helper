import os
import time
import psutil
import openpyxl
from solve import main


# Функция для чтения данных из input.txt
# Необходимо изменить под себя!
def read_input_file(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split('\n')

    datasets = []
    i = 0
    while i < len(content):
        datasets.append(int(content[i]))
        i += 1

    return datasets


# Функция для записи результатов в results.xlsx
def write_results_to_excel(results):
    filename = 'results.xlsx'

    # Удаление файла, если он существует
    if os.path.exists(filename):
        os.remove(filename)

    # Создание нового файла и добавление заголовков
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Индекс', 'Результат', 'Время (с)', 'Память (МБ)'])

    # Запись новых данных
    for index, result in enumerate(results, start=1):
        ws.append([index, result['result'], result['time'], result['memory']])

    # Сохранение файла
    wb.save(filename)


# Основная функция
def main_script():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    datasets = read_input_file(input_filename)
    results = []

    with open(output_filename, 'w') as output_file:
        for i, data in enumerate(datasets, start=1):
            start_time = time.time()
            process = psutil.Process(os.getpid())

            result = main(data)

            end_time = time.time()
            memory_usage = process.memory_info().rss / (1024 ** 2)  # Память в МБ
            execution_time = end_time - start_time

            output_file.write(f"{result}\n")

            results.append({
                'result': result,
                'time': f"{execution_time:.6f}",
                'memory': f"{memory_usage:.2f}"
            })

    write_results_to_excel(results)


if __name__ == "__main__":
    main_script()
