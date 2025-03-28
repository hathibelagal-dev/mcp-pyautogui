# MCP Server for PyAutoGUI 

<img width="958" alt="sshot1 pmg" src="https://github.com/user-attachments/assets/0eeb1e1e-78ae-4c8c-8427-86079b3d94fe" />

`mcp-pyautogui` implements a **Model Context Protocol (MCP)** server for **PyAutoGUI**. It provides control of mouse, keyboard, and screen interactions, allowing AI systems to automate tasks on a host machine.

The server runs over `stdio` transport and provides tools for clicking, typing, taking screenshots, and more, with a focus on simplicity and reliability. It’s designed for developers and AI enthusiasts looking to integrate desktop automation into their workflows.

## Features

- Control mouse movements, clicks, and drags.
- Simulate keyboard input (single keys, text, hotkeys).
- Capture screenshots and retrieve mouse position.
- Get the current operating system for platform-specific logic.
- Consistent error handling with boolean success indicators (where applicable).

## Prerequisites

- **Python 3.11+**

You'll also have to grant the relevant permissions.

<img width="950" alt="sshot2" src="https://github.com/user-attachments/assets/dcb193e0-e800-410f-aaf0-12319e120404" />

## Installation

Use `pip` to install the server.

```bash
pip install mcp-pyautogui
```

You can then run the following comand to determine the location at which the server was installed:

```bash
which mcp-pyautogui

# Sample output:
# /Users/bob/miniconda3/envs/desk/bin/mcp-pyautogui
```

Use that location when you're adding `mcp-pyautogui` to your `claude_desktop_config.json` file. Here's a sample configuration:

```json
{
  "mcpServers": {
    "mcp-pyautogui": {
      "command": "/Users/bob/miniconda3/envs/desk/bin/mcp-pyautogui",
      "args": [
          ""
      ]
  }
  }
}
```

## Usage
If you followed the above installation steps, you don't need to do anything else. Just use Claude Desktop and you should see all the tools this MCP server offers automatically. You could test this server by saying something like *"can you click at (200,200) ?"*.

The server runs over `stdio` transport, meaning it communicates through standard input/output. To use it, connect an MCP-compatible client (e.g., an AI assistant or custom script) that can send JSON-RPC commands and receive responses.

# Example Commands

- Click at (100, 200): `click(100, 200)` → Returns true if successful.
- Type "hello": `type_text("hello")` → Returns true.
- Take a screenshot: `take_screenshot("screenshot.png")` → Saves to screenshot.png.
- Get mouse position: `get_mouse_position()` → Returns (500, 300) (example).
- Copy text: `hotkey("ctrl c")` → Returns true.
- Get current operating system: `get_os()` → Returns "Windows" (if on Windows).

## Full List of Available Tools

- **`click(x, y)`**: Left-click at coordinates (x, y).  
  - *Parameters*: `x: int`, `y: int`  
  - *Return Type*: `bool`
- **`right_click(x, y)`**: Right-click at coordinates (x, y).  
  - *Parameters*: `x: int`, `y: int`  
  - *Return Type*: `bool`
- **`move_to(x, y)`**: Move mouse to coordinates (x, y) over 3 seconds.  
  - *Parameters*: `x: int`, `y: int`  
  - *Return Type*: `bool`
- **`drag_to(x, y, duration)`**: Drag mouse to (x, y) over specified duration (default 1.0s).  
  - *Parameters*: `x: int`, `y: int`, `duration: float`  
  - *Return Type*: `bool`
- **`type_text(text)`**: Type the given text.  
  - *Parameters*: `text: str`  
  - *Return Type*: `bool`
- **`press_key(key)`**: Press and release a single key (e.g., `'enter'`, `'space'`, `'a'`).  
  - *Parameters*: `key: str`  
  - *Return Type*: `bool`
- **`hotkey(keys)`**: Press multiple keys together (e.g., `'ctrl c'`). Space-separated string.  
  - *Parameters*: `keys: str`  
  - *Return Type*: `bool`
- **`scroll(amount)`**: Scroll up (positive) or down (negative) by amount.  
  - *Parameters*: `amount: int`  
  - *Return Type*: `bool`
- **`take_screenshot(filename)`**: Save a screenshot to the specified file (e.g., `'screen.png'`).  
  - *Parameters*: `filename: str`  
  - *Return Type*: `bool`
- **`get_mouse_position()`**: Get current mouse coordinates as (x, y).  
  - *Parameters*: None  
  - *Return Type*: `Tuple[int, int]`
- **`get_os()`**: Get the current OS name (e.g., `'Windows'`, `'macOS'`, `'Linux'`).  
  - *Parameters*: None  
  - *Return Type*: `str`
- **`double_click(x, y)`**: Perform a double-click at the given (x, y) coordinates.  
  - *Parameters*: `x: int`, `y: int`  
  - *Return Type*: `bool`
- **`get_screen_size()`**: Get the screen resolution as (width, height).  
  - *Parameters*: None  
  - *Return Type*: `Tuple[int, int]`
- **`pixel_color(x, y)`**: Get the RGB color of the pixel at (x, y). Returns (r, g, b) tuple.  
  - *Parameters*: `x: int`, `y: int`  
  - *Return Type*: `Tuple[int, int, int]`
