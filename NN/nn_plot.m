% Richard Levenson, Hunter Dubel, Daniel Sarnelli, Jeremy Leon
% HackTCNJ 2017
% February 26, 2017
%
% Hack Harassment Convergence Plot
%

clear
close all
E = csvread('dump.txt');
numIterations = 20000;
sum = 0;
scale = 50;
E_ = zeros(numIterations, 1);
E_(1:49) = E(1:49);
for i = 50:numIterations
    total = 0;
    for i2 = i - 49:i
        total = total + E(i2);
    end
    average = total / 50;
    E_(i) = average;
end
plot(1:numIterations, E_);
title('Harassment Monitor Neural Network Convergence'); xlabel('Number of Iterations'); ylabel('Average Error');