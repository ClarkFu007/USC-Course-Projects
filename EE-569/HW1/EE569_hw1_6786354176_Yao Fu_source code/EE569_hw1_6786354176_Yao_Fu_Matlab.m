% EE569 Homework Assignment # 1 
% Submission Date: January 28, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: Show the original and resulting images
%% 
img1=readraw('Corn_gray.raw');
figure(1)
imshow(uint8(img1))
imwrite(uint8(img1),'Corn_gray.png')
%%
img2=readraw('Corn_noisy.raw');
figure(2)
imshow(uint8(img2))
imwrite(uint8(img2),'Corn_noisy.png')
%% Problem 1
%% Extend the boundaries of images
fid=fopen('Dog_ext100.raw','r');
img3=fread(fid,[800,732]);
fclose(fid);
figure(3)
imshow(uint8(img3'))
%% Problem1_part(a)
fid=fopen('Dog_rgb_bili.raw','r');
img4_temp=fread(fid,inf);
fclose(fid);
Y=532;X=600;p=Y*X;
img4=zeros(Y,X,3);
img4_r=zeros(X,Y);img4_g=zeros(X,Y);img4_b=zeros(X,Y);
img4_r(1:p)=img4_temp(1:3:3*p);
img4_g(1:p)=img4_temp(2:3:3*p);
img4_b(1:p)=img4_temp(3:3:3*p);
img4(:,:,1)=img4_r';
img4(:,:,2)=img4_g';
img4(:,:,3)=img4_b';
figure(4)
imshow(uint8(img4))
imwrite(uint8(img4),'Dog_rgb_bili.png')
%% Problem1_part(b)
fid=fopen('Dog_rgb_MHC.raw','r');
img4_temp=fread(fid,inf);
fclose(fid);
Y=532;X=600;p=Y*X;
img4=zeros(Y,X,3);
img4_r=zeros(X,Y);img4_g=zeros(X,Y);img4_b=zeros(X,Y);
img4_r(1:p)=img4_temp(1:3:3*p);
img4_g(1:p)=img4_temp(2:3:3*p);
img4_b(1:p)=img4_temp(3:3:3*p);
img4(:,:,1)=img4_r';
img4(:,:,2)=img4_g';
img4(:,:,3)=img4_b';
figure(1)
imshow(uint8(img4))
imwrite(uint8(img4),'MHC_Output.png')
%%
fid=fopen('Dog_ori.raw','r');
img4_temp=fread(fid,inf);
fclose(fid);
Y=532;X=600;p=Y*X;
img4=zeros(Y,X,3);
img4_r=zeros(X,Y);img4_g=zeros(X,Y);img4_b=zeros(X,Y);
img4_r(1:p)=img4_temp(1:3:3*p);
img4_g(1:p)=img4_temp(2:3:3*p);
img4_b(1:p)=img4_temp(3:3:3*p);
img4(:,:,1)=img4_r';
img4(:,:,2)=img4_g';
img4(:,:,3)=img4_b';
figure(1)
imshow(uint8(img4))
imwrite(uint8(img4),'Dog_ori.png')
%%
fid=fopen('Toy.raw','r');
img5_temp=fread(fid,inf,'uchar');
fclose(fid);
Y=560;X=400;p=Y*X;
img5=zeros(Y,X,3);
img5_r=zeros(X,Y);img5_g=zeros(X,Y);img5_b=zeros(X,Y);
img5_r(1:p)=img5_temp(1:3:3*p);
img5_g(1:p)=img5_temp(2:3:3*p);
img5_b(1:p)=img5_temp(3:3:3*p);
img5(:,:,1)=img5_r';
img5(:,:,2)=img5_g';
img5(:,:,3)=img5_b';
figure(1)
imshow(uint8(img5))
imwrite(uint8(img5),'Toy.png')
%% Problem1_part(c)_(1)
fid=fopen('Prob_1c1_data.raw','r');
DataProb_1c1=fread(fid,inf,'int');
fclose(fid);
Channel_R=zeros(1,256);Channel_G=zeros(1,256);Channel_B=zeros(1,256);
for i =1:1:256
    Channel_R(1:256)=DataProb_1c1(1:3:3*256);
    Channel_G(1:256)=DataProb_1c1(2:3:3*256);
    Channel_B(1:256)=DataProb_1c1(3:3:3*256);
end
figure(1)
bar(Channel_R)
xlabel('The intensity values (0-255)')
ylabel('The number of pixels')
figure(2)
bar(Channel_G)
xlabel('The intensity values (0-255)')
ylabel('The number of pixels')
figure(3)
bar(Channel_B)
xlabel('The intensity values (0-255)')
ylabel('The number of pixels')
%% Problem1_part(c)_(2):Method A
fid=fopen('EnhanA_RGB.raw','r');
img_temp=fread(fid,inf,'uchar');
fclose(fid);
Y=560;X=400;p=Y*X;
img=zeros(Y,X,3);
img_r=zeros(X,Y);img_g=zeros(X,Y);img_b=zeros(X,Y);
img_r(1:p)=img_temp(1:3:3*p);
img_g(1:p)=img_temp(2:3:3*p);
img_b(1:p)=img_temp(3:3:3*p);
img(:,:,1)=img_r';
img(:,:,2)=img_g';
img(:,:,3)=img_b';
figure(1)
imshow(uint8(img))
imwrite(uint8(img),'EnhanA_RGB.png')
%Plot transfer functions for each channel
fid=fopen('Prob_1c1_data.raw','r');
Equ_Channel=fread(fid,inf,'uchar');
Equ_Channel_R=zeros(1,256);Equ_Channel_G=zeros(1,256);Equ_Channel_B=zeros(1,256);
Equ_Channel_R(1:256)=Equ_Channel(1:3:3*256);
Equ_Channel_G(1:256)=Equ_Channel(2:3:3*256);
Equ_Channel_B(1:256)=Equ_Channel(3:3:3*256);
fclose(fid);

x_Ar = 0:255;
y_Ar = Equ_Channel_R(x_Ar+1);
figure(2)
plot(x_Ar,y_Ar)
xlim([0 255])
ylim([0 255])
xlabel('The gray scale (0-255) of input images')
ylabel('The gray scale (0-255) of output images')
line([0,100],[197,197],'linestyle','--','color','g');
line([100,100],[0,197],'linestyle','--','color','g');
text(100,199,'(100,197)','FontWeight','bold','Color','g','horiz','center','vert','bottom')

x_Ag = 0:255;
y_Ag = Equ_Channel_G(x_Ag+1);
figure(3)
plot(x_Ag,y_Ag)
xlim([0 255])
ylim([0 255])
xlabel('The gray scale (0-255) of input images')
ylabel('The gray scale (0-255) of output images')
line([0,100],[199,199],'linestyle','--','color','g');
line([100,100],[0,199],'linestyle','--','color','g');
text(100,201,'(100,199)','FontWeight','bold','Color','g','horiz','center','vert','bottom')

x_Ab = 0:255;
y_Ab = Equ_Channel_B(x_Ab+1);
figure(4)
plot(x_Ab,y_Ab)
xlim([0 255])
ylim([0 255])
xlabel('The gray scale (0-255) of input images')
ylabel('The gray scale (0-255) of output images')
line([0,100],[202,202],'linestyle','--','color','g');
line([100,100],[0,202],'linestyle','--','color','g');
text(100,204,'(100,202)','FontWeight','bold','Color','g','horiz','center','vert','bottom')
%% Problem1_part(c)_(3):Method B
fid=fopen('EnhanB_RGB.raw','r');
img_temp=fread(fid,inf,'uchar');
fclose(fid);
Y=560;X=400;p=Y*X;
img=zeros(Y,X,3);
img_r=zeros(X,Y);img_g=zeros(X,Y);img_b=zeros(X,Y);
img_r(1:p)=img_temp(1:3:3*p);
img_g(1:p)=img_temp(2:3:3*p);
img_b(1:p)=img_temp(3:3:3*p);
img(:,:,1)=img_r';
img(:,:,2)=img_g';
img(:,:,3)=img_b';
figure(1)
imshow(uint8(img))
imwrite(uint8(img),'EnhanB_RGB.png')
% Obtain the cumulative histograms
Y=560;X=400;total=Y*X;
Channel_R_B=zeros(1,256);Channel_G_B=zeros(1,256);Channel_B_B=zeros(1,256);
for i =1:1:total
    temp_r=img_r(i)+1;
    temp_g=img_g(i)+1;
    temp_b=img_b(i)+1;
    Channel_R_B(temp_r)=Channel_R_B(temp_r)+1;
    Channel_G_B(temp_g)=Channel_G_B(temp_g)+1;
    Channel_B_B(temp_b)=Channel_B_B(temp_b)+1;
end
figure(2)
bar(Channel_R_B)
figure(3)
bar(Channel_G_B)
figure(4)
bar(Channel_B_B)

Cum_Channel_R_B=zeros(1,256);Cum_Channel_G_B=zeros(1,256);Cum_Channel_B_B=zeros(1,256);
for i =1:1:256
    for j=1:1:i
        Cum_Channel_R_B(i)=Cum_Channel_R_B(i)+Channel_R_B(j);
        Cum_Channel_G_B(i)=Cum_Channel_G_B(i)+Channel_G_B(j);
        Cum_Channel_B_B(i)=Cum_Channel_B_B(i)+Channel_B_B(j);
    end
end

figure(5)
bar(Cum_Channel_R_B)
xlabel('The gray scale (0-255) of the output image')
ylabel('The cumulative number of pixels')
figure(6)
bar(Cum_Channel_G_B)
xlabel('The gray scale (0-255) of the output image')
ylabel('The cumulative number of pixels')
figure(7)
bar(Cum_Channel_B_B)
xlabel('The gray scale (0-255) of the output image')
ylabel('The cumulative number of pixels')
%% Problem 2
%% 
img_ori=readraw('Corn_gray.raw');
figure(1)
imshow(uint8(img_ori))
imwrite(uint8(img_ori),'Corn_gray.png')
img_noise=readraw('Corn_noisy.raw');
figure(2)
imshow(uint8(img_noise))
imwrite(uint8(img_noise),'Corn_noisy.png')
psnr0=getPSNR(img_ori, img_noise)
%% Problem2_part(a)
fid=fopen('UniFil_Image.raw','r');
img_uni=fread(fid,[320,320]);
fclose(fid);
figure(1)
imshow(uint8(img_uni'))
imwrite(uint8(img_uni'),'UniFil_Image.png')
psnr1=getPSNR(img_uni', img_noise)
fid=fopen('GauFil1_Image.raw','r');
img_gau1=fread(fid,[320,320]);
fclose(fid);
figure(2)
imshow(uint8(img_gau1'))
imwrite(uint8(img_gau1'),'GauFil1_Image.png')
psnr2=getPSNR(img_gau1', img_noise)
fid=fopen('GauFil2_Image.raw','r');
img_gau2=fread(fid,[320,320]);
fclose(fid);
figure(3)
imshow(uint8(img_gau2'))
imwrite(uint8(img_gau2'),'GauFil2_Image.png')
psnr3=getPSNR(img_gau2', img_noise)
%% Problem2_part(b)
fid=fopen('BilFil_Image.raw','r');
img_bil=fread(fid,[320,320]);
fclose(fid);
figure(1)
imshow(uint8(img_bil'))
imwrite(uint8(img_bil'),'BilFil_Image.png')
psnr4=getPSNR(img_bil', img_noise)
%% Problem2_part(c)
[img_nlm]=simple_nlm(img_noise,3,2,4,10,1);
figure(1)
imshow(uint8(img_nlm))
psnr5=getPSNR(img_nlm, img_noise)
imwrite(uint8(img_nlm),'Corn_nlm.png')
%% Problem2_part(d) BM3D
% Use online source code