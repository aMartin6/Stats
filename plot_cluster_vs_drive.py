"""
Make a plot of cluster size vs drive 
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


plt.rc('font', size=12)


if __name__ == "__main__":


    #------------------------------------------------------------------------
    #get data for initial frame, 
    #------------------------------------------------------------------------
    
    plot_file = "cluster_stats.txt"
    p_data = di.get_data(plot_file,3,sep=" ")

    rows=1
    columns=1

    gs=gridspec.GridSpec(rows,columns)
    fig = plt.figure(figsize=(6*columns,6*rows))

    ax1 = fig.add_subplot(gs[:])  #scatter plot of particles
    
    ax1.set_xlabel("Drive Force")
    ax1.set_ylabel("Average Largest Clump Fraction")   
    ax1.set_title("Largest Clump vs Drive Force")
    #ax1.set_ylim(0,0.5)

    drive1 = p_data[0][0:15] 
    pd02 = p_data[1][0:15]
    pd1 = p_data[1][15:30]
    pd2 = p_data[1][30:45]
    pd3 = p_data[1][45:60]
    pd4 = p_data[1][60:75]
    pd5 = p_data[1][75:90]
    pd6 = p_data[1][90:105]
    pd7 = p_data[1][105:120]
    stddev02 = p_data[2][0:15]
    stddev1 = p_data[2][15:30]
    stddev2 = p_data[2][30:45]
    stddev3 = p_data[2][45:60]
    stddev4 = p_data[2][60:75]
    stddev5 = p_data[2][75:90]
    stddev5 = p_data[2][90:105]
    stddev5 = p_data[2][105:120]
    
    drive, pd02 = zip(*sorted(zip(drive1, pd02)))
    #drive, pd1 = zip(*sorted(zip(drive1, pd1)))
    #drive, pd2 = zip(*sorted(zip(drive1, pd2)))
    #drive, pd3 = zip(*sorted(zip(drive1, pd3)))
    #drive, pd4 = zip(*sorted(zip(drive1, pd4)))
    #drive, pd5 = zip(*sorted(zip(drive1, pd5)))
    #drive, pd6 = zip(*sorted(zip(drive1, pd6)))
    #drive, pd7 = zip(*sorted(zip(drive1, pd7)))

    drive, stddev02 = zip(*sorted(zip(drive1, stddev02)))
    #drive, stddev1 = zip(*sorted(zip(drive1, stddev1)))
    #drive, stddev2 = zip(*sorted(zip(drive1, stddev2)))
    #drive, stddev3 = zip(*sorted(zip(drive1, stddev3)))
    #drive, stddev4 = zip(*sorted(zip(drive1, stddev4)))
    #drive, stddev5 = zip(*sorted(zip(drive1, stddev5)))

    #print (stddev02)
    
    ax1.errorbar(drive, pd02, stddev02, color = 'b',
             label = "$n_p$ = 0.02 ($\phi_p$ = 0.0628)")
    #ax1.plot(drive, pd1, color = 'g',
    #         label = "$n_p$ = 0.1 ($\phi_p$ = 0.314)")
    #ax1.plot(drive, pd2, color = 'r',
    #         label = "$n_p$ = 0.2 ($\phi_p$ = 0.628)")
    #ax1.plot(drive, pd3,color = 'c',
    #         label = "$n_p$ = 0.3 ($\phi_p$ = 0.942)")
    #ax1.plot(drive, pd4, color = 'm',
    #         label = "$n_p$ = 0.4 ($\phi_p$ = 1.257)")
    #ax1.plot(drive, pd5, color = 'y',
    #         label = "$n_p$ = 0.5 ($\phi_p$ = 1.571)")
    #ax1.plot(drive, pd6, color = 'y',
    #         label = "$n_p$ = 0.6 ($\phi_p$ = 1.885)")
    #ax1.plot(drive, pd7, color = 'y',
    #         label = "$n_p$ = 0.7 ($\phi_p$ = 2.199)")

    #plt.fill_between(drive, pd02-stddev02, pd02+stddev02, facecolor = 'b',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd1-stddev1, pd1+stddev1, facecolor = 'g',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd2-stddev2, pd2+stddev2, facecolor = 'r',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd3-stddev3, pd3+stddev3, facecolor = 'c',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd4-stddev4, pd4+stddev4, facecolor = 'm',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd5-stddev5, pd5+stddev5, facecolor = 'y',
    #                 alpha = 0.2)

    ax1.legend(loc = "best", fontsize = 12)

    #------------------------------------------------------------------------
    # (turned off) add an annotation
    # note: "force" was for a different system, here time is relevant
    #------------------------------------------------------------------------
    if 0:
        force_template = r'$F_D/F_p = %1.2f$'
        #force_template = r'time = %d'        
        force_text = ax1.text(0.5, 1.05, '', ha='center',
                              transform=ax1.transAxes,fontsize=22)

    out_name="clump_vs_drive_plot.png"
    fig.savefig(out_name)
        
    sys.exit()
