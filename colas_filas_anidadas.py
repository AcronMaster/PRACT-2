class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"     Customer: {self.get_customer()}")
        print(f"     Quantity: {self.get_qtty()}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer
class QueueInterface:
    def size(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def is_empty(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def front(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def enqueue(self, info):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def dequeue(self):
        raise NotImplementedError("This method should be overridden by subclasses.")
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

class Queue(QueueInterface):
    def __init__(self):
        self.front_node = None  # Apunta al primer nodo
        self.rear_node = None   # Apunta al último nodo
        self.size_count = 0

    def size(self):
        return self.size_count

    def is_empty(self):
        return self.front_node is None

    def front(self):
        if self.is_empty():
            return None
        return self.front_node.get_data()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next_node = new_node
            self.rear_node = new_node
        self.size_count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self.front_node.get_data()
        self.front_node = self.front_node.get_next()
        self.size_count -= 1
        if self.front_node is None:  # Si no quedan más elementos
            self.rear_node = None
        return removed_data

    def print_queue(self):
        node = self.front_node
        while node is not None:
            node.get_data().print()  # Imprime la información de la orden
            node = node.get_next()
# Crear la cola de pedidos
order_queue = Queue()

# Crear algunos pedidos (orders)
order1 = Order(10, "Customer A")
order2 = Order(5, "Customer B")
order3 = Order(7, "Customer C")

# Encolar las órdenes
order_queue.enqueue(order1)
order_queue.enqueue(order2)
order_queue.enqueue(order3)

# Imprimir el contenido de la cola
print("Contenido de la cola:")
order_queue.print_queue()

# Desencolar una orden
print("\nDesencolando una orden...")
removed_order = order_queue.dequeue()
if removed_order:
    removed_order.print()

# Ver el frente de la cola sin desencolar
print("\nFrente de la cola:")
front_order = order_queue.front()
if front_order:
    front_order.print()

# Ver el tamaño de la cola
print(f"\nTamaño de la cola: {order_queue.size()}")

# Volver a imprimir la cola después de desencolar
print("\nContenido de la cola después de desencolar:")
order_queue.print_queue()
