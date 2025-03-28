# MCP Server for PyAutoGUI 

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

## Usage
The server runs over `stdio` transport, meaning it communicates through standard input/output. To use it, connect an MCP-compatible client (e.g., an AI assistant or custom script) that can send JSON-RPC commands and receive responses.

# Example Commands

- Click at (100, 200): `click(100, 200)` → Returns true if successful.
- Type "hello": `type_text("hello")` → Returns true.
- Take a screenshot: `take_screenshot("screenshot.png")` → Saves to screenshot.png.
- Get mouse position: `get_mouse_position()` → Returns (500, 300) (example).
- Copy text: `hotkey("ctrl c")` → Returns true.
- Get current operating system: `get_os()` → Returns "Windows" (if on Windows).

