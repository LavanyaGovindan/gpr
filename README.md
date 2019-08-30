# Introduction
   <p> Ground Penetrating radar(GPR) is used to view buried object under ground. gprMax is open source software which is designed for simulating GPR. Validation of GPR environment is done using ParaView software.
  
### GUI for gprMax
* Developed a shell script which allows flexible graphical user interface (GUI) for generating A-scan/B-scan using gprMax.
   
### Steps to run GUI(Refer demo video https://drive.google.com/file/d/1eG3KxvZza9633Qveo4DBzrX4T2i3W2Yd/view?usp=sharing)
   * Click GUI_gprMax.sh file
   * Start filling GUI (For new users,refer Example file "sample_input.txt". To know about more visit http://www.gprmax.com/).
   * Fill file name(input).
   * For generating A-scan SRC steps not required. 
   * Then click "OK" button.
   * Validate the environment using ParaView software.To download, https://www.paraview.org/
   * Following files are created in your directory.
        <p>input.txt, input_merged.out, input.csv
   * You can use this generated input.csv or you can directly use sample_Bscan.csv for GPR1_0 software.
       
## About GPR1_0 software
 * Background subtraction of B-scan image using mean subtraction and average window subtraction method.
 * Time gating for removal of crosstalk in B-scan and enhance the visibility of targets.
 * Advanced noise processing tools like PCA, SVD, ICA etc., for B-scan raw.
 * Displaying of individual A-scans for any location in B-scan.
 * Conditioning of A-scan signal like filtering, smoothing, averaging etc.

## Install GPR1_0
 * To download visit https://drive.google.com/file/d/1lho69RvH3GacAXJoFyIUokQlPPmQOSYo/view?usp=sharing
 * Since the app is unrecognized. Choose "Run anyway" to proceed further.
 
## How to use GPR1_0?
### To view B-scan
    Go to File-> Load ->Load csv file	
###To view A-scan
    Click anywhere in B-scan, corresponding A-scan will display on its right side. 

### To apply Image Processing Algorithms
    Go to Tools-> Select your method. 
    
Note: 1. For PCA and SVD select No of components and click the method. 2. For time gating, enter gating range in time gating widget which is on right side corner, then go to Tools->Time Gating

