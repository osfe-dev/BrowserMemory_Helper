# Browser Memory Helper #
The Browser Memory Helper is a tool I designed to help save & manage your web browser windows.
The tool is designed to help you save an entire browser window, so you can safely close it and restore it at a later time. As someone that likes to have separate browser windows for each little project I find myself working on, I often find myself with 4+ Chrome windows open at a time, each one often containing upwards of 10 tabs. Not only does this add strain to your computer's resources, but it can also add a lot of clutter. Normally, if you want to close the window but know you're going to want those tabs back at some later date (if you have say, 10 man pages for a programming assignment open that you know you'll have to get back to in a couple days) you'd have to manually go back and search for/re-open each individual tab. This tool is meant to save you that time & effort, allowing you to seamlessly resume exactly where you left off. By creating a savepoint for a browser window that gets stored on a local file on your computer, you can safely close the browser window and quickly restore at a later date.

# Installation #
- Navigate to "Releases" and download one of the zip files into its own folder. This is important because it will also generate a `savepoints.json` file that will track/save all of your browser window data, and needs to be located in the same directory as the executable.
- Alternatively, you can also just download `BrowserMemory_Helper.exe` and `savepoints.json` from the main directory and put them in their own folder. This will often be the most current release
- That's it! Just run 'Chrome_BrowserMemory.exe' and follow the instructions to start saving/restoring your browser windows! For a more detailed explanation of how the program works, read 'Usage' below

# Usage #
## General Description ##
Upon initially opening the program, there won't be any browser 'savepoints'. In this context, a savepoint is just a json object stored in `savepoints.json` that keeps track of a browser window's unique id (chosen by the user), the number of tabs, and the urls for each saved tab. With the program, you can save, restore, and delete savepoints, and these changes will persist upon closing the program so long as you don't alter `savepoints.json`

## Creating a Savepoint ##
When creating a savepoint, you first must enter an id in the given text box next to the "Add new savepoint" button. Upon clicking the "Add new savepoint" button, you will be given a prompt explaining what you need to do to ensure the correct window gets saved. Upon closing the prompt, you will then have 5 seconds to click on the browser window that you'd like to save. After 5 seconds, the program will attempt to look at whatever window is currently active and iterate through/save all the tabs if it is a chrome window. This is why you must make sure the window you'd like to save is the currently selected one. Once it starts shuffling through the windows (you'll be able to see it go through each tab), patiently wait for it to finish. Once the new savepoint entry has been added to the list in the main program, you can then safely go back to using other windows and/or closing the browser window you just saved.

## Restoring a Savepoint ##
Similar to creating a Savepoint, when restoring a savepoint you must once again select a browser window. This time, the program will open all of the tabs that were saved in the savepoint in whatever browser window is currently selected. If you have multiple google profiles (like I do), it is generally a good idea to restore the savepoint in a browser window corresponding to the google profile for which it was originally created. This is mostly to account for websites that may depend on being signed in to a specific account (like a Google Doc, for example).

## Deleting a Savepoint ##
Deleting a savepoint is quite simple. Simply select the savepoint from the list and click delete. There will be a prompt to confirm the deletion, after which there's no going back!

# Future/Planned Features #
- Support for browsers beyond Chrome
- More robust pop-ups/dialogues that make using the program more user-friendly

# Version History #
### v1.1 ###
- Added cusom AppIcon to exe

### v1.0 ###
- Initial Commit
