import os, sys
import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import math
from scipy.stats import skew
from scipy.stats import kurtosis
import matplotlib.colors as mcolors
import scipy.fftpack as fftpack
from scipy import interpolate
import pkg_resources
import types

# DEF1
def get_imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            # Split ensures you get root package, 
            # not just imported function
            name = val.__name__.split(".")[0]

        elif isinstance(val, type):
            name = val.__module__.split(".")[0]

        # Some packages are weird and have different
        # imported names vs. system/pip names. Unfortunately,
        # there is no systematic way to get pip names from
        # a package's imported name. You'll have to had
        # exceptions to this list manually!
        poorly_named_packages = {
            "PIL": "Pillow",
            "sklearn": "scikit-learn"
        }
        if name in poorly_named_packages.keys():
            name = poorly_named_packages[name]

        yield name
imports = list(set(get_imports()))

# The only way I found to get the version of the root package
# from only the name of the package is to cross-check the names 
# of installed packages vs. imported packages
requirements = []
for m in pkg_resources.working_set:
    if m.project_name in imports and m.project_name!="pip":
        requirements.append((m.project_name, m.version))

for r in requirements:
    print("{}=={}".format(*r))

# DEF2
def test_function(FE_xr):
    
    ust = np.squeeze(FE_xr.fricVel.isel(time=0).values)
    ust_mean = np.mean(np.mean(ust,1),0)
    
    print('Executing test_function: ust_mean =',ust_mean)
    
    return ust_mean

# DEF3
def mean_profiles(FE_xr):
    
    u_3d = np.squeeze(FE_xr.u.isel(time=0).values)
    v_3d = np.squeeze(FE_xr.v.isel(time=0).values)
    th_3d = np.squeeze(FE_xr.theta.isel(time=0).values)
    z_3d = np.squeeze(FE_xr.zPos.isel(time=0).values)

    Nz = u_3d.shape[0]
    wd_1d = np.zeros([Nz])

    u_1d = np.mean(np.mean(u_3d,axis=2),axis=1)
    v_1d = np.mean(np.mean(v_3d,axis=2),axis=1)
    th_1d = np.mean(np.mean(th_3d,axis=2),axis=1)
    z_1d = np.mean(np.mean(z_3d,axis=2),axis=1)

    #ws_1d = np.sqrt(np.power(u_1d,2.0)+np.power(v_1d,2.0))
    for kk in range(0,Nz):
        wd_tmp = math.atan2(-u_1d[kk],-v_1d[kk]) * 180.0 / np.pi
        if (wd_tmp<0.0):
            wd_tmp = 180.0 + (180.0 + wd_tmp)
        wd_1d[kk] = wd_tmp

    array_out = np.zeros([Nz,5])
    array_out[:,0] = z_1d
    array_out[:,1] = u_1d
    array_out[:,2] = v_1d
    array_out[:,3] = wd_1d
    array_out[:,4] = th_1d
    
    return array_out

# DEF4
def plot_XY_UVWTHETA(case, case_open, zChoose, save_plot_opt, path_figure):

    ufield = case_open.u.isel(time=0).values
    vfield = case_open.v.isel(time=0).values
    wfield = case_open.w.isel(time=0).values
    thetafield = case_open.theta.isel(time=0).values
    xPos = case_open.xPos.isel(time=0,zIndex=zChoose).values
    yPos = case_open.yPos.isel(time=0,zIndex=zChoose).values
    zPos = case_open.zPos.isel(time=0,zIndex=zChoose).values
    
    if case == 'neutral':
        xticks_vals=[0,3.2,6.4,9.6,12.8]
        xticks_ticks=['0','3.2','6.4','9.6','12.8']
        yticks_vals=[0,3.170,6.340,9.510,12.68]
        yticks_ticks=['0','3.170','6.340','9.510','12.68']
    elif case == 'convective':
        xticks_vals=[0,1.5,3.0,4.5,6.0]
        xticks_ticks=['0','1.5','3.0','4.5','6.0']
        yticks_vals=[0,1.5,3.0,4.5,6.0]
        yticks_ticks=['0','1.5','3.0','4.5','6.0']
    elif case == 'stable':
        xticks_vals=[0,0.10,0.20,0.3,0.4]
        xticks_ticks=['0','0.1','0.2','0.3','0.4']
        yticks_vals=[0,0.10,0.20,0.3,0.4]
        yticks_ticks=['0','0.1','0.2','0.3','0.4']
    else:
        print("ERROR: INVALID CASE SELECTED")
        
    u_min = np.amin(np.amin(ufield))
    u_max = np.amax(np.amax(ufield))
    v_min = np.amin(np.amin(vfield))
    v_max = np.amax(np.amax(vfield))
    w_min = np.amin(np.amin(wfield))
    w_max = np.amax(np.amax(wfield))
    t_min = np.amin(np.amin(thetafield[zChoose,:,:]))
    t_max = np.amax(np.amax(thetafield[zChoose,:,:]))
    
    fig_name = "UVWTHETA-XY-"+case+".png"
    colormap1 = 'viridis'
    colormap2 = 'seismic'
    colormap3 = 'YlOrRd'
    FE_legend = [r'u [m/s] at z='+str(np.amax(zPos))+' m',r'v [m/s] at z='+str(np.amax(zPos))+' m',r'w [m/s] at z='+str(np.amax(zPos))+' m', \
                 '\u03B8 [K] at z='+str(np.amax(zPos))+' m']
    
    fntSize=20
    fntSize_title=22
    plt.rcParams['xtick.labelsize']=fntSize
    plt.rcParams['ytick.labelsize']=fntSize
    plt.rcParams['axes.linewidth']=2.0
    plt.rcParams['pcolor.shading']='auto'

    numPlotsX=2
    numPlotsY=2
    fig,axs = plt.subplots(numPlotsX,numPlotsY,sharey=False,sharex=False,figsize=(26,20))

    ###############
    ### U plot ###
    ###############
    ax=axs[0][0]
    im = ax.pcolormesh(xPos/1e3,yPos/1e3,ufield[zChoose,:,:],cmap=colormap1,linewidth=0,rasterized=True,vmin=u_min,vmax=u_max)
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_ticks)
    ax.set_yticks(yticks_vals)
    ax.set_yticklabels(yticks_ticks)
    ax.set_ylabel(r'$y$ $[\mathrm{km}]$',fontsize=fntSize)
    ax.set_xlabel(r'$x$ $[\mathrm{km}]$',fontsize=fntSize)
    cbar=fig.colorbar(im, ax=ax) #, orientation='horizontal')

    title_fig_0 = FE_legend[0]
    ax.set_title(title_fig_0,fontsize=fntSize)

    ###############
    ### V plot ###
    ###############
    ax=axs[1][0]
    im = ax.pcolormesh(xPos/1e3,yPos/1e3,vfield[zChoose,:,:],cmap=colormap1,linewidth=0,rasterized=True,vmin=v_min,vmax=v_max)
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_ticks)
    ax.set_yticks(yticks_vals)
    ax.set_yticklabels(yticks_ticks)
    ax.set_ylabel(r'$y$ $[\mathrm{km}]$',fontsize=fntSize)
    ax.set_xlabel(r'$x$ $[\mathrm{km}]$',fontsize=fntSize)
    cbar=fig.colorbar(im, ax=ax) #, orientation='horizontal')

    title_fig_1 = FE_legend[1]
    ax.set_title(title_fig_1,fontsize=fntSize)

    ###############
    ### W plot ###
    ###############
    w_min=-1.0*w_max
    ax=axs[0][1]
    im = ax.pcolormesh(xPos/1e3,yPos/1e3,wfield[zChoose,:,:],cmap=colormap2,linewidth=0,rasterized=True,vmin=w_min,vmax=w_max)
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_ticks)
    ax.set_yticks(yticks_vals)
    ax.set_yticklabels(yticks_ticks)
    ax.set_ylabel(r'$y$ $[\mathrm{km}]$',fontsize=fntSize)
    ax.set_xlabel(r'$x$ $[\mathrm{km}]$',fontsize=fntSize)
    cbar=fig.colorbar(im, ax=ax) #, orientation='horizontal')

    title_fig_2 = FE_legend[2]
    ax.set_title(title_fig_2,fontsize=fntSize)
    
    ###############
    ### THETA plot ###
    ###############
    ax=axs[1][1]
    im = ax.pcolormesh(xPos/1e3,yPos/1e3,thetafield[zChoose,:,:],cmap=colormap3,linewidth=0,rasterized=True,vmin=t_min,vmax=t_max)
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_ticks)
    ax.set_yticks(yticks_vals)
    ax.set_yticklabels(yticks_ticks)
    ax.set_ylabel(r'$y$ $[\mathrm{km}]$',fontsize=fntSize)
    ax.set_xlabel(r'$x$ $[\mathrm{km}]$',fontsize=fntSize)
    cbar=fig.colorbar(im, ax=ax) #, orientation='horizontal')

    title_fig_3 = FE_legend[3]
    ax.set_title(title_fig_3,fontsize=fntSize)

    if (save_plot_opt==1):
        print(path_figure + fig_name)
        plt.savefig(path_figure + fig_name,dpi=300,bbox_inches = "tight")

# DEF5
def plot_XZ_UVWTHETA(case, case_open, yChoose, save_plot_opt, path_figure):
    
    numPlotsX=4
    numPlotsY=1
    
    ufield = case_open.u.isel(time=0).values
    vfield = case_open.v.isel(time=0).values
    wfield = case_open.w.isel(time=0).values
    thetafield = case_open.theta.isel(time=0).values
    xPos = case_open.xPos.isel(time=0,yIndex=yChoose).values
    yPos = case_open.yPos.isel(time=0,yIndex=yChoose).values
    zPos = case_open.zPos.isel(time=0,yIndex=yChoose).values
    
    if case == 'neutral':
        xticks_vals=[0,3.2,6.4,9.6,12.8]
        xticks_ticks=['0','3.2','6.4','9.6','12.8']
        yticks_vals=[0,0.287,0.574,0.861,1.148]
        yticks_ticks=['0','0.287','0.574','0.861','1.148']
    elif case == 'convective':
        xticks_vals=[0,1.5,3.0,4.5,6.0]
        xticks_ticks=['0','1.5','3.0','4.5','6.0']
        yticks_vals=[0,0.729,1.458,2.187,2.916]
        yticks_ticks=['0','0.729','1.458','2.187','2.916']
    elif case == 'stable':
        xticks_vals=[0,0.10,0.20,0.3,0.4]
        xticks_ticks=['0','0.1','0.2','0.3','0.4']
        yticks_vals=[0,0.10,0.20,0.3,0.4]
        yticks_ticks=['0','0.1','0.2','0.3','0.4']
    else:
         print("ERROR: INVALID CASE SELECTED")
            
    u_min = np.amin(np.amin(ufield))
    u_max = np.amax(np.amax(ufield))
    v_min = np.amin(np.amin(vfield))
    v_max = np.amax(np.amax(vfield))
    w_min = np.amin(np.amin(wfield))
    w_max = np.amax(np.amax(wfield))
    t_min = np.amin(np.amin(thetafield))
    t_max = np.amax(np.amax(thetafield))
    
    print(np.amax(zPos))

    fig_name = "UVWTHETA-XZ-"+case+".png"
    colormap1 = 'viridis'
    colormap2 = 'seismic'
    colormap3 = 'YlOrRd'
    FE_legend = [r'u [m/s] at y='+str(yPos[0,yChoose]/1e3)+' km',r'v [m/s] at y='+str(yPos[0,yChoose]/1e3)+' km',r'w [m/s] at y='+str(yPos[0,yChoose]/1e3)+' km', \
                 '\u03B8 [K] at y='+str(yPos[0,yChoose]/1e3)+' km']
    
    fntSize=20
    fntSize_title=22
    plt.rcParams['xtick.labelsize']=fntSize
    plt.rcParams['ytick.labelsize']=fntSize
    plt.rcParams['axes.linewidth']=2.0
    plt.rcParams['pcolor.shading']='auto'
    
    fig,axs = plt.subplots(numPlotsX,numPlotsY,sharey=False,sharex=False,figsize=(26,20))

    ###############
    ### U plot ###
    ###############
    ax=axs[0]
    im = ax.pcolormesh(xPos/1e3,zPos/1e3,ufield[:,yChoose,:],cmap=colormap1,linewidth=0,rasterized=True,vmin=u_min,vmax=u_max)
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_ticks)
    ax.set_yticks(yticks_vals)
    ax.set_yticklabels(yticks_ticks)
    ax.set_ylabel(r'$z$ $[\mathrm{km}]$',fontsize=fntSize)
    #ax.set_xlabel(r'$x$ $[\mathrm{km}]$',fontsize=fntSize)
    cbar=fig.colorbar(im, ax=ax) #, orientation='horizontal')

    title_fig_0 = FE_legend[0]
    ax.set_title(title_fig_0,fontsize=fntSize)

    ###############
    ### V plot ###
    ###############
    ax=axs[1]
    im = ax.pcolormesh(xPos/1e3,zPos/1e3,vfield[:,yChoose,:],cmap=colormap1,linewidth=0,rasterized=True,vmin=v_min,vmax=v_max)
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_ticks)
    ax.set_yticks(yticks_vals)
    ax.set_yticklabels(yticks_ticks)
    ax.set_ylabel(r'$z$ $[\mathrm{km}]$',fontsize=fntSize)
    #ax.set_xlabel(r'$x$ $[\mathrm{km}]$',fontsize=fntSize)
    cbar=fig.colorbar(im, ax=ax) #, orientation='horizontal')

    title_fig_1 = FE_legend[1]
    ax.set_title(title_fig_1,fontsize=fntSize)

    ###############
    ### W plot ###
    ###############
    w_min=-1.0*w_max
    ax=axs[2]
    im = ax.pcolormesh(xPos/1e3,zPos/1e3,wfield[:,yChoose,:],cmap=colormap2,linewidth=0,rasterized=True,vmin=w_min,vmax=w_max)
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_ticks)
    ax.set_yticks(yticks_vals)
    ax.set_yticklabels(yticks_ticks)
    ax.set_ylabel(r'$z$ $[\mathrm{km}]$',fontsize=fntSize)
    #ax.set_xlabel(r'$x$ $[\mathrm{km}]$',fontsize=fntSize)
    cbar=fig.colorbar(im, ax=ax) #, orientation='horizontal')
    
    title_fig_2 = FE_legend[2]
    ax.set_title(title_fig_2,fontsize=fntSize)
    
    ###############
    ### THETA plot ###
    ###############
    ax=axs[3]
    im = ax.pcolormesh(xPos/1e3,zPos/1e3,thetafield[:,yChoose,:],cmap=colormap3,linewidth=0,rasterized=True,vmin=t_min,vmax=t_max)
    ax.set_xticks(xticks_vals)
    ax.set_xticklabels(xticks_ticks)
    ax.set_yticks(yticks_vals)
    ax.set_yticklabels(yticks_ticks)
    ax.set_ylabel(r'$z$ $[\mathrm{km}]$',fontsize=fntSize)
    ax.set_xlabel(r'$x$ $[\mathrm{km}]$',fontsize=fntSize)
    cbar=fig.colorbar(im, ax=ax) #, orientation='horizontal')

    title_fig_3 = FE_legend[3]
    ax.set_title(title_fig_3,fontsize=fntSize)

    # save figure
    if (save_plot_opt==1):
        print(path_figure + fig_name)
        plt.savefig(path_figure + fig_name,dpi=300,bbox_inches = "tight")
        
           
# DEF6
def plot_mean_profiles(case, case_open, save_plot_opt, path_figure):

    colores_v = []
    colores_v.append('darkblue')
    colores_v.append('darkred')
    colores_v.append('dodgerblue')
    colores_v.append('orangered')

    lineas_v = []
    lineas_v.append('-')
    lineas_v.append('--')
    lineas_v.append('-.')
    lineas_v.append('.')
  
    y_min = 0.0
    y_max = 700.0 # FE_mean_MO[FE_mean_MO.shape[0]-1,0]
    
    ufield = case_open.u.isel(time=0).values
    vfield = case_open.v.isel(time=0).values
    wfield = case_open.w.isel(time=0).values
    thetafield = case_open.theta.isel(time=0).values
    fricVelfield = case_open.fricVel.isel(time=0).values
    #tkefield = case_0.TKE_0.isel(time=0).values
    xPos = case_open.xPos.isel(time=0,yIndex=0).values
    yPos = case_open.yPos.isel(time=0,yIndex=0).values
    zPos = case_open.zPos.isel(time=0,yIndex=0).values

    if case == 'neutral':
        xticks_vals=[0,1.0,2.0,3.0,4.0]
        xticks_ticks=['0','1.0','2.0','3.0','4.0']
        yticks_vals=[0,0.287,0.574,0.861,1.148]
        yticks_ticks=['0','0.287','0.574','0.861','1.148']
    elif case == 'convective':
        xticks_vals=[0,1.5,3.0,4.5,6.0]
        xticks_ticks=['0','1.5','3.0','4.5','6.0']
        yticks_vals=[0,0.729,1.458,2.187,2.916]
        yticks_ticks=['0','0.729','1.458','2.187','2.916']
    elif case == 'stable':
        xticks_vals=[0,0.10,0.20,0.3,0.4]
        xticks_ticks=['0','0.1','0.2','0.3','0.4']
        yticks_vals=[0,0.10,0.20,0.3,0.4]
        yticks_ticks=['0','0.1','0.2','0.3','0.4']
    else:
         print("ERROR: INVALID CASE SELECTED")
            
    yaxis_ticks = yticks_vals
    yaxis_vals = yticks_ticks
    yaxis_vals_empty = ['','','','','']
    
    print(zPos.shape)
    print(np.amax(zPos/1000.0))
    
    spdtemp = ufield * ufield + vfield * vfield + wfield * wfield
    spdfield = np.power(spdtemp,0.5)
    mean_U = np.mean(ufield,axis=(1,2))
    mean_V = np.mean(vfield,axis=(1,2))
    mean_THETA = np.mean(thetafield,axis=(1,2))
    mean_SPD = np.mean(spdfield,axis=(1,2))
    #mean_TKE = np.mean(tkefield,axis=(1,2))
    if case == 'neutral':
        mean_FRICVEL=np.mean(fricVelfield,axis=(0,1))
        print(fricVelfield.shape)
        print(mean_FRICVEL.shape)
    
    fntSize=20
    fntSize_title=22
    fntSize_legend=16
    plt.rcParams['xtick.labelsize']=fntSize
    plt.rcParams['ytick.labelsize']=fntSize
    plt.rcParams['axes.linewidth']=2.0
    numPlotsX=1
    numPlotsY=4
    fig,axs = plt.subplots(numPlotsX,numPlotsY,sharey=False,sharex=False,figsize=(28,12))
    
    fig_name = "MEAN-PROF-"+case+".png"
    
    ###############
    ### panel 0 ###
    ###############
    ax = axs[0]
    im = ax.plot(mean_SPD,zPos[:,0]/1000.0,lineas_v[0],color=colores_v[0],linewidth=2.5,markersize=8,label=case)
    if case == 'neutral':
        im2 = ax.plot((mean_FRICVEL/0.4)*np.log(zPos[:,0]/np.amax(case_open.z0m.isel(time=0).values)),zPos[:,0]/1000.0,lineas_v[1],color=colores_v[1],linewidth=2.5,markersize=8,label='log law')
    #ax.set_ylim([y_min,y_max])
    ax.set_xlabel(r"$WS$ $[$m s$^{-1}]$",fontsize=fntSize)
    ax.set_ylabel(r"$z$ $[$km$]$",fontsize=fntSize)
    ax.grid(True)
    ax.legend(loc=2,prop={'size': fntSize},edgecolor='white')
    ax.set_yticks(yaxis_ticks)
    ax.set_yticklabels(yaxis_vals,fontsize=fntSize)
    
    ###############
    ### panel 1 ###
    ###############
    ax = axs[1]
    im = ax.plot(mean_U,zPos[:,0]/1000.0,lineas_v[0],color=colores_v[0],linewidth=2.5,markersize=8,label=case)
    #ax.set_ylim([y_min,y_max])
    ax.set_xlabel(r"$U$ $[$m s$^{-1}]$",fontsize=fntSize)
    #ax.set_ylabel(r"$z$ $[$km$]$",fontsize=fntSize)
    ax.grid(True)
    #ax.legend(loc=2,prop={'size': fntSize_legend},edgecolor='white')
    ax.set_yticks(yaxis_ticks)
    ax.set_yticklabels(yaxis_vals_empty,fontsize=fntSize)
    
    ###############
    ### panel 2 ###
    ###############
    ax = axs[2]
    im = ax.plot(mean_V,zPos[:,0]/1000.0,lineas_v[0],color=colores_v[0],linewidth=2.5,markersize=8,label=case)
    #ax.set_ylim([y_min,y_max])
    ax.set_xlabel(r"$V$ $[$m s$^{-1}]$",fontsize=fntSize)
    #ax.set_ylabel(r"$z$ $[$m$]$",fontsize=fntSize)
    ax.grid(True)
    #ax.legend(loc=2,prop={'size': fntSize_legend},edgecolor='white')
    ax.set_yticks(yaxis_ticks)
    ax.set_yticklabels(yaxis_vals_empty,fontsize=fntSize)
    
    ###############
    ### panel 3 ###
    ###############
    ax = axs[3]
    im = ax.plot(mean_THETA,zPos[:,0]/1000.0,lineas_v[0],color=colores_v[0],linewidth=2.5,markersize=8,label=case)
    #ax.set_ylim([y_min,y_max])
    ax.set_xlabel("\u03B8 [K]",fontsize=fntSize)
    #ax.set_ylabel(r"$z$ $[$km$]$",fontsize=fntSize)
    ax.grid(True)
    #ax.legend(loc=2,prop={'size': fntSize_legend},edgecolor='white')
    ax.set_yticks(yaxis_ticks)
    ax.set_yticklabels(yaxis_vals_empty,fontsize=fntSize)
    
    if (save_plot_opt==1):
        print(path_figure + fig_name)
        plt.savefig(path_figure + fig_name,dpi=300,bbox_inches = "tight")

# DEF6
def compute_turb_profiles(FE_xr, array_out, case, save_plot_opt, path_figure):
    
    u_3d = np.squeeze(FE_xr.u.isel(time=0).values)
    v_3d = np.squeeze(FE_xr.v.isel(time=0).values)
    w_3d = np.squeeze(FE_xr.w.isel(time=0).values)
    th_3d = np.squeeze(FE_xr.theta.isel(time=0).values)
    z_3d = np.squeeze(FE_xr.zPos.isel(time=0).values)
    tau13_3d = np.squeeze(FE_xr.Tau31.isel(time=0).values)
    tau23_3d = np.squeeze(FE_xr.Tau32.isel(time=0).values)
    
    tau33_3d = np.squeeze(FE_xr.Tau33.isel(time=0).values) #w^2 SGS
    tauTH3_3d = np.squeeze(FE_xr.TauTH3.isel(time=0).values) #vertical heat flux SGS

    Nz = u_3d.shape[0]
    Ny = u_3d.shape[1]
    Nx = u_3d.shape[2]

    u_1d = np.mean(np.mean(u_3d,axis=2),axis=1)
    v_1d = np.mean(np.mean(v_3d,axis=2),axis=1)
    w_1d = np.mean(np.mean(w_3d,axis=2),axis=1)
    th_1d = np.mean(np.mean(th_3d,axis=2),axis=1)
    z_1d = np.mean(np.mean(z_3d,axis=2),axis=1)
    
    u_2d_mean = np.tile(u_1d,[Nx,1])
    u_3d_mean = np.tile(u_2d_mean,[Ny,1,1])
    u_3d_mean = np.swapaxes(u_3d_mean,0,2)
    u_3d_mean = np.swapaxes(u_3d_mean,1,2)
    
    v_2d_mean = np.tile(v_1d,[Nx,1])
    v_3d_mean = np.tile(v_2d_mean,[Ny,1,1])
    v_3d_mean = np.swapaxes(v_3d_mean,0,2)
    v_3d_mean = np.swapaxes(v_3d_mean,1,2)
    
    w_2d_mean = np.tile(w_1d,[Nx,1])
    w_3d_mean = np.tile(w_2d_mean,[Ny,1,1])
    w_3d_mean = np.swapaxes(w_3d_mean,0,2)
    w_3d_mean = np.swapaxes(w_3d_mean,1,2)
    
    th_2d_mean = np.tile(th_1d,[Nx,1])
    th_3d_mean = np.tile(th_2d_mean,[Ny,1,1])
    th_3d_mean = np.swapaxes(th_3d_mean,0,2)
    th_3d_mean = np.swapaxes(th_3d_mean,1,2)
    
    up = u_3d - u_3d_mean
    vp = v_3d - v_3d_mean
    wp = w_3d - w_3d_mean
    thp = th_3d - th_3d_mean
    
    upup = up*up
    upwp = up*wp
    vpvp = vp*vp
    vpwp = vp*wp
    wpwp = wp*wp
    thpwp = thp*wp
    tke = 0.5*(upup+vpvp+wpwp)
    
    upup_1d = np.mean(np.mean(upup,axis=2),axis=1)
    upwp_1d = np.mean(np.mean(upwp,axis=2),axis=1)
    vpvp_1d = np.mean(np.mean(vpvp,axis=2),axis=1)
    vpwp_1d = np.mean(np.mean(vpwp,axis=2),axis=1)
    tau13_1d = np.mean(np.mean(tau13_3d,axis=2),axis=1)
    tau23_1d = np.mean(np.mean(tau23_3d,axis=2),axis=1)
    
    tau33_1d = np.mean(np.mean(tau33_3d,axis=2),axis=1)
    tauTH3_1d = np.mean(np.mean(tauTH3_3d,axis=2),axis=1)
    
    Upwp_1d = np.sqrt(np.power(upwp_1d,2.0)+np.power(vpwp_1d,2.0))
    #Upwp_1d = np.mean(np.mean(np.sqrt(np.power(upwp,2.0)+np.power(vpwp,2.0)),axis=2),axis=1)
    wpwp_1d = np.mean(np.mean(wpwp,axis=2),axis=1)
    tke_1d = np.mean(np.mean(tke,axis=2),axis=1)
    thpwp_1d = np.mean(np.mean(thpwp,axis=2),axis=1)
    #tau1323_1d = np.mean(np.mean(np.sqrt(np.power(tau13_3d,2.0)+np.power(tau23_3d,2.0)),axis=2),axis=1)
    tau1323_1d = np.sqrt(np.power(tau13_1d,2.0)+np.power(tau23_1d,2.0))
    #tau1323_1d = np.mean(np.mean(tau13_3d,axis=2),axis=1) + np.mean(np.mean(tau23_3d,axis=2),axis=1)
    
    array_out = np.zeros([Nz,15])
    array_out[:,0] = z_1d
    array_out[:,1] = upup_1d
    array_out[:,2] = upwp_1d
    array_out[:,3] = vpvp_1d
    array_out[:,4] = vpwp_1d
    array_out[:,5] = Upwp_1d
    array_out[:,6] = wpwp_1d
    array_out[:,7] = tke_1d
    array_out[:,8] = thpwp_1d
    array_out[0:Nz-1,9] = 0.5*(tau1323_1d[0:Nz-1]+tau1323_1d[1:Nz])
    array_out[:,10] = 0.5*(upup_1d*upup_1d+vpwp_1d*vpwp_1d+wpwp_1d*wpwp_1d)
    #array_out[:,9] = tau1323_1d
    array_out[:,11]=tau33_1d
    array_out[:,12]=tauTH3_1d
                               
    return array_out

#DEF7
def plot_turb_profiles(case, case_open, FE_turb_tmp, save_plot_opt, path_figure):

    colores_v = []
    colores_v.append('darkblue')
    colores_v.append('darkred')
    colores_v.append('dodgerblue')
    colores_v.append('orangered')

    lineas_v = []
    lineas_v.append('-')
    lineas_v.append('--')
    lineas_v.append('-.')
    lineas_v.append('.')
  
    y_min = 0.0
    y_max = 700.0 # FE_mean_MO[FE_mean_MO.shape[0]-1,0]
    zPos = case_open.zPos.isel(time=0,yIndex=0).values
    
    if case == 'neutral':
        xticks_vals=[0,1.0,2.0,3.0,4.0]
        xticks_ticks=['0','1.0','2.0','3.0','4.0']
        yticks_vals=[0,0.287,0.574,0.861,1.148]
        yticks_ticks=['0','0.287','0.574','0.861','1.148']
    elif case == 'convective':
        xticks_vals=[0,1.5,3.0,4.5,6.0]
        xticks_ticks=['0','1.5','3.0','4.5','6.0']
        yticks_vals=[0,0.729,1.458,2.187,2.916]
        yticks_ticks=['0','0.729','1.458','2.187','2.916']
    elif case == 'stable':
        xticks_vals=[0,0.10,0.20,0.3,0.4]
        xticks_ticks=['0','0.1','0.2','0.3','0.4']
        yticks_vals=[0,0.10,0.20,0.3,0.4]
        yticks_ticks=['0','0.1','0.2','0.3','0.4']
    else:
         print("ERROR: INVALID CASE SELECTED")
            
    yaxis_ticks = yticks_vals
    yaxis_vals = yticks_ticks
    yaxis_vals_empty = ['','','','','']


    fntSize=20
    fntSize_title=22
    fntSize_legend=16
    plt.rcParams['xtick.labelsize']=fntSize
    plt.rcParams['ytick.labelsize']=fntSize
    plt.rcParams['axes.linewidth']=2.0

    numPlotsX=1
    numPlotsY=4
    fig,axs = plt.subplots(numPlotsX,numPlotsY,sharey=False,sharex=False,figsize=(28,12))

    ###############
    ### panel 0 ###
    ###############
    ax = axs[0]
    im2 = ax.plot(FE_turb_tmp[:,10]+FE_turb_tmp[:,7],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[0],linewidth=2.5,markersize=8,label='Total')
    im2 = ax.plot(FE_turb_tmp[:,7],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[1],linewidth=2.5,markersize=8,label='Res.')
    im2 = ax.plot(FE_turb_tmp[:,10],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[2],linewidth=2.5,markersize=8,label='SGS')
    ax.set_xlabel(r"TKE $[$m$^2$ s$^{-2}]$",fontsize=fntSize)
    ax.set_ylabel(r"$z$ $[$km$]$",fontsize=fntSize)
    ax.legend(loc=1,prop={'size': fntSize},edgecolor='white')
    ax.set_yticks(yaxis_ticks)
    ax.grid(True)
    ax.set_yticklabels(yaxis_vals,fontsize=fntSize)
    
    ###############
    ### panel 1 ###
    ###############
    ax = axs[1]
    im2 = ax.plot(FE_turb_tmp[:,6]+FE_turb_tmp[:,11],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[0],linewidth=2.5,markersize=8,label=case)
    ax.set_xlabel(r"$\sigma_w^2$ $[$m$^2$ s$^{-2}]$",fontsize=fntSize)
    ax.set_yticks(yaxis_ticks)
    ax.grid(True)
    ax.set_yticklabels(yaxis_vals_empty,fontsize=fntSize)
    
    ###############
    ### panel 2 ###
    ###############
    ax = axs[2]
    im2 = ax.plot(FE_turb_tmp[:,8]+FE_turb_tmp[:,12],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[0],linewidth=2.5,markersize=8,label=case)
    im2 = ax.plot(FE_turb_tmp[:,8],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[1],linewidth=2.5,markersize=8,label=case)
    im2 = ax.plot(FE_turb_tmp[:,12],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[2],linewidth=2.5,markersize=8,label=case)
    ax.set_yticks(yaxis_ticks)
    ax.grid(True)
    ax.set_yticklabels(yaxis_vals_empty,fontsize=fntSize)
    ax.set_xlabel(r"$\langle w'"+"\u03B8'"+r"\rangle$ $[$m K s$^{-1}]$",fontsize=fntSize) 
    
    ###############
    ### panel 3 ###
    ###############
    ax = axs[3]
    im2 = ax.plot(FE_turb_tmp[:,5]+FE_turb_tmp[:,9],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[0],linewidth=2.5,markersize=8,label=case+': total')
    im2 = ax.plot(FE_turb_tmp[:,5],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[1],linewidth=2.5,markersize=8,label=case+': res.')
    im2 = ax.plot(FE_turb_tmp[:,9],zPos[:,0]/1000.0,lineas_v[0],color=colores_v[2],linewidth=2.5,markersize=8,label=case+': SGS')
    ax.set_xlabel(r"$\sigma_w^2$ $[$m$^2$ s$^{-2}]$",fontsize=fntSize)
    ax.set_yticks(yaxis_ticks)
    ax.grid(True)
    ax.set_yticklabels(yaxis_vals_empty,fontsize=fntSize)
    ax.set_xlabel(r"$\langle U' w' \rangle$ $[$m$^2$ s$^{-2}]$",fontsize=fntSize)
    
    fig_name = "TURB-PROF-"+case+".png"
    
    if (save_plot_opt==1):
        print(path_figure + fig_name)
        plt.savefig(path_figure + fig_name,dpi=300,bbox_inches = "tight")

