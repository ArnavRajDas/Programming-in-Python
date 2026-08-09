#  Setting Up VS Code for Python

![VS Code](https://img.shields.io/badge/Editor-VS%20Code-blue?style=for-the-badge&logo=visualstudiocode)
![Python](https://img.shields.io/badge/Python-Ready-green?style=for-the-badge&logo=python)
---


## Before setting up VS Code let's talk about IDE.

### *What is an IDE?*
- An *Integrated Development Environment* (IDE) is a software application that provides tools for *writing, testing and debugging code*

### Popular Python IDEs
* VS Code: *Lightweight, customizable and support extensions* for Python (We are using thi one as our primary IDE)

* PyCharm: Powerful IDE with advanced features for professional developers

* Jupyter Notebook: Great for data science and interactive coding

* IDLE: Comes pre installed wiyh Python, good for beginners

---
### We will use VS Code:
Visual Studio Code, commonly called **VS Code**, is a popular code editor used for writing and managing programs.

In this repository, VS Code will be used to write Python programs.

---

##  Step 1 — Install VS Code

Download Visual Studio Code from:

**https://code.visualstudio.com/**

Download the Windows version and complete the installation.

---
 
## Step 2 — Create Your Python Workspace

Create a folder for your Python programs.

For example:

```text
Programming-in-Python/
```

Open this folder in VS Code.

You can also create a smaller practice folder such as:

```text
Python-Practice/
```

---

##  Step 3 — Install the Python Extension

Open VS Code.

Go to the **Extensions** panel.

Search for:

```text
Python
```

Install the official Python extension provided by Microsoft.

---

##  Step 4 — Select the Python Interpreter

Open a Python file:

```text
hello.py
```

VS Code may automatically detect your Python installation.

If it does not:

1. Open the Command Palette.
2. Search for:

```text
Python: Select Interpreter
```

3. Select your installed Python 3 version.

---

##  Step 5 — Create a Python File

Create:

```text
hello.py
```

Add:

```python
print("Hello, Python!")
```

Save the file.

---

##  Step 6 — Run the Program

You can run the program using the **Run Python File** button in VS Code.

You can also use the terminal:

```bash
python hello.py
```

Expected output:

```text
Hello, Python!
```

---

##  VS Code Terminal

You can open the integrated terminal using:

```text
Terminal → New Terminal
```

You can then execute Python commands directly.

Example:

```bash
python --version
```

---

##  Recommended Workspace Structure

Your learning repository will eventually look something like:

```text
Programming-in-Python/
│
├── 01_Getting_Started/
├── 02_Python_Basics/
├── 03_Operators/
├── 04_Control_Flow/
├── ...
└── README.md
```

---

##  Useful VS Code Features

You will frequently use:

### Explorer

Used to browse your files.

### Editor

Used to write code.

### Terminal

Used to run commands.

### Extensions

Used to add functionality to VS Code.

### Command Palette

Shortcut:

```text
Ctrl + Shift + P
```

It allows you to quickly search for VS Code commands.

---

##  Useful Shortcuts

| Shortcut           | Action          |
| ------------------ | --------------- |
| `Ctrl + S`         | Save            |
| `Ctrl + C`         | Copy            |
| `Ctrl + V`         | Paste           |
| `Ctrl + X`         | Cut             |
| `Ctrl + Z`         | Undo            |
| `Ctrl + Shift + P` | Command Palette |
| `Ctrl + ``         | Open Terminal   |


 ### Enable Auto Save (small but powerful)
 This automatically saves your files while coding. No need to press Ctrl + S each time.



---

## ⚠️ Common Beginner Mistakes

### Wrong File Extension

Python files should normally end with:

```text
.py
```

Correct:

```text
hello.py
```

Incorrect:

```text
hello.txt
```

---

### Wrong Interpreter

If VS Code reports that Python cannot be found, check:

```text
Python: Select Interpreter
```

and select the correct Python installation.

---

### Running the Wrong Folder

Make sure the terminal is opened in the directory containing your Python file.

For example:

```text
C:\Projects\Python\hello.py
```

Then run:

```bash
python hello.py
```

---

## ✅ Setup Checklist

* [x] Install VS Code
* [x] Open your Python project
* [x] Install the Python extension
* [x] Select the Python interpreter
* [x] Create a `.py` file
* [x] Open the terminal
* [x] Run a Python program

---

##  Next

Continue to:

```text
04_Hello_World.py
```

Write and run your first Python program.


