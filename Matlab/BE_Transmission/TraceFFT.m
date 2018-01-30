function [] = TraceFFT(fs, L, f)
T = 1 / fs;
t = (0:L-1) * T;
fx = fs * (0:(L/2)) / L;

S = f(t);

FFT = fft(S);
P2 = abs(FFT/L);
P1 = P2(1:(L/2) + 1);
P1(2:end-1) = 2 * P1(2:end - 1);

plot(fx, P1)
end
