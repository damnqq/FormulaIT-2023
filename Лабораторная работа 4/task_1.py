import json

FILE_NAME = 'input.json'

def task() -> float:
    with open(FILE_NAME) as file:
        data = json.load(file)
        result_sum = sum(item['score'] * item['weight'] for item in data)
        return round(result_sum, 3)

print(task())
