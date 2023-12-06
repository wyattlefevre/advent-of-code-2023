input_file_path = "input.txt"
output_file_path = "output.txt"

DIGITS = "0123456789"


def get_first_digit(line_str):
    for c in line_str:
        if c in DIGITS:
            return c
    pass


def get_last_digit(line_str):
    for c in line_str[::-1]:
        if c in DIGITS:
            return c


try:
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        sum = 0
        for line in input_file:
            # Process each line and write to the output file
            num_str = get_first_digit(line) + get_last_digit(line)
            print(num_str)
            sum += int(num_str)
        output_file.write(f"{sum}")

    print(f"Processing completed. Results written to '{output_file_path}'.")

except FileNotFoundError:
    print(f"File '{input_file_path}' not found.")

except Exception as e:
    print(f"An error occurred: {e}")
