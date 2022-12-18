# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

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