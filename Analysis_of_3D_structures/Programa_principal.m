clc
clear all
close all

%Ingreso de módulo de elasticidad y sección transversal de cada elemento
% E=200e9;
E=50e9;
A=0.000076;
EA=E*A;

%Ingreso de los elementos mediante su comunicacion entre nodos
% elementNodes=[2 4;1 4;3 4]
elementNodes=[1 5;1 8;2 5;2 6;3 6;3 7;4 7;4 8;5 6;5 8;6 7;7 8;5 9;6 9;7 9;8 9];
numberElements=size(elementNodes,1);
numberNodes=max(max(elementNodes));

%Ingreso de coordenadas de cada nodo en orden
% nodeCoordinates=[0 0 0;0 0 30;40 0 0;30 -20 25];
nodeCoordinates=[0 0 0;20 0 0;20 20 0;0 20 0;
                10 0 40; 20 10 40;10 20 40;0 10 40;
                10 10 60];

%Extraccion de las coordenadas en x,y,z
xx=nodeCoordinates(:,1);
yy=nodeCoordinates(:,2);
zz=nodeCoordinates(:,3);

GDof=3*numberNodes;
displacements=zeros(GDof,1);
force=zeros(GDof,1);

%carga en nodos 1,2 y 3
%force(1)=1;
force(27)=-15000;


%Matriz de rigidez
[stiffness]=formStiffness3Dtruss(GDof,numberElements,elementNodes,nodeCoordinates,xx,yy,zz,EA)

%Desplazamientos que son cero
prescribedDof=[1:12]';

%Calculo de desplazamientos
displacements=solution3d(GDof,prescribedDof,stiffness,force)

%Calculo de los esfuerzos en cada elemento
stress=stresses3Dtruss(numberElements,elementNodes,xx,yy,zz,displacements,E)

%Calculo de las fuerzas los tres ejes en cada nodo
force=(stiffness*displacements)

%Comprobación de que la sumatoria de fuerzas del sistema da cero (estático)
sumatoria_de_fuerzas=0;
for i=1:GDof
sumatoria_de_fuerzas=force(i,1)+sumatoria_de_fuerzas;
end
sumatoria_de_fuerzas

%Graficación de la armadura
Grafica(elementNodes,numberElements,xx,yy,zz,displacements,nodeCoordinates,stress)
