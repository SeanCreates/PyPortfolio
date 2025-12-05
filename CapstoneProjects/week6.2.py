#Singly Linked Lists
"""A dynamic data structure: data structure - organization of data"""
#nodes and references(links)
class Node:
    """Represents a node in the data structure - a single element in the data structure"""

    def __init__(self, data):
        #1 Data held by the node
        self.data = data
        #2 Pointer to the next node in the sequence (initially none)
        self.next = None

class SinglyLinkedList():
    """manages the link structure starting from the head node"""

    def __init__(self):
        #The starting point of the list that is initially empty
        self.head = None
    def insert_at_beginning(self, data):
        """Inserts a new node at the head of the list (0(1)operation)"""
        new_node = Node(data)

        #1 new nodes next pointer points to the current head
        new_node.next = self.head

        #2 The head is updated to the new node
        self.head = new_node
        print(f"Inserted {data} at the beginning of the list.")
    def insert_at_end(self, data):
        """Inserts a new node at the end of the list (0(n)Operation"""
        new_node = Node(data)

        #case 1 : If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end of the list (new head).")
            return

        #case 2: Traverse the list to find the last node
        last = self.head
        while last.next:
            last = last.next

        #the last nodes pointer points to the new node
        last.next = new_node
        print(f"Inserted {data} at the end of the list.")

    def display(self):
        """Prints the data of all nodes n the list by traversing from the head"""
        current = self.head
        elements = []

        while current:
            #Add the current node's data to the list of elements
            elements.append(current.data)
            #move the current pointer to the next node
            current = current.next
            #print the final sequence of elements
            print(f"\n Linked List: {'->'.join(elements)}")


def main():
    # Create the list manager object
    my_list = SinglyLinkedList()

    # 1. Insert elements at the end
    my_list.insert_at_end("Task 1")
    my_list.insert_at_end("Task 2")
    my_list.insert_at_end("Task 3")
    my_list.display() # Output: Task 1 -> Task 2 -> Task 3

    # 2. Insert at the beginning (changes the head)
    my_list.insert_at_beginning("NEW HEAD")
    my_list.display() # Output: NEW HEAD -> Task 1 -> Task 2 -> Task 3

if __name__ == "__main__":
    main()

            





