Non-precipitating shallow cumuls case
=====================================

This tutorial case is the BOMEX LES intercomparison study from Siebesma et al. (2003), corresponding to a non-precipitating shallow cumulus cloud case informed by the Barbados Oceanographic and Meteorological Experiment (BOMEX, Holland & Rasmusson, 1973). The forcing consists of two different sources including prescribed kinematic surface fluxes of sensible and latent heat and large-scale forcing (LSF) tendencies due to mesoscale horizontal advection of water vapor mixing ratio, liquid potential temperature and horizontal momentum. The LSF includes subsidence to compensate the integrated effect of surface fluxes and advection tendencies, formulated as a prescribed time-invariant subsidence profile multiplied by the vertical gradient of horizontally averaged fields accros the domain. The main settings of this case are described below and are further detailed in Munoz-Esparza et al. (2022).

Input parameters
----------------

* Number of grid points: :math:`[N_x,N_y,N_z]=[152,146,122]`
* Isotropic grid spacings: :math:`[dx,dy,dz]=[100,100,40]` m
* Domain size: :math:`[15.2 \times 14.6 \times 4.9]` km
* Model time step: :math:`0.075` s
* Geostrophic wind: :math:`[U_g,V_g]=[10,0]` m s:math:`^{-1}`
* Advection schemes: 5th-order upwind (dry dynamics), 3rd-order upwind (water vapor), and 3rd-order WENO (liquid water)
* Time scheme: 3rd-order Runge Kutta
* Latitude: :math:`14.94^{\circ}` N
* Surface potential temperature: :math:`299.1` K
* Surface sensible heat flux: :math:`8 \times 10^{-3}` K m s:math:`^{-1}`
* Surface latent heat flux: :math:`5.2 \times 10^{-5}` m s:math:`^{-1}`
* Surface roughness length: :math:`z_0=0.0002` m
* Rayleigh damping layer: uppermost :math:`500` m of the domain
* Initial perturbations: :math:`\pm 0.1` K
* Depth of perturbations: :math:`1600` m
* Top boundary condition: free slip
* Lateral boundary conditions: periodic
* Time period: :math:`6` h
* Initital conditions: vertical profiles of :math:`u`, :math:`q_v`, and :math:`SGSTKE` as specified in Siebesma et al. (2003)
* Large-scale forcings: vertical profiles of subsidence and horizontal advection of potential temperature and water vapor as specified in Siebesma et al. (2003)
