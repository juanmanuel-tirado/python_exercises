import argparse

"""
There are different solutions for this problem. Probably, 
the most straight forward consists on sorting the letters
of two words and compare them. If both are the same this 
means that they are anagrams. By finding the negative case
we can detect ananagrams.
"""

def compute_ananagrams(words):
    ananagrams = []
    for i in range(len(words)):
        sortedA = sorted(words[i].lower())
        found_anagram = False
        for j in range(len(words)):
            if i == j:
                continue
            sortedB = sorted(words[j].lower())

            if sortedA == sortedB:
                found_anagram = True
                break
        if not found_anagram:
            ananagrams.append(words[i])
    return ananagrams

def find_ananagrams(input_file):
    words = []
    with open(input_file) as reader:
        num_line = 1
        for line in reader:
            if len(line) > 80:
                print(f'Line {num_line} larger than 80 characters')
                return None
            tokens = line.strip().split(' ')
            for t in tokens:
                if len(t) > 20:
                    print(f'Word {t} is larger than 20 characters')
                    return None
            words.extend(tokens)
            num_line += 1
    if len(words) > 0:
        return compute_ananagrams(words)
    return None
        

def main():
   parser = argparse.ArgumentParser(description='Ananagrams')
   parser.add_argument('--input_file', dest='input_file', type=str, help='Path to the input file')
   args = parser.parse_args()
   res = find_ananagrams(args.input_file)
   if res is not None:
       print('\n'.join(res))

if __name__ == '__main__':
    main()