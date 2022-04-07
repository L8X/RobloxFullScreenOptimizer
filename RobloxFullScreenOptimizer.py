# Import Libraries
import os
import time
import json

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

# Create ClientSettings Folder
if found:
    try:
        os.makedirs(f"{found}\\ClientSettings")
        found = f"{found}\\ClientSettings"
        print("Created ClientSettings Folder")
    except FileExistsError:
        print("ClientSettings folder already exists")
        found = f"{found}\\ClientSettings"
else:
    print(f"Roblox Game directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()


# Create ClientAppSettings.json
if found:
    if not os.path.exists(f"{found}\\ClientAppSettings.json"):
        os.path.join(found, "ClientAppSettings.json")
        found = f"{found}\\ClientAppSettings.json"
        print("ClientAppSettings.json created successfully")
    else:
        print("ClientAppSettings.json already exists")
        print(f"Full screen optimization is already enabled.")
        print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
        input("Press any key to exit...")
        exit()
else:
    print(f"ClientSettings directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()

# Write to ClientAppSettings.json
if found:
    try:
        with open(found, 'w') as ClientAppSettings:
            data = {"FFlagHandleAltEnterFullscreenManually": "False"}
            json.dump(data, ClientAppSettings)
            print("Full Screen Optimization Enabled successfully")
    except FileNotFoundError:
        print("ClientAppSettings.json not found. Please retry.")
        print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
        input("Press any key to exit...")
        exit()
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()
else:
    print(f"ClientSettings directory not found.")
    print(f"\n\nFinished in {round(time.time() - start) + 1}ms.")
    input("Press any key to exit...")
    exit()