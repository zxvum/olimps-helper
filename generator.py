import random
from PyInquirer import prompt

# Определение вопросов для PyInquirer
questions = [
    {
        'type': 'input',
        'name': 'num_datasets',
        'message': 'Сколько наборов данных вы хотите сгененировать?',
        'validate': lambda val: val.isdigit() and int(val) > 0,
    }
]

# Получение ответа от пользователя
answers = prompt(questions)
num_datasets = int(answers['num_datasets'])

# Генерация и запись данных в output.txt
output_filename = 'input.txt'
with open(output_filename, 'w') as output_file:
    for _ in range(num_datasets):
        n = random.randint(1, 100)
        numbers = [str(random.randint(1, 10**2)) for _ in range(n)]
        output_file.write(f"{n}\n")
        output_file.write(" ".join(numbers) + "\n")

print(f"{num_datasets} наборов данных успешно записаны в '{output_filename}'")
