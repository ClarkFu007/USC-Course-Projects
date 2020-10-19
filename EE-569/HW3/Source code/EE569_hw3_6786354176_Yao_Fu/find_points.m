% EE569 Homework Assignment #3:Problem1_part(b) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to find matching point pairs

function [matchedPoints1,matchedPoints2]=find_points(img1,img2)

% Read the stereo images 
points1 = detectHarrisFeatures(img1);
points2 = detectHarrisFeatures(img2);

% Extract the neighborhood features.
[features1,valid_points1] = extractFeatures(img1,points1);
[features2,valid_points2] = extractFeatures(img2,points2);

% Match the features.
indexPairs = matchFeatures(features1,features2,'MaxRatio',0.4,'Unique', true);

% Retrieve the locations of the corresponding points for each image.
matchedPoints1 = valid_points1(indexPairs(:,1),:);
matchedPoints2 = valid_points2(indexPairs(:,2),:);

% Visualize the corresponding points. You can see the effect of translation 
% between the two images despite several erroneous matches.

%output_img=interpolate_demo(output_img,512,512);  
figure; showMatchedFeatures(img1,img2,matchedPoints1,matchedPoints2);