function [pair,impair] = pairimpair(n)
pair = [];
impair = [];
for i = 1:1:n
    if rem(i^2,2) == 0
        pair = [pair i^2];
    else
        impair = [impair i^2];
    end
end
