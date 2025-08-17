
# 🎨 Color Dot Art with Turtle 🐢

This fun project combines Python's `turtle` module with the `colorgram` library to create beautiful abstract art with colorful dots! Inspired by randomness and color play, it generates a vibrant grid of dots, making each run a unique artistic experience.

## 🚀 Key Features
- **Turtle Graphics**: Uses Python’s Turtle to draw colorful dots 🖌️.
- **Randomized Colors**: Picks colors from an image using the `colorgram` library 🎨.
- **Fast Drawing**: With `turtle.speed("fastest")`, the art is drawn in no time ⚡.
- **Interactive Screen**: Just click anywhere to close the program 🖱️.

## 💻 Installation

To get started, you’ll need Python and the required libraries:

1. **Install Python**: If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
2. **Install the required libraries**:
    ```bash
    pip install colorgram
    ```

## 🧑‍💻 How It Works
1. **Extract Colors**: The program uses `colorgram.extract()` to pull a palette of colors from an image (`bank_color.jpg`).
2. **Create Dot Art**: Turtle moves across the screen, placing a dot of randomly chosen color in each position 🎨.
3. **Grid Layout**: Dots are arranged in a neat grid with 40-pixel spacing, creating a mesmerizing effect 🔲.

## 🏁 Usage
1. **Run the Program**: Once you’ve installed the libraries, run the Python script.
2. **Enjoy the Art**: Watch as a grid of colorful dots appears on the screen. Click anywhere to close it when you're done 🌈.

## 📝 Code Breakdown
- **Turtle Setup**: The turtle is set up with `niko = Turtle()`, given a turtle shape, and hidden to keep the drawing process neat.
- **Color Extraction**: Colors are extracted from the image `bank_color.jpg` using `colorgram` and stored in the `colors` list 🌈.
- **Dot Drawing**: A loop runs through rows and columns, where turtle draws a dot in a random color selected from the palette 🖍️.

## 📸 Example Output
The program generates a colorful grid of dots, like an abstract art piece! Each run is different, thanks to the random color selection 🎨.

## 📝 License
This project is open-source! Feel free to modify and play around with the code as you like 🔓.
