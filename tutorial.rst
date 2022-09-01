Build the code
==============

The procedure below describes the procedure to build the code on the NCAR `Casper`_ supercomputer.

.. _Casper: https://arc.ucar.edu/knowledge_base/70549550

1. mkdir /glade/scratch/${USER}/FastEddy/
2. cd /glade/scratch/${USER}/FastEddy/
3. git clone https://github.com/NCAR/<name of public version> vtest
4. git checkout <branchname>
5. cd vtest/SRC/TIME_INTEGRATION/TEST/
6. module purge
7. module load ncarenv/1.3
8. module load intel/19.0.5
9. module load ncarcompilers/0.5.0
10. module load openmpi/3.1.6
11. module load netcdf/4.7.4
12. module load cuda/11.4.0
13. make
14. ls -ltr (check to make sure executable file named timeInt_test is created)

Execute the model
=================

1. mkdir /glade/scratch/${USER}/FastEddy/simulations/neutralPBL
2. cd /glade/scratch/${USER}/FastEddy/simulations/neutralPBL
3. mkdir output
4. cp /glade/scratch/${USER}/FastEddy/vtest/SRC/TIME_INTEGRATION/TEST/TEST_Params.in . (note the tutorial neutral test case needs to be added here)
5. Create PBS submission script ('submit-FE-pbs')

.. code-block:: bash

  #PBS -N FastEddy 
  #PBS -A <CHARGE ACCCOUNT>
  #PBS -l select=1:ncpus=1:mpiprocs=1:ngpus=1:mem=100GB
  #PBS -l gpu_type=v100
  #PBS -l walltime=02:00:00
  #PBS -q casper
  #PBS -j oe
  
  mpirun /glade/scratch/${USER}/FastEddy/vtest/SRC/TIME_INTEGRATION/TEST/timeInt_test TEST_Params.in    

5. chmod a+x submit-FE-pbs
6. qsub < submit-FE-pbs

Visualize the output
====================

Here we will have the user go through a Jupyter notebook to make some key plots (use Domingo's notebook as a starting point)

Analyze the output
==================

Here we will ask some basic questions about the plots to gain an understanding of the simulation

Modify the parameter file
=========================

Here, the user will make some modifications to the default parameters such as changing the grid spacing, stretching, model time step, advection scheme, number of grid points, domain decomposition and number of GPUs, etc, etc.

Execute the sensitivity test and examine output
===============================================

Here, the user will execute the sensitivity test, and visualize and analyze the output
