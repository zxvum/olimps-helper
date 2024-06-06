# Python Performance and Memory Usage Analyzer

Эта программа предназначена для упрощения измерения скорости выполнения кода, измерения затраченной памяти и генерации наборов данных.

## Установка зависимостей

Перед началом работы установите необходимые зависимости, выполнив следующую команду:

```bash
pip install -r requirements.txt
```

# Как использовать
## Шаг 1: Написание решения

В файле `solve.py` напишите своё решение в функции `main`. Вы также можете вызвать сторонние функции из этой функции. Ответ должен быть возвращён через `return`.

Пример:
```python
# solve.py
def main():
    # Ваша логика здесь
    result = your_function()
    return result
```

## Шаг 2: Генерация наборов данных
Перейдите в файл `generator.py`. В функции generate напишите свою логику для генерации наборов данных, которые будут помещены в `input.txt`.

Пример:
```python
n = random.randint(1, 100)
numbers = [str(random.randint(1, 10 ** 2)) for _ in range(n)]
output_file.write(f"{n}\n")
output_file.write(" ".join(numbers) + "\n")
```

## Шаг 3: Чтение данных
В файле main.py измените функцию read_input_file для корректного считывания данных из input.txt.

Пример:
```python
# main.py
def read_input_file(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split('\n')

    datasets = []
    i = 0
    while i < len(content):
        datasets.append(int(content[i]))
        i += 1

    return datasets
```

## Шаг 4: Генерация данных
Для генерации наборов данных выполните следующую команду:
```bash
python generator.py
```

## Шаг 5: Запуск анализатора
Для запуска анализатора выполните следующую команду:
```bash
python main.py
```

По вопросам писать - [@sallyqx](http://t.me/sallyqx)