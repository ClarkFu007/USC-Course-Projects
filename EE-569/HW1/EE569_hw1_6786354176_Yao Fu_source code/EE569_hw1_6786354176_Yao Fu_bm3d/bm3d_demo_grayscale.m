% Grayscale BM3D denoising demo file, based on Y. M??kinen, L. Azzari, A. Foi, 2019.
% Exact Transform-Domain Noise Variance for Collaborative Filtering of Stationary Correlated Noise.
% In IEEE International Conference on Image Processing (ICIP), pp. 185-189

% ---
% The location of the BM3D files -- this folder only contains demo data
addpath('bm3d');

% Experiment specifications   
imagename = 'Corn_noisy.png';

% Load noise-free image
img_noise = im2double(imread(imagename));

% Possible noise types to be generated 'g0', 'g1', 'g2', 'g3', 'g4', 'g1w',
% 'g2w', 'g3w', 'g4w'.

noise_type =  'g2w';
noise_var = 0.0028;   % Noise variance
seed = 0;           % seed for pseudorandom noise realization

% Generate noise with given PSD
[noise, PSD, kernel] = getExperimentNoise(noise_type, noise_var, seed, size(img_noise));

% N.B.: For the sake of simulating a more realistic acquisition scenario,
% the generated noise is *not* circulant. Therefore there is a slight
% discrepancy between PSD and the actual PSD computed from infinitely many
% realizations of this noise with different seeds.

% Generate noisy image corrupted by additive spatially correlated noise
% with noise power spectrum PSD
%z = y + noise;

% Call BM3D With the default settings.
img_bm3d = BM3D(img_noise, PSD);


% To include refiltering:
%y_est = BM3D(z, PSD, 'refilter');

% For other settings, use BM3DProfile.
% profile = BM3DProfile(); % equivalent to profile = BM3DProfile('np');
% profile.gamma = 6;  % redefine value of gamma parameter
% y_est = BM3D(z, PSD, profile);

% Note: For white noise, you may instead of the PSD 
% also pass a standard deviation 
% y_est = BM3D(z, sqrt(noise_var));


psnr = getPSNR(img_noise, img_bm3d)

% PSNR ignoring 16-pixel wide borders (as used in the paper), due to refiltering potentially leaving artifacts
% on the pixels near the boundary of the image when noise is not circulant
% psnr_cropped = getCroppedPSNR(y, y_est, [16, 16]);

figure(1)
imshow(img_noise)

figure(2)
imshow(img_bm3d)
imwrite(img_bm3d,'Corn_bm3d.png')
