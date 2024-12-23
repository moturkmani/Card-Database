# Pokemon Card Database GUI

This Python project provides a graphical user interface (GUI) for managing a database of Pokémon cards. Users can add new entries, search for cards, edit existing entries, and save them in a text file.

## Features

- **Add New Card Entries**: Enter details like year, card number, name, set, condition, and tags.
- **Search for Cards**: Search by tags, card number, or name.
- **Edit Card Details**: Modify details of existing cards.
- **Persistent Storage**: Saves card details to a text file on the user's desktop (`cards_list.txt`).
- **User-Friendly GUI**: Simple and intuitive interface built with Tkinter.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## File Structure

The script automatically creates a text file `cards_list.txt` on the user's desktop to store card details.

## Installation

1. Clone this repository or download the script file.
2. Make sure you have Python installed.
3. Run the script using:

   ```bash
   python card_database.py
   ```

## Usage

1. **Main Menu**: Choose to add a new entry, look up a Pokémon card, or exit the application.
2. **New Entry**: Fill out all fields to add a new card to the database.
3. **Search**: Search for cards by tags, card number, or name.
4. **Edit**: Select a search result to edit its details.

## Code Highlights

- **Centralized Database Management**:
  - All card data is saved in a text file for simplicity.
  - Entries are formatted for easy reading and editing.

- **Responsive UI**:
  - Windows are dynamically centered and sized.
  - Buttons and labels are styled for clear navigation.

- **Search and Edit Functionalities**:
  - Search results are displayed as buttons for quick access.
  - Edit window allows full modification of card details.

## Example Entry Format

When a card is saved, it is stored in the following format:

```
Year: 2023  Card Number: 001  Card Name: Pikachu  Set Name: Base Set  Condition: Mint  Tags: Electric, Rare
```

## Screenshots

### Main Menu
- Add new cards, search, or exit.

### Add New Entry
- Form fields for detailed card information.

### Search
- Search by tags, card number, or name and display results.

### Edit Entry
- Modify and save existing card details.

## Contribution

Feel free to submit issues or pull requests to improve this project.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the Pokémon community for inspiration!

---
Start organizing your Pokémon card collection today with this simple and effective database tool!

