# ydl
This is a command line youtube script to download YouTube video using [pytube](https://pypi.org/project/pytube/) python module.


# Setup steps

Steps 1 & 2 are only required for fresh install.
1. Create new virtual env.<br/>
   *virtualenv -p /usr/bin/python3 ydl*
   or 
   *python3 -m venv ydl*

1. Activate new env.<br/>
   . ./ydl/bin/activate

1. Install pytube module.<br/>
   pip install pytube
   
1. To run program
   python ydl.py "url_of_video"
