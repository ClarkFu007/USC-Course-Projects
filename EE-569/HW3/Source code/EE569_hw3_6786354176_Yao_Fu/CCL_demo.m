% EE569 Homework Assignment #3:Problem2_part(b) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the connected component labeling

function output_img=CCL_demo(input_img,height,width,occurrence)

% Extend the boundaries of images by padding zeros
ext_num=1;
ext_temp_img=zeros(height+ext_num*2,width+ext_num*2);
for m=1:1:height
    for n=1:1:width
        ext_temp_img(m+ext_num,n+ext_num)=input_img(m,n);
    end
end

output_img=zeros(height,width);
% The first pass
flag=2;
for m=1+ext_num:1:height+ext_num
    for n=1+ext_num:1:width+ext_num
        if ext_temp_img(m,n)==1
            temp21=ext_temp_img(m,n-1);
            temp11=ext_temp_img(m-1,n-1);
            temp12=ext_temp_img(m-1,n);
            temp13=ext_temp_img(m-1,n+1);
            if (temp21||temp11||temp12||temp13)==0
               ext_temp_img(m,n)=flag;
               flag=flag+1;
            else
                temp=[temp21,temp11,temp12,temp13];
                temp=sort(temp);
                for i=1:1:4
                    if temp(i)~=0
                        temp_value=temp(i);
                        ext_temp_img(m,n)=temp_value;
                        break
                    end
                end
            end
        end
    end
end

% The second pass
for occur=1:1:occurrence
    for m=1+ext_num:1:height+ext_num
        for n=1+ext_num:1:width+ext_num
            if ext_temp_img(m,n)~=0 
                temp11=ext_temp_img(m-1,n-1);temp12=ext_temp_img(m-1,n);temp13=ext_temp_img(m-1,n+1);
                temp21=ext_temp_img(m,n-1);temp22=ext_temp_img(m,n);temp23=ext_temp_img(m,n+1);
                temp31=ext_temp_img(m+1,n-1);temp32=ext_temp_img(m+1,n);temp33=ext_temp_img(m+1,n+1);
                temp=[temp11,temp12,temp13,temp21,temp22,temp23,temp31,temp32,temp33];
                temp=sort(temp);
                for i=1:1:9
                    if temp(i)~=0
                        temp_value=temp(i);
                        for k=-1:1:1
                            for j=-1:1:1
                                if ext_temp_img(m+k,n+j)~=0
                                    ext_temp_img(m+k,n+j)=temp_value;
                                end
                            end
                        end
                        break 
                    end
                end  
            end
        end
    end
end

for m=1:1:height
    for n=1:1:width
        output_img(m,n)=ext_temp_img(m+ext_num,n+ext_num);
    end
end



