% EE569 Homework Assignment #3:Problem1_part(b) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do image stiching

function output_img=stich_demo(img_l,img_m,img_r,height,width,img1,img2,img3)
% Step1: Find 4 matching point pairs
im_l_gray = rgb2gray(uint8(img_l));
im_m_gray = rgb2gray(uint8(img_m));
im_r_gray = rgb2gray(uint8(img_r));
[matchedPoints_l,matchedPoints_m1]=find_points(im_l_gray,im_m_gray,0.4);

x_l1=double(matchedPoints_l.Location(3,1));y_l1=double(matchedPoints_l.Location(3,2));
x_l2=double(matchedPoints_l.Location(5,1));y_l2=double(matchedPoints_l.Location(5,2));
x_l3=double(matchedPoints_l.Location(7,1));y_l3=double(matchedPoints_l.Location(7,2));
x_l4=double(matchedPoints_l.Location(9,1));y_l4=double(matchedPoints_l.Location(9,2));

x_m1_1=double(matchedPoints_m1.Location(3,1));y_m1_1=double(matchedPoints_m1.Location(3,2));
x_m2_1=double(matchedPoints_m1.Location(5,1));y_m2_1=double(matchedPoints_m1.Location(5,2));
x_m3_1=double(matchedPoints_m1.Location(7,1));y_m3_1=double(matchedPoints_m1.Location(7,2));
x_m4_1=double(matchedPoints_m1.Location(9,1));y_m4_1=double(matchedPoints_m1.Location(9,2));

% Step2: Calculate transform matrix T
syms h1_11 h1_12 h1_13 h1_21 h1_22 h1_23 h1_31 h1_32 
eqns=[...
(h1_31*x_l1+h1_32*y_l1+1)*x_m1_1==h1_11*x_l1+h1_12*y_l1+h1_13,...
(h1_31*x_l1+h1_32*y_l1+1)*y_m1_1==h1_21*x_l1+h1_22*y_l1+h1_23,...
     ...
(h1_31*x_l2+h1_32*y_l2+1)*x_m2_1==h1_11*x_l2+h1_12*y_l2+h1_13,...
(h1_31*x_l2+h1_32*y_l2+1)*y_m2_1==h1_21*x_l2+h1_22*y_l2+h1_23,...
     ...
(h1_31*x_l3+h1_32*y_l3+1)*x_m3_1==h1_11*x_l3+h1_12*y_l3+h1_13,...
(h1_31*x_l3+h1_32*y_l3+1)*y_m3_1==h1_21*x_l3+h1_22*y_l3+h1_23,...
     ...
(h1_31*x_l4+h1_32*y_l4+1)*x_m4_1==h1_11*x_l4+h1_12*y_l4+h1_13,...
(h1_31*x_l4+h1_32*y_l4+1)*y_m4_1==h1_21*x_l4+h1_22*y_l4+h1_23];

vars = [h1_11 h1_12 h1_13 h1_21 h1_22 h1_23 h1_31 h1_32];
h = solve(eqns, vars);
h1_11=double(h.h1_11);
h1_12=double(h.h1_12);
h1_13=double(h.h1_13);
h1_21=double(h.h1_21);
h1_22=double(h.h1_22);
h1_23=double(h.h1_23);
h1_31=double(h.h1_31);
h1_32=double(h.h1_32);

im_l_gray_XY=zeros(height,width,2);
im_m_gray_XY=zeros(height,width,2);
for m=1:1:height
    for n=1:1:width
        im_l_gray_XY(m,n,1)=n-0.5;
        im_l_gray_XY(m,n,2)=m-0.5;
        
        im_m_gray_XY(m,n,1)=n-0.5;
        im_m_gray_XY(m,n,2)=m-0.5;
    end
end

im_l_gray_XY_new=zeros(height,width,2);
x1_min=0;
x1_max=0;
y1_min=0;
y1_max=0;
for m=1:1:height
    for n=1:1:width
        lamda=h1_31*im_l_gray_XY(m,n,1)+h1_32*im_l_gray_XY(m,n,2)+1;  
        temp_x=(h1_11*im_l_gray_XY(m,n,1)+...
                                 h1_12*im_l_gray_XY(m,n,2)+h1_13)/lamda;
        im_l_gray_XY_new(m,n,1)=temp_x;
        if temp_x<x1_min
            x1_min=temp_x;
        end
        if temp_x>x1_max
            x1_max=temp_x;
        end
   
        temp_y=(h1_21*im_l_gray_XY(m,n,1)+...
                                 h1_22*im_l_gray_XY(m,n,2)+h1_23)/lamda;
        im_l_gray_XY_new(m,n,2)=temp_y;
        if temp_y<y1_min
            y1_min=temp_y;
        end
        if temp_y>y1_max
            y1_max=temp_y;
        end
    end
end

[matchedPoints_r,matchedPoints_m2]=find_points(im_r_gray,im_m_gray);
x_r1=double(matchedPoints_r.Location(2,1));y_r1=double(matchedPoints_r.Location(2,2));
x_r2=double(matchedPoints_r.Location(4,1));y_r2=double(matchedPoints_r.Location(4,2));
x_r3=double(matchedPoints_r.Location(6,1));y_r3=double(matchedPoints_r.Location(6,2));
x_r4=double(matchedPoints_r.Location(8,1));y_r4=double(matchedPoints_r.Location(8,2));

x_m1_2=double(matchedPoints_m2.Location(2,1));y_m1_2=double(matchedPoints_m2.Location(2,2));
x_m2_2=double(matchedPoints_m2.Location(4,1));y_m2_2=double(matchedPoints_m2.Location(4,2));
x_m3_2=double(matchedPoints_m2.Location(6,1));y_m3_2=double(matchedPoints_m2.Location(6,2));
x_m4_2=double(matchedPoints_m2.Location(8,1));y_m4_2=double(matchedPoints_m2.Location(8,2));

% Step2: Calculate transform matrix T
syms h2_11 h2_12 h2_13 h2_21 h2_22 h2_23 h2_31 h2_32 
eqns=[...
(h2_31*x_r1+h2_32*y_r1+1)*x_m1_2==h2_11*x_r1+h2_12*y_r1+h2_13,...
(h2_31*x_r1+h2_32*y_r1+1)*y_m1_2==h2_21*x_r1+h2_22*y_r1+h2_23,...
     ...
(h2_31*x_r2+h2_32*y_r2+1)*x_m2_2==h2_11*x_r2+h2_12*y_r2+h2_13,...
(h2_31*x_r2+h2_32*y_r2+1)*y_m2_2==h2_21*x_r2+h2_22*y_r2+h2_23,...
     ...
(h2_31*x_r3+h2_32*y_r3+1)*x_m3_2==h2_11*x_r3+h2_12*y_r3+h2_13,...
(h2_31*x_r3+h2_32*y_r3+1)*y_m3_2==h2_21*x_r3+h2_22*y_r3+h2_23,...
     ...
(h2_31*x_r4+h2_32*y_r4+1)*x_m4_2==h2_11*x_r4+h2_12*y_r4+h2_13,...
(h2_31*x_r4+h2_32*y_r4+1)*y_m4_2==h2_21*x_r4+h2_22*y_r4+h2_23];

vars = [h2_11 h2_12 h2_13 h2_21 h2_22 h2_23 h2_31 h2_32];
h = solve(eqns, vars);
h2_11=double(h.h2_11);
h2_12=double(h.h2_12);
h2_13=double(h.h2_13);
h2_21=double(h.h2_21);
h2_22=double(h.h2_22);
h2_23=double(h.h2_23);
h2_31=double(h.h2_31);
h2_32=double(h.h2_32);

im_r_gray_XY=zeros(height,width,2);
im_m2_gray_XY=zeros(height,width,2);
for m=1:1:height
    for n=1:1:width
        im_r_gray_XY(m,n,1)=n-0.5;
        im_r_gray_XY(m,n,2)=m-0.5;
        
        im_m2_gray_XY(m,n,1)=n-0.5;
        im_m2_gray_XY(m,n,2)=m-0.5;
    end
end

im_r_gray_XY_new=zeros(height,width,2);
x2_min=0;
x2_max=0;
y2_min=0;
y2_max=0;
for m=1:1:height
    for n=1:1:width
        lamda=h2_31*im_r_gray_XY(m,n,1)+h2_32*im_r_gray_XY(m,n,2)+1;
        
        temp_x=(h2_11*im_r_gray_XY(m,n,1)+...
                                 h2_12*im_r_gray_XY(m,n,2)+h2_13)/lamda;
        im_r_gray_XY_new(m,n,1)=temp_x;
        if temp_x<x2_min
            x2_min=temp_x;
        end
        if temp_x>x2_max
            x2_max=temp_x;
        end
    
        temp_y=(h2_21*im_r_gray_XY(m,n,1)+...
                                 h2_22*im_r_gray_XY(m,n,2)+h2_23)/lamda;
        im_r_gray_XY_new(m,n,2)=temp_y;
        if temp_y<y2_min
            y2_min=temp_y;
        end
        if temp_y>y2_max
            y2_max=temp_y;
        end
    end
end

x1_min=floor(x1_min)-1;x1_max=ceil(x1_max)+1;
y1_min=floor(y1_min)-1;y1_max=ceil(y1_max)+1;
x2_min=floor(x2_min)-1;x2_max=ceil(x2_max)+1;
y2_min=floor(y2_min)-1;y2_max=ceil(y2_max)+1;

im_l_gray_new=zeros(y1_max-y1_min,x1_max-x1_min);
im_r_gray_new=zeros(y2_max-y2_min,x2_max-x2_min);
for m=1:1:height
    for n=1:1:width
        m1_new=floor(im_l_gray_XY_new(m,n,2)+0.5)-y1_min+1;
        n1_new=floor(im_l_gray_XY_new(m,n,1)+0.5)-x1_min+1;
        im_l_gray_new(m1_new,n1_new)=img1(m,n); 

        m2_new=floor(im_r_gray_XY_new(m,n,2)+0.5)-y2_min+1;
        n2_new=floor(im_r_gray_XY_new(m,n,1)+0.5)-x2_min+1;
        im_r_gray_new(m2_new,n2_new)=img3(m,n); 
    end
end

y_max=max(y1_max,y2_max);y_min=min(y1_min,y2_min);
increment=785;
output_img=zeros(y_max-y_min,(x1_max-x1_min)+(x2_max-x2_min)-increment+479);

for m=1:1:y1_max-y1_min
    for n=1:1:x1_max-x1_min
        output_img(m+73,n)=im_l_gray_new(m,n);
    end
end

for m=1:1:y2_max-y2_min
    for n=1:1:x2_max-x2_min
        output_img(m,n+width+x1_max-x1_min+x2_min-increment)=im_r_gray_new(m,n);
    end
end

k=5;j=3;
for m=1:1:height
    for n=1:1:width
        if output_img(m-y2_min+j,n+width+x1_max-x1_min-k-increment) ~= 0
            if abs(output_img(m-y2_min+j,n+width+x1_max-x1_min-k-increment)-img2(m,n))>30             
                output_img(m-y2_min+j,n+width+x1_max-x1_min-k-increment)=img2(m,n);
            else
                sum=(output_img(m-y2_min+j,n+width+x1_max-x1_min-k-increment)+img2(m,n))/2;
                output_img(m-y2_min+j,n+width+x1_max-x1_min-k-increment)=floor(sum);
            end
        else
            output_img(m-y2_min+j,n+width+x1_max-x1_min-k-increment)=img2(m,n);
        end

    end
end

for i=1:1:5
    output_img=interpolate_demo(output_img,y_max-y_min,(x1_max-x1_min)+(x2_max-x2_min)-increment+479,1);
end
 
kernel=[1,1,1;
        1,1,1;
        1,1,1]/9;
output_img= imfilter(output_img, kernel);

