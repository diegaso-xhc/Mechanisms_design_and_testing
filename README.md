# Mechanisms_design_and_testing

## Overview of the repostitory
<div align="justify">
Designing and testing mechanisms is essential for the development of mechatronic systems, such as manufacturing machinery or robotic assemblies. In an attempt to speed up mechanism calculations, specialized software as Autocad or Solidworks has been developed. Nevertheless, in many instances, complex FEM simulations are required in final stages of manufacturing. Initially, theoretical force and stress estimations are enough for making design decisions.
<br />
<br />
This repository provides algorithms to automatically design, visualize and calculate planar mechanisms. It also provides algorithms to calculate stress and force effects on 3D structures for initial design estimations. 
<br /> 
<br /> 

## Understanding repository

The repository contains two parts. One for planar mechanism synthesis, and another one for 3D structures analysis. The algorithms were implemented using:

```
- Mechanism synthesis --> Initially Python 2.0, currently tested and running in Python 3.9 (some minor functionalities might need updating)
- Analysis of 3D structures --> Tested in Matlab R2021b
```
Mechanism synthesis launches a graphical interface where the user needs to input expected link motions. Then the program generates a visualization of the resulting mechanism (if plausible) and outputs corresponding dimensions for testing. 
<br />

For analysis of 3D structures the user needs to run the main.m file (programa principal in Spanish). Nodes and forces applied to the structure can be modified according to the user application. The algorithms in this repository use the theory of virtual work to calculate forces and stress values in the entirety of the structure. 
<br />
<br />

## Examples
  
### Mechanism synthesis for two given positions

The following figure shows the calculated mechanism by using our algorithms. Dimensional information is displayed at the bottom left:

<p align="center">
  <img src="/Visualizations/Mechanism_synthesis_1.png" width="650" />  
</p>

<br />

### Mechanism synthesis for three given positions

The following figure shows the calculated mechanism by using our algorithms. Dimensional information is displayed at the bottom left:

<p align="center">
  <img src="/Visualizations/Mechanism_synthesis_2.png" width="650" />  
</p>

<br />

### Structure deformation after appliyng a vertical force of 15kN

The following figure shows the structure with a force applied vertically at its top. Color coded elements show which ones are under the most stress due to external forces (red being the highest). On the right side the deformed structure can be visualized:

<p align="center">
  <img src="/Visualizations/Structures.png" width="650" />  
</p>

<br />

## License

Developed by Diego Hidalgo C. (2023). This repository is intended for research purposes only. If you wish to use any parts of the provided code for commercial purposes, please contact the author at hidalgocdiego@gmail.com.
