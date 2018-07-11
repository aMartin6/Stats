"""
Make a plot of P3, 4, 5, and 6
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors
#from matplotlib import cm
import matplotlib.ticker as ticker
import sys
#functions written by D.M. to get and plot specific data files
import data_importerDM as di


plt.rc('font', size=10)


if __name__ == "__main__":


    #------------------------------------------------------------------------
    #get data for initial frame, 
    #------------------------------------------------------------------------
    
    plot_file = "voro_stats.txt"
    p_data = di.get_data(plot_file,4,sep=" ")

    rows=1
    columns=1

    gs=gridspec.GridSpec(rows,columns)
    fig = plt.figure(figsize=(6*columns,6*rows))

    ax1 = fig.add_subplot(gs[:])  #scatter plot of particles
    
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Fraction of Particles")   
    ax1.set_title("P4, P5, P6, and P7 Over Time")

    p4   = p_data[0] 
    p5   = p_data[1]  
    p6   = p_data[2] 
    p7   = p_data[3]
    
    ax1.plot(p4, label = "P4")
    ax1.plot(p5, label = "P5")
    ax1.plot(p6, label = "P6")
    ax1.plot(p7, label = "P7")

    ax1.legend()

    #------------------------------------------------------------------------
    # (turned off) add an annotation
    # note: "force" was for a different system, here time is relevant
    #------------------------------------------------------------------------
    if 0:
        force_template = r'$F_D/F_p = %1.2f$'
        #force_template = r'time = %d'        
        force_text = ax1.text(0.5, 1.05, '', ha='center',
                              transform=ax1.transAxes,fontsize=22)

    out_name="Nearest Neighbor_Plot.png"
    fig.savefig(out_name)

    p4_average = np.mean(p4)
    p4_std = np.std(p4)
    p5_average = np.mean(p5)
    p5_std = np.std(p5)
    p6_average = np.mean(p6)
    p6_std = np.std(p6)
    p7_average = np.mean(p7)
    p7_std = np.std(p7)
    
    print "Average P4 =", p4_average, "+/-", p4_std
    print "Average P5 =", p5_average, "+/-", p5_std
    print "Average P6 =", p6_average, "+/-", p6_std
    print "Average P7 =", p7_average, "+/-", p7_std

    #out = open("../voro_statistics", "a")
    #print out
    #out.write("%f", p4_average)
    #out.write(p4_std)
    #out.write(p5_average)
    #out.write(p5_std)
    #out.write(p6_average)
    #out.write(p6_std)
    #out.write(p7_average)
    #out.write(p7_std)
    #out.write("\n")
    #out.close()
    
    sys.exit()
