import os
import random
import asyncio
import sys

# Leet speak dictionary with characters typically allowed in a WiFi password
leet_dict = {
    'a': ['4', '@', 'A', '^', 'aye'],
    'b': ['8', 'B', '6'],
    'c': ['C', '<', '(', '{', '['],
    'd': ['D', '|)', '|]', '|}'],
    'e': ['3', 'E', '&'],
    'f': ['F', '|=', 'ph'],
    'g': ['9', 'G', '6'],
    'h': ['H', '#', '/-/', '[-]', ']-[', '}-{', '}{', 'aych'],
    'i': ['1', 'I', '!', '|', 'eye', '3y3', 'ai'],
    'j': ['J', '_|', '_/', '_)'],
    'k': ['K', '|<', '|{', 'X'],
    'l': ['1', 'L', '|_', '|', '7'],
    'm': ['M', '/\\/\\', '|v|', 'em'],
    'n': ['N', '|\\|', '/\\/', '/V'],
    'o': ['0', 'O', '()', '[]', '<>', 'oh'],
    'p': ['P', '|2', '|D', '|>', '|*', '[]D', '|"'],
    'q': ['Q', '(_,)', '()_', '2', 'cue'],
    'r': ['R', '|2', '|?', '/2', '|^', 'l2'],
    's': ['5', 'S', '$', 'z', 'ehs', 'es'],
    't': ['T', '7', '+'],
    'u': ['U', '|_|', 'v', 'L|'],
    'v': ['V', '\\/', '|/', '\\\\//'],
    'w': ['W', '\\/\\/', 'vv', '\\X/', 'uu'],
    'x': ['X', '%', '*', '><', ')(', '}{', 'ecks'],
    'y': ['Y', "''/", '`/', '%', 'j'],
    'z': ['Z', '2', '7', '~/_', '-/_']
}

# Precompute leet options
leet_options = {char.lower(): [char] + leet_chars for char, leet_chars in leet_dict.items()}

def leetify_word(word, mutations):
    return ''.join(random.choice(leet_options.get(char, [char])) for char in word)

async def process_line(line, mutations):
    words = line.split()
    leet_words_alpha = [leetify_word(word, mutations) for word in words]
    leet_words_spec = [leetify_word(word, mutations) if leetify_word(word, mutations) != word else word for word in words]
    return ' '.join(leet_words_alpha), ' '.join(leet_words_spec)

async def leetify_text(input_file_path, output_file_path_alpha, output_file_path_spec, mutations):
    with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
        lines = input_file.readlines()

    total_lines = len(lines)
    leet_words_alpha = []
    leet_words_spec = []

    chunk_size = 10000
    total_chunks = total_lines // chunk_size + (1 if total_lines % chunk_size != 0 else 0)
    dumped_chunks = 0

    for index, line in enumerate(lines, start=1):
        alpha, spec = await process_line(line, mutations)
        leet_words_alpha.append(alpha)
        leet_words_spec.append(spec)

        if index % chunk_size == 0 or index == total_lines:
            with open(output_file_path_alpha, 'a', encoding='utf-8') as output_file_alpha:
                output_file_alpha.write('\n'.join(leet_words_alpha) + '\n')
            with open(output_file_path_spec, 'a', encoding='utf-8') as output_file_spec:
                output_file_spec.write('\n'.join(leet_words_spec) + '\n')
            leet_words_alpha = []
            leet_words_spec = []
            dumped_chunks += 1

            sys.stdout.write(f"\rProcessed {index}/{total_lines} lines ({index * 100 / total_lines:.2f}%) - Dumped {dumped_chunks}/{total_chunks} chunks")
            sys.stdout.flush()

    print("\nProcessing complete!")

if __name__ == "__main__":
    input_file_name = input("Enter the input file name (must be in the same directory): ")
    input_file_path = os.path.join(os.path.dirname(__file__), input_file_name)
    base_file_name = os.path.splitext(input_file_name)[0]
    output_file_path_alpha = base_file_name + "_leet.txt"
    output_file_path_spec = base_file_name + "_leet_spec.txt"

    mutations = int(input("Enter the number of mutations per word: "))

    asyncio.run(leetify_text(input_file_path, output_file_path_alpha, output_file_path_spec, mutations))
