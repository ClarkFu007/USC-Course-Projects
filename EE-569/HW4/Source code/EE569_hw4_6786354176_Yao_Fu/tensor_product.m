% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the tensor product

function output_kernel=tensor_product(kernel1,kernel2,size)

output_kernel=zeros(size,size);

for m=1:1:size
    for n=1:1:size
       output_kernel(m,n)=kernel1(m)*kernel2(n);
    end
end
end