# birthday
word of mouth phone tree

Here's a README file for the Birthday App:

---

# Birthday App

This Birthday App uses a phone tree to notify people about a birthday, collect birthday wishes, and visualize the communication network.

## Features

- **Phone Tree Creation**: Initializes a phone tree for managing notifications.
- **Phone Tree Communication**: Sends out birthday notifications through the phone tree.
- **Notification Dissemination and Response Collection**: Collects birthday wishes from the network.
- **Visualization**: Displays the communication network and responses.

## Requirements

- Python 3.x
- `networkx` library
- `matplotlib` library
- `matplotlib-venn` library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install the required libraries using pip:

```bash
pip install networkx matplotlib matplotlib-venn
```

## Usage

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script:

```bash
python birthday_app.py
```

## Code Overview

### Functions

1. **create_phone_tree()**: Creates and returns a directed graph representing the phone tree.
2. **draw_graph(G, title)**: Draws the graph with the given title.
3. **phone_tree_communication(G, source, message)**: Simulates phone tree communication, sending a message from the source to all nodes.
4. **disseminate_birthday_notification(G, source, notification)**: Disseminates a birthday notification through the phone tree.
5. **collect_birthday_wishes(G, source)**: Collects birthday wishes from the network.
6. **rank_birthday_wishes(wishes)**: Ranks collected birthday wishes based on the length of the messages.

### Main Application

The main application creates a phone tree, simulates sending out a birthday notification, collects birthday wishes, ranks them, and visualizes the communication network.

## Example Output

When you run the script, you will see:

1. A graphical representation of the phone tree.
2. A log of the birthday notification communication.
3. A log of the dissemination of the birthday notification.
4. Collected birthday wishes.
5. Ranked birthday wishes.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, feel free to reach out to the repository owner.

---

This README provides a comprehensive guide on the Birthday App's features, installation, usage, and other relevant information.
