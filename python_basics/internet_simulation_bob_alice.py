# prompt: Write a set of Python classes that can simulate an Internet application in which one party, Alice, is periodically creating a set of packets that she wants to send to Bob. An Internet process is continually checking if Alice has any packets to send, and if so, it delivers them to Bob’s computer, and Bob is periodically checking if his computer has a packet from Alice, and, if so, he reads and deletes it


class Alice:
    def __init__(self, name, internet):
        self.name = name
        self.internet = internet
        self.packets = []

    def create_packet(self, data):
        self.packets.append(data)

    def send_packets(self):
        for packet in self.packets:
            self.internet.send_packet(packet)
        self.packets = []


class Bob:
    def __init__(self, name, internet):
        self.name = name
        self.internet = internet
        self.packets = []

    def receive_packets(self):
        while self.internet.has_packets():
            self.packets.append(self.internet.receive_packet())

    def read_packets(self):
        for packet in self.packets:
            print(f"{self.name} received packet: {packet}")
        self.packets = []


class Internet:
    def __init__(self):
        self.packets = []

    def send_packet(self, packet):
        self.packets.append(packet)

    def receive_packet(self):
        return self.packets.pop(0)

    def has_packets(self):
        return len(self.packets) > 0

if __name__ == '__main__':
    internet = Internet()
    alice = Alice("Alice", internet)
    bob = Bob("Bob", internet)

    for i in range(10):
        alice.create_packet(f"Packet {i}")
        alice.send_packets()
        bob.receive_packets()
        bob.read_packets()
