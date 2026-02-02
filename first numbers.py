def first_n_primes(num):
    if num < 2:
        return []
    
    # Το 2 είναι ο μόνος άρτιος πρώτος αριθμός
    if num == 2:
        return True
    
    # Οι άρτιοι αριθμοί μεγαλύτεροι του 2 δεν είναι πρώτοι
    if num % 2 == 0:
        return False
    
    # Ελέγχουμε μόνο τους μονούς διαιρέτες μέχρι την τετραγωνική ρίζα του n
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

print(first_n_primes(75)) 
