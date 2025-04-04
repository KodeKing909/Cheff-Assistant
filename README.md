# Chef Assistant
##   How to Set Up and Run the Project on Your Computer

### **Step 1: Clone the Repository**
1. Open **Terminal (Mac/Linux)** or **Command Prompt (Windows)**.
2. Navigate to the folder where you want to store the project (e.g., `Documents`).
   ```sh
   cd ~/Documents
   ```
3. Clone the repository:
   ```sh
   git clone https://github.com/KodeKing909/cheff-assistant.git
   ```
   
4. Move into the project folder:
   ```sh
   cd cheff-assistant
   ```

---

### **Step 2: Install Python & Dependencies**
#### **1️⃣ Check if Python is Installed**
Run:
```sh
python3 --version
```
If Python is not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/).
- **Mac/Linux**: Install via:
  ```sh
  brew install python3  # macOS
  sudo apt-get install python3  # Linux
  ```

#### **2️⃣ Check if Tkinter is Installed**
Run:
```sh
python3 -m tkinter
```
- If a **window pops up**, Tkinter is installed.
- If not, install it:
  - **Linux**:  
    ```sh
    sudo apt-get install python3-tk
    ```
  - **Mac (Homebrew users)**:  
    ```sh
    brew install python-tk
    ```

---

### **Step 3: Run the Program**
1. Navigate to the project folder:
   ```sh
   cd ~/Documents/cheff-assistant  # Or wherever you cloned it
   ```
2. Run the Tkinter GUI script:
   ```sh
   python3 OrderGUI.py
   ```

---

### **(Optional) Step 4: Make It Easier to Run**
#### **1️⃣ Make the Script Executable (Mac/Linux)**
```sh
chmod +x OrderGUI.py
./OrderGUI.py
```

#### **2️⃣ Convert It to a Windows Executable**
If you want a `.exe` file (Windows):
```sh
pip install pyinstaller
pyinstaller --onefile --windowed OrderGUI.py
```
This will generate an **executable file** inside the `dist/` folder.

---

## Summary of Steps
1️⃣ **Clone the repository**
   ```sh
   git clone https://github.com/KodeKing909/cheff-assistant.git
   cd cheff-assistant
   ```
2️⃣ **Install Python (if not installed)**
   ```sh
   python3 --version
   ```
3️⃣ **Check and install Tkinter (if missing)**
   ```sh
   python3 -m tkinter
   ```
4️⃣ **Run the Tkinter GUI script**
   ```sh
   python3 OrderGUI.py
   ```