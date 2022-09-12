CASE 1: DRY NEUTRAL BOUNDARY LAYER
==================================

Background
----------

This is a canonical neutral boundary layer scenario described by Sauer and Munoz-Esparza (2020). A geostrophic wind is prescribed over ground with a set aerodynamic roughness length under a neutrally stratified boundary layer. The purpose of this test case is to visualize and analyze the resultant flow and turbulence characteristics that develop when the LES reaches statistical steady-state.

Input parameters
----------------

* Number of grid points: :math:`[N_x,N_y,N_z]=[800,800,122]`
* Isotropic grid spacings: :math:`[dx,dy,dz]=[5,5,5]`
* Domain size: :math:`[4 \times 4 \times 1.2]` km
* Model time step: 0.01 s
* Advection scheme: 3rd order QUICK
* Time scheme: 3rd order Runge Kutta
* Geostrophic wind: :math:`[U_g,V_g]=[10,0]` m/s
* Latitude: :math:`54.0^{\circ}` N
* \begin{equation}
  D_{it} =
    \begin{cases}
      1 & \text{if bank $i$ issues ABs at time $t$}\\
      2 & \text{if bank $i$ issues CBs at time $t$}\\
      0 & \text{otherwise}
    \end{cases}       
\end{equation}
* Potential temperature gradients: The potential temperature is constant at 300 K from the surface to :math:`z= 500` m. Between :math:`500-650` m, the vertical gradient is :math:`0.08` K/m. Above :math:`650` m, the vertical gradient is :math:`0.003` K/m.
* Surface heat flux:  :math:`0.0` Km/s
* Surface roughness length: :math:`z_0=0.1` m
* Rayleigh damping layer: uppermost :math:`400` m of the domain
* Cell perturbations: :math:`\pm 0.25` K 
* Top boundary condition: free slip
* Lateral boundary conditions: periodic
* Time period: 2 h

Execute FastEddy
----------------

Here we will describe how to download the FastEddy package and run the model. The package will include the executables, a script to install the executables in a directory structure, and other files such as the Jupyter notebooks.

Visualize the output
--------------------

Open the Jupyter notebook entitled "FE-TUTORIAL-analyses.ipynb" and execute it. Please ensure you create the plots exactly as shown below.

XY-plane views of instantaneous velocity components at t=1.8 h (FE_TEST.648000).

.. image:: notebooks/UVW-XY-neutral.png
  :width: 1200
  :alt: Alternative text
  
XZ-plane views of instantaneous velocity components at t=1.8 h (FE_TEST.648000).

.. image:: notebooks/UVW-XZ-neutral.png
  :width: 600
  :alt: Alternative text
  
Mean profiles at t=1.8 h (FE_TEST.648000).

.. image:: notebooks/MEAN-PROF-neutral.png
  :width: 600
  :alt: Alternative text
  
Other plots TBD...

Analyze the output
------------------

* Using the XY and XZ cross sections, discuss the characteristics of the resolved turbulence.
* What is the boundary layer height in the neutral case?
* Using the vertical profile plots, explain why the boundary layer is neutral.
* Other...
