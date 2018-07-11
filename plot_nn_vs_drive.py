"""
Make a plot of nearest neighbor measurements vs drive
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
    
    plot_file = "nn_stats.txt"
    p_data = di.get_data(plot_file,9,sep=" ")
    
    drive1 = p_data[0][0:15] 
    p4_02 = p_data[1][0:15]
    p4_1 = p_data[1][15:30]
    p4_2 = p_data[1][30:45]
    p4_3 = p_data[1][45:60]
    p4_4 = p_data[1][60:75]
    p4_5 = p_data[1][75:90]
    p4_6 = p_data[1][90:105]
    p4_7 = p_data[1][105:120]
    stddev4_02 = p_data[2][0:15]
    stddev4_1 = p_data[2][15:30]
    stddev4_2 = p_data[2][30:45]
    stddev4_3 = p_data[2][45:60]
    stddev4_4 = p_data[2][60:75]
    stddev4_5 = p_data[2][75:90]
    stddev4_6 = p_data[2][90:105]
    stddev4_7 = p_data[2][105:120]
    p5_02 = p_data[3][0:15]
    p5_1 = p_data[3][15:30]
    p5_2 = p_data[3][30:45]
    p5_3 = p_data[3][45:60]
    p5_4 = p_data[3][60:75]
    p5_5 = p_data[3][75:90]
    p5_6 = p_data[3][90:105]
    p5_7 = p_data[3][105:120]
    stddev5_02 = p_data[4][0:15]
    stddev5_1 = p_data[4][15:30]
    stddev5_2 = p_data[4][30:45]
    stddev5_3 = p_data[4][45:60]
    stddev5_4 = p_data[4][60:75]
    stddev5_5 = p_data[4][75:90]
    stddev5_6 = p_data[4][90:105]
    stddev5_7 = p_data[4][105:120]
    p6_02 = p_data[5][0:15]
    p6_1 = p_data[5][15:30]
    p6_2 = p_data[5][30:45]
    p6_3 = p_data[5][45:60]
    p6_4 = p_data[5][60:75]
    p6_5 = p_data[5][75:90]
    p6_6 = p_data[5][90:105]
    p6_7 = p_data[5][105:120]
    stddev6_02 = p_data[6][0:15]
    stddev6_1 = p_data[6][15:30]
    stddev6_2 = p_data[6][30:45]
    stddev6_3 = p_data[6][45:60]
    stddev6_4 = p_data[6][60:75]
    stddev6_5 = p_data[6][75:90]
    stddev6_6 = p_data[6][90:105]
    stddev6_7 = p_data[6][105:120]
    p7_02 = p_data[7][0:15]
    p7_1 = p_data[7][15:30]
    p7_2 = p_data[7][30:45]
    p7_3 = p_data[7][45:60]
    p7_4 = p_data[7][60:75]
    p7_5 = p_data[7][75:90]
    p7_6 = p_data[7][90:105]
    p7_7 = p_data[7][105:120]
    stddev7_02 = p_data[8][0:15]
    stddev7_1 = p_data[8][15:30]
    stddev7_2 = p_data[8][30:45]
    stddev7_3 = p_data[8][45:60]
    stddev7_4 = p_data[8][60:75]
    stddev7_5 = p_data[8][75:90]
    stddev7_6 = p_data[8][90:105]
    stddev7_7 = p_data[8][105:120]

    #Put in order of drive force (haven't yet done this for stddev)
    drive, p4_02 = zip(*sorted(zip(drive1, p4_02)))
    drive, p4_1 = zip(*sorted(zip(drive1, p4_1)))
    drive, p4_2 = zip(*sorted(zip(drive1, p4_2)))
    drive, p4_3 = zip(*sorted(zip(drive1, p4_3)))
    drive, p4_4 = zip(*sorted(zip(drive1, p4_4)))
    drive, p4_5 = zip(*sorted(zip(drive1, p4_5)))
    drive, p4_6 = zip(*sorted(zip(drive1, p4_6)))
    drive, p4_6 = zip(*sorted(zip(drive1, p4_7)))

    drive, p5_02 = zip(*sorted(zip(drive1, p5_02)))
    drive, p5_1 = zip(*sorted(zip(drive1, p5_1)))
    drive, p5_2 = zip(*sorted(zip(drive1, p5_2)))
    drive, p5_3 = zip(*sorted(zip(drive1, p5_3)))
    drive, p5_4 = zip(*sorted(zip(drive1, p5_4)))
    drive, p5_5 = zip(*sorted(zip(drive1, p5_5)))
    drive, p5_6 = zip(*sorted(zip(drive1, p5_6)))
    drive, p5_7 = zip(*sorted(zip(drive1, p5_7)))

    drive, p6_02 = zip(*sorted(zip(drive1, p6_02)))
    drive, p6_1 = zip(*sorted(zip(drive1, p6_1)))
    drive, p6_2 = zip(*sorted(zip(drive1, p6_2)))
    drive, p6_3 = zip(*sorted(zip(drive1, p6_3)))
    drive, p6_4 = zip(*sorted(zip(drive1, p6_4)))
    drive, p6_5 = zip(*sorted(zip(drive1, p6_5)))
    drive, p6_6 = zip(*sorted(zip(drive1, p6_6)))
    drive, p6_7 = zip(*sorted(zip(drive1, p6_7)))

    drive, p7_02 = zip(*sorted(zip(drive1, p7_02)))
    drive, p7_1 = zip(*sorted(zip(drive1, p7_1)))
    drive, p7_2 = zip(*sorted(zip(drive1, p7_2)))
    drive, p7_3 = zip(*sorted(zip(drive1, p7_3)))
    drive, p7_4 = zip(*sorted(zip(drive1, p7_4)))
    drive, p7_5 = zip(*sorted(zip(drive1, p7_5)))
    drive, p7_6 = zip(*sorted(zip(drive1, p7_6)))
    drive, p7_7 = zip(*sorted(zip(drive1, p7_7)))
    
    rows=2
    columns=2

    gs=gridspec.GridSpec(rows,columns)
    fig = plt.figure(figsize=(6*columns,6*rows))

    ax1 = fig.add_subplot(gs[0,0])
    
    ax1.set_xlabel("Drive Force")
    ax1.set_ylabel("P4")   
    ax1.set_title("P4 vs Drive Force")
    #ax1.set_ylim(0.02,0.042)

    ax1.plot(drive, p4_02, #color = 'y',
             label = "Pin Density = 0.02 (Area Density = 0.0157)")
    ax1.plot(drive, p4_1, #color = 'b',
             label = "Pin Density = 0.1 (Area Density = 0.0785)")
    ax1.plot(drive, p4_2, #color = 'g',
             label = "Pin Density = 0.2 (Area Density = 0.157)")
    ax1.plot(drive, p4_3, #color = 'r',
             label = "Pin Density = 0.3 (Area Density = 0.237)")
    ax1.plot(drive, p4_4, #color = 'c',
             label = "Pin Density = 0.4 (Area Density = 0.314)")
    ax1.plot(drive, p4_5, #color = 'm',
             label = "Pin Density = 0.5 (Area Density = 0.393)")
    ax1.plot(drive, p4_6, #color = 'm',
             label = "Pin Density = 0.6 (Area Density = 0.472)")
    ax1.plot(drive, p4_7, #color = 'm',
             label = "Pin Density = 0.7 (Area Density = 0.550)")
    
    #ax1.legend(loc = "best", fontsize = 10)
    
    ax1 = fig.add_subplot(gs[0,1])
    
    ax1.set_xlabel("Drive Force")
    ax1.set_ylabel("P5")   
    ax1.set_title("P5 vs Drive Force")
    #ax1.set_ylim(0.21,0.30)

    ax1.plot(drive, p5_02, #color = 'y',
             label = "Pin Density = 0.02 (Area Density = 0.0157)")
    ax1.plot(drive, p5_1, #color = 'b',
             label = "Pin Density = 0.1 (Area Density = 0.0785)")
    ax1.plot(drive, p5_2, #color = 'g',
             label = "Pin Density = 0.2 (Area Density = 0.157)")
    ax1.plot(drive, p5_3, #color = 'r',
             label = "Pin Density = 0.3 (Area Density = 0.237)")
    ax1.plot(drive, p5_4, #color = 'c',
             label = "Pin Density = 0.4 (Area Density = 0.314)")
    ax1.plot(drive, p5_5, #color = 'm',
             label = "Pin Density = 0.5 (Area Density = 0.393)")
    ax1.plot(drive, p5_6, #color = 'm',
             label = "Pin Density = 0.6 (Area Density = 0.472)")
    ax1.plot(drive, p5_7, #color = 'm',
             label = "Pin Density = 0.7 (Area Density = 0.550)")
    
    #ax1.legend(loc = "best", fontsize = 10)
    
    ax1 = fig.add_subplot(gs[1,0])
    
    ax1.set_xlabel("Drive Force")
    ax1.set_ylabel("P6")   
    ax1.set_title("P6 vs Drive Force")
    #ax1.set_ylim(0.39,0.57)

    ax1.plot(drive, p6_02, #color = 'y',
             label = "Pin Density = 0.02 (Area Density = 0.0157)")
    ax1.plot(drive, p6_1, #color = 'b',
             label = "Pin Density = 0.1 (Area Density = 0.0785)")
    ax1.plot(drive, p6_2, #color = 'g',
             label = "Pin Density = 0.2 (Area Density = 0.157)")
    ax1.plot(drive, p6_3, #color = 'r',
             label = "Pin Density = 0.3 (Area Density = 0.237)")
    ax1.plot(drive, p6_4, #color = 'c',
             label = "Pin Density = 0.4 (Area Density = 0.314)")
    ax1.plot(drive, p6_5, #color = 'm',
             label = "Pin Density = 0.5 (Area Density = 0.393)")
    ax1.plot(drive, p6_6, #color = 'm',
             label = "Pin Density = 0.6 (Area Density = 0.472)")
    ax1.plot(drive, p6_7, #color = 'm',
             label = "Pin Density = 0.7 (Area Density = 0.550)")
    
    #ax1.legend(loc = "best", fontsize = 10)
    
    ax1 = fig.add_subplot(gs[1,1])
    
    ax1.set_xlabel("Drive Force")
    ax1.set_ylabel("P7")   
    ax1.set_title("P7 vs Drive Force")
    #ax1.set_ylim(0.17,0.24)

    ax1.plot(drive, p7_02, #color = 'y',
             label = "$n_p$ = 0.02 ($\phi_p$ = 0.0628)")
    ax1.plot(drive, p7_1, #color = 'b',
             label = "$n_p$ = 0.1 ($\phi_p$ = 0.314)")
    ax1.plot(drive, p7_2, #color = 'g',
             label = "$n_p$ = 0.2 ($\phi_p$ = 0.828)")
    ax1.plot(drive, p7_3, #color = 'r',
             label = "$n_p$ = 0.3 ($\phi_p$ = 0.942)")
    ax1.plot(drive, p7_4, #color = 'c',
             label = "$n_p$ = 0.4 ($\phi_p$ = 1.257)")
    ax1.plot(drive, p7_5, #color = 'm',
             label = "$n_p$ = 0.5 ($\phi_p$ = 1.571)")
    ax1.plot(drive, p7_6, #color = 'm',
             label = "$n_p$ = 0.6 ($\phi_p$ = 1.885)")
    ax1.plot(drive, p7_7, #color = 'm',
             label = "$n_p$ = 0.7 ($\phi_p$ = 2.199)")

    ax1.legend(loc = "best", fontsize = 10)
    
    #plt.fill_between(drive, pd02-stddev02, pd02+stddev02, facecolor = 'y',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd1-stddev1, pd1+stddev1, facecolor = 'b',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd2-stddev2, pd2+stddev2, facecolor = 'g',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd3-stddev3, pd3+stddev3, facecolor = 'r',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd4-stddev4, pd4+stddev4, facecolor = 'c',
    #                 alpha = 0.2)
    #plt.fill_between(drive, pd5-stddev5, pd5+stddev5, facecolor = 'm',
    #                 alpha = 0.2)


    #------------------------------------------------------------------------
    # (turned off) add an annotation
    # note: "force" was for a different system, here time is relevant
    #------------------------------------------------------------------------
    if 0:
        force_template = r'$F_D/F_p = %1.2f$'
        #force_template = r'time = %d'        
        force_text = ax1.text(0.5, 1.05, '', ha='center',
                              transform=ax1.transAxes,fontsize=22)

    out_name="nn_vs_drive_plot.png"
    fig.savefig(out_name)
        
    sys.exit()
