% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to extend the boundary of images

function output_img=ext_bound(input_img,height,width,ext_num)

output_img=zeros(height+2*ext_num,width+2*ext_num);
% Copy the center
for m=1+ext_num:1:height+ext_num
    for n=1+ext_num:1:width+ext_num
        output_img(m,n)=input_img(m-ext_num,n-ext_num);
    end
end
        
% Reflect the two vertical parts
index_l=2*ext_num+1;
index_r=2*(width+2*ext_num+1)-index_l;
for m=1+ext_num:1:height+ext_num
    for n=1:1:ext_num
        output_img(m,n)=input_img(m-ext_num,index_l-n-ext_num);
		output_img(m,width+2*ext_num+1-n)=...
          input_img(m-ext_num,index_r-(width+2*ext_num+1-n)-ext_num); 
    end
end

% Reflect the two horizontal parts
index_u=2*ext_num+1;
index_b=2*(height+2*ext_num+1)-index_u;
for m=1:1:ext_num
    for n=1+ext_num:1:ext_num+width
        output_img(m,n)=input_img(index_u-m-ext_num,n-ext_num);
	    output_img(height+2*ext_num+1-m,n)=...
           input_img(index_b-(height+2*ext_num+1-m)-ext_num,n-ext_num);
    end
end
		
% Reflect the four corners
for m=1:1:ext_num
    for n=1:1:ext_num
        output_img(m,n)=output_img(index_u-m,n);
		output_img(m+height+ext_num,n)=output_img(index_b-(m+height+ext_num),n);
		output_img(m,n+width+ext_num)=output_img(m,index_r-(n+width+ext_num));
		output_img(m+height+ext_num,n+width+ext_num)=...
               output_img(index_b-(m+height+ext_num),n+width+ext_num);
    end
end
end
