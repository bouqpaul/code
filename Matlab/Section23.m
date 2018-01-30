close all
x = linspace(-1,1,50);
y = linspace(-1,1,50);

[X,Y] = meshgrid(x,y);

Z = cos(pi*X).*cos(pi*Y);
figure
subplot(1,2,1)
contour3(Z, [-0.5 0 0.5])

subplot(1,2,2)
mesh(X,Y,Z)
% ginput()
% gtext('Du texte')