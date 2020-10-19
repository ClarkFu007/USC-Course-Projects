% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to average energy for feature segmenation

function element=aver_energy_new(input,height,width,w_size)

ext_num=(w_size-1)/2;
element=zeros(height,width);
ext_input=ext_bound(input,height,width,ext_num);
sum=0;
for m=1+ext_num:1:height+ext_num
    for n=1+ext_num:1:width+ext_num
        for i=-ext_num:1:ext_num
            for j=-ext_num:1:ext_num
                sum=abs(ext_input(m+i,n+j))+sum;
            end
        end
        element(m-ext_num,n-ext_num)=sum; 
        sum=0;
    end
end
element=element(:)';