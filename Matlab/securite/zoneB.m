function [resultat] = zoneB(x, Vt, Vdd)

L = (x - Vdd + Vt);
K = (x - Vt)^2;

resultat = max(roots([1, 2*L + 2*Vdd, K + 2*L*Vdd + Vdd^2]);)

end