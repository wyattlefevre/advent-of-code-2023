input_file_path = "input.txt"
output_file_path = "output.txt"

try:
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            # Process each line and write to the output file
            processed_line = f"Processed: {line.strip()}\n"
            output_file.write(processed_line)

    print(f"Processing completed. Results written to '{output_file_path}'.")

except FileNotFoundError:
    print(f"File '{input_file_path}' not found.")

except Exception as e:
    print(f"An error occurred: {e}")
