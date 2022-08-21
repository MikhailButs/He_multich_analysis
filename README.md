# He_multich_analysis
The code to analyze data from He-polychromator (492, 668, 706 nm) with high high speed camera Phantom on Globus-M2 tokamak to find ELM's

!!! in the pipeline !!!

This code is being developed by JoanaFedorenko & MikhailButs for Sergeev's Lab in SPbSTU to study edge modes in thermonuclear plasma of Globus-M2 tokamak in Ioffe Institute St.Petersburg

File to start programm with UI :  mainWindowUi.py

Current functions : 
> load .jpg and .cine (format by Phantom AMETEK) files with images Phantom high speed camera (only with 3 channels)
> calculate integral intensity of the images (it is correlate with D-alpha peaks!)
> filter loaded images usign chosen filter from PIL lib
> calculate and show differential images to looking for ELM's without background (previous image is used as background)
> load .sht files wich is used to store monitor diagnostics data on Globus-M2
> coming soon...
