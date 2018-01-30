close all
x = 0:0.1:5;
y = exp(-x).*sin(x.^2);
figure
% 
% subplot(2,2,1)
% plot(x,y)
% 
% subplot(2,2,2)
% semilogx(x,abs(x))
% 
% subplot(2,2,3)
% semilogy(x,abs(x))
% 
% subplot(2,2,4)
% loglog(x,y)
hold on
grid on
plot(x,y,'r-')
plot(x,-y,'b:')
axis([0 2 -1 1])