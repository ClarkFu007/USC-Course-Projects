# EE569 Homework Assignment #1
# Date: January 28, 2020
# Name: Yao Fu
# USC ID: 6786354176
# email: yaof@usc.edu
#
# Software: Visual Studio 2019
# Operating System: Windows 10
========================================================================
    CONSOLE APPLICATION : [EE569_hw1_6786354176_Yao Fu] Project Overview
========================================================================

This file contains a summary of what I will find in each of the files that
make up my [EE569_hw1_6786354176_Yao Fu] application.

Steps:

1. Open "EE569_hw1_6786354176_Yao Fu.cpp.sln".
	This is the solution for the project.


2. Open "EE569_hw1_6786354176_Yao Fu_prob1.cpp".
	This is the main program for the algorithms in problem 1.
     
   Step1: You need to read images into image data matrix by putting images into the same file directory.
	
          The important statements are
                                      "const char *name_1ab = "Dog.raw";
	                               read_image_1ab(ImageData_1ab, name_1ab);
                                       const char* name_1c = "Toy.raw";
	                               read_image_1c_a(ImageData_1c_a, name_1c);
	                               read_image_1c_b(ImageData_1c_b, name_1c);".
   
   Step2: After running the program, you may have several raw data files.
	
	                              const char *name_1a = "Dog_rgb_bili.raw";
	                              const char *name_1b = "Dog_rgb_MHC.raw";
	
	// To plot the histograms of the red, green and blue channels of the original image  
	                              const char *name_1c1 = "Prob_1c1_data.raw";
	// The method A: the transfer-function-based histogram equalization method
	                              const char* name_1cA = "EnhanA_RGB.raw";
	// The method B: the cumulative-probability-based histogram equalization method
                                      const char* name_1cB = "EnhanB_RGB.raw";

   Step3: After getting raw data files, you need to "Open EE569_hw1_6786354176_Yao_Fu_Matlab.m"
to use Matlab to see resulting pictures. Also, I use Matlab to draw histograms of Prob1-part(c)-1, 
transfer functions of Prob1-part(c)-2, and cumulative histograms of Prob1-part(c)-3.


3.   Open “EE569_hw1_6786354176_Yao Fu_prob2.cpp”.
	This is the main program for the algorithms in problem 2.

   Step1: You need to read images into image data matrix by putting images into the same file directory.
	
          The important statements are
                                      "const char* name_input1 = "Corn_noisy.raw";
	                               read_image(InputImageData, name_input1);
	                               const char* name_input2 = "Corn_gray.raw";
	                               read_image(ImageData, name_input2);".
   
   Step2: After running the program, you may have several raw data files.
                                       const char* name_noise = "Noise_data.raw";
	                               const char * name_Uni = "UniFil_Image.raw";
                                       const char* name_Gau1 = "GauFil1_Image.raw";
                                       const char* name_Gau2 = "GauFil2_Image.raw";
                                       const char* name_Bil = "BilFil_Image.raw";
	
   Step3: After getting raw data files, you need to "Open EE569_hw1_6786354176_Yao_Fu_Matlab.m"
to use Matlab to see resulting pictures. Also, I use Matlab to draw PDF of Noise data. 

   Step4：Open "EE569_hw1_6786354176_Yao_Fu_Matlab_nlm.m" to run the NLM filtering algorithm by putting 
images into the same file directory.
	
   Step5：Open the file "EE569_hw1_6786354176_Yao Fu_Matlab_bm3d" and then open "bm3d_demo_grayscale.m"
 to run the BM3D transform filtering algorithm putting images into the same file directory.


4. All the header files and the source files have already been included in the project. 


5. Run the program and follow the instructions. 
  

/////////////////////////////////////////////////////////////////////////////
Other notes:

   I guarantee you that in my computer I can see all the pictures in my report and plot required figures.
But I need to say that I only use Matlab to see pictures. Someone tells me that some raw-data files can be
be read by Matlab very well but fails to be read by other Image Viewing Softwares. But in my project, I haven't
download other Image Viewing Softwares.
   
   If you cannot run my program successfully, please let me know and I will come to your office to show you.
   
   Thank you very much!

/////////////////////////////////////////////////////////////////////////////

