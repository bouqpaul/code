function [aff] = affichageDict(dict)
aff = dict;
aff(:, 2) = cellfun(@num2str, aff(:, 2), 'UniformOutput', false);
end