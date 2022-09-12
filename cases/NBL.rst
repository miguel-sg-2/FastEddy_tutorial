CASE 1: DRY NEUTRAL BOUNDARY LAYER
==================================

Background
----------

This is a canonical neutral boundary layer scenario. The case is broadly based upon Sauer and Munoz-Esparza (2020) but is not identical. A geostrophic wind is prescribed over ground with a set aerodynamic roughness length under a neutrally stratified boundary layer. The purpose of this test case is to visualize and analyze the resultant flow and turbulence characteristics that develop when the LES reaches statistical steady-state.

Input parameters
----------------

* Number of grid points: :math:`[N_x,N_y,N_z]=[640,634,58]`
* Isotropic grid spacings: :math:`[dx,dy,dz]=[20,20,05]`
* Domain size: :math:`[6.4 \times 6.34 \times 1.148]` km
* Model time step: 0.05 s
* Advection scheme: 3rd order QUICK
* Time scheme: 3rd order Runge Kutta
* Geostrophic wind: :math:`[U_g,V_g]=[10,0]` m/s
* Latitude: :math:`54.0^{\circ}` N
* Surface potential temperature: :math:`300` K
* Potential temperature profile:
.. math::
  \partial{\theta}/\partial z =
    \begin{cases}
      0 & \text{if $z$ $\le$ 500 m}\\
      0.08 & \text{if 500 m < $z$ $\le$ 650 m}\\
      0.003 & \text{if $z$ > 650 m}
    \end{cases} 
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

XY-plane views of instantaneous velocity components at t=7 h (FE_TEST.504000).

.. image:: ../images/UVWTHETA-XY-neutral.png
  :width: 1200
  :alt: Alternative text
  
XZ-plane views of instantaneous velocity components at t=7 h (FE_TEST.504000).

.. image:: ../images/UVWTHETA-XZ-neutral.png
  :width: 600
  :alt: Alternative text
  
Mean state variable profiles at t=7 h (FE_TEST.504000).

.. image:: ../images/MEAN-PROF-neutral.png
  :width: 600
  :alt: Alternative text
 
Mean turbulence profiles at t=7 h (FE_TEST.504000) (using previous 1-hour mean).

.. image:: ../images/TURB-PROF-neutral.png
  :width: 600
  :alt: Alternative text 
 
Other plots TBD...

Analyze the output
------------------

* Using the XY and XZ cross sections, discuss the characteristics of the resolved turbulence.
* What is the boundary layer height in the neutral case?
* Using the vertical profile plots, explain why the boundary layer is neutral.
* Other...
