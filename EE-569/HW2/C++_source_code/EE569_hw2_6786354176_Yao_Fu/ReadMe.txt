# EE569 Homework Assignment #2
# Date: February 16, 2020
# Name: Yao Fu
# USC ID: 6786354176
# email: yaof@usc.edu
#
# Software: Visual Studio 2019
# Operating System: Windows 10
========================================================================
    CONSOLE APPLICATION : [EE569_hw2_6786354176_Yao Fu] Project Overview
========================================================================

This file contains a summary of what I will find in each of the files that
make up my [EE569_hw1_6786354176_Yao Fu] application.

Steps:

1. Open "EE569_hw2_6786354176_Yao Fu.cpp.sln".
	This is the solution for the project.


2. Open "EE569_hw2_6786354176_Yao Fu_prob1_a.cpp".
	This is the main program for the algorithms in problem 1_part(a).
     
   Step1: You need to read images into image data matrix by putting images into the same file directory.
	
          The important statements are
                        const char* name_input1 = "Dogs.raw";
	                read_image(ImageDataRGB1, name_input1);
	                const char* name_input2 = "Gallery.raw";
	                read_image(ImageDataRGB2, name_input2);
   
   Step2: After running the program, you may have several raw data files.
	
	                              cconst char* name_gray1 = "GrayImage1.raw";
	                              save_image(ImageDataGray1, name_gray1);
	                              const char* name_gray2 = "GrayImage2.raw";
	                              save_image(ImageDataGray2, name_gray2);

	                              const char* name_Sobx1 = "SobFilImage_x1.raw";
	                              save_image(SobFil_Image1_x, name_Sobx1);
	                              const char* name_Soby1 = "SobFilImage_y1.raw";
	                              save_image(SobFil_Image1_y, name_Soby1);

	                              const char* name_Sobx2 = "SobFilImage_x2.raw";
	                              save_image(SobFil_Image2_x, name_Sobx2);
	                              const char* name_Soby2 = "SobFilImage_y2.raw";
	                              save_image(SobFil_Image2_y, name_Soby2);

	                              const char* name_NorGr1 = "NorGrImage_1.raw";
	                              save_image(NorGrad_Image1, name_NorGr1);
	                              const char* name_NorGr2 = "NorGrImage_2.raw";
	                              save_image(NorGrad_Image2, name_NorGr2);

	                              const char* name_Thresh1 = "ThreshImage_1.raw";
	                              save_image(Thresh_Image1, name_Thresh1);
	                              const char* name_Thresh2 = "ThreshImage_2.raw";
	                              save_image(Thresh_Image2, name_Thresh2);

   Step3: After getting raw data files, you need to "Open EE569_hw2_6786354176_Yao_Fu_Matlab.m"
to use Matlab to see resulting pictures. 
   
   Step4:Open "EE569_hw2_6786354176_Yao Fu_prob1_b.cpp" to use OpenCV source code to implement Canny detector.

   Step5:Open "edgesDemo.m" to use MATLAB source code to implement SE detector.

   Step6:Open "edgesEvallmg12.m" to use MATLAB source code to calculate recall and precision.


3.   Open “EE569_hw2_6786354176_Yao Fu_prob2_a.cpp”.
	This is the main program for the algorithms in problem 2_part(a).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
	
          The important statements are
                                       const char* name_input = "LightHouse.raw";
	                               read_image(ImageDataGray, name_input);
   
   Step2: After running the program, you may have several raw data files.
                                       
                                       const char* name_fix_thresh = "FixThresh_Image.raw";
	                               save_image(FixThresh_Image, name_fix_thresh);

	                               const char* name_random_thresh = "RandomThresh_Image.raw";
	                               save_image(RandomThresh_Image, name_random_thresh);

	                               const char* name_DithMatrix_2 = "DithMatrix_2_Image.raw";
	                               save_image(DithMatrix_2_Image, name_DithMatrix_2);
	                               const char* name_DithMatrix_8 = "DithMatrix_8_Image.raw";
	                               save_image(DithMatrix_8_Image, name_DithMatrix_8);
	                               const char* name_DithMatrix_32 = "DithMatrix_32_Image.raw";
	                               save_image(DithMatrix_32_Image, name_DithMatrix_32);
	
   Step3: After getting raw data files, you need to "Open EE569_hw2_6786354176_Yao_Fu_Matlab.m"
to use Matlab to see resulting pictures.


4.   Open “EE569_hw2_6786354176_Yao Fu_prob2_b.cpp”.
	This is the main program for the algorithms in problem 2_part(b).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
	
          The important statements are
                                       const char* name_input = "LightHouse.raw";
	                               read_image(ImageDataGray, name_input);
   
   Step2: After running the program, you may have several raw data files.
                                       
	                               const char* name_fs_thresh = "FS_ErrDif_Image.raw";
	                               save_image(FS_Image, name_fs_thresh);

	                               const char* name_jjn_thresh = "JJN_ErrDif_Image.raw";
	                               save_image(JJN_Image, name_jjn_thresh);

	                               const char* name_stucki_thresh = "Stucki_ErrDif_Image.raw";
	                               save_image(Stucki_Image, name_stucki_thresh);
	
   Step3: After getting raw data files, you need to "Open EE569_hw2_6786354176_Yao_Fu_Matlab.m"
to use Matlab to see resulting pictures.


5.   Open “EE569_hw2_6786354176_Yao Fu_prob2_c.cpp”.
	This is the main program for the algorithms in problem 2_part(c).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
	
          The important statements are
               	                        const char* name_input = "Rose.raw";
	                                read_image(ImageDataRGB, name_input);

   Step2: After running the program, you may have several raw data files.
                                       
	                               const char* name_SED_thresh = "Sep_ErrDif_Image.raw";
	                               save_image(SED_ImageDataRGB, name_SED_thresh);

	                               const char* name_MBVQ_thresh = "MBVQ_ErrDif_Image.raw";
	                               save_image(MBVQ_ImageDataRGB, name_MBVQ_thresh);
	
   Step3: After getting raw data files, you need to "Open EE569_hw2_6786354176_Yao_Fu_Matlab.m"
to use Matlab to see resulting pictures.


6. All the header files and the source files have already been included in the project. 


7. Run the program and follow the instructions. 
  

/////////////////////////////////////////////////////////////////////////////
Other notes:

   I guarantee you that in my computer I can see all the pictures in my report and plot required figures.
If you cannot run my program successfully, please let me know and I will come to your office to show you.
   
   Thank you very much!

/////////////////////////////////////////////////////////////////////////////

