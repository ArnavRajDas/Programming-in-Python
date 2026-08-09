#  Installing Python

Before writing Python programs, Python needs to be installed on your computer.

This guide explains how to install Python on Windows.

---

##  Step 1 — Download Python

Go to the official Python website:

**https://www.python.org/**

Navigate to the Downloads section and download the latest stable **Python 3** release for Windows.

> ⚠️ Always prefer downloading Python from the official Python website.

---

##  Step 2 — Start the Installation

Open the downloaded installer.

You will see the Python installation window.

Before clicking **Install Now**, make sure you select:

```text
☑ Add python.exe to PATH
```

This is important because it allows you to run Python directly from the terminal.

Then select:

```text
Install Now
```

---

##  Step 3 — Wait for Installation

Python will now be installed on your computer.

After the installation finishes, you should see a success message.

Click:

```text
Close
```

---

##  Step 4 — Verify Python Installation

Open **Command Prompt** or **PowerShell**.

Run:

```bash
python --version
```

You should see something similar to:

```text
Python 3.x.x
```

The exact version number may be different depending on when you install Python.

---

##  Step 5 — Check the Python Interpreter

Run:

```bash
python
```

You should see something similar to:

```text
Python 3.x.x ...
>>>
```

The:

```text
>>>
```

is called the **Python interactive prompt**.

Try:

```python
print("Hello, Python!")
```

You should get:

```text
Hello, Python!
```

To exit the interpreter, type:

```python
exit()
```

---

##  If `python` Does Not Work

Sometimes Windows may not recognize:

```bash
python
```

You can try:

```bash
py --version
```

If that works, you can run Python using:

```bash
py
```

For example:

```bash
py hello.py
```

---

##  Common Problem: Python Not Recognized

If you see an error similar to:

```text
'python' is not recognized as an internal or external command
```

Python may not have been added to PATH.

Possible solutions:

1. Reinstall Python.
2. Make sure **Add python.exe to PATH** is selected.
3. Restart the terminal.
4. Restart VS Code if it was already open.
5. Verify the installation again.

---

## 📌 Check Installation

Run:

```bash
python --version
```

and:

```bash
pip --version
```

`pip` is Python's package installer.

You will use it later to install external Python packages.

---

## ✅ Installation Checklist

* [x] Download Python 3
* [x] Install Python
* [x] Add Python to PATH
* [x] Run `python --version`
* [x] Run `python`
* [x] Test `print()`
* [x] Exit the Python interpreter
* [x] Check `pip --version`

---

## 🎯 Goal

At this point, Python should be successfully installed and accessible from your terminal.

---

## ➡️ Next

Continue to:

```text
03_Setting_Up_VS_Code.md
```

There you will configure Visual Studio Code for Python development.
