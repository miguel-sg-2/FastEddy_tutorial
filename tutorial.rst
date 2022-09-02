CASE 1: NEUTRAL BOUNDARY LAYER
===============================

Background
----------

This is a canonical neutral boundary layer scenario described by Sauer and Munoz-Esparza (2020). A geostrophic wind is prescribed over ground with a set aerodynamic roughness length under a neutrally stratified boundary layer. The purpose of this test case is to visualize and analyze the resultant flow and turbulence characteristics that develop when the LES reaches statistical steady-state.

Input parameters
----------------

The number of grid points are [$N_x$,$N_y$,$N_z$]=[800,800,122]. The isotropic grid spacings are [dx,dy,dz]=[5,5,5] m. The domain extents are
4 km X 4 km X 1.2 km. The latitude is 54.0 N. The geostrophic wind is [U_g,V_g]=[10,0] m/s. The surface roughness length is z_0=0.1 m. There is zero surface kinematic heat flux. The potential temperature is constant from the surface to z=500 m. Between 500-650 m, the vertical gradient of theta is 0.08 K/m. Above 650 m, the vertical gradient of potential temperature is 0.003 K/m. A Rayleigh damping layer is applied in the uppermost 400 m of the domain. Cell perturbations of +/-0.25 K are added in the first 400 m of the domain to instigate turbulence. Periodic lateral boundary conditions are applied the top boundary is free slip.

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

Input parameters
----------------

Execute FastEddy
----------------

Visualize the output
--------------------

Analyze the output
------------------
