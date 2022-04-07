# Import Libraries
import os
import time
import shutil

# Define Variables
path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions"
found = ""
start = time.time()

# Find Roblox Game Directory
for file in os.listdir(path):
    if file.startswith("version-"):
        for exe in os.listdir(f"{path}\\{file}"):
            if "RobloxPlayerBeta.exe" in exe:
                found = f"{path}\\{file}"
                print(f"Found Roblox Game directory: {found}")
                break

# Remove ClientSettings Folder
if found:
    try:
        shutil.rmtree(f"{found}\\ClientSettings")
        print("ClientSettings Folder removed successfully")
    except FileNotFoundError:
        print("Full screen optimizer is not enabled.")
        print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
        input("Press any key to exit...")
        exit()
    print("Full screen optimizations successfully removed")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()
else:
    print(f"Roblox Game directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()
