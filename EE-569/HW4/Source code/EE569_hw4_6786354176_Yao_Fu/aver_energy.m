% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to average energy 

function element=aver_energy(input,height,width)

sum=0;
for m=1:1:height
    for n=1:1:width
        sum=sum+abs(input(m,n));
    end
end
element=sum/(height*width);