function [res] = kraft(dict)

N = strlength(dict);
k = 0;

for i = 1:length(N)
    k = k + 2^(-N(i));
end

if k <= 1
    res = true;
else
    res = false;
    
end
