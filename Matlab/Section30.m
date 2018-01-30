% close all
% x = -1: 0.02:4;
% y1 = x;
% y2 = sqrt (1 + x);
% 
% phi = 1,618033988749895;
% figure;
% hold on;
% plot ( x, y1, '-b');
% plot ( x, y2, '-g');
% plot ( phi, phi, 'or');
% % axis([0 3 0 3])
% xlabel('x') ; ylabel('Courbe y1 ety2') ;
% title('le nombre dor') ;
% 
% 
% x = 3;
% for i = 1:1:31
%     x = sqrt(1+x);
% end
% x;
% 
% y = 3;
% while y ~= sqrt(1+y)
%     y = sqrt(1+y);
% end
% y
[a,b] = pairimpair(20);
a
% b

% tic
% x = 3
% toc
% 
% tic
% x = 3;
% toc
courbe(linspace(0,2*pi,100),'cos')
