function [EulerMatrix] = eulermat(phi, theta, psi)
X = [1; 0; 0];
Y = [0; 1; 0];
Z = [0; 0; 1];

x = phi*adj(X);
x = expm(x);

y = theta*adj(Y);
y = expm(y);

z = psi*adj(Z);
z = expm(z);

EulerMatrix = z*y*x;
end


