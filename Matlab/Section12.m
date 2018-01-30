A = [1 2 3; 4 5 6; 7 8 0]
A(1,:);
A(:,2);

A/A;

S = sum(A(:));
MM = max(A(:));

L = 20*log10(A);

x = [-1; 0; 2];
y = inv(A)*x;

err = A*y-x;

ecart = std(x);
ecart2 = std(A);
ecart3 = std(A(:));

C = [1 -1 2; -2 -4 1; 8 1 -1];
A;
P = (C<0);
H = (A<5);
M = (A~=0)
temp = find(A)
MM = zeros(3,3)
MM(temp)
MM


