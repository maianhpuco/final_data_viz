
# OS
```
Ubuntu 20.04
```

# Install Python 3.8 & PyQt5
```
apt install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt install python3.8
apt install python3-pyqt5
apt install pyqt5-dev-tools
apt install qttools5-dev-tools
qtchooser -run-tool=designer -qt=5
```
## Setup something in this folder for PyQt5
```
chmod +x uic.py
sudo ln uic.py "/usr/lib/x86_64-linux-gnu/qt5/bin/uic"
mv qt5.desktop ~/.local/share/application
```

# Install requirements
```
apt install python3.8-venv
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

# Run
```
python main.py
```

# Note
```
Python 3.8.10
Ubuntu 20.04
```
