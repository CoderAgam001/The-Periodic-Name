# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from elements import elements

print("Welcome to The Periodic Name App!")
    
name = input("Enter you Name:\n").lower()

length = len(name)

def select_element():
    selected_elements = []
    
    for ele in elements:
        if name.count(elements[ele]) > 0:
            selected_elements.append(ele)

    print(f"{name} contains {selected_elements}")