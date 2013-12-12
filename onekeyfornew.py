#!/use/bin/python

import os

#install brew
os.system('ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go/install)"')

#install brew-cask
os.system('brew tap phinze/homebrew-cask')
os.system('brew install brew-cask')

#install basic tools
os.system('brew install wget')
os.system('brew install curl')
os.system('brew install openssl')
os.system('brew install zsh')
os.system('brew install tree')
os.system('brew install mysql')
os.system('brew install sqlite')
os.system('brew install libtool')
os.system('brew install git')
os.system('brew install python')

#install normal applications [sname(string),add to Dock(BOOL),path(string))]
apps = [
     ['brew cask install firefox',False],
     ['brew cask install google-chrome',True,'/Applications/Google\ Chrome.app'],
     ['brew cask install iterm2',True,'/Applications/iTerm.app'],
     ['brew cask install sublime-text',True,'/Applications/Sublime\ Text\ 2.app'],
     ['brew cask install textexpander',False],
     ['brew cask install jumpcut',False],
     ['brew cask install dropbox',False],
     ['brew cask install cornerstone',True,'/Applications/Cornerstone.app'],
     ['brew cask install dash',False],
     ['brew cask install alfred',False],
     ['brew cask install mou',False],
     ['brew cask install vmware-fusion',False],
     ['brew cask install qq',True,'/Applications/QQ.app'],
     ['brew cask install appzapper',True,'/Applications/AppZapper.app'],
     ['brew cask install xmind',True,'/Applications/XMind.app'],
     ['brew cask install wireshark',False]
]

for item in apps:
     os.system(item[0])
     if item[1]:
          command = "defaults write com.apple.dock persistent-apps -array-add '<dict><key>tile-data</key><dict><key>file-data</key><dict><key>_CFURLString</key><string>%s</string><key>_CFURLStringType</key><integer>15</integer></dict></dict></dict>'" % item[2]
          os.system(command)
