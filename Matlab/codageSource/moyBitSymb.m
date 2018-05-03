function [moy] = moyBitSymb(N, P)

moy = 0;

for i = 1:length(P)
    
moy = moy + P(i) * N(i);    
end



end