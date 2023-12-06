input_file_path = "input.txt"
output_file_path = "output2.txt"

DIGITS = "0123456789"


def get_first_digit(line_str):
    for c in line_str:
        if c in DIGITS:
            return c


def get_last_digit(line_str):
    for c in line_str[::-1]:
        if c in DIGITS:
            return c


def convert_line(line_str):
    line_str = line_str.replace("one", "o1e")
    line_str = line_str.replace("two", "t2o")
    line_str = line_str.replace("three", "t3e")
    line_str = line_str.replace("four", "f4r")
    line_str = line_str.replace("five", "f5e")
    line_str = line_str.replace("six", "s6x")
    line_str = line_str.replace("seven", "s7n")
    line_str = line_str.replace("eight", "e8t")
    line_str = line_str.replace("nine", "n9n")

    return line_str


try:
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        sum = 0
        for line in input_file:
            line = line.strip()
            print(line)
            converted_line = convert_line(line)
            print(converted_line)
            num_str = get_first_digit(converted_line) + \
                get_last_digit(converted_line)
            print(num_str)
            sum += int(num_str)
        print("SUM", sum)
        output_file.write(f"{sum}")

    print(f"Processing completed. Results written to '{output_file_path}'.")

except FileNotFoundError:
    print(f"File '{input_file_path}' not found.")

except Exception as e:
    print(f"An error occurred: {e}")
