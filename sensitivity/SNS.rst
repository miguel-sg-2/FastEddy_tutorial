OVERARCHING QUESTIONS

What are main differences in the scale and magnitude of the resolved turbulence among the three cases?
How do the boundary layer heights differ among the cases? Why?
How does the TKE vary among the three cases? Which case has the highest TKE and why?
Other...
SENSITIVITY TESTS

(Here, the user will make some modifications to the default parameters such as changing the grid spacing, stretching, model time step, advection scheme, number of grid points, domain decomposition and number of GPUs, etc, etc. Here, the user will execute the sensitivity test, and visualize and analyze the output)

Re-run the neutral case with [N_x,N_y,N_z]=[400,400,122] and isotropic grid spacings of: [dx,dy,dz]=[10,10,10]. Adjust the model time step accordingly. Re-make all plots and discuss the differences between the control case. How much faster was the simulation completed?
Re-run the convective case with a surface heat flux of 0.70 Km/s. Re-make all plots and discuss the differences between the control case.
Re-run the neutral case with z_0=0.3 m. Re-make all plots and discuss the differences between the control case.
Re-run the neutral case with the first order upwind advection scheme. Re-make all plots and discuss the differences between the control case. Why is the first order scheme a bad choice?
Re-run the stable case with a surface cooling rate of -0.5 K/h. Re-make all plots and discuss the differences between the control case.
Re-run the stable case using 4 GPUs instead of the control simulation's 8 GPUs. How much slower does the case run?
EXTRA

x^2+y^2=z^2

\frac{ \sum_{t=0}^{N}f(t,k) }{N}
