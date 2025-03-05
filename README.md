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
   python3 CheffAssistant_GUI.py
   ```

---

### **(Optional) Step 4: Make It Easier to Run**
#### **1️⃣ Make the Script Executable (Mac/Linux)**
```sh
chmod +x CheffAssistant_GUI.py
./CheffAssistant_GUI.py
```

#### **2️⃣ Convert It to a Windows Executable**
If you want a `.exe` file (Windows):
```sh
pip install pyinstaller
pyinstaller --onefile --windowed CheffAssistant_GUI.py
```
This will generate an **executable file** inside the `dist/` folder.

---

##  Summary of Steps
1️⃣ **Clone the repository**
   ```sh
   git clone https://github.com/your-username/cheff-assistant.git
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
   python3 CheffAssistant_GUI.py
   ```

---

## Contributing
If you’d like to contribute to the project, feel free to fork the repository and submit pull requests!

For any issues, contact steven.solorzano@csu.fullerton.edu .

---

# Enjoy using Cheff Assistant!** 👨🏾‍🍳 🍳 👩🏽‍🍳

