# Mert Dönmez
# 2016203039

# Question1: A function that counts the number of amino acids in a given chain of nucleotids.
def count_aa(chain): 

    # Check if the chain is empty
    if not chain:
        print("The chain is empty") 
        return None
    
    # Check if the chain length is not a multiple of 3
    if len(chain) % 3 != 0:
        print("The chain length is not a multiple of 3")
        return None
    
    # Initialize a counter for amino acids, and flags to check for start and stop codons
    counter_aa = 0
    check_start_codon = False
    check_stop_codon = False
    i = 0
    
    # Loop through the chain in increments of 3
    while i < len(chain):
        codon = chain[i:i+3]  # Extract the current codon
        
        # Check if the codon is a start codon
        if codon == "AUG":
            check_start_codon = True  # Set start codon flag to True
            counter_aa += 1  # Increment the amino acid counter

        # Check if the codon is a stop codon
        elif codon in ("UAG", "UAA", "UGA"):
            check_stop_codon = True  # Set stop codon flag to True
            break  # Exit the loop

        # If stop codons not found in current codon, and a start codon has been already encountered, increment the amino acid counter.
        elif check_start_codon == True:
            counter_aa += 1  
        
        i += 3  # Move to the next codon in the chain
        
    # Check if there is no start codon
    if check_start_codon == False:
        print("There is no start codon")
        return None
    
    # Check if there is no stop codon
    if check_stop_codon == False:
        print("There is no stop codon")
        return None
    
    # Return the final count of amino acids
    return counter_aa

# Test cases
chain1 = "UGGCUAUGUAUGGGUUUGGCUCCUAGAUAGACAUACGAAUGU"
chain2 = "UGGCUAUGUAUGGGUUUGGCUCCUAGA"
chain3 = "UGGCUAUGUAGGGGUUUGGCUCCUAGA"
print(count_aa(chain1))  # Output: 6
print(count_aa(chain2))  # Output: None with "There is no stop codon" message
print(count_aa(chain3))  # Output: None with "There is no start codon" message

# Question2: Duration to save enough money for the dream house

# Input for the price of the dream home
home = float(input("Enter the price of your dream home: "))

# Input for the salary
salary = float(input("Enter your salary: "))

# Input for the percentage of salary saved monthly
saving_percentage = float(input("Enter the percentage of your salary you save monthly (25 for 25%): "))

# Calculate the amount of money saved monthly
saving_money = salary * (saving_percentage / 100)

# Calculate the number of months needed to save enough money for the dream home by dividing the home price by the monthly saving amount
months = home / saving_money

# Round up the number of months to the upper integer, using the round() function. For example: 40.1 months rounds up to 41
# Adding 0.49999999 helps to correct upper rounding. If we use +0.5, 51 months(for example) rounds to 52 because it is a odd number.
months_upper_rounded = round(months + 0.49999999)

# Print the result with a formatted string, displaying the calculated number of months.
print(f"It will take {months_upper_rounded} months to save enough money for your dream home.")


# Question3: Counting words in a sentence

# Assign the given sentence
sentence = "The saddest aspect of life right now is that science gathers knowledge faster than society gathers wisdom."

# Use split() to split the sentence into words
words_list = sentence.split()
# len() function to get the number of items in the list
number_of_words = len(words_list)

# Print the result using a formatted string that includes the number of words
print(f"The sentence consists of {number_of_words} words.")
# The sentence consists of 17 words