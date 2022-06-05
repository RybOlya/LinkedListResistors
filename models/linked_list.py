from traceback import print_list
from models.sort_order import SortOrder
from models.node import Node


class ResistorLinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            self.head = new_node

        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.previous = current_node
            new_node.next = None

    def sort_by_value(self, order : SortOrder):
        if self.head is None:
            return
        else:
            if order == SortOrder.ASCENDING:
                current_node = self.head
                while current_node.next is not None:
                    next_node = current_node.next
                    while next_node is not None:
                        if current_node.data.value > next_node.data.value:
                            temporary_variable = current_node.data
                            current_node.data = next_node.data
                            next_node.data = temporary_variable
                        next_node = next_node.next
                    current_node = current_node.next
            elif order == SortOrder.DESCENDING:
                current_node = self.head
                while current_node.next is not None:
                    next_node = current_node.next
                    while next_node is not None:
                        if current_node.data.value < next_node.data.value:
                            temporary_variable = current_node.data
                            current_node.data = next_node.data
                            next_node.data = temporary_variable
                        next_node = next_node.next
                    current_node = current_node.next
    def sort_by_name(self, order : SortOrder):
        if self.head is None:
            return
        else:
            if order == SortOrder.ALPHABETIC:
                current_node = self.head
                while current_node.next is not None:
                    next_node = current_node.next
                    while next_node is not None:
                        if current_node.data.name > next_node.data.name:
                            temporary_variable = current_node.data
                            current_node.data = next_node.data
                            next_node.data = temporary_variable
                        next_node = next_node.next
                    current_node = current_node.next
            elif order == SortOrder.NON_ALPHABETIC:
                current_node = self.head
                while current_node.next is not None:
                    next_node = current_node.next
                    while next_node is not None:
                        if current_node.data.name < next_node.data.name:
                            temporary_variable = current_node.data
                            current_node.data = next_node.data
                            next_node.data = temporary_variable
                        next_node = next_node.next
                    current_node = current_node.next

    def print_resistors_with_tolerance_bigger_than(self, input_tolerance: float):
        current_node = self.head

        if self.head is None:
            print("List is empty")
            return

        while current_node is not None:
            if input_tolerance < current_node.data.tolerance:
                print(current_node.data)
            current_node = current_node.next

    def find_resistor_by_value(self, value: float):
        current_node = self.head

        if self.head is None:
            print("List is empty")
            return

        while current_node is not None:
            if value == current_node.data.value:
                print(current_node.data)
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        if self.head is None:
            print("List is empty")
            return

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    def delete_by_value(self, value: float):
        current_node = self.head

        if current_node is None:
            print("List is empty")
            return
        if (current_node is not None):
            if (value == current_node.data.value):
                self.head = current_node.next
                current_node = None
                return
        while(current_node is not None):
            if value == current_node.data.value:
                break
            prev = current_node
            current_node = current_node.next

        prev.next = current_node.next
        current_node = None

    def delete_list(self):
        current_node = self.head
        if self.head is None:
            print("List is empty")
            return

        while current_node is not None:
            current_node.data = None
            current_node = current_node.next