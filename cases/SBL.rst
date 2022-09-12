CASE 3: DRY STABLE BOUNDARY LAYER
=================================

Background
------------------

This is the stable boundary layer scenario described by Sauer and Munoz-Esparza (2020). This the stable boundary layer scenario outlined in Kosovic and Curry (2000).

Input parameters
----------------

* Number of grid points: :math:`[N_x,N_y,N_z]=[128,128,122]`
* Isotropic grid spacings: :math:`[dx,dy,dz]=[3.125,3.125,3.125]`
* Domain size: :math:`[0.4 \times 0.4 \times 0.4]` km
* Model time step: 0.005 s
* Geostrophic wind: :math:`[U_g,V_g]=[9,0]` m/s
* Advection scheme: Hybrid 5th-6th order, blending coefficient of 0.8
* Time scheme: 3rd order Runge Kutta
* Latitude: :math:`72.5^{\circ}` N
* Surface potential temperature: :math:`265` K
* Potential temperature profile:
.. math::
  \partial{\theta}/\partial z =
    \begin{cases}
      0 & \text{if $z$ $\le$ 100 m}\\
      0.01 & \text{$z$ > 100 m}
    \end{cases}   
* Surface heat flux:  :math:`-0.25` K/h
* Surface roughness length: :math:`z_0=0.05` m
* Rayleigh damping layer: uppermost :math:`100` m of the domain
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

XY-plane views of instantaneous velocity components at t=2 h (FE_TEST.1440000).

.. image:: notebooks/UVW-XY-stable.png
  :width: 1200
  :alt: Alternative text
  
XZ-plane views of instantaneous velocity components at t=2 h (FE_TEST.1440000).

.. image:: notebooks/UVW-XZ-stable.png
  :width: 1200
  :alt: Alternative text
  
Mean profiles at t=2 h (FE_TEST.1440000).

.. image:: notebooks/MEAN-PROF-stable.png
  :width: 600
  :alt: Alternative text

Analyze the output
------------------

* Using the XY and XZ cross sections, discuss the characteristics of the resolved turbulence.
* What is the boundary layer height in the stable case?
* Using the vertical profile plots, explain why the boundary layer is stable.
* Other...
