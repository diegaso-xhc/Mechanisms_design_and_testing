function Grafica(elementNodes,numberElements,xx,yy,zz,displacements,nodeCoordinates,stress)
rval = abs(stress/max(abs(stress)));
bval = 0.2;
gval = 1-rval;
for e=1:numberElements
   indice=[elementNodes(e,1) elementNodes(e,2)];
   X=[xx(indice(1)) xx(indice(2))];
   Y=[yy(indice(1)) yy(indice(2))];
   Z=[zz(indice(1)) zz(indice(2))];
   axis([min(xx) max(xx) min(yy) max(yy) min(zz) max(zz)])
   title('Structure and affected links','FontSize', 20);
   plot3(X,Y,Z,'Color', [rval(e),bval,gval(e)], 'LineWidth', 10)
   grid on
   hold on
end
hold off
figure
for e=1:max(max(size(nodeCoordinates)))
   nodeCoordinates1(e,1)=nodeCoordinates(e,1)+80*displacements(3*e-2);
   nodeCoordinates1(e,2)=nodeCoordinates(e,2)+80*displacements(3*e-1);
   nodeCoordinates1(e,3)=nodeCoordinates(e,3)+80*displacements(3*e);
end
xxdef=nodeCoordinates1(:,1);
yydef=nodeCoordinates1(:,2);
zzdef=nodeCoordinates1(:,3);


for e=1:numberElements
   indice2=[elementNodes(e,1) elementNodes(e,2)];
   X1=[xxdef(indice2(1)) xxdef(indice2(2))];
   Y1=[yydef(indice2(1)) yydef(indice2(2))];
   Z1=[zzdef(indice2(1)) zzdef(indice2(2))];
   axis([min(xxdef) max(xxdef) min(yydef) max(yydef) min(zzdef) max(zzdef)])
   title('Deformed Structure', 'FontSize', 20);
   plot3(X1,Y1,Z1,'color',[0.7,0.5,0.2], 'LineWidth', 10)
   grid on
   hold on
end


   