# Roblox FullScreen Optimizer

## Roblox Fullscreen Optimizer allows your Roblox client to enter a state called "True Fullscreen". 
Roblox by default only runs with a borderless window instead of an actual fullscreen, often times leaving behind performance and generating input lag. This small program fixes this. It will modify your Client Settings to disable a certain flag to allow for True fullscreen to be applied.

### How can I download it?
Visit the [releases](https://github.com/KEA12/RobloxFullScreenOptimizer/releases) page here and download the latest Version. Unzip it and run the `RobloxFullScreenOptimizer.exe` and you're good to go!

### What does it do?
- It will create a new folder inside your Roblox game directory named ClientSettings
- Inside this Folder a new json file named ClientAppSettings will be added, with the following data: `{"FFlagHandleAltEnterFullscreenManually": "False"}`
- That's literally it

### How do i apply it?
- Once installed, enter any Roblox game and make sure you are running the game in Fullscreen mode, otherwise this will not work
- After your game is started, you will need to press Alt + Enter to toggle True full screen mode. You can tell if you are in it by pressinf F11, if you switch to windowed mode then you are NOT in True fullscreen
- (Optional) Press Shift + F5 to view your ingame FPS, use this to monitor if you are achieving FPS improvements or not. If not, don't use this.
- (Optional) You can pair this with [Roblox FPS unlocker](https://github.com/axstin/rbxfpsunlocker/releases) to go above 60 FPS (Please note to follow the Games rules you intend to use this on.)

### Windows Defender / x Antivirus is flagging this as unsafe, is this true?
If windows defender or any other Antivirus is flagging it as unsafe or as a Threat, you can ignore it and continue with installation. You're free to not use this if you don't trust an open source application (somehow)

### Is this against Roblox ToS?
No. This is a Roblox feature shipped with the Client. It follows the Roblox rules, and should follow game rules aswell

### I'm getting Errors installing, what do I do?
[Report the Error here](https://github.com/KEA12/RobloxFullScreenOptimizer/issues)

### I'm getting worse performance/screen tearing, help!
It's best to not use this then. Run the uninstaller included in the package. This works differently for everyone since we all don't share the same PC Setups, hence why this is disabled by default on the Roblox client. 

### I'm still having issues after Uninstalling.
Reinstall the Roblox client. There shouldn't be any issues after uninstalling, however if there are, reinstalling the Roblox client should fix it
