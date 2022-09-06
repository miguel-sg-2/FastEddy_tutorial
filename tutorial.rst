CASE 1: NEUTRAL BOUNDARY LAYER
===============================

Background
----------

This is a canonical neutral boundary layer scenario described by Sauer and Munoz-Esparza (2020). A geostrophic wind is prescribed over ground with a set aerodynamic roughness length under a neutrally stratified boundary layer. The purpose of this test case is to visualize and analyze the resultant flow and turbulence characteristics that develop when the LES reaches statistical steady-state.

Input parameters
----------------

* Number of grid points: :math:`[N_x,N_y,N_z]=[800,800,122]`
* Isotropic grid spacings: :math:`[N_x,N_y,N_z]=[800,800,122]`
* Domain size: :math:`4 km \times 4 km \times 1.2 km`
* Geostrophic wind: :math:`[U_g,V_g]=[10,0]` m/s
* Latitude: :math:`54.0` N
* Potential temperature gradients: The potential temperature is constant from the surface to :math:`z= 500` m. Between :math:`500-650` m, the vertical gradient is :math:`0.08` K/m. Above :math:`650` m, the vertical gradient is :math:`0.003` K/m.
* Surface heat flux:  :math:`0.0 W/m^2`
* Surface roughness length: :math:`z_0=0.1` m
* Rayleigh damping layer: uppermost :math:`400` m of the domain
* Cell perturbations: :math:`\pm 0.25` K are added in the first :math:`400` m
* Top boundary condition: free slip
* Lateral boundary conditions: periodic

Execute FastEddy
----------------

Visualize the output
--------------------

Analyze the output
------------------


CASE 2: CONVECTIVE BOUNDARY LAYER
==================================

Background
----------

Input parameters
----------------

Execute FastEddy
----------------

Visualize the output
--------------------

Analyze the output
------------------

CASE 3: STABLE BOUNDARY LAYER
=============================

Background
----------

Input parameters
----------------

Execute FastEddy
----------------

Visualize the output
--------------------

Analyze the output
------------------


CASE 4: SENSITIVITY TEST
========================

Here, the user will make some modifications to the default parameters such as changing the grid spacing, stretching, model time step, advection scheme, number of grid points, domain decomposition and number of GPUs, etc, etc. Here, the user will execute the sensitivity test, and visualize and analyze the output

Background
----------

:math:`x^2+y^2=z^2`

.. math::

   \frac{ \sum_{t=0}^{N}f(t,k) }{N}


Input parameters
----------------

Execute FastEddy
----------------

Visualize the output
--------------------

Analyze the output
------------------
