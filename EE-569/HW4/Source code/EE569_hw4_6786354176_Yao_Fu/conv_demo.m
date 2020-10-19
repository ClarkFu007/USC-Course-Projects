% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the convolution

function output_img=conv_demo(input_img,height,width,ext_num,kernel,size)

ext_input_img=ext_bound(input_img,height,width,ext_num);
index_i=(size-1)/2;
index_j=(size-1)/2;
temp_value=0;
output_img=zeros(height,width);
for m=1+ext_num:1:height+ext_num
    for n=1+ext_num:1:width+ext_num
        for i=-index_i:1:index_i
            for j=-index_j:1:index_j
               temp_value=temp_value+ext_input_img(m+i,n+j)*...
                      kernel(i+index_i+1,j+index_j+1);
            end
        end
        output_img(m,n)=temp_value;
        temp_value=0;
    end
end
end
