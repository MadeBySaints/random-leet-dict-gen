# random-leet-dict-gen
Same concept as the leet dict gen, except generates the characters at random instead of methodically


# Leet Speak Converter

This Python script converts text from a given input file into Leet Speak (also known as "leet" or "1337" speak) and outputs two new files with the Leet Speak transformations. One file contains Leet Speak with alphanumeric combinations, and the other file contains Leet Speak with alphanumeric and special characters.

## Usage

1. **Clone the Repository:**

git clone https://github.com/MadeBySaints/random-leet-dict-gen.git

2. **Navigate to the Project Directory:**

cd random-leet-dict-gen

3. **Run the Script:**

python leet3.py

Follow the prompts to enter the input file name (must be in the same directory) and the number of mutations per word.

4. **Output:**

- The script will generate two new files:
  - `{input_file_name}_leet.txt`: Contains Leet Speak with alphanumeric combinations.
  - `{input_file_name}_leet_spec.txt`: Contains Leet Speak with alphanumeric and special characters.

## Requirements

- Python 3.x
- No additional libraries or packages are required.

## Example

Suppose you have a file named `input.txt` with the following content:

Hello world! This is a test.

Running the script and entering `input.txt` as the input file name and `2` as the number of mutations per word will produce two output files:

`input_leet.txt`:

He110 w0r1d! Th1s 15 a te5t.

`input_leet_spec.txt`:

H3llo w0r/_d! Th!s !s a t3s7.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
