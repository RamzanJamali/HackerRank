#!/bin/sh

kill $(ps aux | grep "chrome")

python3 C:\Users\ramza\OneDrive\Desktop\blogg.py C:\Users\ramza\OneDrive\Desktop\websites.txt chrome
exit 0
