# Defining letters and the scores 
def get_letter_score(letter, position, is_first, is_last):
    letter_scores = {
        'Q': 1, 'Z': 1,
        'J': 3, 'X': 3,
        'K': 6,
        'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7,
        'B': 8, 'C': 8, 'M': 8, 'P': 8,
        'D': 9, 'G': 9,
        'L': 15, 'N': 15, 'R': 15, 'S': 15, 'T': 15,
        'O': 20, 'U': 20,
        'A': 25, 'I': 25,
        'E': 35
    }

    if is_first:
        return 0 # Score for the 1st letter assigned as 0
    elif is_last:
        if letter == 'E':
            return 20 # If letter E comes last, score is assigned as 20
        else:
            return 5 # For all remaining last letters score is 5 
    else:
        # Assigning values to the position of letters
        position_value = 1 if position == 2 else (2 if position == 3 else 3)
        return position_value + letter_scores.get(letter, 0)

def generate_abbreviations(names):
    abbreviations = {}

    for name in names:
        # Clean the name by removing non-alphabetic characters and split into words
        clean_name = ''.join(char for char in name if char.isalpha() or char.isspace())
        words = clean_name.split()

        for word in words:
            word = word.upper()
            for i in range(len(word) - 2):
                abbreviation = word[i] + word[i+1] + word[i+2]
                first_letter = word[i]
                second_letter = word[i+1]
                third_letter = word[i+2]

                is_first = (i == 0)
                is_last = (i + 2 == len(word) - 1)

                # Calculate the score for the abbreviation based on letter positions
                score = get_letter_score(second_letter, 2, is_first, is_last) + get_letter_score(third_letter, 3, is_first, is_last)

                if abbreviation not in abbreviations:
                    abbreviations[abbreviation] = {'name': name.strip(), 'score': score}
                else:
                    # Exclude abbreviation if it can be formed from more than one name
                    if name.strip() != abbreviations[abbreviation]['name']:
                        # Exclude abbreviation if it can be formed from multiple names
                        del abbreviations[abbreviation]
                        break

    return abbreviations

def main():
    # Defining file location
    input_path = input("C:\Users\kkart\Desktop\ASSIGNMENTS\Python - 16th\p_assignment_trees.txt ")

    try:
        # Read the input file and process its contents
        with open(input_path, 'r') as file:
            names = file.readlines()
            abbreviations = generate_abbreviations(names)

            if abbreviations:
                file_name = input_path.split('/')[-1].split('.')[0]
                output_path = f"{file_name}_abbrevs.txt"

                # Write abbreviations along with scores to the output file
                with open(output_path, 'w') as output_file:
                    for abbreviation, info in abbreviations.items():
                        output_file.write(f"{abbreviation}: {info['name']} (Score: {info['score']})\n")

                print(f"Abbreviations have been generated and saved to {output_path}")
            else:
                print("No abbreviations generated.")

    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

if __name__ == "__main__":
    main()
