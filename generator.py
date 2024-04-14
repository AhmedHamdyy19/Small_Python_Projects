# Generators in Python are particularly useful when dealing with large datasets or when you need to generate a sequence of values lazily 
# (i.e., on demand). They can help you save memory and improve performance. Here's a practical example where generators can be beneficial:

# Suppose you have a large file containing lines of text, and you want to process each line. Instead of reading the entire file into memory
# at once, which can be inefficient for large files, you can use a generator to read and process one line at a time. This way, you only keep
# one line in memory at a time, reducing memory usage.

def read_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file_path = 'large_file.txt'
line_generator = read_lines(file_path)

for line in line_generator:
    print(line)
