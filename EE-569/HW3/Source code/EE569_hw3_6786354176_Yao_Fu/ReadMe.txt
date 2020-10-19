# EE569 Homework Assignment #3
# Date: March 03, 2020
# Name: Yao Fu
# USC ID: 6786354176
# email: yaof@usc.edu
#
# Software: MATLAB 2019b
# Operating System: Windows 10
========================================================================
    CONSOLE APPLICATION : [EE569_hw3_6786354176_Yao Fu] Project Overview
========================================================================

This file contains a summary of what I will find in each of the files that
make up my [EE569_hw3_6786354176_Yao Fu] application.

Steps:

1. Open "EE569_hw3_6786354176_Yao_Fu_Matlab.m".
	This is the main part for the project.


2. Run the section "Geometric warping".
	This is the main program for the algorithms in problem 1_part(a).
     
   Step1: You need to read images into image data matrix by putting images into the same file directory.	
          The important statements are
                        fid=fopen('hedwig.raw','r');
	                fid=fopen('raccoon.raw','r');
	                fid=fopen('bb8.raw','r');
   
   Step2: While running this section, you may notice tow MATLAB files.
	                "geo_warping.m"
                        "rev_warping.m"
                        "interpolate_demo.m"
   Those three functions can realize the forward geometric warping, reverse geometric warping, and interpolation 
respectively.

   Step3: After finishing running this section, you will see resulting pictures. 
                        "warp_hedwig.png"
                        "warp_raccoon.png"
                        "warp_bb8.png"
                        "rev_warp_hedwig.png"
                        "rev_warp_raccoon.png"
                        "rev_warp_bb8.png"


3. Run the section "Homographic Transformation and Image Stiching".
	This is the main program for the algorithms in problem 1_part(b).

   Step1: You need to read images into image data matrix by putting images into the same file directory.	
          The important statements are
                                       fid=fopen('left.raw','r');
	                               fid=fopen('middle.raw','r');
                                       fid=fopen('right.raw','r');
   Step2: While running this section, you may notice tow MATLAB files.
	                               "stich_demo.m"
                                       "find_points.m"
                                       "interpolate_demo.m"
   Those three functions can realize the images stitching, finding control points, and interpolation 
respectively.
   
   Step3: After finishing running this section, you will see resulting pictures.
                                       "stiched_RGB.png"
	

4. Run the section "Basic morphological process implementation".
	This is the main program for the algorithms in problem 2_part(a).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
          The important statements are
                                       fid=fopen('fan.raw','r');
	                               fid=fopen('cup.raw','r');
                                       fid=fopen('maze.raw','r');
   
   Step2: While running this section, you may notice tow MATLAB files.
	                               "shrink_demo.m"
                                       "thin_demo.m"
                                       "skeleton_demo.m"
   Those three functions can realize the images shrinking, thinning, and skeletonizing respectively. By 
adjusting numbers of iterations, you will see different intermediate images.
   
   Step3: After finishing running this section, you will see resulting pictures.
                                       "shrink_fan.png"
                                       "shrink_cup.png"
                                       "shrink_maze.png"
                                       "thin_fan.png"
                                       "thin_cup.png"
                                       "thin_maze.png"
                                       "skeleton_fan.png"
                                       "skeleton_cup.png"
                                       "skeleton_maze.png"


5. Run the section "Counting games".
	This is the main program for the algorithms in problem 2_part(b).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
          The important statements are
                                       fid=fopen('stars.raw','r');
   
   Step2: While running this section, you may notice tow MATLAB files.
	                               "bound_matrix.m"
                                       "CCL_demo.m"
                                       "condi_match.m"
   Those three functions can realize the finding every pixel's bonds, connected-component-labeling, and 
checking whether two matrices match each other. By adjusting values of the threshold value, you will 
see different results.
   
   Step3: After finishing running this section, you will see resulting pictures.
                                       "binary_stars.png"
                                       "shrink_stars.png"
and two histograms. Also, you will get the number of stars.


6. Run the section "PCB analysis".
	This is the main program for the algorithms in problem 2_part(c).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
          The important statements are
                                       fid=fopen('PCB.raw','r');
   
   Step2: While running this section, you may notice tow MATLAB files.
	                               "bound_matrix.m"
                                       "CCL_demo.m"
                                       "condi_match.m"
   Those three functions can realize the finding every pixel's bonds, connected-component-labeling, and 
checking whether two matrices match each other. By adjusting values of the threshold value, you will 
see different results.
   
   Step3: After finishing running this section, you will see resulting pictures.
                                       "binar_PCB.png"
                                       "rever_PCB.png"
                                       "shrink1_PCB.png"
                                       "thin_PCB_original.png"
                                       "thin2_PCB.png"
Also, you will get the numbers of holes and pathways.



7. Run the section "Defect detection".
	This is the main program for the algorithms in problem 2_part(d).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
          The important statements are
                                       fid=fopen('Geartooth.raw','r');
   
   Step2: While running this section, you may notice tow MATLAB files.
	                               "bound_matrix.m"
                                       "CCL_demo.m"
                                       "condi_match.m"
   Those three functions can realize the finding every pixel's bonds, connected-component-labeling, and 
checking whether two matrices match each other. By adjusting values of the threshold value, you will 
see different results.
   
   Step3: After finishing running this section, you will see resulting pictures.
                                       "binar_Geartooth.png"
                                       "rever_Geartooth.png"
                                       "shrink1_Geartooth.png"
                                       "step1_img.png"
                                       "step3_img.png"
                                       "step4_img.png"
Also, you will get the value of radius and positions of the center, intact teeth, and missing teeth.



8. Run the program and follow the instructions. 
  

/////////////////////////////////////////////////////////////////////////////
Other notes:

   I guarantee you that in my computer I can see all the pictures in my report and plot required figures.
If you cannot run my program successfully, please let me know and I will come to your office to show you.
   
   Thank you very much!

Sincerely,
Yao Fu

/////////////////////////////////////////////////////////////////////////////

