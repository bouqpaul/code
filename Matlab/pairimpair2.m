function [pair, impair] = pairimpair2(n)
temp = 1:1:n;
pair = find(rem(temp,2)==0);
impair = find(rem(temp,2)~=0);

pair = pair.^2;
impair = impair.^2;
