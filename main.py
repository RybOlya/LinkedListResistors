from models.linked_list import ResistorLinkedList
from models.resistor import Resistor
from models.sort_order import SortOrder
if __name__ == '__main__':
    key = 0
    resistor_list = ResistorLinkedList()
    while key != 7:
            print(
                """Choose option:
                1 - Add element
                2 - Find element by key
                3 - Print all elements
                4 - Print elements with presicion bigger than <> 
                5 - Delete element
                6 - Delete list
                7 - Quit""")
            key = int(input("Your option: "))
            match key:
                case 1:
                    resistor_list.add_node(Resistor("Variable",5.6, 2, 0.6))
                    resistor_list.add_node(Resistor("Fixed Value",8.2, 7, 0.1))
                    resistor_list.add_node(Resistor("Magneto",2.5, 20, 0.12))
                    resistor_list.add_node(Resistor("Networks",8, 5, 0.2))
                case 2:
                    print()
                    print("Found resistor by value: ")
                    resistor_list.find_resistor_by_value(2.5)    
                case 3:                    
                    print("Original list: ")
                    resistor_list.print_list()
                    print()
                    print("Sorted list by resistance: ")
                    resistor_list.sort_by_value(SortOrder.DESCENDING)
                    resistor_list.print_list()
                    print()
                    print("Sorted list by name: ")
                    resistor_list.sort_by_name(SortOrder.ALPHABETIC)
                    resistor_list.print_list()
                case 4:   
                    print()
                    print("Resistors with tolerance greater than: ")
                    resistor_list.print_resistors_with_tolerance_bigger_than(0.2)
                case 5:   
                    print()
                    print("Delete resistor by value: ")
                    resistor_list.delete_by_value(2.5)
                case 6:                    
                    print()
                    print("Delete list: ")
                    resistor_list.delete_list()