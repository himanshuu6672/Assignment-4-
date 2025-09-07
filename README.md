# Assignment-4-

This repository contains two Python programs for basic file handling operations.

---

## Files

- **Task 1.py**  
  Reads a text file named `sample.txt` and prints its content line by line.  
  If the file does not exist, it shows an error message.

- **Task 2.py**  
  - Takes user input and writes it to `output.txt`.  
  - Asks for more input and appends it on a new line.  
  - Finally, reads and displays the full content of `output.txt`.

- **sample.txt**  
  A sample text file used for testing Task 1.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/himanshuu6672/Assignment-4-.git
   cd Assignment-4-
   ```

2. Run the programs:
   ```bash
   python "Task 1.py"
   python "Task 2.py"
   ```

---

## Example Outputs

### Task 1 (Reading a file)

If `sample.txt` contains:
```
Hello
Welcome to Python
```

Running the program:
```
Hello
Welcome to Python
```

If the file is missing:
```
Error: The file 'sample.txt' does not exist.
```

---

### Task 2 (Writing, Appending, and Reading a file)

**Input/Output example:**
```
Enter text to write to the file output.txt : Hello World
Data successfully written to output.txt

Enter additional text to append : Welcome to Python
Data successfully appended

Final content of the output.txt :
Hello World
Welcome to Python
```

---

## Results

- **Task 1** successfully reads a text file and handles errors if the file is not found.  
- **Task 2** allows the user to write to a file, append additional text, and view the final file contents.  
- Together, both programs demonstrate basic **file handling operations in Python** (read, write, append).

---

## Requirements

- Python 3.x
