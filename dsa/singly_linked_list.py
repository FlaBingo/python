class Node:
  def __init__(self, data: int) -> None:
    self.data = data
    self.next: Node | None = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

temp = head

while temp:
  print(temp.data, end=" -> ")
  temp = temp.next

print(None)

print(head.data)