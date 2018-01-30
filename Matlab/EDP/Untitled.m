function [] = diffusion( thetaA, thetaE )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

A = [];
for i = 1:100
    if mod(i, 2) == 0
        A = [A 0];
    else
        temp = 4 * (thetaA - thetaE) / (i * pi)
end
end


