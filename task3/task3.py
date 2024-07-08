import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def create_values_dict(values):
    return {item['id']: item['value'] for item in values}

def update_test_values(tests, values_dict):
    stack = tests.copy()
    
    while stack:
        current_test = stack.pop()
        test_id = current_test['id']
        
        if test_id in values_dict:
            current_test['value'] = values_dict[test_id]
        
        if 'values' in current_test:
            stack.extend(current_test['values'])


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <values_file> <tests_file> <report_file>")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)

    values_dict = create_values_dict(values_data['values'])
    update_test_values(tests_data['tests'], values_dict)

    save_json(tests_data, report_file)
