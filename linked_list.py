class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def iterate(self):
        if self.head is None:
            print('The list is empty')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, value, index):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                temp_node = self.head
                itr_count = 0
                while itr_count < index - 1:
                    temp_node = temp_node.next
                    itr_count += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def search(self, node_value):
        if self.head is None:
            print('The list is empty')
        else:
            node = self.head
            while node is not None:
                if node.value == node_value:
                    return node.value
                node = node.next
            return 'The value does not exist in the list'

    def pop(self):
        if self.head is None:
            print('The list is empty')
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node

    def delete_node(self, index):
        if self.head is None:
            print('The list is empty')
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            else:
                temp_node = self.head
                itr_count = 0
                while itr_count < index - 1:
                    temp_node = temp_node.next
                    itr_count += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    def delete_list(self):
        if self.head is None:
            print('The list is empty')
        else:
            self.head = None
            self.tail = None


singly_linked_list = SLinkedList()
singly_linked_list.insert(1, 1)
singly_linked_list.insert(0, 0)
singly_linked_list.append(3)
singly_linked_list.append(2)
singly_linked_list.delete_list()
singly_linked_list.iterate()
