Non-precipitating shallow cumuls case
=====================================

This tutorial case is the BOMEX LES intercomparison study from Siebesma et al. (2003), corresponding to a non-precipitating shallow cumulus cloud case informed by the Barbados Oceanographic and Meteorological Experiment (BOMEX, Holland & Rasmusson, 1973). The forcing consists of two different sources including prescribed kinematic surface fluxes of sensible and latent heat and large-scale forcing (LSF) tendencies due to mesoscale horizontal advection of water vapor mixing ratio, liquid potential temperature and horizontal momentum. The LSF includes subsidence to compensate the integrated effect of surface fluxes and advection tendencies, formulated as a prescribed time-invariant subsidence profile multiplied by the vertical gradient of horizontally averaged fields accros the domain. The main settings of this case are described below and are further detailed in Munoz-Esparza et al. (2022).

Input parameters
----------------

* Number of grid points: :math:`[N_x,N_y,N_z]=[152,146,122]`
* Isotropic grid spacings: :math:`[dx,dy,dz]=[100,100,40]` m
* Domain size: :math:`[15.2 \times 14.6 \times 4.9]` km
* Model time step: 0.075 s
