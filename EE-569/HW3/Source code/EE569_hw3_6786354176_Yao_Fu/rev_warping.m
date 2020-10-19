% EE569 Homework Assignment #3:Problem1_part(a) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the reverse spatial warping

function output_img=rev_warping(input_img,height,width,occurence)

% Transform the imput image 512 by 512 into 513 by 513
ext_input_img=zeros(height+1,width+1);
for m=1:1:height
    for n=1:1:width
        ext_input_img(m,n)=input_img(m,n);
    end
end

% Get the location of the center pixel of the imput image
m_center=height/2+1;      % The value of the row of the center 
n_center=width/2+1;       % The value of the column of the center

% Do the inverse geometric warping in the polar coordinate system
% Split the system into four parts:A,B,C,and D like [A,B;C,D]
img_A=zeros(m_center,n_center);img_B=zeros(m_center,n_center);
img_C=zeros(m_center,n_center);img_D=zeros(m_center,n_center);
for m=1:1:height+1
    for n=1:1:width+1
        if m<=m_center && n<=n_center
            img_A(m,n)=ext_input_img(m,n);
        end
        if m<=m_center && n>=n_center
            img_B(m,n-n_center+1)=ext_input_img(m,n);
        end 
        if m>=m_center && n<=n_center
            img_C(m-m_center+1,n)=ext_input_img(m,n);
        end 
        if m>=m_center && n>=n_center
            img_D(m-m_center+1,n-n_center+1)=ext_input_img(m,n);
        end 
    end
end

% Count the number pixels whose distance < max_radius in every row for four parts 
max_radius=m_center-1;

row_pixel_num_A=zeros(1,m_center);   % Count the number pixels whose distance < max_radius 
                                    % in every row for the part 'A'
row_pixel_num_B=zeros(1,m_center);   % Count the number pixels whose distance < max_radius 
                                    % in every row for the part 'B'
row_pixel_num_C=zeros(1,m_center);   % Count the number pixels whose distance < max_radius 
                                    % in every row for the part 'C'
row_pixel_num_D=zeros(1,m_center);   % Count the number pixels whose distance < max_radius 
                                    % in every row for the part 'D'                                                            
for m=1:1:m_center
    for n=1:1:n_center
       distance_A=sqrt((m-m_center)^2+(n-n_center)^2);
       if distance_A<=max_radius
            row_pixel_num_A(m)=row_pixel_num_A(m)+1;
       end
       
       distance_B=sqrt((m-m_center)^2+(n-0)^2);
       if distance_B<=max_radius
            row_pixel_num_B(m)=row_pixel_num_B(m)+1;
       end
       
       distance_C=sqrt((m-0)^2+(n-n_center)^2);
       if distance_C<=max_radius
            row_pixel_num_C(m)=row_pixel_num_C(m)+1;
       end
       
       distance_D=sqrt((m-0)^2+(n-0)^2);
       if distance_D<=max_radius
            row_pixel_num_D(m)=row_pixel_num_D(m)+1;
       end
       
    end
end

% Do the reverse spatial wrapping
img_A_new=zeros(m_center,n_center);img_B_new=zeros(m_center,n_center);
img_C_new=zeros(m_center,n_center);img_D_new=zeros(m_center,n_center);

for m=1:1:m_center
    for n=1:1:n_center
        if n>m_center-row_pixel_num_A(m)
            n_A=floor(m_center-(m_center-n)/row_pixel_num_A(m)*m_center)+1;
            img_A_new(m,n_A)=img_A(m,n);
        else
            n_A=floor(m_center-(m_center-n)/m_center*row_pixel_num_A(m))+1;
            img_A_new(m,n)=img_A(m,n_A);
        end
        
        if n<row_pixel_num_B(m)
            n_B=floor(n/row_pixel_num_B(m)*m_center);
            img_B_new(m,n_B)=img_B(m,n);
        else
            n_B=floor(n/m_center*row_pixel_num_B(m))+1;
            img_B_new(m,n)=img_B(m,n_B);
        end
        
        if n>m_center-row_pixel_num_C(m)
            n_C=floor(m_center-(m_center-n)/row_pixel_num_C(m)*m_center)+1;
            img_C_new(m,n_C)=img_C(m,n);
        else
            n_C=floor(m_center-(m_center-n)/m_center*row_pixel_num_C(m));
            img_C_new(m,n)=img_C(m,n_C);
        end
        
        if n<row_pixel_num_D(m)
            n_D=floor(n/row_pixel_num_D(m)*m_center);
            img_D_new(m,n_D)=img_D(m,n);
        else
            n_D=floor(n/m_center*row_pixel_num_D(m))+1;
            img_D_new(m,n)=img_D(m,n_D);
        end
        
    end
end
        

% Converge four parts:A,B,C,and D into one image        
ext_output_img=zeros(height+1,width+1);       
for m=1:1:height+1
    for n=1:1:width+1
        if m<=m_center && n<=n_center
            ext_output_img(m,n)=img_A_new(m,n);
        end
        
        if m<=m_center && n>=n_center
            ext_output_img(m,n)=img_B_new(m,n-n_center+1);
        end 
        
        if m>=m_center && n<=n_center
            ext_output_img(m,n)=img_C_new(m-m_center+1,n);
        end 
        
        if m>=m_center && n>=n_center
            ext_output_img(m,n)=img_D_new(m-m_center+1,n-n_center+1);
        end 
        
    end
end        

% Transform the image into the original size
output_img=zeros(height,width);
for m=1:1:height
    for n=1:1:width
        output_img(m,n)=ext_output_img(m,n);
    end
end  
for i=1:1:occurence
    output_img=interpolate_demo(output_img,512,512,1); 
end
