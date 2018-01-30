close all
phi = linspace(0,2*pi,50);
teta = linspace(0,pi,25);
[PHI, TETA] = meshgrid(phi,teta);

X = sin(TETA).*cos(PHI)
Y = sin(TETA).*sin(PHI)
Z = cos(TETA)

figure
subplot(1,2,1)
mesh(X,Y,Z)
title('MESH')

subplot(1,2,2)
surfl(X,Y,Z)
shading interp
title('SURFL')
% x = linspace(-1,1,20);
% y = linspace(-2,2,40);
% [X,Y] = meshgrid(x,y);
% z = cos(pi*sqrt(X.^2+Y.^2));

% figure
% subplot(2,2,1)
% mesh(X,Y,z)
% title('Mesh')
% 
% subplot(2,2,2)
% meshc(X,Y,z)
% % colorbar()
% colormap(hot)
% title('Meshz')
% 
% subplot(2,2,3)
% surf(X,Y,z)
% title('Surf')
% 
% subplot(2,2,4)
% contour3(X,Y,z)
% title('Contour')
