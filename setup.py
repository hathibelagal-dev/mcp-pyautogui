from setuptools import setup, find_packages

long_description = ""
with open("README.md", "r", encoding="utf-8") as f:
    contents = f.readlines()
    for line in contents:
        if "user-attachments/assets" not in line:
            long_description += line

setup(
    name="mcp-pyautogui",
    version="0.0.2",
    author="Ashraff Hathibelagal",
    description="A powerful MCP server for PyAutoGUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hathibelagal-dev/mcp-pyautogui",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[
        "pyautogui",
        "mcp"
    ],
    entry_points={
        "console_scripts": [
            "mcp-pyautogui=mcp_pyautogui.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="ai mcp claude llm llama pyautogui",
    project_urls={
        "Source": "https://github.com/hathibelagal-dev/mcp-pyautogui",
        "Tracker": "https://github.com/hathibelagal-dev/mcp-pyautogui/issues",
    },
)
