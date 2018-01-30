close all
% Maison
% X = [ -6 -6 -7 0 7 6 6 -3 -3 0 0 -6;
%     -7 2 1 8 1 2 -7 -7 -2 -2 -7 -7] ;

%% Motif d'une main
X = [3.15  -9.00
     4.43  -6.55
     6.13  -4.39
     7.65  -2.21
     7.52  -1.26
     6.75  -0.95
     5.60  -1.56
     4.45  -2.85
     3.07  -3.00
     2.60  -1.70
     2.73   0.59
     3.22   3.66
     3.39   6.79
     2.84   7.92
     2.10   7.41
     1.48   4.25
     0.68   0.79
     0.81   4.96
     0.66   8.36
    -0.33   9.06
    -0.99   8.09
    -1.04   4.68
    -1.17   0.90
    -1.81   4.15
    -2.63   7.45
    -3.39   7.80
    -3.86   6.97
    -3.49   3.35
    -3.13  -0.44
    -4.78   1.87
    -6.00   3.81
    -6.95   3.92
    -7.12   3.04
    -5.82  -0.07
    -4.76  -2.29
    -4.52  -5.62
    -4.00  -9.00]';


% Création des matrices de transformation
A1 = [1/2 0; 0 1];
A2 = [1 0; 0 1/2];
A3 = [0 1; 1/2 0];
A4 = [1/2 0; 0 -1];

R = rand(2,2)-rand(2,2);
teta = 30;
G = [cosd(teta) -sind(teta); sind(teta) cosd(teta)];

% Application de la transformation A1 sur le motif X
Y1 = A1*X;
Y2 = A2*X;
Y3 = A3*X;
Y4 = A4*X;

Y5 = R*X;

Y6 = G*X;

% Affichage du nouveau motif Y1
figure ;
hold on ;
plot( Y6(1,: ), Y6(2,: ), '-g.' ) ;
grid on; axis square; xlabel(' A1') ;
axis([-10 10 -10 10]) ;

plot(X(1,:),X(2,:),'-r.');
grid on;
axis square;
xlabel(' Motif de base ');
axis([-10 10 -10 10]);

