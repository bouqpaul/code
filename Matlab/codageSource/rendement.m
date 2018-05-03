function [rend] = rendement(N, P)


H = entropy(P);
R = moyBitSymb(N, P);

rend = H / R;

end