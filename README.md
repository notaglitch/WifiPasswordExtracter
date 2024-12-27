# Wifi Password Viewer Tool

Welcome to the **Wifi Password Viewer Tool**! This simple command-line tool helps you see the list of WiFi networks saved on your Windows machine and retrieve their corresponding passwords. It interacts with your system’s `netsh wlan` commands to display and manage your saved WiFi credentials.

---

## Features

- **List WiFi Networks**: View all WiFi profiles saved on your computer.
- **View WiFi Details**: Get complete details for any selected WiFi, including passwords (if saved).
- **Helpful Menus**: Easy-to-navigate menu system with clear options.

---

## Screenshots

```
See all the WIFI passwords on your computer
--------------------------------------------
             Made by notaglitch             
--------------------------------------------

[ 1 ] See Wifi List
[ 2 ] About
[ 3 ] Help
[ 4 ] Exit
---------------------------------------
```

---

## How to Use

### 1. **Clone the Repository**

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/notaglitch/WifiPasswordExtracter.git
```

### 2. **Run the Tool**

After cloning the repository, navigate to the directory where the script is located, and run it using Python:

```bash
python main.py
```

### 3. **Interact with the Menu**

The tool will present a simple menu with the following options:

- **Option 1**: View the list of WiFi networks saved on your machine.
- **Option 2**: Learn more about the tool and the developer.
- **Option 3**: Access helpful tips for using the tool.
- **Option 4**: Exit the tool.

### 4. **View and Retrieve WiFi Passwords**

- After selecting **Option 1**, you can choose which WiFi network to get information about.
- The tool will prompt you to enter the WiFi network name (use quotes if the name contains spaces).
- If the WiFi network has a saved password, the tool will display it.

---

## Detailed Usage

### Main Menu

When you start the tool, you will be presented with a main menu:

```
[ 1 ] See Wifi List
[ 2 ] About
[ 3 ] Help
[ 4 ] Exit
```

- **Option 1**: Lists all saved WiFi networks.
  - Choose the WiFi network you want to get detailed information about.
- **Option 2**: Displays information about how the tool works and its developer.
- **Option 3**: Provides help, tips, and troubleshooting steps.
- **Option 4**: Exits the program.

### How it Works

The tool uses the `netsh wlan` command to interact with your system and retrieve saved WiFi profiles. When you choose **Option 1**, the script runs `netsh wlan show profile` to display all available WiFi profiles. If you select a WiFi profile and enter its name, it will show you detailed information, including the WiFi password if it's saved on your machine.

---

## Example Walkthrough

1. **See WiFi List**:
   ```
   -- Here's the list of your wifi's --
   ...
   [ 1 ] Choose a wifi
   [ 2 ] Main Menu
   [ 3 ] Exit
   ```

2. **Choose WiFi**: Enter the name of the WiFi, and if a password is saved, it will be displayed:
   ```
   Put the name of the WIFI here ==> "Home WiFi"
   ```

3. **View WiFi Details**: Displays information about the selected WiFi:
   ```
   -- WiFi Details --
   SSID: Home WiFi
   Key: mypassword123
   ```

---

## Commands and Functions

- `netsh wlan show profile`: Lists all WiFi networks saved on your system.
- `netsh wlan show profile name="WiFiName" key=clear`: Shows detailed information about a selected WiFi network, including the password (if saved).

---

## Help & Troubleshooting

If you encounter any issues, you can always access the **Help** option from the menu:

```
[ + ] Type only digits to select an option
[ + ] Make sure the wifi name is correct
[ + ] Ensure no spelling mistakes
[ + ] If you get an error, put the wifi's name inside double quotes
[ + ] If you get the info but not the key, it means it's not saved
```

---

## About the Developer

The **Wifi Password Viewer Tool** was developed by **notaglitch**. The goal of this tool is to provide an easy-to-use interface for viewing saved WiFi passwords on Windows systems.

---

## Requirements

- **Python 3.x**
- **Windows OS** (The `netsh` command is Windows-specific and will not work on macOS or Linux)

---

## Contributing

If you want to contribute to the project, feel free to fork the repository, create a branch, and submit a pull request. Any improvements or bug fixes are welcome!

---

## Disclaimer

- This tool will only work if you have administrator access on your computer.
- This tool is for educational purposes only. Ensure that you have permission to access and view the WiFi credentials on the system.
