# NITRO SNIPER IS CURRENTLY BROKEN. DON'T ENABLE IT OR YOU WILL BREAK THE SELFBOT AND IT WON'T WORK. PLEASE BE PATIENT FOR A FIX. THANK YOU.

# This selfbot is semi forked alucard. (A ton of added commands.)

# Setup
 - just set it up as a normal selfbot
 - https://www.youtube.com/watch?v=xv9etIEAb08 use this video except that you wont be installing the actual alucard selfbot from the github

# Legality

Everything you can see here has been made for educational purposes and proof of concepts. I do not promote the usage of my tools, I do not take responsability on the bad usage of this tool.

**YOU CAN CLOUD HOST IT** (with some modifications)

# Q&A
- Q: **`SSL Certificate Error`**
- A: Just install [CRT File](https://crt.sh/?id=2835394). Then run it and install. (This is common and it was a certificate that expired May 30th 2020. But a new one came out so install it.). If you wanna go into further detail then head to [SITE](https://support.sectigo.com/Com_KnowledgeDetailPage?Id=kA03l00000117LT).  
- Q: **`Module Missing`**
- A: Just run `pip install -r requirements.txt` in console. This insures that all modules required for Alucard are installed and up to date!
- Q: **`Windll not found`**
- A: Alucard uses some windows features from modules. Example windll from ctypes. windll is used to add the console title. You can remove the title setters in-order to fix it.
- Q: **`TypeError: __new__() got an unexpected keyword argument 'deny_new'`**
- A: This error occured on an old installation of discord.py to fix simply run :`pip install -U discord.py` this updates discord.py!
