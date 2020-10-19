% EE569 Homework Assignment #3:Problem2_part(a) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to get numbers of bounds at each pixel

function output_matrix=bound_matrix(input_img,height,width)

% Extend the boundaries of images by padding zeros
ext_num=1;
ext_input_img=zeros(height+ext_num*2,width+ext_num*2);
for m=1:1:height
    for n=1:1:width
        ext_input_img(m+ext_num,n+ext_num)=input_img(m,n);
    end
end

% Get the bound matrix
output_matrix=zeros(height,width);

for m=1+ext_num:1:height+ext_num
    for n=1+ext_num:1:width+ext_num
        if ext_input_img(m,n)==1
            num=0;
            if ext_input_img(m-1,n-1)==1
                num=num+1;
            end
            if ext_input_img(m+1,n-1)==1
                num=num+1;
            end
            if ext_input_img(m-1,n+1)==1
                num=num+1;
            end
            if ext_input_img(m+1,n+1)==1
                num=num+1;
            end
        
            if ext_input_img(m-1,n)==1
                num=num+2;
            end
            if ext_input_img(m+1,n)==1
                num=num+2;
            end
            if ext_input_img(m,n+1)==1
                num=num+2;
            end
            if ext_input_img(m,n-1)==1
                num=num+2; 
            end 
            output_matrix(m-ext_num,n-ext_num)=num;
            
        end
    end
end