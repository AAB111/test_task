def circular_array_path(n, m):
    path = []
    current_position = 0
    if m == 0:
        first_element = 1
        return str(first_element)
    while True:
        first_element = current_position + 1
        path.append(first_element)
        current_position = (current_position + m - 1) % n
        if current_position == 0:
            break
    
    return ''.join(map(str, path))


try:
    print("Enter n and m:")
    arr_params = [int(x) for x in input().split()]
    if len(arr_params) != 2 or arr_params[0] <= 0 or arr_params[1] < 0:
        raise ValueError
    n, m = arr_params
    print(circular_array_path(n, m))
except ValueError:
    print("Incorrect input data")