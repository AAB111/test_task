import sys
import os

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"File {file_path} not found.")
        sys.exit(1)

    nums = read_numbers_from_file(file_path)
    result = min_moves_to_equal_elements(nums)

    print(result)