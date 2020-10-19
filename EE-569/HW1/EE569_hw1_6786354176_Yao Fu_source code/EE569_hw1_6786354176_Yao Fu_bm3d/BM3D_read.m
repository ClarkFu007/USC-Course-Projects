img_noise=readraw('Corn_noisy.raw');
figure(1)
imshow(uint8(img_noise))

[J,sigma_psd] = imnlmfilt(img_noise);
img_bm3d=BM3D(img_noise, 1);
figure(2)
imshow(uint8(img_bm3d))