# Define a class called 'Node' to represent individual nodes in a network.
class Node:
    # Initialize a node with a 'name' and an empty list of 'edges.'
    def __init__(self, name):
        self.name = name
        self.edges = []

    # Method to add a relationship ('relation') to another 'node.'
    def add_edge(self, relation, node):
        self.edges.append((relation, node))

    # Method to represent the node as a string (its 'name').
    def __str__(self):
        return self.name

# Define a class called 'SemanticNetwork' to represent a network of nodes.
class SemanticNetwork:
    # Initialize the network with an empty list of 'nodes.'
    def __init__(self):
        self.nodes = []

    # Method to add a new 'node' to the network and return a reference to it.
    def add_node(self, name):
        node = Node(name)
        self.nodes.append(node)
        return node

    # Method to represent the entire network as a string.
    def __str__(self):
        result = "Semantic Network:\n"
        for node in self.nodes:
            result += f"{node} has relations:\n"
            for relation, related_node in node.edges:
                result += f"  - {relation}: {related_node}\n"
        return result

# Create an instance of the 'SemanticNetwork' class to start building a network.
semantic_net = SemanticNetwork()

# Enter a loop that allows users to interact with the semantic network.
while True:
    print("1. Add Node")
    print("2. Add Relationship")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        # If the user chooses to add a node, prompt for a 'node_name' and add it to the network.
        node_name = input("Enter node name: ")
        semantic_net.add_node(node_name)
        print(f"Node '{node_name}' added.")
    elif choice == '2':
        # If the user chooses to add a relationship, prompt for details and establish the relationship.
        node_name = input("Enter node name: ")
        relation = input("Enter relation: ")
        related_node_name = input("Enter related node name: ")

        # Find the nodes with the specified names in the network.
        node = next((n for n in semantic_net.nodes if n.name == node_name), None)
        related_node = next((n for n in semantic_net.nodes if n.name == related_node_name), None)

        if node and related_node:
            # If both nodes are found, add the relationship between them.
            node.add_edge(relation, related_node)
            print(f"Relationship added: {node_name} -> {relation} -> {related_node_name}")
        else:
            # If one or both nodes are not found, show an error message.
            print("One or both nodes not found.")
    elif choice == '3':
        # If the user chooses to exit, break out of the loop.
        break
    else:
        # If the user enters an invalid choice, show an error message.
        print("Invalid choice. Please try again.")

# Display the entire semantic network, including nodes and relationships.
print(semantic_net)
