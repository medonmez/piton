def count_aa(chain):


    if not chain:
        print("The chain is empty") 
        return None
    if len(chain) % 3 != 0:
        print("The chain length is not a multiple of 3")
        return None
    
    counter_aa = 0
    check_start_codon = False
    check_stop_codon = False
    i = 0
    while i < len(chain):
        codon = chain[i:i+3]

        if codon == "AUG":
            check_start_codon = True
            counter_aa += 1
        elif codon in ("UAG", "UAA", "UGA"):
            check_stop_codon = True
            break
        elif check_start_codon == True:
            counter_aa += 1
        i += 3

    if check_start_codon == False:
        print("There is no start codon")
        return None
    if check_stop_codon == False:
        print("There is no stop codon")
        return None
    
    return counter_aa

# Test cases
chain1 = "UGGCUAUGUAUGGGUUUGGCUCCUAGAUAGACAUACGAAUGU"
chain2 = "UGGCUAUGUAUGGGUUUGGCUCCUAGA"
chain3 = "UGGCUAUGUAGGGGUUUGGCUCCUAGA"
print(count_aa(chain1))  # Output: 
print(count_aa(chain2))  # Output: 
print(count_aa(chain3))  # Output: 