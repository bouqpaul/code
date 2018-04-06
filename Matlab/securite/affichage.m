function [] = affichage(Vdd, Vt, N)

X = 0:Vdd/N:Vdd;
Y = ones(size(X));

for i = 1:size(X)
    if X(i) <= Vt
        X(i) = Vdd;
    elseif X(i) >= Vdd - Vt
        X(i) = 0;
    elseif X(i) > Vt & X(i) < Vdd/2
        X(i) = zoneB(X(i));
    elseif X(i) > Vdd/2 & X(i) < Vdd - Vt
        X(i) = zoneD(X(i));
    
    end


end
