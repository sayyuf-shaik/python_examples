class Node:
    """Node class for linked list elements"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List implementation"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None

    def append(self, data):
        """Add a node at the end of the list"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Add a node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        """Insert a new node after the given node"""
        if not prev_node:
            print("Previous node must be in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key):
        """Delete node containing the given data"""
        curr_node = self.head

        # If head node contains the key
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        # Search for the key
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        # If key not found
        if curr_node is None:
            return

        # Unlink the node
        prev.next = curr_node.next
        curr_node = None

    def delete_at_position(self, position):
        """Delete node at given position (0-based index)"""
        if self.is_empty():
            return

        curr_node = self.head

        # If position is 0 (head)
        if position == 0:
            self.head = curr_node.next
            curr_node = None
            return

        # Find the position
        for i in range(position - 1):
            curr_node = curr_node.next
            if curr_node is None:
                break

        # If position is out of bounds
        if curr_node is None or curr_node.next is None:
            return

        # Unlink the node
        next_node = curr_node.next.next
        curr_node.next = None
        curr_node.next = next_node

    def length(self):
        """Return the length of the list"""
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def search(self, key):
        """Search for a node containing the given data"""
        curr_node = self.head
        while curr_node:
            if curr_node.data == key:
                return True
            curr_node = curr_node.next
        return False

    def reverse(self):
        """Reverse the linked list in place"""
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def print_list(self):
        """Print all elements of the list"""
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")


# Example usage
if __name__ == "__main__":
    llist = LinkedList()

    # Append some nodes
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)

    print("Original list:")
    llist.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> None

    # Prepend a node
    llist.prepend(0)
    print("\nAfter prepending 0:")
    llist.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> None

    # Insert after node with value 2
    node = llist.head.next.next.next  # Node with value 2
    llist.insert_after(node, 2.5)
    print("\nAfter inserting 2.5 after 2:")
    llist.print_list()  # Output: 0 -> 1 -> 2 -> 2.5 -> 3 -> 4 -> None

    # Delete node with value 2.5
    llist.delete(2.5)
    print("\nAfter deleting 2.5:")
    llist.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> None

    # Reverse the list
    llist.reverse()
    print("\nAfter reversing:")
    llist.print_list()  # Output: 4 -> 3 -> 2 -> 1 -> 0 -> None

    print("\nLength of list:", llist.length())  # Output: 5
    print("Is 3 in list?", llist.search(3))  # Output: True
    print("Is 5 in list?", llist.search(5))  # Output: False