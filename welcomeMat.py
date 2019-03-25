# -*- coding: utf-8 -*-
import os
import random
opList = ["hey there human", "Howdy!","( •_•)\n( •_•)>⌐■-■\n(⌐■_■)", "(╯°□°）╯︵ ┻━┻"]
os.system('sudo defaults write /Library/Preferences/com.apple.loginwindow LoginwindowText -string "%s"'%(random.choice(opList)))


