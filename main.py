# Created by Agamdeep Singh
# Github: @CoderAgam001
# Find Me Everywhere: https://linktr.ee/coderagam001

from elements import elements

print("Welcome to The Periodic Name App!")

on = True
while on:
    name = input("Enter The Name or Sentence to Begin: ").lower()

    selected_elements = []
    separator = ', '
    
    for ele in elements:
        if name.count(elements[ele]) > 0:
            selected_elements.append(ele)
    
    print(f"'{name.title()}' Consists Of {separator.join(selected_elements)}")

    run_again = input("Do You Want To Run Again? (y/n): ").lower()
    
    if run_again == 'y':
        on = True
    
    else:
        on = False