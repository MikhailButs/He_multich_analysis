# He multichannel analysis on Globus-M2 tokamak
The code to analyze data from FLIP4 polychromator (728, 668, 706 nm) with high speed camera Phantom M110 on Globus-M2 tokamak to find ELMs

!!! in the pipeline !!!

>This code is being developed by JoanaFedorenko & MikhailButs for Sergeev's Lab in SPbSTU to study edge localized modes in thermonuclear plasma of Globus-M2 tokamak in Ioffe Institute St.Petersburg

File to start programm with UI :  mainWindowUi.py

Current functions : 
- load .jpg and .cine (format by Phantom AMETEK) files containing images made by Phantom high speed camera (only with 3 channels)
- calculate integral intensity of the images (it correlates with D-alpha peaks!)
- filter loaded images usign chosen filter from PIL lib
- calculate and show differential images to look for ELMs without any background (previous image is used as the background)
- load .sht files wich is used to store monitor diagnostics data on Globus-M2
- coming soon...
