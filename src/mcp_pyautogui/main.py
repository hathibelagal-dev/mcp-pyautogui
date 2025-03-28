import pyautogui
from mcp.server.fastmcp import FastMCP
import platform

server = FastMCP("MCP for PyAutoGUI")

@server.tool()
def click(x: int, y: int) -> bool:
    """Perform a mouse click at the given (x, y) coordinates. Returns true if success, else false."""
    try:
        pyautogui.click(x, y)
        return True
    except Exception as e:
        return False

@server.tool()
def type_text(text: str) -> bool:
    """Type the given text using the keyboard. Returns true if success, else false."""
    try:
        pyautogui.typewrite(text)
        return True
    except Exception as e:
        return False

@server.tool()
def move_to(x, y) -> bool:
    """Move the mouse to the given (x, y) coordinates. Returns true if success, else false."""
    try:
        pyautogui.moveTo(x, y, duration=2.0)
        return True
    except Exception as e:
        return False

@server.tool()
def right_click(x: int, y: int) -> bool:
    """Perform a right-click at the given (x, y) coordinates. Returns true if success, else false."""
    try:
        pyautogui.rightClick(x, y)
        return True
    except Exception as e:
        return False

@server.tool()
def press_key(key: str) -> bool:
    """Press and release a single key (e.g., 'enter', 'space', 'a'). Returns true if success, else false."""
    try:
        pyautogui.press(key)
        return True
    except Exception as e:
        return False

@server.tool()
def take_screenshot(filename: str) -> bool:
    """Take a screenshot and save it to the specified filename. Returns true if success, else false."""
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        return True
    except Exception as e:
        return False

@server.tool()
def scroll(amount: int) -> bool:
    """Scroll the mouse up (positive amount) or down (negative amount). Returns true if success, else false."""
    try:
        pyautogui.scroll(amount)
        return True
    except Exception as e:
        return False

@server.tool()
def get_mouse_position() -> str:
    """Get the current (x, y) coordinates of the mouse. Returns (x, y). The string will have negative values if failed."""
    try:
        x, y = pyautogui.position()
        return str((x, y))
    except Exception as e:
        return str((-1, -1))

@server.tool()
def hotkey(keys: str) -> bool:
    """Press multiple keys together (e.g., 'ctrl+c'). Keys should be space-separated. Returns true if success, else false."""
    try:
        key_list = keys.split()
        pyautogui.hotkey(*key_list)
        return True
    except Exception as e:
        return False
    
@server.tool()
def double_click(x: int, y: int) -> bool:
    """Perform a double-click at the given (x, y) coordinates. Returns true if success, else false."""
    try:
        pyautogui.doubleClick(x, y)
        return True
    except Exception as e:
        return False

@server.tool()
def get_screen_size() -> str:
    """Get the screen resolution as (width, height). Returns a string in the format (width, height). On failure it returns (-1, -1)"""
    try:
        width, height = pyautogui.size()
        return (width, height)
    except Exception as e:
        return (-1, -1)
    
@server.tool()
def get_pixel_color(x: int, y: int) -> str:
    """Get the RGB color of the pixel at (x, y). Returns a string in the format (r, g, b). On failure it returns (-1, -1, -1)"""
    try:
        r, g, b = pyautogui.pixel(x, y)
        return str((r, g, b))
    except Exception as e:
        return str((-1, -1, -1))

@server.tool()
def get_os() -> str:
    """Get the name of the current operating system (e.g., 'Windows', 'macOS', 'Linux'). Returns OS name or 'Unknown' on failure."""
    try:
        os_name = platform.system()
        if os_name == "Windows":
            return "Windows"
        elif os_name == "Darwin":
            return "macOS"
        elif os_name == "Linux":
            return "Linux"
        else:
            return os_name
    except Exception as e:
        return "Unknown"       

def main():
    try:
        server.run(transport="stdio")
    except KeyboardInterrupt:
        print("Server stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")        

if __name__ == "__main__":
    main()