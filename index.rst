:orphan:

FastEddy
========

`FastEddy`_ is a resident-GPU large eddy simulation (LES) model owned by the National Center for Atmospheric Research (`NCAR`_) Research Applications Laboratory (`RAL`_). It is designed for future turbulence-resolving numerical weather prediction. This is a tutorial designed so that a user can understand how to execute the model, and visualize and analyze the output.

.. _FastEddy: https://ral.ucar.edu/solutions/products/fasteddy
.. _NCAR: https://ncar.ucar.edu
.. _RAL: https://ral.ucar.edu
  
.. raw:: html

   <style>
   /* front page: hide chapter titles
    * needed for consistent HTML-PDF-EPUB chapters
    */
   div#introduction.section,
   div#cases.section,
   div#questions.section,
   </style>
   
.. only:: comment

    This is a comment
  
.. toctree::
  :hidden:

   coc
  
.. toctree::
  :caption: INTRODUCTION 
 
  temp1
  temp2
  temp3
  
  introduction.rst
  
.. toctree::
  :caption: CASES 
  :maxdepth: 1
  :hidden:
  
  cases/NBL.rst
  cases/CBL.rst
  cases/SBL.rst
  cases/MBL.rst
 
.. toctree::
  :caption: SENSITIVITY TEST
  :maxdepth: 1
  :hidden:
  
   sensitivity/SNS.rst
   
.. toctree::
  :caption: QUESTIONS
  :maxdepth: 1
  :hidden:
