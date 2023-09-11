function sigma=stresses3Dtruss(numberElements,elementNodes,xx,yy,zz,displacements,E)

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

sigma(e)=(E/length_element)*[-cx -cy -cz cx cy cz]*displacements(elementDof);
end

