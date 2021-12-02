import argparse


def check_sentence(sentence, dictionary, used, results):
        
    for w in dictionary:
        if w in used:
            continue
        # find how many words from the dict we can create 
        # with all the letters from the sentence
        aux = sentence
        found = True
        
        for l in w:
            i = 0
            try: 
                i = aux.index(l)
            except:
                found = False
                i = -1

            if i != -1:
                if i == 0:
                    aux = aux[i+1:]
                elif i == len(aux):
                    aux = aux[0:i]
                else:
                    aux = aux[0:i]+aux[i+1:]
                
            else:
                found = False
                next   
        if found:
            new_used = used + [w]
            if len(aux) == 0:
                # all the letter were used
                results.append(new_used)
                return results
            leaves = check_sentence(aux, dictionary, new_used, results)
    
    return results


def find_anagrams(input_file):
    d = []
    sentences = []
    with open(input_file) as reader:
        reading_dict = True
        reading_sentences = False
        for line in reader:
            line = line.strip()
            if reading_dict:
                if line == '#':
                    reading_dict = False
                    reading_sentences = True
                    continue
                d.append(line.upper())
            elif reading_sentences:
                if line == '#':
                    break
                sentences.append(line.upper())
    
    res = {}
    for sentence in sentences:
        aux = list(sentence.replace(' ',''))
        results = check_sentence(aux, d, [], [])
        if len(results) != 0:
            res[sentence] = results
 
    return res


def main():
   parser = argparse.ArgumentParser(description='Anagrams')
   parser.add_argument('--input_file', dest='input_file', type=str, help='Path to the input file')
   args = parser.parse_args()
   res = find_anagrams(args.input_file)
   for sentence, perms in res.items():
       for p in perms:
           print(f"{sentence} = {' '.join(p)}")

if __name__ == '__main__':
    main()
