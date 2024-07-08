import sys

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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task1.py <n> <m>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        
        if n <= 0 or m < 0:
            raise ValueError
        
        print(circular_array_path(n, m))
    except ValueError:
        print("Incorrect input data")
