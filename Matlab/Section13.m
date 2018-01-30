R = rand(3,3);
H = randn(3,3)

Trace = trace(H);
Diag = diag(H);
Sd = sum(Diag);

diag(diag(H));
det(H);
rank(H);

K = magic(4)
Sc = sum(K);
Sl = sum(K(1,:));

L = flipud(K);
R = fliplr(K);

a = triu(K);
b = tril(K);

