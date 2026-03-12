# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:59:39 2025

@author: Jorrit Bakker
"""

import tools as tools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#%%
# Relative file path to the excel file with the data
file_path = "./S9081 HMVT CR1000X_measurements.dat"

#%%           
# Relative file path to the excel file with the data
file_path = "./S9081 HMVT CR1000X_measurements.dat"
write_images = True
write_excel = True
fig_dpi = 150
if not os.path.exists("Output"):
    os.makedirs("Output")


# The correction factor with regards to 3M KCl electrode reference
correction = 200

# Load in the file as Excel and clean it up into a seperate dataframe for temperature and redox data
df_redox, df_temp = tools.cleanup_redox(file_path,
                                        correction = correction,
                                        rename = tools.CW_rename
                                        )

# find outliers in temperature data and replace with average from other sensors
df_temp2 = tools.temp_outliers(df_temp, tools.node_T_dictionary)


#%%
# The nodes you want to plot for the redox plot using node_dictionary
# redox_nodes = tools.node_dictionary["CW3_80cm"]
# Or alternatively by manually choosing the redox nodes
# Naming as: CW# = which wetland, S# = which position along the wetland, -# = which depth
# Options: CW1, CW2, CW3 | S1, S2, S3, S4 | -1 (20cm), -2 (40cm), -3 (60cm), -4 (80cm)
# redox_nodes = ["CW3S1-4", "CW3S2-4", "CW3S3-4", "CW3S4-4"]

# =====#CW1=====
# redox_nodes0 = ["CW1S1-1", "CW1S1-2", "CW1S1-3", "CW1S1-4"]
# redox_nodes1 = ["CW1S2-1", "CW1S2-2", "CW1S2-3", "CW1S2-4"]
# redox_nodes2 = ["CW1S3-1", "CW1S3-2", "CW1S3-3", "CW1S3-4"]
# redox_nodes3 = ["CW1S4-1", "CW1S4-2", "CW1S4-3", "CW1S4-4"]

# temp_nodes = tools.node_T_dictionary["CW1"]
# redox_nodes = [redox_nodes0,redox_nodes1,redox_nodes2,redox_nodes3]
# plot_temp = True

# =====#CW2=====
redox_nodes0 = ["CW2S1-1", "CW2S1-2", "CW2S1-3", "CW2S1-4"]
redox_nodes1 = ["CW2S2-1", "CW2S2-2", "CW2S2-3", "CW2S2-4"]
redox_nodes2 = ["CW2S3-1", "CW2S3-2", "CW2S3-3", "CW2S3-4"]
redox_nodes3 = ["CW2S4-1", "CW2S4-2", "CW2S4-3", "CW2S4-4"]

redox_nodes = [redox_nodes0,redox_nodes1,redox_nodes2,redox_nodes3]
temp_nodes = tools.node_T_dictionary["CW2"]
plot_temp = True

# =====#CW3=====
# redox_nodes0 = ["CW3S1-1", "CW3S1-2", "CW3S1-3", "CW3S1-4"]
# redox_nodes1 = ["CW3S2-1", "CW3S2-2", "CW3S2-3", "CW3S2-4"]
# redox_nodes2 = ["CW3S3-1", "CW3S3-2", "CW3S3-3", "CW3S3-4"]
# redox_nodes3 = ["CW3S4-1", "CW3S4-2", "CW3S4-3", "CW3S4-4"]

# redox_nodes = [redox_nodes0,redox_nodes1,redox_nodes2,redox_nodes3]
# temp_nodes = tools.node_T_dictionary["CW3"]
# plot_temp = True

# # =====#CW's over deep nodes=====
# redox_nodes0 = tools.node_dictionary["CW1_80cm"]
# redox_nodes1 = tools.node_dictionary["CW2_80cm"]
# redox_nodes2 = tools.node_dictionary["CW3_80cm"]

# redox_nodes = [redox_nodes0,redox_nodes1,redox_nodes2]
# temp_nodes  = ['CW1S1', 'CW1S2', 'CW1S3', 'CW1S4', 'CW2S1', 'CW2S2', 'CW2S3', 'CW2S4', 'CW3S1', 'CW3S2', 'CW3S3']
# plot_temp = True

# # =====#CW's over undeep nodes=====
# redox_nodes0 = tools.node_dictionary["CW1_20cm"]
# redox_nodes1 = tools.node_dictionary["CW2_20cm"]
# redox_nodes2 = tools.node_dictionary["CW3_20cm"]

# redox_nodes = [redox_nodes0,redox_nodes1,redox_nodes2]
# temp_nodes  = ['CW1S1', 'CW1S2', 'CW1S3', 'CW1S4', 'CW2S1', 'CW2S2', 'CW2S3', 'CW2S4', 'CW3S1', 'CW3S2', 'CW3S3']
# plot_temp = True

# The nodes you want to plot for the temperature plot
# temp_nodes  = ['CW1S1', 'CW1S2', 'CW1S3', 'CW1S4', 'CW2S1', 'CW2S2', 'CW2S3', 'CW2S4', 'CW3S1', 'CW3S2', 'CW3S3']
# temp_nodes  = ['CW2S1', 'CW2S2', 'CW2S3', 'CW2S4']
# temp_nodes  = ['CW1S1', 'CW1S2', 'CW1S3', 'CW1S4', 'CW3S1', 'CW3S2', 'CW3S3']
# The start and end date of the data you want to plot, as 'YYYY-MM-DD hh-mm-ss'. Hour, minute and second specification is optional

start_date, end_date = '2025-11-01', '2099-09-30' # start nanobubbels: 27-2-2025

# # Plots the redox data
# fig, ax = tools.plot_redox(df_redox,
#                  redox_nodes,
#                  start_date,
#                  end_date,
#                  ylimit = (-300, -200),
#                  )
# fig.legend(bbox_to_anchor = (0.985, 0.97))
# plt.show()

# # Plots the temperature data
# fig, ax = tools.plot_temp(df_temp,
#                  temp_nodes,
#                  start_date,
#                  end_date,
#                  )
# fig.legend(bbox_to_anchor = (0.985, 0.97))
# plt.show() 

#%% plot redox nodes
for redox_node in redox_nodes:
    # Alternatively, plot temperature and redox in the same figure:
    fig, ax1 = tools.plot_redox(df_redox,
                     redox_node,
                     start_date,
                     end_date,
                     # ylimit = (-300, 650)
                     )
    
    # Twinning the x-axis to allow for second y-axis.
    if plot_temp:
        ax2 = ax1.twinx()
        
        # Pass the twinned axes object to the plot_temperature function to plot it on the second y-axis.
        ax2 = tools.plot_temp(df_temp,
                         temp_nodes,
                         start_date,
                         end_date,
                         mean = True,
                         ax = ax2,
                         color = "black",
                         alpha = 0.8,
                         )
    fig.legend(bbox_to_anchor = (0.35, 0.97))
    if write_images:
        plt.savefig(f"Output//{redox_node[0][0:5]}.png",dpi=fig_dpi,bbox_inches='tight')
        plt.savefig(f"Output//{redox_node[0][0:5]}.svg",dpi=fig_dpi,bbox_inches='tight')
    plt.show()

#%% plot temp nodes
# for temp_node in temp_nodes:
# Pass the twinned axes object to the plot_temperature function to plot it on the second y-axis.
fig, ax = tools.plot_temp(df_temp,
                  temp_nodes,
                  start_date,
                  end_date,
                  mean = False,
                  )
# <<<<<<< Updated upstream
# fig.legend(bbox_to_anchor = (0.985, 0.97))
# plt.show()
# =======
fig.legend(bbox_to_anchor = (0.22, 0.97))
if write_images:
    plt.savefig(f"Output//{temp_nodes[0][0:5]}_T.png",dpi=fig_dpi,bbox_inches='tight')
    plt.savefig(f"Output//{temp_nodes[0][0:5]}_T.svg",dpi=fig_dpi,bbox_inches='tight')
plt.show()

#%% Save to excel
if write_excel:
    with pd.ExcelWriter('Output\\CW_measurements.xlsx') as writer:  
        df_redox.to_excel(writer, sheet_name='Redox_potential')
        df_temp.to_excel(writer, sheet_name='Temperature')

