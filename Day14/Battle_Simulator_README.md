
# Fantasy Battle Simulator

## Description

Welcome to the **Fantasy Battle Simulator**! This engaging Python project allows players to step into a thrilling world where they can battle fearsome monsters. The simulator encapsulates the essence of role-playing games by embodying player interactions and monster confrontations in a structured format. Through this project, users can experience the excitement of combat and strategic planning.

## Features

- **Player Creation**: Define your hero with a name, health, and energy attributes.
- **Monster Encounters**: Feature monsters with unique names, health, and damage capabilities.
- **Combat Mechanics**: Engage in combat where players can utilize their energy to attack monsters.
- **Health Management**: Monitor the health and energy levels of both players and monsters in real-time.

## Installation

To get started with the **Fantasy Battle Simulator**, follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/fantasy-battle-simulator.git
   cd fantasy-battle-simulator
   ```

2. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Simulator**: Execute the Python script to start the game:
   ```bash
   python simulator.py
   ```

## Usage

Here's a quick walkthrough of how to engage with the simulator:

1. **Create Players**: Instantiate `Player` objects by specifying their names:
   ```python
   player1 = Player("Gangga")
   player2 = Player("Rudy")
   ```

2. **Initialize Monsters**: Create monsters with names and health attributes:
   ```python
   monster = Monster("Lizard", 500)
   ```

3. **Engage in Combat**: Use the `attack` method where players can attack the monsters:
   ```python
   player1.attack(monster, 50)
   player2.attack(monster, 50)
   ```

4. **Display Status**: Check the health and energy levels of players and monsters with the `info` method:
   ```python
   print(player1.info())
   print(monster.info())
   ```

## Example

Here’s a brief code snippet demonstrating the usage:

```python
# Create players and a monster
player = Player("Gangga")
monster = Monster("Lizard")

# Player attacks the monster
result = player.attack(monster, 50)
print(result)

# Display current status
print(player.info())
print(monster.info())
```

## Contribution

We welcome contributions! If you'd like to enhance the **Fantasy Battle Simulator** or report a bug, please consider the following:

1. **Fork the Repository**: Click the "Fork" button at the top-right of the page.
2. **Create a New Branch**: 
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make Your Changes**: Implement your feature or fix the bug.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add Your Feature"
   ```
5. **Push to the Branch**: 
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Open a Pull Request**: Go to the original repository and click on "New pull request".

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Happy Battling!

Dive into the world of strategic battles and enjoy creating engaging stories with your players and monsters!
