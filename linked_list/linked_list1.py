class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None

        for node in data_list:
            self.insert_at_end(node)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index!")
        if index == 0:
            self.head = self.head.next

        i_index = 0

        itr = self.head
        while itr:
            if i_index == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            i_index += 1

    def insert_at(self,index,data):
        if index == 0:
            self.insert_at_beginning(data)

        i_index = 0

        itr=self.head

        while itr:
            if i_index == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next

            i_index+=1
    def get_length(self):
        ll_length = 0
        itr = self.head
        while itr:
            itr = itr.next
            ll_length += 1
        return ll_length

    def print(self):
        llstring = ""

        if self.head is None:
            print("LL is empty")
            return

        itr = self.head

        while itr:
            llstring += str(itr.data) + "-->"
            itr = itr.next

        print(llstring)


if __name__ == "__main__":
    ll = LinkedList()

    # ll.print()

    # print(ll.get_length())

    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(99)

    # ll.insert_at_end(99)

    ll.insert_values(["apple", "banana", "cherry", "figs"])
    ll.print()
    print(ll.get_length())

    ll.remove_at(3)
    ll.print()
    print(ll.get_length())

    ll.insert_at(2, "melon")
    ll.print()
    print(ll.get_length())

