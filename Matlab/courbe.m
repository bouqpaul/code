function [] = courbe(X, chaine)
chaine = lower(chaine);
switch chaine
    case sin
        Y = sin(X);
    case sinc
        Y = sinc(X);
    case cos
        Y = cos(X);
    otherwise
        Y = X;
        disp('Erreur');
end
close all;
figure;
plot(X,Y);
xlabel('X');
ylabel('Y');
title(chaine);