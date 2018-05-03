function [encod, rend, huffDict] = huffEnco(msg, dict, P)
[huffDict, average] = huffmandict(dict, P);
encod = huffmanenco(msg, huffDict);
%huffDict(:, 2) = cellfun(@num2str, huffDict(:, 2), 'UniformOutput', false);
H = entropy(P);
rend = H / average;
end