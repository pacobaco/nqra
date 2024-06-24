import networkx as nx
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Create a directed graph for the phone tree
def create_phone_tree():
    G = nx.DiGraph()
    nodes = ['Coordinator', 'Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6', 'Person7', 'Person8']
    G.add_nodes_from(nodes)
    
    edges = [
        ('Coordinator', 'Person1'), ('Coordinator', 'Person2'), ('Person1', 'Person3'),
        ('Person1', 'Person4'), ('Person2', 'Person5'), ('Person2', 'Person6'),
        ('Person4', 'Person7'), ('Person5', 'Person8')
    ]
    G.add_edges_from(edges)
    return G

# Draw the graph
def draw_graph(G, title):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, edge_color='gray')
    plt.title(title)
    plt.show()

# Simulate phone tree communication
def phone_tree_communication(G, source, message):
    visited = set()
    queue = [source]
    communication_log = []
    
    while queue:
        current_node = queue.pop(0)
        visited.add(current_node)
        
        personalized_message = f"{current_node}, you have a message: {message}. How are you today?"
        communication_log.append(personalized_message)
        
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)
    
    return communication_log

# Define birthday wishes each person has
birthday_wishes = {
    'Person1': "Happy Birthday! Have a fantastic day!",
    'Person2': "Wishing you a day filled with love and cheer!",
    'Person3': "Happy Birthday! Enjoy your special day!",
    'Person4': "Many happy returns of the day!",
    'Person5': "Wishing you all the best on your special day!",
    'Person6': "Happy Birthday! Hope you have a great year ahead!",
    'Person7': "Cheers to you on your birthday!",
    'Person8': "Happy Birthday! Make it a memorable one!"
}

# Function to disseminate birthday notification
def disseminate_birthday_notification(G, source, notification):
    visited = set()
    queue = [source]
    notification_log = []

    while queue:
        current_node = queue.pop(0)
        visited.add(current_node)
    
        log_entry = f"Birthday notification '{notification}' sent to {current_node}"
        notification_log.append(log_entry)
    
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)

    return notification_log

# Function to collect birthday wishes from the network
def collect_birthday_wishes(G, source):
    collected_wishes = {}
    queue = [source]
    visited = set()

    while queue:
        current_node = queue.pop(0)
        visited.add(current_node)
    
        if current_node in birthday_wishes:
            collected_wishes[current_node] = birthday_wishes[current_node]
    
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)

    return collected_wishes

# Function to rank collected birthday wishes
def rank_birthday_wishes(wishes):
    return sorted(wishes.items(), key=lambda item: len(item[1]), reverse=True)

# Main application
if __name__ == "__main__":
    G = create_phone_tree()
    
    print("Drawing Phone Tree Graph...")
    draw_graph(G, "Phone Tree for Birthday Notification")
    
    notification = "It's Jane's Birthday today! Don't forget to wish her!"
    communication_log = phone_tree_communication(G, 'Coordinator', notification)
    
    print("Phone Tree Communication Log:")
    for log in communication_log:
        print(log)
    
    notification_log = disseminate_birthday_notification(G, 'Coordinator', notification)
    
    print("\nBirthday Notification Dissemination Log:")
    for log in notification_log:
        print(log)
    
    wishes = collect_birthday_wishes(G, 'Coordinator')
    
    print("\nCollected Birthday Wishes:")
    for person, wish in wishes.items():
        print(f"{person}: {wish}")
    
    ranked_wishes = rank_birthday_wishes(wishes)
    
    print("\nRanked Birthday Wishes:")
    for rank, (person, wish) in enumerate(ranked_wishes, start=1):
        print(f"{rank}. {person}: {wish}")
    
    # Optionally visualize shared wishes using Venn diagrams and network graphs if applicable
    # This part is more relevant if there were overlapping wishes, which isn't the case here
    # but is left here for completeness based on the previous functionalities
    # create_venn_diagram(wishes['Person1'], wishes['Person2'], wishes['Person3'], ('Person1', 'Person2', 'Person3'))
    draw_graph(G, "Network of Birthday Wishes")
