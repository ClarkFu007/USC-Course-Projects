% EE569 Homework Assignment # 2 
% Submission Date: January 28, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: Show the original and resulting images

%% Problem 1
fid=fopen('Dogs.raw','r');
img1_temp=fread(fid,inf);
fclose(fid);
Y=321;X=481;p=Y*X;
img1=zeros(Y,X,3);
img1_r=zeros(X,Y);img1_g=zeros(X,Y);img1_b=zeros(X,Y);
img1_r(1:p)=img1_temp(1:3:3*p);
img1_g(1:p)=img1_temp(2:3:3*p);
img1_b(1:p)=img1_temp(3:3:3*p);
img1(:,:,1)=img1_r';
img1(:,:,2)=img1_g';
img1(:,:,3)=img1_b';
figure(1)
imshow(uint8(img1))

fid=fopen('Gallery.raw','r');
img2_temp=fread(fid,inf);
fclose(fid);
Y=321;X=481;p=Y*X;
img2=zeros(Y,X,3);
img2_r=zeros(X,Y);img2_g=zeros(X,Y);img2_b=zeros(X,Y);
img2_r(1:p)=img2_temp(1:3:3*p);
img2_g(1:p)=img2_temp(2:3:3*p);
img2_b(1:p)=img2_temp(3:3:3*p);
img2(:,:,1)=img2_r';
img2(:,:,2)=img2_g';
img2(:,:,3)=img2_b';
figure(2)
imshow(uint8(img2))
%% 
fid=fopen('GrayImage1.raw','r');
img1=fread(fid,[481,321]);
fclose(fid);
figure(1)
imshow(uint8(img1'))
imwrite(uint8(img1'),'GrayImage1.jpg')

fid=fopen('GrayImage2.raw','r');
img2=fread(fid,[481,321]);
fclose(fid);
figure(2)
imshow(uint8(img2'))
imwrite(uint8(img2'),'GrayImage2.jpg')

%% Problem1_Dogs
% Problem1_part(a)_1
fid=fopen('SobFilImage_x1.raw','r');
img_sob_x1=fread(fid,[481,321]);
fclose(fid);
figure(1)
imshow(uint8(img_sob_x1'))
imwrite(uint8(img_sob_x1'),'SobFilImage_x1.png');

fid=fopen('SobFilImage_y1.raw','r');
img_sob_y1=fread(fid,[481,321]);
fclose(fid);
figure(2)
imshow(uint8(img_sob_y1'))
imwrite(uint8(img_sob_y1'),'SobFilImage_y1.png');

% Problem1_part(a)_2
fid=fopen('NorGrImage_1.raw','r');
img_nor_gra1=fread(fid,[481,321]);
fclose(fid);
figure(3)
imshow(uint8(img_nor_gra1'))
imwrite(uint8(img_nor_gra1'),'NorGrImage_1.png');

% Problem1_part(a)_3
fid=fopen('ThreshImage_1.raw','r');
img_thresh1=fread(fid,[481,321]);
fclose(fid);
figure(4)
imshow(uint8(img_thresh1'))
imwrite(uint8(img_thresh1'),'ThreshImage_1_Sobel.png');

%% Problem1_Gallery
% Problem1_part(a)_1
fid=fopen('SobFilImage_x2.raw','r');
img_sob_x1=fread(fid,[481,321]);
fclose(fid);
figure(1)
imshow(uint8(img_sob_x1'))
imwrite(uint8(img_sob_x1'),'SobFilImage_x2.png')

% Problem1_part(a)_2
fid=fopen('SobFilImage_y2.raw','r');
img_sob_y1=fread(fid,[481,321]);
fclose(fid);
figure(2)
imshow(uint8(img_sob_y1'))
imwrite(uint8(img_sob_y1'),'SobFilImage_y2.png')

% Problem1_part(a)_3
fid=fopen('NorGrImage_2.raw','r');
img_nor_gra2=fread(fid,[481,321]);
fclose(fid);
figure(3)
imshow(uint8(img_nor_gra2'))
imwrite(uint8(img_nor_gra2'),'NorGrImage_2.png')

% Problem1_part(a)_4
fid=fopen('ThreshImage_2.raw','r');
img_thresh2=fread(fid,[481,321]);
fclose(fid);
figure(4)
imshow(uint8(img_thresh2'))
imwrite(uint8(img_thresh2'),'ThreshImage_2_Sobel.png')

%% Problem 2
fid=fopen('LightHouse.raw','r');
img_LightHouse=fread(fid,[750,500]);
fclose(fid);
figure(1)
imshow(uint8(img_LightHouse'))
imwrite(uint8(img_LightHouse'),'img_LightHouse.png')

fid=fopen('Rose.raw','r');
img_temp=fread(fid,inf);
fclose(fid);
Y=480;X=640;p=Y*X;
img_Rose=zeros(Y,X,3);
img_Rose_r=zeros(X,Y);img_Rose_g=zeros(X,Y);img_Rose_b=zeros(X,Y);
img_Rose_r(1:p)=img_temp(1:3:3*p);
img_Rose_g(1:p)=img_temp(2:3:3*p);
img_Rose_b(1:p)=img_temp(3:3:3*p);
img_Rose(:,:,1)=img_Rose_r';
img_Rose(:,:,2)=img_Rose_g';
img_Rose(:,:,3)=img_Rose_b';
figure(2)
imshow(uint8(img_Rose))
imwrite(uint8(img_Rose),'img_Rose.png')


%% Problem2_psrt(a):Dithering
% Problem2_part(a)_1: Fixed thresholding
fid=fopen('FixThresh_Image.raw','r');
img_fix_th=fread(fid,[750,500]);
fclose(fid);
figure(1)
imshow(uint8(img_fix_th'))
imwrite(uint8(img_fix_th'),'FixThresh_Image.png');

% Problem2_part(a)_2: Random thresholding
fid=fopen('RandomThresh_Image.raw','r');
img_random_th=fread(fid,[750,500]);
fclose(fid);
figure(2)
imshow(uint8(img_random_th'))
imwrite(uint8(img_random_th'),'RandomThresh_Image.png');

% Problem2_part(a)_3: Dithering Matrix
%The result of I2
fid=fopen('DithMatrix_2_Image.raw','r');
img_random_th=fread(fid,[750,500]);
fclose(fid);
figure(3)
imshow(uint8(img_random_th'))
imwrite(uint8(img_random_th'),'DithMatrix_2_Image.png');
%The result of I8
fid=fopen('DithMatrix_8_Image.raw','r');
img_random_th=fread(fid,[750,500]);
fclose(fid);
figure(4)
imshow(uint8(img_random_th'))
imwrite(uint8(img_random_th'),'DithMatrix_8_Image.png');
%The result of I32
fid=fopen('DithMatrix_32_Image.raw','r');
img_random_th=fread(fid,[750,500]);
fclose(fid);
figure(5)
imshow(uint8(img_random_th'))
imwrite(uint8(img_random_th'),'DithMatrix_32_Image.png');

%% Problem2_part(b): Error diffusion
% Problem2_part(b)_1: Floy-Steinberg's error diffusion
fid=fopen('FS_ErrDif_Image.raw','r');
img_FS=fread(fid,[750,500]);
fclose(fid);
figure(1)
imshow(uint8(img_FS'))
imwrite(uint8(img_FS'),'FS_ErrDif_Image.png');

% Problem2_part(b)_2: Jarvis,Judice,and Ninke(JJN)'s error diffusion
fid=fopen('JJN_ErrDif_Image.raw','r');
img_JJN=fread(fid,[750,500]);
fclose(fid);
figure(2)
imshow(uint8(img_JJN'))
imwrite(uint8(img_JJN'),'JJN_ErrDif_Image.png');

% Problem2_part(b)_3: Stucki's error diffusion
fid=fopen('Stucki_ErrDif_Image.raw','r');
img_Stucki=fread(fid,[750,500]);
fclose(fid);
figure(3)
imshow(uint8(img_Stucki'))
imwrite(uint8(img_Stucki'),'Stucki_ErrDif_Image.png');

%% Problem2_part(c): Color Halftoning with Error diffusion
Y=480;X=640;p=Y*X;
% Problem2_part(c)_1: Seperable Error Diffusion
fid=fopen('Sep_ErrDif_Image.raw','r');
img_SED_temp=fread(fid,inf);
fclose(fid);
img_SED=zeros(Y,X,3);
img_SED_r=zeros(X,Y);img_SED_g=zeros(X,Y);img_SED_b=zeros(X,Y);
img_SED_r(1:p)=img_SED_temp(1:3:3*p);
img_SED_g(1:p)=img_SED_temp(2:3:3*p);
img_SED_b(1:p)=img_SED_temp(3:3:3*p);
img_SED(:,:,1)=img_SED_r';
img_SED(:,:,2)=img_SED_g';
img_SED(:,:,3)=img_SED_b';
figure(1)
imshow(uint8(img_SED))
imwrite(uint8(img_SED),'Sep_ErrDif_Image.png');

% Problem2_part(c)_2: MBVQ-based Error Diffusion
fid=fopen('MBVQ_ErrDif_Image.raw','r');
img_MBVQ_temp=fread(fid,inf);
fclose(fid);
img_MBVQ=zeros(Y,X,3);
img_MBVQ_r=zeros(X,Y);img_MBVQ_g=zeros(X,Y);img_MBVQ_b=zeros(X,Y);
img_MBVQ_r(1:p)=img_MBVQ_temp(1:3:3*p);
img_MBVQ_g(1:p)=img_MBVQ_temp(2:3:3*p);
img_MBVQ_b(1:p)=img_MBVQ_temp(3:3:3*p);
img_MBVQ(:,:,1)=img_MBVQ_r';
img_MBVQ(:,:,2)=img_MBVQ_g';
img_MBVQ(:,:,3)=img_MBVQ_b';
figure(2)
imshow(uint8(img_MBVQ))
imwrite(uint8(img_MBVQ),'MBVQ_ErrDif_Image.png');










