import os

class UniqueInt:
    def __init__(self):
        self.seen_integers = set()

    def readNextItemFromFile(self, inputFileStream):
        while True:
            line = inputFileStream.readline()
            if not line:
                return None

            # Strip whitespace and check if the line is empty
            stripped_line = line.strip()
            if not stripped_line:
                continue

            # Check if the line contains exactly one integer
            parts = stripped_line.split()
            if len(parts) != 1:
                continue

            try:
                number = int(parts[0])
                return number
            except ValueError:
                continue

    def processFile(self, inputFilePath, outputFilePath):
        self.seen_integers.clear()
        try:
            with open(inputFilePath, 'r') as inputFileStream:
                while True:
                    number = self.readNextItemFromFile(inputFileStream)
                    if number is None:
                        break
                    self.seen_integers.add(number)

            # Convert the set to a sorted list without using sort
            unique_integers = list(self.seen_integers)
            unique_integers.sort()  # Sort the list in ascending order

            with open(outputFilePath, 'w') as outputFileStream:
                for number in unique_integers:
                    outputFileStream.write(f"{number}\n")
        
        except Exception as e:
            print(f"Error processing file {inputFilePath}: {e}")

# Create directories if they don't exist
os.makedirs(r'C:\dsa\hw01\code\src', exist_ok=True)
os.makedirs(r'C:\dsa\hw01\sample_inputs', exist_ok=True)
os.makedirs(r'C:\dsa\hw01\sample_results', exist_ok=True)

# Example of processing files
unique_int = UniqueInt()
input_files = ['sample_input_01.txt', 'sample_input_02.txt']  # Example input files
for input_file in input_files:
    input_path = rf'C:\Users\HP\Desktop\unquien\Unique-Integers\dsa\hw01\sample_inputs\{input_file}'
    output_path = rf'C:\Users\HP\Desktop\unquien\Unique-Integers\dsa\hw01\sample_results\{input_file}_results.txt'
    if os.path.exists(input_path):
        unique_int.processFile(input_path, output_path)
        print(f"Processed input file {input_file}. Output file: {output_path}")
    else:
        print(f"Input file {input_file} does not exist in sample_inputs directory.")
