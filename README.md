Kivy Apps

Installtion of environment
Linux (Ubuntu):
  for running app on OS ubuntu run these command on terminal:
sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get update
sudo apt-get install python-kivy #for python3 use python3 instead of python 
  for making an apk file run these commands:
    #installing p4a 
    pip install python-for-android
    python-for-android recipes
    p4a apk --requirements=kivy --private /home/asandy/devel/planewave_frozen/     --package=net.inclem.planewavessdl2   --name="planewavessdl2" --version=0.5 --bootstrap=sdl2
    #installing buildozer
    pip install --upgrade buildozer
    pip install --upgrade cython #use pip or other tool to install cython
    apt-get install ccache lib32stdc++6 openjdk-7-jdk #if you are using Debian-like OS
    #to make an apk for android
buildozer android debug deploy run
    #for build file for IOS
buildozer ios deploy run  
    
now copy this file into android/ios
and install it and then RUN

for any Query
E-mail: sandeepsajan0@gmail.com
