class Node:  # Represents each node
    def __init__(self, data=None, next=None):
        self.data = data  # data part of the node
        self.next = next  # address of the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Points to the head(first node) of the Linked List. Initial value is set to none.

    # TC = O(1)
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    # TC = O(n)  (This method can also be optimized to work in O(1) by keeping an extra pointer to the tail of the linked list)
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # TC = O(n)
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == (index - 1):
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    # TC = O(1)
    def insert_after_node(self, prev_node, data_to_insert):
        node = Node(data_to_insert, prev_node.next)
        prev_node.next = node

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurrence of data_after value in linked list.
        # Now insert data_to_insert after data_after node.
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == (index-1):
                itr.next = itr.next.next
                break

            itr = itr.next
            counter += 1

    def remove_by_value(self, data):
        # Remove first node that contains data

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return  # why return (Answer: because otherwise the next lines will execute (not supposed to execute) & give error)

        itr = self.head
        while itr.next:  # why itr.next and not just itr (else will be problem for last element)
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        linked_list_string = ''

        while itr:
            linked_list_string += str(itr.data) + '-->'
            itr = itr.next

        print(linked_list_string)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count


if __name__ == '__main__':

#   ll = LinkedList()
#   ll.insert_at_beginning(5)
#   ll.insert_at_beginning(89)
#   ll.insert_at_end(79)

#   ll.insert_values(["sandwich", "burger", "pizza", "pasta", "maggie"])
#   ll.print()

#   ll.remove_at(3)
#   ll.print()

#   ll.insert_at(0, "momos")
#   ll.insert_at(2, "Subway")
#   ll.print()

#   print("Linked list size = ", str(ll.get_length()))

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()