number_of_lines = int(input())

unique_chem_els = set()

for i in range (number_of_lines):
    chem_elements = input().split()
    for el in chem_elements:
        unique_chem_els.add(el)
print(*unique_chem_els, sep='\n')