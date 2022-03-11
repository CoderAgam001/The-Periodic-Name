# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from elements import elements

def main():
    print("Welcome to The Periodic Name App!")
    name = input("Enter The Name: ").lower()

    selected_elements = []
    separator = ', '
    
    for ele in elements:
        if name.count(elements[ele]) > 0:
            selected_elements.append(ele)
    
    print(f"The Name '{name.title()}' Consists Of {separator.join(selected_elements)}")
main()