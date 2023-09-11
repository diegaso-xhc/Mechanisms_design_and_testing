function [stiffness]=formStiffness3Dtruss(GDof,numberElements,elementNodes,nodeCoordinates,xx,yy,zz,EA)
stiffness=zeros(GDof);
for e=1:numberElements;
indice=elementNodes(e,:);
elementDof=[indice(1)*3-2 indice(1)*3-1 indice(1)*3 indice(2)*3-2 indice(2)*3-1 indice(2)*3];
xa=xx(indice(2))-xx(indice(1));
ya=yy(indice(2))-yy(indice(1));
za=zz(indice(2))-zz(indice(1));
length_element=sqrt(xa*xa+ya*ya+za*za);
cx=xa/length_element;
cy=ya/length_element;
cz=za/length_element;

k1=EA/length_element*[cx*cx cx*cy cx*cz -cx*cx -cx*cy -cx*cz;cx*cy cy*cy cy*cz -cy*cx -cy*cy -cy*cz;cx*cz cy*cz cz*cz -cx*cz -cy*cz -cz*cz;-cx*cx -cx*cy -cx*cz cx*cx cx*cy cx*cz;-cx*cy -cy*cy -cy*cz cy*cx cy*cy cy*cz;-cx*cz -cy*cz -cz*cz cx*cz cy*cz cz*cz]; %aqui se debe cambiar si se tiene diferentes areas o materiales
stiffness(elementDof,elementDof)=stiffness(elementDof,elementDof)+k1;
end