function [entropy] = entropy(P)
N = length(P);

res = 0;
for i = 1:N
    if P(i) ~= 0
        res = res + P(i) * log(P(i));
    end

end

entropy = - res;
end