# Import necessary packages for csv generartion
import matplotlib.pyplot as plt
import pandas as pd
import h5py
import numpy as np
import os
import glob

scale_x = 1e-9
title = []
time_window = 3e-9

for files in glob.glob("Documents/*.out"):
    f = h5py.File(files)
    base = os.path.basename(files)  # this base contains only file name followed by .csv
    base = os.path.splitext(base)[0]  # this base only contains base name
    rxs = f['rxs']
    rx1 = rxs['rx1']
    Ez = rx1['Ez']
    # print(Ez)
    time, a_scan = np.shape(Ez)
    # print(time)
    df = pd.DataFrame(columns=np.arange(0, time, 1))
    # df1=pd.DataFrame()
    for i in range(0, time, 1):
        df[i] = Ez[i]
    # df1 = df.T
    t = np.linspace(0, time_window, len(rx1['Ex']))
    x = (1 / scale_x) * t
    print('Enter Time window: ')
    time = input()
    print('Enter Permittivity: ')
    perm = input()
    print('Enter Distance between A-scans: ')
    dist_ascan = input()
    print('Enter Target radius: ')
    target_rad = input()
    print('Enter distance between ground and TxRx: ')
    offset_dist = input()
    print('Enter depth of target: ')
    depth_target = input()

    filename = "Documents/" + base + ".csv"
    print(filename)
    f = open(filename, 'a')
    f.write("Time: " + str(time) + "\n")
    f.write("Permittivity: " + str(perm) + "\n")
    f.write("A-scan distance:" + str(dist_ascan) + "\n")
    f.write("Target Radius: " + str(target_rad) + "\n")
    f.write("Offset Distance: " + str(offset_dist) + "\n")
    f.write("Depth of target: " + str(depth_target) + "\n")
    f.write("\n")

    df.to_csv(filename, index=False)
    plt.imshow(Ez, cmap='jet', aspect='auto')
    plt.colorbar()
    plt.show()