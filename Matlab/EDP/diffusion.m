function [] = diffusion( thetaA, thetaE, L )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here


lst = [];
for i = 1:100
    if mod(i, 2) == 0
        A = 0;
    else
        A = 4 * (thetaA - thetaE) / (i * pi);
    end
   lst = [lst A *- sin(i * pi  * x / L)];
end



