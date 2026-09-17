# Cherry Chase

Cherry Chase is an embedded systems game developed in C for the STM32F031K6 microcontroller using the Nucleo-F031K6 development board.

The project was created as part of my Computer Science coursework and demonstrates low-level embedded programming, GPIO input handling, SPI display communication, graphics rendering, collision detection, and basic game logic.

The player controls an animated character using physical directional buttons and moves around the display to reach the target.

---

## Features

- Four-direction player movement using physical GPIO buttons
- Animated character sprites
- Horizontal and vertical sprite orientation
- Collision detection
- Win-state detection
- Custom bitmap graphics
- Text and number rendering
- 128 × 160 colour display support
- SPI communication with the display
- Custom graphics functions for:
  - Pixels
  - Images
  - Lines
  - Rectangles
  - Circles
  - Filled circles
  - Text
- SysTick-based timing and delays
- Custom BMP-to-C image conversion utility

---

## Controls

The game uses four physical buttons connected to GPIO pins:

| Action | GPIO |
|---|---|
| Move Right | PB4 |
| Move Left | PB5 |
| Move Up | PA8 |
| Move Down | PA11 |

The character sprite changes orientation depending on the direction of movement.

---

## Technologies Used

- C
- Python
- STM32
- CMSIS
- PlatformIO
- GPIO
- SPI
- Embedded Systems Programming

### Hardware Target

- STM32F031K6
- Nucleo-F031K6 development board
- 128 × 160 colour display
- Physical directional buttons

---

## How It Works

### Player Movement

The program continuously reads the state of four GPIO inputs.

When a directional button is pressed, the player's `x` or `y` position is updated.

The character is restricted to the visible game area so it cannot move outside the screen.

Different sprite images are used depending on the direction of movement to create simple animation.

### Collision Detection

The game checks the player's position against the target area.

When the player overlaps the target, the game displays:

```text
WIN
```

on the screen.

### Display System

The project contains a custom display driver which communicates with the screen using SPI.

The display code supports operations including:

```text
putPixel()
putImage()
drawLine()
drawRectangle()
drawCircle()
fillCircle()
printText()
printTextX2()
printNumber()
```

This allows the game graphics to be drawn directly from the STM32 without using a high-level graphics framework.

---

## Custom Graphics

Several bitmap images are used for the game interface and character animations, including:

```text
CC.bmp
Cherriesfix.bmp
START1.bmp
EXIT_IMAGE.bmp
deco1.bmp
deco2.bmp
deco3.bmp
```

These include the Cherry Chase graphics, menu elements, and character animation frames.

A Python utility called:

```text
bmptoh.py
```

converts BMP image pixels into 16-bit colour values that can be stored as C arrays and rendered by the microcontroller.

Example:

```bash
python bmptoh.py image.bmp
```

The resulting pixel values can then be included in the C source code.

---

## Project Structure

```text
CherryChase/
│
├── include/
│   └── README
│
├── lib/
│   └── README
│
├── src/
│   ├── main.c
│   ├── display.c
│   ├── display.h
│   └── font5x7.h
│
├── test/
│   └── README
│
├── CC.bmp
├── Cherriesfix.bmp
├── EXIT_IMAGE.bmp
├── START1.bmp
├── deco1.bmp
├── deco2.bmp
├── deco3.bmp
├── bmptoh.py
└── platformio.ini
```

### `main.c`

Contains the main game logic, including:

- Hardware initialization
- GPIO configuration
- Player movement
- Sprite animation
- Collision detection
- Game loop
- Timing

### `display.c`

Implements the low-level display and graphics functionality, including:

- SPI initialization
- Display initialization
- Pixel rendering
- Bitmap rendering
- Drawing primitives
- Text rendering
- Colour conversion

### `display.h`

Contains function declarations for the display and graphics system.

### `font5x7.h`

Contains a 5 × 7 ASCII bitmap font used for displaying text on the screen.

### `bmptoh.py`

Python utility used to convert bitmap images into colour data suitable for use in the embedded C application.

---

## ⚙️ Building the Project

This project uses PlatformIO.

### Requirements

- Visual Studio Code
- PlatformIO
- Nucleo-F031K6 board
- Compatible SPI colour display

Clone the repository:

```bash
git clone https://github.com/Rinat300706/cherrychasethis.git
```

Open the project directory:

```bash
cd cherrychasethis
```

Build using PlatformIO:

```bash
pio run
```

Upload to the connected board:

```bash
pio run --target upload
```

The PlatformIO environment is configured as:

```ini
[env:nucleo_f031k6]
platform = ststm32
board = nucleo_f031k6
framework = cmsis
```

---

## What I Learned

This project gave me practical experience with:

- Embedded C programming
- Programming STM32 microcontrollers
- Direct register manipulation
- GPIO configuration and input handling
- SPI communication
- Hardware/software integration
- Rendering graphics on embedded displays
- Bitmap and pixel representation
- Collision detection
- Real-time game loops
- Interrupt-based timing using SysTick
- Debugging embedded applications
- PlatformIO project development

---

## Academic Project

Cherry Chase was developed as part of my Computer Science coursework at Technological University Dublin.

The project provided practical experience working directly with microcontroller hardware and developing an interactive embedded application without relying on a high-level game engine or graphics framework.

---

## Author

**Rinat Galearschi**

Computer Science Student  
Technological University Dublin
