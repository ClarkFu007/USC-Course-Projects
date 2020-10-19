% EE569 Homework Assignment # 3 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: Show the original and resulting images

%% Problem 1: Geometric Image Modification

%% Part(a):Geometric warping
%% Display the original images
Y=512;X=512;p=Y*X;
fid=fopen('hedwig.raw','r');
img1_temp=fread(fid,inf);
fclose(fid);
img1=zeros(Y,X,3);
img1_r=zeros(X,Y);img1_g=zeros(X,Y);img1_b=zeros(X,Y);
img1_r(1:p)=img1_temp(1:3:3*p);
img1_g(1:p)=img1_temp(2:3:3*p);
img1_b(1:p)=img1_temp(3:3:3*p);
img1_r=img1_r';img1_g=img1_g';img1_b=img1_b';
img1(:,:,1)=img1_r;
img1(:,:,2)=img1_g;
img1(:,:,3)=img1_b;
figure(1)
imshow(uint8(img1))
imwrite(uint8(img1),'hedwig.png');

fid=fopen('raccoon.raw','r');
img2_temp=fread(fid,inf);
fclose(fid);
img2=zeros(Y,X,3);
img2_r=zeros(X,Y);img2_g=zeros(X,Y);img2_b=zeros(X,Y);
img2_r(1:p)=img2_temp(1:3:3*p);
img2_g(1:p)=img2_temp(2:3:3*p);
img2_b(1:p)=img2_temp(3:3:3*p);
img2_r=img2_r';img2_g=img2_g';img2_b=img2_b';
img2(:,:,1)=img2_r;
img2(:,:,2)=img2_g;
img2(:,:,3)=img2_b;
figure(2)
imshow(uint8(img2))
imwrite(uint8(img2),'raccoon.png');

fid=fopen('bb8.raw','r');
imgPCB_temp=fread(fid,inf);
fclose(fid);
imgPCB=zeros(Y,X,3);
imgPCB_r=zeros(X,Y);imgPCB_g=zeros(X,Y);imgPCB_b=zeros(X,Y);
imgPCB_r(1:p)=imgPCB_temp(1:3:3*p);
imgPCB_g(1:p)=imgPCB_temp(2:3:3*p);
imgPCB_b(1:p)=imgPCB_temp(3:3:3*p);
imgPCB_r=imgPCB_r';imgPCB_g=imgPCB_g';imgPCB_b=imgPCB_b';
imgPCB(:,:,1)=imgPCB_r;
imgPCB(:,:,2)=imgPCB_g;
imgPCB(:,:,3)=imgPCB_b;
figure(3)
imshow(uint8(imgPCB))
imwrite(uint8(imgPCB),'bb8.png');

%% Do the geometric warping
out_img1_r=geo_warping(img1_r,512,512);
out_img1_g=geo_warping(img1_g,512,512);
out_img1_b=geo_warping(img1_b,512,512);
out_img1=zeros(Y,X,3);
out_img1(:,:,1)=out_img1_r;
out_img1(:,:,2)=out_img1_g;
out_img1(:,:,3)=out_img1_b;
figure(1)
imshow(uint8(out_img1))
imwrite(uint8(out_img1),'warp_hedwig.png');

out_img2_r=geo_warping(img2_r,512,512);
out_img2_g=geo_warping(img2_g,512,512);
out_img2_b=geo_warping(img2_b,512,512);
out_img2=zeros(Y,X,3);
out_img2(:,:,1)=out_img2_r;
out_img2(:,:,2)=out_img2_g;
out_img2(:,:,3)=out_img2_b;
figure(2)
imshow(uint8(out_img2))
imwrite(uint8(out_img2),'warp_raccoon.png');

out_img3_r=geo_warping(imgPCB_r,512,512);
out_img3_g=geo_warping(imgPCB_g,512,512);
out_img3_b=geo_warping(imgPCB_b,512,512);
out_img3=zeros(Y,X,3);
out_img3(:,:,1)=out_img3_r;
out_img3(:,:,2)=out_img3_g;
out_img3(:,:,3)=out_img3_b;
figure(3)
imshow(uint8(out_img3))
imwrite(uint8(out_img3),'warp_bb8.png');

% Do the reverse spatial warping
rev_out_img1_r=rev_warping(out_img1_r,512,512,5);
rev_out_img1_g=rev_warping(out_img1_g,512,512,5);
rev_out_img1_b=rev_warping(out_img1_b,512,512,5);
rev_out_img1=zeros(Y,X,3);
rev_out_img1(:,:,1)=rev_out_img1_r;
rev_out_img1(:,:,2)=rev_out_img1_g;
rev_out_img1(:,:,3)=rev_out_img1_b;
figure(4)
imshow(uint8(rev_out_img1))
imwrite(uint8(rev_out_img1),'rev_warp_hedwig.png');

rev_out_img2_r=rev_warping(out_img2_r,512,512,4);
rev_out_img2_g=rev_warping(out_img2_g,512,512,4);
rev_out_img2_b=rev_warping(out_img2_b,512,512,4);
rev_out_img2=zeros(Y,X,3);
rev_out_img2(:,:,1)=rev_out_img2_r;
rev_out_img2(:,:,2)=rev_out_img2_g;
rev_out_img2(:,:,3)=rev_out_img2_b;
figure(5)
imshow(uint8(rev_out_img2))
imwrite(uint8(rev_out_img2),'rev_warp_raccoon.png');

rev_out_img3_r=rev_warping(out_img3_r,512,512,5);
rev_out_img3_g=rev_warping(out_img3_g,512,512,5);
rev_out_img3_b=rev_warping(out_img3_b,512,512,5);
rev_out_img3=zeros(Y,X,3);
rev_out_img3(:,:,1)=rev_out_img3_r;
rev_out_img3(:,:,2)=rev_out_img3_g;
rev_out_img3(:,:,3)=rev_out_img3_b;
figure(6)
imshow(uint8(rev_out_img3))
imwrite(uint8(rev_out_img3),'rev_warp_bb8.png');

%% Part(b):Homographic Transformation and Image Stiching
%% Display the original images
Y=720;X=480;p=Y*X;
fid=fopen('left.raw','r');
img1_temp=fread(fid,inf);
fclose(fid);
img1=zeros(Y,X,3);
img1_r=zeros(X,Y);img1_g=zeros(X,Y);img1_b=zeros(X,Y);
img1_r(1:p)=img1_temp(1:3:3*p);
img1_g(1:p)=img1_temp(2:3:3*p);
img1_b(1:p)=img1_temp(3:3:3*p);
img1_r=img1_r';img1_g=img1_g';img1_b=img1_b';
img1(:,:,1)=img1_r;
img1(:,:,2)=img1_g;
img1(:,:,3)=img1_b;
figure(1)
imshow(uint8(img1))
imwrite(uint8(img1),'left.png');

fid=fopen('middle.raw','r');
img2_temp=fread(fid,inf);
fclose(fid);
img2=zeros(Y,X,3);
img2_r=zeros(X,Y);img2_g=zeros(X,Y);img2_b=zeros(X,Y);
img2_r(1:p)=img2_temp(1:3:3*p);
img2_g(1:p)=img2_temp(2:3:3*p);
img2_b(1:p)=img2_temp(3:3:3*p);
img2_r=img2_r';img2_g=img2_g';img2_b=img2_b';
img2(:,:,1)=img2_r;
img2(:,:,2)=img2_g;
img2(:,:,3)=img2_b;
figure(2)
imshow(uint8(img2))
imwrite(uint8(img2),'middle.png');

fid=fopen('right.raw','r');
img3_temp=fread(fid,inf);
fclose(fid);
img3=zeros(Y,X,3);
img3_r=zeros(X,Y);img3_g=zeros(X,Y);img3_b=zeros(X,Y);
img3_r(1:p)=img3_temp(1:3:3*p);
img3_g(1:p)=img3_temp(2:3:3*p);
img3_b(1:p)=img3_temp(3:3:3*p);
img3_r=img3_r';img3_g=img3_g';img3_b=img3_b';
img3(:,:,1)=img3_r;
img3(:,:,2)=img3_g;
img3(:,:,3)=img3_b;
figure(3)
imshow(uint8(img3))
imwrite(uint8(img3),'right.png');

%% Do the image stitching
output_r=stich_demo(img1,img2,imgPCB,720,480,img1_r,img2_r,imgPCB_r);
output_g=stich_demo(img1,img2,imgPCB,720,480,img1_g,img2_g,imgPCB_g);
output_b=stich_demo(img1,img2,imgPCB,720,480,img1_b,img2_b,imgPCB_b);

output_rgb(:,:,1)=output_r;
output_rgb(:,:,2)=output_g;
output_rgb(:,:,3)=output_b;
figure(1)
imshow(uint8(output_rgb))
imwrite(uint8(output_rgb),'stiched_RGB.png');
% Find match points
img1_g = rgb2gray(uint8(img1));
img2_g = rgb2gray(uint8(img2));
img3_g = rgb2gray(uint8(img3));
[matchedPoints1,matchedPoints2_1]=find_points(img1_g,img2_g);
[matchedPoints3,matchedPoints2_2]=find_points(img3_g,img2_g);
%% Problem 2:Morphological processing

%% Part(a):Basic morphological process implementation
%% Display the original images
fid=fopen('fan.raw','r');
img_fan=fread(fid,[558,558]);
fclose(fid);
img_fan=img_fan';
figure(1)
imshow(uint8(img_fan))
imwrite(uint8(img_fan),'fan.png')

fid=fopen('cup.raw','r');
img_cup=fread(fid,[315,356]);
fclose(fid);
img_cup=img_cup';
figure(2)
imshow(uint8(img_cup))
imwrite(uint8(img_cup),'cup.png')

fid=fopen('maze.raw','r');
img_maze=fread(fid,[558,558]);
fclose(fid);
img_maze=img_maze';
figure(3)
imshow(uint8(img_maze))
imwrite(uint8(img_maze),'maze.png')

binary_fan=img_fan;
binary_cup=img_cup;
binary_maze=img_maze;

%% Do the shrinking
shrink_fan=zeros(558,558);
for m=1:1:558
    for n=1:1:558
        if img_fan(m,n)>=50
            shrink_fan(m,n)=1;
        end
    end
end
shrink_cup=zeros(356,315);
for m=1:1:356
    for n=1:1:315
        if img_cup(m,n)>=50
            shrink_cup(m,n)=1;
        end
    end
end
shrink_maze=zeros(558,558);
for m=1:1:558
    for n=1:1:558
        if img_maze(m,n)>=40
            shrink_maze(m,n)=1;
        end
    end
end

for i=1:1:250  % The number of iterations 
    shrink_fan=shrink_demo(shrink_fan,558,558);
    
end

for i=1:1:150  % The number of iterations 
    shrink_cup=shrink_demo(shrink_cup,356,315);
end

for i=1:1:950  % The number of iterations 
    shrink_maze=shrink_demo(shrink_maze,558,558);
end

shrink_fan=shrink_fan*255;
figure(1)
imshow(uint8(shrink_fan))
imwrite(uint8(shrink_fan),'shrink_fan.png')

shrink_cup=shrink_cup*255;
figure(2)
imshow(uint8(shrink_cup))
imwrite(uint8(shrink_cup),'shrink_cup.png')

shrink_maze=shrink_maze*255;
figure(3)
imshow(uint8(shrink_maze'))
imwrite(uint8(shrink_maze'),'shrink_maze.png')


%% Do the thinning
thin_fan=zeros(558,558);
for m=1:1:558
    for n=1:1:558
        if img_fan(m,n)>=50
            thin_fan(m,n)=1;
        end
    end
end
thin_cup=zeros(356,315);
for m=1:1:356
    for n=1:1:315
        if img_cup(m,n)>=50
            thin_cup(m,n)=1;
        end
    end
end
thin_maze=zeros(558,558);
for m=1:1:558
    for n=1:1:558
        if img_maze(m,n)>=127
            thin_maze(m,n)=1;
        end
    end
end

for i=1:1:250   % The number of iterations 
    thin_fan=thin_demo(thin_fan,558,558);
end

for i=1:1:150   % The number of iterations 
    thin_cup=thin_demo(thin_cup,356,315);
end

for i=1:1:1000  % The number of iterations 
    thin_maze=shrink_demo(thin_maze,558,558);
end

thin_fan=thin_fan*255;
figure(1)
imshow(uint8(thin_fan))
imwrite(uint8(thin_fan),'thin_fan.png')

thin_cup=thin_cup*255;
figure(2)
imshow(uint8(thin_cup))
imwrite(uint8(thin_cup),'thin_cup.png')

thin_maze=thin_maze*255;
figure(3)
imshow(uint8(thin_maze'))
imwrite(uint8(thin_maze'),'thin_maze.png')

%% Do the skeletonizing
skeleton_fan=zeros(558,558);
for m=1:1:558
    for n=1:1:558
        if img_fan(m,n)>=50
            skeleton_fan(m,n)=1;
        end
    end
end
skeleton_cup=zeros(356,315);
for m=1:1:356
    for n=1:1:315
        if img_cup(m,n)>=50
            skeleton_cup(m,n)=1;
        end
    end
end
skeleton_maze=zeros(558,558);
for m=1:1:558
    for n=1:1:558
        if img_maze(m,n)>=40
            skeleton_maze(m,n)=1;
        end
    end
end

for i=1:1:250    % The number of iterations 
    skeleton_fan=skeleton_demo(skeleton_fan,558,558);
end

for i=1:1:150    % The number of iterations 
    skeleton_cup=skeleton_demo(skeleton_cup,356,315);
end

for i=1:1:1000   % The number of iterations 
    skeleton_maze=shrink_demo(skeleton_maze,558,558);
end

skeleton_fan=skeleton_fan*255;
figure(1)
imshow(uint8(skeleton_fan))
imwrite(uint8(skeleton_fan),'skeleton_fan.png')

skeleton_cup=skeleton_cup*255;
figure(2)
imshow(uint8(skeleton_cup))
imwrite(uint8(skeleton_cup),'skeleton_cup.png')

skeleton_maze=skeleton_maze*255;
figure(3)
imshow(uint8(skeleton_maze'))
imwrite(uint8(skeleton_maze'),'skeleton_maze.png')

%% Part(b):Counting games
%% Display the original images
fid=fopen('stars.raw','r');
img_PCB=fread(fid,[640,480]);
fclose(fid);
img_PCB=img_PCB';
figure(1)
imshow(uint8(img_PCB))
imwrite(uint8(img_PCB),'stars.png')

binary_stars=zeros(480,640);
for m=1:1:480
    for n=1:1:640
        if img_PCB(m,n)>=120  % Set the threshold value as 120
            binary_stars(m,n)=255;
        else
            binary_stars(m,n)=0;
        end
    end
end
figure(2)
imshow(uint8(binary_stars))
imwrite(uint8(binary_stars),'binary_stars.png')

%% part(1) Do the shrinking and count the total number of stars in the image
 shrink_stars1=zeros(480,640);
 shrink_stars2=zeros(480,640);
for m=1:1:480
    for n=1:1:640
        shrink_stars1(m,n)=binary_stars(m,n)/255;
        shrink_stars2(m,n)=binary_stars(m,n)/255;
    end
end

for i=1:1:100
    shrink_stars1=shrink_demo(shrink_stars1,480,640);
end

shrink_stars1=shrink_stars1*255;
figure(1)
imshow(uint8(shrink_stars1))
imwrite(uint8(shrink_stars1),'shrink_stars.png')

stars_number=0;
for m=1:1:480
    for n=1:1:640
        if shrink_stars1(m,n)==255
            stars_number=stars_number+1;
        end
    end
end
stars_number
%% Count how many different star sizes are present in the image
stars_size=ones(stars_number,1); % The initial size of stars is 1
stars_location=zeros(stars_number,2); % The 1st number represents the row, the 2nd represents the column
num=1;
for m=1:1:480
    for n=1:1:640
        if shrink_stars1(m,n)==255         % Get every star's location
            stars_location(num,1)=m;
            stars_location(num,2)=n;
            num=num+1;
        end
    end
end

for i=1:1:100
    shrink_stars2=shrink_demo(shrink_stars2,480,640);
    for j=1:1:stars_number
        m=stars_location(j,1);
        n=stars_location(j,2);
        temp_value=shrink_stars2(m-1,n-1)||shrink_stars2(m-1,n)||shrink_stars2(m-1,n+1)||...
                   shrink_stars2(m,n-1)||shrink_stars2(m,n+1)||...
                   shrink_stars2(m+1,n-1)||shrink_stars2(m+1,n)||shrink_stars2(m+1,n+1);
        if temp_value==1
            stars_size(j)=stars_size(j)+1; % Regard the number of iterations as every star's size
        end
    end
end

% Obtain the cumulative histograms
min_size=min(stars_size);
max_size=max(stars_size);
stars_size_number=zeros(max_size,1);
for i=1:1:stars_number
    size=stars_size(i);
    stars_size_number(size)=stars_size_number(size)+1;
end
figure(1)
b=bar(stars_size_number,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);
xtips1 = b(1).XEndPoints;
ytips1 = b(1).YEndPoints;
labels1 = string(b(1).YData);
xlabel('The different size of stars')
ylabel('The frequency of different sizes of stars')
text(xtips1,ytips1,labels1,'HorizontalAlignment','center','VerticalAlignment','bottom')

%% part(3) Do the connected component labeling
input_img=binary_stars/255;
output_img=CCL_demo(input_img,480,640,3);
output_array=output_img(:);
output_array=sort(output_array);
stars_number=0;
for i=1:1:length(output_array)-1
    if output_array(i)~=0 && output_array(i)~=output_array(i+1)
        stars_number=stars_number+1;
    end
end
stars_number=stars_number+1 % Add the final kind of element in the output array

% Get the unique elements in the output array except 0
marker_value=zeros(stars_number,1);
location=1;
for i=1:1:length(output_array)-1
    if output_array(i)~=0 && output_array(i)~=output_array(i+1)
        marker_value(location)=output_array(i);
        marker_value(location+1)=output_array(i+1);
        location=location+1;
    end
end        

% Count the number of each unique element in the output array except 0
marker_area=zeros(stars_number,1);        
for i=1:1:length(output_array)
    for j=1:1:length(marker_value)
        if output_array(i)==marker_value(j)
            marker_area(j)=marker_area(j)+1;
        end
    end
end          
        
min_area=min(marker_area);
max_area=max(marker_area);
stars_area_number=zeros(max_area,1);
for i=1:1:length(marker_area)
    area=marker_area(i);
    stars_area_number(area)=stars_area_number(area)+1;
end
figure(1)
b=bar(stars_area_number,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);

xlabel('The different size of stars')
ylabel('The frequency of different sizes of stars')
     
%% Part(c):PCB analysis
%% Display the original images 
fid=fopen('PCB.raw','r');
img_PCB=fread(fid,[372,239]);
fclose(fid);
img_PCB=img_PCB';
figure(1)
imshow(uint8(img_PCB))
imwrite(uint8(img_PCB),'PCB.png')

% Binarize the image
binar_PCB1=zeros(239,372);
binar_PCB2=zeros(239,372);
for m=1:1:239
    for n=1:1:372
        if img_PCB(m,n)>=100
            binar_PCB1(m,n)=255;
        else
            binar_PCB1(m,n)=0;
        end
        if img_PCB(m,n)>=30
            binar_PCB2(m,n)=255;
        else
            binar_PCB2(m,n)=0;
        end
    end
end
figure(2)
imshow(uint8(binar_PCB1))
imwrite(uint8(binar_PCB1),'binar_PCB.png')

% Reverse thr binarized image
rever_PCB1=zeros(239,372);
rever_PCB2=zeros(239,372);
for m=1:1:239
    for n=1:1:372
        rever_PCB1(m,n)=255-binar_PCB1(m,n);
        rever_PCB2(m,n)=255-binar_PCB2(m,n);
    end
end
figure(3)
imshow(uint8(rever_PCB1))
imwrite(uint8(rever_PCB1),'rever_PCB.png')

%% Do the shrinking 
 shrink1_PCB=zeros(239,372);
for m=1:1:239
    for n=1:1:372
        shrink1_PCB(m,n)=binar_PCB1(m,n);
    end
end

shrink1_PCB = bwmorph(shrink1_PCB,'shrink',inf);

for m=1:1:239
    for n=1:1:372
        shrink1_PCB(m,n)=shrink1_PCB(m,n)*255;
    end
end

figure(1)
imshow(shrink1_PCB)
imwrite(shrink1_PCB,'shrink1_PCB.png')

% Count how many white dots (holes)
% Extend the boundaries of images by padding zeros
ext_num=1;
ext_shrink_PCB=zeros(239+ext_num*2,372+ext_num*2);
for m=1:1:239
    for n=1:1:372
        ext_shrink_PCB(m+ext_num,n+ext_num)=shrink1_PCB(m,n);
    end
end

holes_number=0;
for m=1+ext_num:1:239+ext_num
    for n=1+ext_num:1:372+ext_num
        if ext_shrink_PCB(m,n)==1
            a11=ext_shrink_PCB(m-1,n-1);a12=ext_shrink_PCB(m-1,n);a13=ext_shrink_PCB(m-1,n+1);
            a21=ext_shrink_PCB(m,n-1);a23=ext_shrink_PCB(m,n+1);
            a31=ext_shrink_PCB(m+1,n-1);a32=ext_shrink_PCB(m+1,n);a33=ext_shrink_PCB(m+1,n+1);
            temp_value=a11||a12||a13||a21||a23||a31||a32||a33;
            if  temp_value==0
                holes_number=holes_number+1;
            end
        end
    end
end

%% Count how many pathways
%% Do the shrinking 
 shrink2_PCB=zeros(239,372);       
for m=1:1:239
    for n=1:1:372
        shrink2_PCB(m,n)=rever_PCB2(m,n)/255;
    end
end

% Assign the 0 to the pixels on the boundary lines
for m=1:1:2   % Four horizontal lines
    for n=1:1:372
        shrink2_PCB(m,n)=0;
        shrink2_PCB(240-m,n)=0;
    end
end
for n=1:1:2   % Three verical lines
    for m=1:1:239
        shrink2_PCB(m,n)=0;
        if n==1
            shrink2_PCB(m,373-n)=0;
        end
    end
end
        
shrink2_PCB = bwmorph(shrink2_PCB,'thin',inf);
figure(1)
imshow(uint8(shrink2_PCB)*255)
imwrite(uint8(shrink2_PCB)*255,'thin_PCB_original.png')



output_img=CCL_demo(shrink2_PCB,239,372,500);
output_array=output_img(:);
output_array=sort(output_array);
elements_number=0;
for i=1:1:length(output_array)-1
    if output_array(i)~=0 && output_array(i)~=output_array(i+1)
        elements_number=elements_number+1;
    end
end
elements_number=elements_number+1;

% Get the unique elements in the output array except 0
marker_value=zeros(elements_number,1);
location=1;
for i=1:1:length(output_array)-1
    if output_array(i)~=0 && output_array(i)~=output_array(i+1)
        marker_value(location)=output_array(i);
        marker_value(location+1)=output_array(i+1);
        location=location+1;
    end
end        

% Count the number of each unique element in the output array except 0
marker_area=zeros(elements_number,1);        
for i=1:1:length(output_array)
    for j=1:1:length(marker_value)
        if output_array(i)==marker_value(j)
            marker_area(j)=marker_area(j)+1;
        end
    end
end          
        
for m=1:1:239
    for n=1:1:372
        if shrink2_PCB(m,n)~=0
            temp_value=output_img(m,n);
            for i=1:1:elements_number
                if marker_value(i)==temp_value
                    index=i;
                    break
                end
            end
            
            temp_area=marker_area(index);
            if temp_area<=30
                shrink2_PCB(m,n)=0;
            end
        end
    end
end
shrink2_PCB = bwmorph(shrink2_PCB,'thin',inf);

for m=1:1:239
    for n=1:1:372
        shrink2_PCB(m,n)=shrink2_PCB(m,n)*255;
    end
end
figure(2)
imshow(shrink2_PCB)
imwrite(shrink2_PCB,'thin2_PCB.png')
%% Use the connected component labeling approach
input_img=zeros(239,372);
for m=1:1:239
    for n=1:1:372
        input_img(m,n)=shrink2_PCB(m,n);
    end
end
output_img=CCL_demo(input_img,239,372,500);
length(unique(output_img))

output_array=output_img(:);
output_array=sort(output_array);
elements_number=0;
for i=1:1:length(output_array)-1
    if output_array(i)~=0 && output_array(i)~=output_array(i+1)
        elements_number=elements_number+1;
    end
end
elements_number=elements_number+1

%% Part(d): Defect detection
%% Display the original images 
fid=fopen('Geartooth.raw','r');
img_Geartooth=fread(fid,[250,250]);
fclose(fid);
img_Geartooth=img_Geartooth';
figure(1)
imshow(uint8(img_Geartooth))
imwrite(uint8(img_Geartooth),'Geartooth.png')

% Binarize the image
binar_Geartooth=zeros(250,250);
for m=1:1:250
    for n=1:1:250
        if img_Geartooth(m,n)>=30
            binar_Geartooth(m,n)=255;
        else
            binar_Geartooth(m,n)=0;
        end
    end
end
figure(2)
imshow(uint8(binar_Geartooth))
imwrite(uint8(binar_Geartooth),'binar_Geartooth.png')

% Reverse thr binarized image
rever_Geartooth=zeros(250,250);
for m=1:1:250
    for n=1:1:250
        rever_Geartooth(m,n)=255-binar_Geartooth(m,n);
    end
end
figure(3)
imshow(uint8(rever_Geartooth))
imwrite(uint8(rever_Geartooth),'rever_Geartooth.png')

%% Do the shrinking 
 shrink1_Geartooth=zeros(239,372);
for m=1:1:250
    for n=1:1:250
        shrink1_Geartooth(m,n)=rever_Geartooth(m,n)/255;
    end
end

for i=1:1:50
    shrink1_Geartooth=shrink_demo(shrink1_Geartooth,250,250);
end

for m=1:1:250
    for n=1:1:250
        shrink1_Geartooth(m,n)=shrink1_Geartooth(m,n)*255;
    end
end

figure(1)
imshow(uint8(shrink1_Geartooth))
imwrite(uint8(shrink1_Geartooth),'shrink1_Geartooth.png')


%% Step1: Find four positions
point1=zeros(1,2);point2=zeros(1,2);
point3=zeros(1,2);point4=zeros(1,2);
flag=1;
for m=1:1:250
    for n=1:1:250
        if shrink1_Geartooth(m,n)==255
            a11=shrink1_Geartooth(m-1,n-1);a12=shrink1_Geartooth(m-1,n);a13=shrink1_Geartooth(m-1,n+1);
            a21=shrink1_Geartooth(m,n-1);a23=shrink1_Geartooth(m,n+1);
            a31=shrink1_Geartooth(m+1,n-1);a32=shrink1_Geartooth(m+1,n);a33=shrink1_Geartooth(m+1,n+1);
            temp_value=a11||a12||a13||a21||a23||a31||a32||a33;
            if  temp_value==0
                if flag==1
                    point1(1,1)=m;point1(1,2)=n;
                    flag=flag+1;
                    break
                end
                if flag==2
                    point2(1,1)=m;point2(1,2)=n;
                    flag=flag+1;
                    break
                end
                if flag==3
                    point3(1,1)=m;point3(1,2)=n;
                    flag=flag+1;  
                    break
                end
                if flag==4
                    point4(1,1)=m;point4(1,2)=n;
                    flag=flag+1;  
                    break
                end
            end
        end
    end
    if flag==5
        break
    end
end

step1_img=zeros(250,250);
for m=1:1:250
    for n=1:1:250
        step1_img(m,n)=binar_Geartooth(m,n);
    end
end
center_m=round((point1(1,1)+point2(1,1)+point3(1,1)+point4(1,1))/4);
center_n=round((point1(1,2)+point2(1,2)+point3(1,2)+point4(1,2))/4);

step1_img(center_m,center_n)=0;

figure(1)
imshow(uint8(step1_img))
hold on; 
plot(center_m,center_n,'ro');
imwrite(uint8(step1_img),'step1_img.png')

%% Step2: Estimate the outside radius of this gear in terms of number of pixels
location_m=center_m;
radius=0;
while 1
    location_m=location_m+1;
    if binar_Geartooth(location_m,center_n)==255
        radius=radius+1;
    else
        break
    end       
end
radius

%% Step3: Find the positions of the gear teeth in this gear
index_distance=radius-7;
situation=zeros(12,1);
location=zeros(12,2);
%% Check the positions: 1,4,7,and 10
% For the position 1
m=center_m;
n=center_n-index_distance;
temp_value=get_temp(binar_Geartooth,m,n);

if temp_value==0
    situation(1)=0;
    while 1
        n=n+1;
        if binar_Geartooth(m,n)==255
            location(1,1)=m;
            location(1,2)=n;
            break
        end
    end
else
    situation(1)=1;
    location(1,1)=m;
    location(1,2)=n;
end

% For the position 4
m=center_m-index_distance;
n=center_n;
temp_value=get_temp(binar_Geartooth,m,n);
if temp_value==0
    situation(4)=0;
    while 1
        m=m+1;
        if binar_Geartooth(m,n)==255
            location(4,1)=m;
            location(4,2)=n;
            break
        end
    end
else
    situation(4)=1;
    location(4,1)=m;
    location(4,2)=n;
end

% For the position 7
m=center_m;
n=center_n+index_distance;
situation(7)=get_temp(binar_Geartooth,m,n);
location(7,1)=m;
location(7,2)=n;

% For the position 10
m=center_m+index_distance;
n=center_n;
temp_value=get_temp(binar_Geartooth,m,n);
if temp_value==0
    situation(10)=0;
    while 1
        m=m-1;
        if binar_Geartooth(m,n)==255
            location(10,1)=m;
            location(10,2)=n;
            break
        end
    end
else
    situation(10)=1;
    location(10,1)=m;
    location(10,2)=n;
end

% Check the positions: 2,3
flag2=1;
flag3=1;
for m=1:1:center_m
    for n=1:1:center_n
        distance=floor(sqrt((m-center_m)^2+(n-center_n)^2));
        if (distance>=index_distance-1)&&(distance<=index_distance+1)
            temp_angle=atan(abs((m-center_m)/(n-center_n)));
            if (temp_angle>=pi/6-0.01)&&(temp_angle<=pi/6+0.01)&&flag2
                temp_m2=m;temp_n2=n;
                flag2=0;
            end
            if (temp_angle>=pi/3-0.01)&&(temp_angle<=pi/3+0.01)&&flag3
                temp_m3=m;temp_n3=n;
                flag3=0;
            end
        end
    end
end

location(2,1)=temp_m2;location(2,2)=temp_n2;
location(3,1)=temp_m3;location(3,2)=temp_n3;  

situation(2)=get_temp(binar_Geartooth,temp_m2,temp_n2);
situation(3)=get_temp(binar_Geartooth,temp_m3,temp_n3);

% Check the positions: 5,6
flag5=1;
flag6=1;
for m=1:1:center_m
    for n=center_n:1:250
        distance=floor(sqrt((m-center_m)^2+(n-center_n)^2));
        if (distance>=index_distance-1)&&(distance<=index_distance+1)
            temp_angle=atan(abs((m-center_m)/(n-center_n)));
            if (temp_angle>=pi/6-0.01)&&(temp_angle<=pi/6+0.01)&&flag6
                temp_m6=m;temp_n6=n;
                flag6=0;
            end
            if (temp_angle>=pi/3-0.01)&&(temp_angle<=pi/3+0.01)&&flag5
                temp_m5=m;temp_n5=n;
                flag5=0;
            end
        end
    end
end

location(5,1)=temp_m5;location(5,2)=temp_n5;
location(6,1)=temp_m6;location(6,2)=temp_n6;  

situation(5)=get_temp(binar_Geartooth,temp_m5,temp_n5);
situation(6)=get_temp(binar_Geartooth,temp_m6,temp_n6);

% Check the positions: 8,9
flag8=1;
flag9=1;
for m=center_m:1:250
    for n=center_n:1:250
        distance=floor(sqrt((m-center_m)^2+(n-center_n)^2));
        if (distance>=index_distance-1)&&(distance<=index_distance+1)
            temp_angle=atan(abs((m-center_m)/(n-center_n)));
            if (temp_angle>=pi/6-0.01)&&(temp_angle<=pi/6+0.01)&&flag8
                temp_m8=m;temp_n8=n;
                flag8=0;
            end
            if (temp_angle>=pi/3-0.01)&&(temp_angle<=pi/3+0.01)&&flag9
                temp_m9=m;temp_n9=n;
                flag9=0;
            end
        end
    end
end

location(8,1)=temp_m8;location(8,2)=temp_n8;
location(9,1)=temp_m9;location(9,2)=temp_n9;  

situation(8)=get_temp(binar_Geartooth,temp_m8,temp_n8);
situation(9)=get_temp(binar_Geartooth,temp_m9,temp_n9);

% Check the positions: 11,12
flag11=1;
flag12=1;
for m=center_m:1:250
    for n=1:1:center_n
        distance=floor(sqrt((m-center_m)^2+(n-center_n)^2));
        if (distance>=index_distance-1)&&(distance<=index_distance+1)
            temp_angle=atan(abs((m-center_m)/(n-center_n)));
            if (temp_angle>=pi/6-0.01)&&(temp_angle<=pi/6+0.01)&&flag12
                temp_m12=m;temp_n12=n;
                flag12=0;
            end
            if (temp_angle>=pi/3-0.01)&&(temp_angle<=pi/3+0.01)&&flag11
                temp_m11=m;temp_n11=n;
                flag11=0;
            end
        end
    end
end

location(11,1)=temp_m11;location(11,2)=temp_n11;
location(12,1)=temp_m12;location(12,2)=temp_n12;  

situation(11)=get_temp(binar_Geartooth,temp_m11,temp_n11);
situation(12)=get_temp(binar_Geartooth,temp_m12,temp_n12);

% Find the positions of the geer teeth in this gear
step3_img=zeros(250,250);
for m=1:1:250
    for n=1:1:250
        step3_img(m,n)=binar_Geartooth(m,n);
    end
end

figure(1)
imshow(uint8(step3_img))
hold on;
for i=1:1:12
    if situation(i)==1
        plot(location(i,2),location(i,1),'go','MarkerFaceColor','g');
    end
end
imwrite(uint8(step3_img),'step3_img.png')

% Find and display the positions of the missing teeth
step4_img=zeros(250,250);
for m=1:1:250
    for n=1:1:250
        step4_img(m,n)=binar_Geartooth(m,n);
    end
end

figure(2)
imshow(uint8(step4_img))
hold on;
for i=1:1:12
    if situation(i)==0
        plot(location(i,2),location(i,1),'ro','MarkerFaceColor','r');
    end
end
imwrite(uint8(step4_img),'step4_img.png')
hold off