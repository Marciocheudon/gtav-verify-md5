gtav-verify-md5
🐍 A Python script to check GTA V's MD5 files. If any are corrupted, it will warn you. Just download the correct file from the internet and replace it. 🐍

GTA V File Integrity Checker
This Python script is used to verify the integrity of GTA V game files. It compares MD5 codes of .rpf files against a predefined list to ensure the files are not corrupted.

How It Works
The script iterates over a list of MD5 codes associated with specific .rpf files from the GTA V game. For each file, the script calculates the current MD5 code and compares it to the expected value. If the MD5 code matches, the file is deemed valid. If not, the file might be corrupted.

Requirements
Python 3.x
Access to the GTA V installation folder
Usage
Clone the repository or download the script to your computer.
Open a terminal or command prompt.
Navigate to the directory where the script is saved.
Run the script using the command: python main.py.
When prompted, enter the path to the GTA V folder.
Contributions
Contributions to improve the script are always welcome. Feel free to fork the repository and submit your pull requests.

Screenshots
Program Start
<p align="center">
  <img src="https://github.com/Marciocheudon/gtav-verify-md5/assets/56776494/12b1c28e-29b5-4a9c-bf2f-2a51c7cf4be6" alt="Program Start">
</p>
Error
<p align="center">
  <img src="https://github.com/Marciocheudon/gtav-verify-md5/assets/56776494/80d467b4-70a9-46b0-b45c-d8a3f9c360d1" alt="Error">
</p>
License
CH3UD0N

