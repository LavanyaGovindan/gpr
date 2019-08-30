# Import necessary packages
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox


# Global variable
c = 3*10**8

# Definition for generating the gprmax input text
def entries():
    validating()
    textFile = "#title: %s \n" % (titleEntry.get())

    textFile = textFile + "#domain: %s %s %s \n" % (domainEntry1.get(),domainEntry2.get(),domainEntry3.get())

    textFile = textFile + "#dx_dy_dz: %s %s %s \n" % (dx_dy_dzEntry1.get(),dx_dy_dzEntry2.get(),dx_dy_dzEntry3.get())

    textFile = textFile + "#time_window: %s \n" % (timeWindowEntry.get())

    textFile = textFile + "#material: %s %s %s %s %s\n" % (materialEntry1.get(),materialEntry2.get(),materialEntry3.get(),
                                                           materialEntry4.get(),materialEntry5.get())
    
    if wfOption.get() is "" and waveformEntry2.get() is "":
        textFile = textFile
    else:
        textFile = textFile + "#waveform: %s %s %s %s\n" % (wfOption.get(),waveformEntry1.get(),waveformEntry2.get(),
                                                        waveformEntry3.get())

    if hertzianEntry6.get() is "" and hertzianEntry7.get() is "":
        textFile = textFile + "#hertzian_dipole: %s %s %s %s %s\n" % (hertzianEntry1.get(), hertzianEntry2.get(),
                                                                      hertzianEntry3.get(), hertzianEntry4.get(),
                                                                      hertzianEntry5.get())
    else:
        textFile = textFile + "#hertzian_dipole: %s %s %s %s %s [%s %s]\n" % (hertzianEntry1.get(),hertzianEntry2.get(),
                                                                          hertzianEntry3.get(),hertzianEntry4.get(),
                                                                          hertzianEntry5.get(),hertzianEntry6.get(),
                                                                          hertzianEntry7.get())

    textFile = textFile + "#rx: %s %s %s %s %s\n" % (rxEntry1.get(), rxEntry2.get(), rxEntry3.get(),rxEntry4.get(),
                                                    rxEntry5.get())

    textFile = textFile + "#src_steps: %s %s %s\n" % (srcEntry1.get(), srcEntry2.get(), srcEntry3.get())
    textFile = textFile + "#rx_steps: %s %s %s\n" % (srcEntry1.get(), srcEntry2.get(), srcEntry3.get())

    if boxOpt2.get() is "":
        textFile = textFile + "#box: %s %s %s %s %s %s %s \n" % (boxEntry1.get(), boxEntry2.get(), boxEntry3.get(),
                                                                     boxEntry4.get(), boxEntry5.get(), boxEntry6.get(),
                                                                     boxOpt1.get())
    else:
        textFile = textFile + "#box: %s %s %s %s %s %s %s [%s]\n" % (boxEntry1.get(), boxEntry2.get(), boxEntry3.get(),
                                                                 boxEntry4.get(),boxEntry5.get(),boxEntry6.get(),
                                                                 boxOpt1.get(),boxOpt2.get())
    if cylOpt2.get() is "":
        textFile = textFile + "#cylinder: %s %s %s %s %s %s %s %s\n" % (cylinderEntry1.get(), cylinderEntry2.get(),
                                                                            cylinderEntry3.get(), cylinderEntry4.get(),
                                                                            cylinderEntry5.get(), cylinderEntry6.get(),
                                                                            cylinderEntry7.get(), cylOpt1.get())
    else:
        textFile = textFile + "#cylinder: %s %s %s %s %s %s %s %s[%s]\n" % (cylinderEntry1.get(), cylinderEntry2.get(),
                                                                        cylinderEntry3.get(),cylinderEntry4.get(),
                                                                        cylinderEntry5.get(), cylinderEntry6.get(),
                                                                        cylinderEntry7.get(), cylOpt1.get(),
                                                                       cylOpt2.get())
    textFile = textFile + "#geometry_view: 0 0 0 %s %s %s %s %s %s %s %s\n" % (domainEntry1.get(),domainEntry2.get()
                                                                                ,domainEntry3.get(),dx_dy_dzEntry1.get(),
                                                                                dx_dy_dzEntry2.get(),dx_dy_dzEntry3.get(),
                                                                        geometryEntry10.get(),geoOpt.get())

    Input=FileEntry.get()
    FileName = str("Documents/" + Input + ".txt")
    file = open(FileName,"w")
    file.write(textFile)
    file.close()

# Definition to display waveforms in GUI
def waveform():
    t = np.arange(0, 6e-9, 1.9e-12)
    wave_type = wfOption.get()
    f = float(waveformEntry2.get())
    y = []
    # Waveform definitions
    if wave_type == "gaussian":
        y = np.exp(-((2 * ((np.pi) ** 2) * (f ** 2)) * (t - 1 / f) ** 2))

    elif wave_type == "gaussiandot":
        y = -(4 * ((np.pi) ** 2) * f ** 2 * (t - 1 / f)) * (np.exp(-(2 * ((np.pi) ** 2) * f ** 2 * (t - 1 / f) ** 2)))

    elif wave_type == "gaussiandotnorm":
        norm = max(
            -(4 * ((np.pi) ** 2) * f ** 2 * (t - 1 / f)) * (np.exp(-(2 * ((np.pi) ** 2) * f ** 2 * (t - 1 / f) ** 2))))
        y = -((4 * ((np.pi) ** 2) * f ** 2 * (t - 1 / f)) * (
            np.exp(-(2 * ((np.pi) ** 2) * f ** 2 * (t - 1 / f) ** 2)))) / norm

    elif wave_type == "gaussiandotdot":
        y = ((2 * (np.pi) ** 2 * f ** 2) * (2 * (np.pi) ** 2 * f ** 2 * (t - (np.sqrt(2) / f)) ** 2 - 1) * (
            np.exp(-(np.pi) ** 2 * f ** 2 * (t - np.sqrt(2) / f) ** 2)))

    elif wave_type == "gaussiandotdotnorm":
        y = ((2 * (np.pi) ** 2 * f ** 2 * (t - np.sqrt(2) / f) ** 2 - 1) * (
            np.exp(-(np.pi) ** 2 * f ** 2 * (t - np.sqrt(2) / f) ** 2)))

    elif wave_type == "ricker":
        y = -(2 * (np.pi) ** 2 * f ** 2 * (t - np.sqrt(2) / f) ** 2 - 1) * (
            np.exp(-((np.pi) ** 2 * f ** 2 * (t - np.sqrt(2) / f) ** 2)))

    elif wave_type == "sine":
        y = []
        for i in range(0, len(t)):
            temp = f * t[i]
            if temp <= 1:
                R = 1
            else:
                R = 0
            y.append(R * np.sin(2 * np.pi * f * t[i]))
            
    elif wave_type == "contsine":
        if (f * t).all() <= 1:
            R = 0.25 * f * t
        else:
            R = 1
        y = R * np.sin(2 * np.pi * f * t)
    scale_x = 1e-9
    x = (1 / scale_x) * t
    
    plt.plot(x, y)
    plt.xlabel('Time[ns]')
    plt.ylabel('Amplitude')
    plt.show()

# Validating

def validating():
    wf=float(waveformEntry2.get())
    deltaL = c/(10.0*wf)
    if float(dx_dy_dzEntry1.get()) <= deltaL and float(dx_dy_dzEntry2.get()) <= deltaL and float(dx_dy_dzEntry3.get()) <= deltaL:
        messagebox.showinfo("Information","dt is in range")
    else :
        messagebox.showwarning("Warning", "Choose dx,dy,dz less than "+ str(deltaL))


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################

# GUI work
# Create GPRMAX user interface
window = Tk()
window.title("GprMax User Interface")
window.geometry("950x650")

# To write title
titleLabel=Label(window, text="Title",font="Helvetica 12", height=3)
titleLabel.grid(column=1, row=0)

directory=StringVar(None)
titleEntry=Entry(window,textvariable=directory,width=45)
titleEntry.grid(column=2, row=0)

# To write domain
domainLabel=Label(window, text="Domain",font="Helvetica 12", height=3)
domainLabel.grid(column=1, row=1)

dE1=StringVar(None)
domainEntry1=Entry(window,textvariable=dE1,width=5)
domainEntry1.grid(column=2, row=1)

dE2=StringVar(None)
domainEntry2=Entry(window,textvariable=dE2,width=5)
domainEntry2.grid(column=3, row=1)

dE3=StringVar(None)
domainEntry3=Entry(window,textvariable=dE3,width=5)
domainEntry3.grid(column=4, row=1)

# To write dx_dy_dz
dx_dy_dzLabel=Label(window, text="dx_dy_dz",font=("Times New Roman",12), height=3)
dx_dy_dzLabel.grid(column=1, row=2)

dx1=StringVar(None)
dx_dy_dzEntry1=Entry(window,textvariable=dx1,width=5)
dx_dy_dzEntry1.grid(column=2, row=2)

dx2=StringVar(None)
dx_dy_dzEntry2=Entry(window,textvariable=dx2,width=5)
dx_dy_dzEntry2.grid(column=3, row=2)

dx3=StringVar(None)
dx_dy_dzEntry3=Entry(window,textvariable=dx3,width=5)
dx_dy_dzEntry3.grid(column=4, row=2)

# To write time_window
timeWindowLabel=Label(window, text="Time Window",font="Helvetica 12", height=3)
timeWindowLabel.grid(column=1, row=3)

tw=StringVar(None)
timeWindowEntry=Entry(window,textvariable=tw,width=6)
timeWindowEntry.grid(column=2, row=3)

# To write material1
materialLabel=Label(window, text="Material",font="Helvetica 12", height=3)
materialLabel.grid(column=1, row=4)

mat1=StringVar(None)
materialEntry1=Entry(window,textvariable=mat1,width=5)
materialEntry1.grid(column=2, row=4)

mat2=StringVar(None)
materialEntry2=Entry(window,textvariable=mat2,width=5)
materialEntry2.grid(column=3, row=4)

mat3=StringVar(None)
materialEntry3=Entry(window,textvariable=mat3,width=5)
materialEntry3.grid(column=4, row=4)

mat4=StringVar(None)
materialEntry4=Entry(window,textvariable=mat4,width=5)
materialEntry4.grid(column=5, row=4)

mat5=StringVar(None)
materialEntry5=Entry(window,textvariable=mat5,width=5)
materialEntry5.grid(column=6, row=4)

# To write waveform
waveformLabel=Label(window, text="Waveform",font="Helvetica 12", height=3)
waveformLabel.grid(column=1, row=6)

waveform_Opt = ["","gaussian","gaussiandot", "gaussiandotnorm","gaussiandotdot","gaussiandotdotnorm","ricker","gaussianprime",
           "gaussiandoubleprime","sine","contsine"]

wfOption = StringVar(window)
wfOption.set(waveform_Opt[0]) # default value
waveformOption = OptionMenu(window, wfOption, *waveform_Opt)
waveformOption.config(font="Helvetica 12")
waveformOption.grid(column=2, row=6)

wav1=StringVar(None)
waveformEntry1=Entry(window,textvariable=wav1,width=5)
waveformEntry1.grid(column=3, row=6)

wav2=StringVar(None)
waveformEntry2=Entry(window,textvariable=wav2,width=5)
waveformEntry2.grid(column=4, row=6)

wav3=StringVar(None)
waveformEntry3=Entry(window,textvariable=wav3,width=5)
waveformEntry3.grid(column=5, row=6)

# To view the waveform in GUI
buttonWaveform = Button(window, text="View",font="Helvetica 12", command = waveform).grid( column=6, row=6)

# To write for hertizian dipole
hertizianLabel=Label(window, text="Hertzian Dipole",font="Helvetica 12", height=3)
hertizianLabel.grid(column=1, row=8)

her1=StringVar(None)
hertzianEntry1=Entry(window,textvariable=her1,width=5)
hertzianEntry1.grid(column=2, row=8)

her2=StringVar(None)
hertzianEntry2=Entry(window,textvariable=her2,width=5)
hertzianEntry2.grid(column=3, row=8)

her3=StringVar(None)
hertzianEntry3=Entry(window,textvariable=her3,width=5)
hertzianEntry3.grid(column=4, row=8)

her4=StringVar(None)
hertzianEntry4=Entry(window,textvariable=her4,width=5)
hertzianEntry4.grid(column=5, row=8)

her5=StringVar(None)
hertzianEntry5=Entry(window,textvariable=her5,width=5)
hertzianEntry5.grid(column=6, row=8)

her6=StringVar(None)
hertzianEntry6=Entry(window,textvariable=her6,width=5)
hertzianEntry6.grid(column=7, row=8)

her7=StringVar(None)
hertzianEntry7=Entry(window,textvariable=her7,width=5)
hertzianEntry7.grid(column=8, row=8)

# To write for rx
rxLabel=Label(window, text="Rx",font="Helvetica 12", height=3)
rxLabel.grid(column=1, row=9)

r1=StringVar(None)
rxEntry1=Entry(window,textvariable=r1,width=5)
rxEntry1.grid(column=2, row=9)

r2=StringVar(None)
rxEntry2=Entry(window,textvariable=r2,width=5)
rxEntry2.grid(column=3, row=9)

r3=StringVar(None)
rxEntry3=Entry(window,textvariable=r3,width=5)
rxEntry3.grid(column=4, row=9)

r4=StringVar(None)
rxEntry4=Entry(window,textvariable=r4,width=5)
rxEntry4.grid(column=5, row=9)

r5=StringVar(None)
rxEntry5=Entry(window,textvariable=r5,width=5)
rxEntry5.grid(column=6, row=9)

# To write for box
boxLabel=Label(window, text="Box",font="Helvetica 12", height=3)
boxLabel.grid(column=1, row=10)

b1=StringVar(None)
boxEntry1=Entry(window,textvariable=b1,width=5)
boxEntry1.grid(column=2, row=10)

b2=StringVar(None)
boxEntry2=Entry(window,textvariable=b2,width=5)
boxEntry2.grid(column=3, row=10)

b3=StringVar(None)
boxEntry3=Entry(window,textvariable=b3,width=5)
boxEntry3.grid(column=4, row=10)

b4=StringVar(None)
boxEntry4=Entry(window,textvariable=b4,width=5)
boxEntry4.grid(column=5, row=10)

b5=StringVar(None)
boxEntry5=Entry(window,textvariable=b5,width=5)
boxEntry5.grid(column=6, row=10)

b6=StringVar(None)
boxEntry6=Entry(window,textvariable=b6,width=5)
boxEntry6.grid(column=7, row=10)

box_Opt1 = ["pec","free_space","half_space"]
boxOpt1 = StringVar(window)
boxOpt1.set(box_Opt1[0])
boxOption1 = OptionMenu(window, boxOpt1, *box_Opt1)
boxOption1.config(font="Helvetica 12")

boxOption1.grid(column=8, row=10)

box_Opt2 = ["","y","n"]
boxOpt2 = StringVar(window)
boxOpt2.set(box_Opt2[0])
boxOption2 = OptionMenu(window, boxOpt2, *box_Opt2)
boxOption2.config(font="Helvetica 12")
boxOption2.grid(column=9, row=10)

# To write for cylinder
cylinderLabel=Label(window, text="Cylinder",font="Helvetica 12", height=3)
cylinderLabel.grid(column=1, row=11)

cy1=StringVar(None)
cylinderEntry1=Entry(window,textvariable=cy1,width=5)
cylinderEntry1.grid(column=2, row=11)

cy2=StringVar(None)
cylinderEntry2=Entry(window,textvariable=cy2,width=5)
cylinderEntry2.grid(column=3, row=11)

cy3=StringVar(None)
cylinderEntry3=Entry(window,textvariable=cy3,width=5)
cylinderEntry3.grid(column=4, row=11)

cy4=StringVar(None)
cylinderEntry4=Entry(window,textvariable=cy4,width=5)
cylinderEntry4.grid(column=5, row=11)

cy5=StringVar(None)
cylinderEntry5=Entry(window,textvariable=cy5,width=5)
cylinderEntry5.grid(column=6, row=11)

cy6=StringVar(None)
cylinderEntry6=Entry(window,textvariable=cy6,width=5)
cylinderEntry6.grid(column=7, row=11)

cy7=StringVar(None)
cylinderEntry7=Entry(window,textvariable=cy7,width=5)
cylinderEntry7.grid(column=8, row=11)

cyl_Opt1 = ["pec","free_space"]
cylOpt1 = StringVar(window)
cylOpt1.set(cyl_Opt1[0]) # default value
cylOption1 = OptionMenu(window, cylOpt1, *cyl_Opt1)
cylOption1.config(font="Helvetica 12")
cylOption1.grid(column=9, row=11)

cyl_Opt2 = ["","y","n"]
cylOpt2 = StringVar(window)
cylOpt2.set(cyl_Opt2[0]) # default value
cylOption2 = OptionMenu(window, cylOpt2, *cyl_Opt2)
cylOption2.grid(column=10, row=11)

# Rxs steps
srcLabel = Label(window, text="SRC steps",font="Helvetica 12", height=3)
srcLabel.grid(column=1, row=13)

bscan1=StringVar(None)
srcEntry1=Entry(window,textvariable=bscan1,width=5)
srcEntry1.grid(column=2, row=13)

bscan2=StringVar(None)
srcEntry2=Entry(window,textvariable=bscan2,width=5)
srcEntry2.grid(column=3, row=13)

bscan3=StringVar(None)
srcEntry3=Entry(window,textvariable=bscan3,width=5)
srcEntry3.grid(column=4, row=13)

#To write for geometry view
geometryLabel=Label(window, text="Geometry view",font="Helvetica 12", height=3)
geometryLabel.grid(column=1, row=12)

geometryEntry4=Entry(window,textvariable=dE1,width=5)
geometryEntry4.grid(column=2, row=12)

#gv5=StringVar(None)
geometryEntry5=Entry(window,textvariable=dE2,width=5)
geometryEntry5.grid(column=3, row=12)

#gv6=StringVar(None)
geometryEntry6=Entry(window,textvariable=dE3,width=5)
geometryEntry6.grid(column=4, row=12)

#gv7=StringVar(None)
geometryEntry7=Entry(window,textvariable=dx1,width=5)
geometryEntry7.grid(column=5, row=12)

#gv8=StringVar(None)
geometryEntry8=Entry(window,textvariable=dx2,width=5)
geometryEntry8.grid(column=6, row=12)

#gv9=StringVar(None)
geometryEntry9=Entry(window,textvariable=dx3,width=5)
geometryEntry9.grid(column=7, row=12)

gv10=StringVar(None)
geometryEntry10=Entry(window,textvariable=gv10,width=5)
geometryEntry10.grid(column=8, row=12)

geo_Opt = ["n","f"]
geoOpt = StringVar(window)
geoOpt.set(box_Opt2[0]) # default value
geoOption = OptionMenu(window, geoOpt, *box_Opt2)
geoOption.grid(column=9, row=12)

#Filename
Filelabel=Label(window, text="File Name",font="Helvetica 12", height=3)
Filelabel.grid(column=7, row=2)

fn=StringVar(None)
FileEntry=Entry(window,textvariable=fn,width=5)
FileEntry.grid(column=8, row=2)

buttonWrite = Button(window, text="OK", command = entries).grid( column=10, row=3)

window.mainloop()