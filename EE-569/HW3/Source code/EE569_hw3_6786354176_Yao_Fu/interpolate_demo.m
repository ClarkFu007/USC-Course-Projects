function output_img=interpolate_demo(input_img,height,width,index)

% Extend the boundary of the image
ext_num=5;
ext_input_img=zeros(height+2*ext_num,width+2*ext_num);
temp_output_img=zeros(height+2*ext_num,width+2*ext_num);
for m=1:1:height
    for n=1:1:width
        ext_input_img(m+ext_num,n+ext_num)=input_img(m,n);
    end
end

% Do the interpolation
% If a pixel is a blck dot,then we make it have the average value of 24 neighborhood values
for m=1:1:height
    for n=1:1:width
        flag=0;
        if ext_input_img(m+ext_num,n+ext_num)==0
            for i=-index:1:index
                for j=-index:1:index
                    if ext_input_img(m+ext_num+i,n+ext_num+j)~=0
                        temp_output_img(m+ext_num,n+ext_num)=...
                            ext_input_img(m+ext_num+i,n+ext_num+j);
                        flag=1;
                        break
                    end
                 if flag==1
                     break
                 end  
                end
            end
        else
            temp_output_img(m+ext_num,n+ext_num)=...
                            ext_input_img(m+ext_num,n+ext_num);
        end
    end
end

% Transform the image into the original size
output_img=zeros(height,width);
for m=1:1:height
    for n=1:1:width
        output_img(m,n)=temp_output_img(m+ext_num,n+ext_num);
    end
end