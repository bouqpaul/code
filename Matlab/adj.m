function [ADJ] = adj(vector)
X = vector(1);
Y = vector(2);
Z = vector(3);
ADJ = zeros(3);
ADJ(1,2) = -Z;
ADJ(1,3) = Y;
ADJ(2,3) = -X;
ADJ = ADJ - ADJ';
end
