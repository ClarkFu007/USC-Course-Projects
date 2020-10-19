% Experiment specifications
imagename_gray = 'Corn_gray.png';
imagename_noisy = 'Corn_noisy.png';
% Load noise-free image
im_gray = im2double(imread(imagename_gray));
% Load noisy image
im_noisy = im2double(imread(imagename_noisy));
psnr1 = getPSNR(im_gray, im_noisy)
%%
fid=fopen('Noise_data.raw','r');
NoiseData=fread(fid,inf,'int');
fclose(fid);
NoiseData=NoiseData(:);
Max_value=max(NoiseData);
Min_value=min(NoiseData);
temp=abs(Min_value);
Noise=zeros(1,Max_value-Min_value+1);
%%
total=320*320;
for i=1:1:size(NoiseData)
    t=NoiseData(i);
    Noise(t+1+temp)=Noise(t+1+temp)+1;
 
end
figure(1)
X=Min_value:Max_value;
plot(X,Noise/total)
xlabel('The noise values')
ylabel('The number of different values')