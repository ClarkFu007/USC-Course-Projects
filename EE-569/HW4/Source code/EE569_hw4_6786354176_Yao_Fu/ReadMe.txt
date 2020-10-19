# EE569 Homework Assignment #4
# Date: March 22, 2020
# Name: Yao Fu
# USC ID: 6786354176
# email: yaof@usc.edu
#
# Software: MATLAB 2019b
# Operating System: Windows 10
========================================================================
    CONSOLE APPLICATION : [EE569_hw4_6786354176_Yao Fu] Project Overview
========================================================================

This file contains a summary of what I will find in each of the files that
make up my [EE569_hw4_6786354176_Yao Fu] application.

Steps:

1. Open "EE569_hw4_6786354176_Yao_Fu_Matlab.m".
	This is the main part for the project.


2. Run the section "Problem 1: Texture Analysis and Segmentation".
	This is the main program for the algorithms in problem 1.
     
   Step1: You need to read images into image data matrix by putting images into the same file directory.	
          The important statements are
                        % blanket
                        fid=fopen('blanket1.raw','r');blanket1=fread(fid,[128,128]);fclose(fid);
                        blanket1=blanket1';imwrite(uint8(blanket1),'blanket1.png');

                        fid=fopen('blanket2.raw','r');blanket2=fread(fid,[128,128]);fclose(fid);
                        blanket2=blanket2';imwrite(uint8(blanket2),'blanket2.png');

                        fid=fopen('blanket3.raw','r');blanket3=fread(fid,[128,128]);fclose(fid);
                        blanket3=blanket3';imwrite(uint8(blanket3),'blanket3.png');

                        fid=fopen('blanket4.raw','r');blanket4=fread(fid,[128,128]);fclose(fid);
                        blanket4=blanket4';imwrite(uint8(blanket4),'blanket4.png');

                        fid=fopen('blanket5.raw','r');blanket5=fread(fid,[128,128]);fclose(fid);
                        blanket5=blanket5';imwrite(uint8(blanket5),'blanket5.png');

                        fid=fopen('blanket6.raw','r');blanket6=fread(fid,[128,128]);fclose(fid);
                        blanket6=blanket6';imwrite(uint8(blanket6),'blanket6.png');

                        fid=fopen('blanket7.raw','r');blanket7=fread(fid,[128,128]);fclose(fid);
                        blanket7=blanket7';imwrite(uint8(blanket7),'blanket7.png');

                        fid=fopen('blanket8.raw','r');blanket8=fread(fid,[128,128]);fclose(fid);
                        blanket8=blanket8';imwrite(uint8(blanket8),'blanket8.png');

                        fid=fopen('blanket9.raw','r');blanket9=fread(fid,[128,128]);fclose(fid);
                        blanket9=blanket9';imwrite(uint8(blanket9),'blanket9.png');

 
                        % brick
                        fid=fopen('brick1.raw','r');brick1=fread(fid,[128,128]);fclose(fid);
                        brick1=brick1';imwrite(uint8(brick1),'brick1.png')

                        fid=fopen('brick2.raw','r');brick2=fread(fid,[128,128]);fclose(fid);
                        brick2=brick2';imwrite(uint8(brick2),'brick2.png')

                        fid=fopen('brick3.raw','r');brick3=fread(fid,[128,128]);fclose(fid);
                        brick3=brick3';imwrite(uint8(brick3),'brick3.png');

                        fid=fopen('brick4.raw','r');brick4=fread(fid,[128,128]);fclose(fid);
                        brick4=brick4';imwrite(uint8(brick4),'brick4.png');

                        fid=fopen('brick5.raw','r');brick5=fread(fid,[128,128]);fclose(fid);
                        brick5=brick5';imwrite(uint8(brick5),'brick5.png');

                        fid=fopen('brick6.raw','r');brick6=fread(fid,[128,128]);fclose(fid);
                        brick6=brick6';imwrite(uint8(brick6),'brick6.png');

                        fid=fopen('brick7.raw','r');brick7=fread(fid,[128,128]);fclose(fid);
                        brick7=brick7';imwrite(uint8(brick7),'brick7.png');

                        fid=fopen('brick8.raw','r');brick8=fread(fid,[128,128]);fclose(fid);
                        brick8=brick8';imwrite(uint8(brick8),'brick8.png');

                        fid=fopen('brick9.raw','r');brick9=fread(fid,[128,128]);fclose(fid);
                        brick9=brick9';imwrite(uint8(brick9),'brick9.png');


                        % grass
                        fid=fopen('grass1.raw','r');grass1=fread(fid,[128,128]);fclose(fid);
                        grass1=grass1';imwrite(uint8(grass1),'grass1.png');

                        fid=fopen('grass2.raw','r');grass2=fread(fid,[128,128]);fclose(fid);
                        grass2=grass2';imwrite(uint8(grass2),'grass2.png');

                        fid=fopen('grass3.raw','r');grass3=fread(fid,[128,128]);fclose(fid);
                        grass3=grass3';imwrite(uint8(grass3),'grass3.png');

                        fid=fopen('grass4.raw','r');grass4=fread(fid,[128,128]);fclose(fid);
                        grass4=grass4';imwrite(uint8(grass4),'grass4.png');

                        fid=fopen('grass5.raw','r');grass5=fread(fid,[128,128]);fclose(fid);
                        grass5=grass5';imwrite(uint8(grass5),'grass5.png');

                        fid=fopen('grass6.raw','r');grass6=fread(fid,[128,128]);fclose(fid);
                        grass6=grass6';imwrite(uint8(grass6),'grass6.png');

                        fid=fopen('grass7.raw','r');grass7=fread(fid,[128,128]);fclose(fid);
                        grass7=grass7';imwrite(uint8(grass7),'grass7.png');

                        fid=fopen('grass8.raw','r');grass8=fread(fid,[128,128]);fclose(fid);
                        grass8=grass8';imwrite(uint8(grass8),'grass8.png');

                        fid=fopen('grass9.raw','r');grass9=fread(fid,[128,128]);fclose(fid);
                        grass9=grass9';imwrite(uint8(grass9),'grass9.png');


                        % rice
                        fid=fopen('rice1.raw','r');rice1=fread(fid,[128,128]);fclose(fid);
                        rice1=rice1';imwrite(uint8(rice1),'rice1.png');

                        fid=fopen('rice2.raw','r');rice2=fread(fid,[128,128]);fclose(fid);
                        rice2=rice2';imwrite(uint8(rice2),'rice2.png');

                        fid=fopen('rice3.raw','r');rice3=fread(fid,[128,128]);fclose(fid);
                        rice3=rice3';imwrite(uint8(rice3),'rice3.png');

                        fid=fopen('rice4.raw','r');rice4=fread(fid,[128,128]);fclose(fid);
                        rice4=rice4';imwrite(uint8(rice4),'rice4.png');

                        fid=fopen('rice5.raw','r');rice5=fread(fid,[128,128]);fclose(fid);
                        rice5=rice5';imwrite(uint8(rice5),'rice5.png');

                        fid=fopen('rice6.raw','r');rice6=fread(fid,[128,128]);fclose(fid);
                        rice6=rice6';imwrite(uint8(rice6),'rice6.png');

                        fid=fopen('rice7.raw','r');rice7=fread(fid,[128,128]);fclose(fid);
                        rice7=rice7';imwrite(uint8(rice7),'rice7.png');

                        fid=fopen('rice8.raw','r');rice8=fread(fid,[128,128]);fclose(fid);
                        rice8=rice8';imwrite(uint8(rice8),'rice8.png');

                        fid=fopen('rice9.raw','r');rice9=fread(fid,[128,128]);fclose(fid);
                        rice9=rice9';imwrite(uint8(rice9),'rice9.png');
 
                        % test
                        fid=fopen('1.raw','r');test1=fread(fid,[128,128]);fclose(fid);
                        test1=test1';imwrite(uint8(test1),'1.png');

                        fid=fopen('2.raw','r');test2=fread(fid,[128,128]);fclose(fid);
                        test2=test2';imwrite(uint8(test2),'2.png');

                        fid=fopen('3.raw','r');test3=fread(fid,[128,128]);fclose(fid);
                        test3=test3';imwrite(uint8(test3),'3.png');

                        fid=fopen('4.raw','r');test4=fread(fid,[128,128]);fclose(fid);
                        test4=test4';imwrite(uint8(test4),'4.png');

                        fid=fopen('5.raw','r');test5=fread(fid,[128,128]);fclose(fid);
                        test5=test5';imwrite(uint8(test5),'5.png');

                        fid=fopen('6.raw','r');test6=fread(fid,[128,128]);fclose(fid);
                        test6=test6';imwrite(uint8(test6),'6.png');

                        fid=fopen('7.raw','r');test7=fread(fid,[128,128]);fclose(fid);
                        test7=test7';imwrite(uint8(test7),'7.png');

                        fid=fopen('8.raw','r');test8=fread(fid,[128,128]);fclose(fid);
                        test8=test8';imwrite(uint8(test8),'8.png');

                        fid=fopen('9.raw','r');test9=fread(fid,[128,128]);fclose(fid);
                        test9=test9';imwrite(uint8(test9),'9.png');

                        fid=fopen('10.raw','r');test10=fread(fid,[128,128]);fclose(fid);
                        test10=test10';imwrite(uint8(test10),'10.png');

                        fid=fopen('11.raw','r');test11=fread(fid,[128,128]);fclose(fid);
                        test11=test11';imwrite(uint8(test11),'11.png');

                        fid=fopen('12.raw','r');test12=fread(fid,[128,128]);fclose(fid);
                        test12=test12';imwrite(uint8(test12),'12.png');
   
   Step2: While running this section, you may notice tow MATLAB files.
	                "operate_each_img.m"
                        "PCA_demo.m"
                        "PCA_demo_test.m"
                        "operate_each_img_new.m"

   Those three functions can realize the feature extraction in part(a), PCA for the train feature vectors, PCA for the test feature 
vectors and the feature extraction in part(c). Also, I wirte my own K-means algorithm and use built-in RF and SVM functions.

   Step3: After finishing running this section, you will see classification results shown in my report and resulting pictures. 
                        "The segmented result.png"
                        "The modified segmented result.png"
   

3. Run the section "Image Matching".
	This is the main program for the algorithms in problem 2_part(b).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
          The important statements are
                                      img_Husky1=imread('Husky_1.jpg');
                                      img_Husky2=imread('Husky_2.jpg');
                                      img_Husky3=imread('Husky_3.jpg');
                                      img_Puppy1=imread('Puppy_1.jpg');

   Step2: While running this section, you may notice tow MATLAB files.
	                               "vl_sift.m"
                                       "vl_ubcmatch.m"
                                       "img_match.m"
   Those three functions can realize finding SIFT points, matching SIFT points, and matching pictures respectively. 
   
   Step3: After finishing running this section, you will see resulting pictures and figures.


4. Run the section "Bag of Words".
	This is the main program for the algorithms in problem 2_part(c).

   Step1: You need to read images into image data matrix by putting images into the same file directory.
          The important statements are
                                      img_Husky1=imread('Husky_1.jpg');
                                      img_Husky2=imread('Husky_2.jpg');
                                      img_Husky3=imread('Husky_3.jpg');
                                      img_Puppy1=imread('Puppy_1.jpg');
   
   Step2: While running this section, you may notice tow MATLAB files.
	                               "vl_sift.m"
                                       "vl_ubcmatch.m"
                                       "img_match.m"
   Those three functions can realize finding SIFT points, matching SIFT points, and matching pictures respectively. 
Also, you will cheack the similarity between pictures to get relevant pictures.
   
   Step3: After finishing running this section, you will see resulting 4+3 histograms.



5. Run the program and follow the instructions. 
  

/////////////////////////////////////////////////////////////////////////////
Other notes:

   I guarantee you that in my computer I can see all the pictures in my report and plot required figures.
If you cannot run my program successfully, please let me know and I will come to your office to show you.
   
   Thank you very much!

Sincerely,
Yao Fu

/////////////////////////////////////////////////////////////////////////////

