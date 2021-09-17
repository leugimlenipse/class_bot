# class_bot

A simple python script to automate entering my vitual classes.

I had been thinking about automating my pc to enter my zoom classes for some time, and i just had some time to code that idea. Very simple script but saves me from opening the notes app, copying the class info, typing it into zoom and recording the class if i need to. It is run automatically by the task scheduler every two hours the days i have classes.

In v1 of the script i used **pyautogui** to open zoom and obs (which are pinned to my taskbar) with a click, but there's a disadvantage with this implementation which is that the mouse/keyboard must remain unused while the script is running, in order for pyautogui to work as planned.

In v2 i used the **os** library to open the programs without the need to use pyautogui. With the help of **os.system()**, it opens the programs via command line, which makes the process to have much less possible problems while running.

#### Tools used (for v1)

* pyautogui
