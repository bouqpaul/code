function [] = TraceTI(fs, L, f)
T = 1 / fs;

t = (0:L-1) * T;
%fx = fs * (0:(L/2)) / L;

S = f(t);

plot(t, S)
end
