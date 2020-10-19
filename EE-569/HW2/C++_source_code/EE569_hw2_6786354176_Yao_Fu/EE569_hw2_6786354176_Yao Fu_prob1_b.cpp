// EE569 Homework Assignment #2 Problem1_b
// Submission Date: February 16, 2020
// Name : Yao Fu
// USC ID : 6786354176
// Email : yaof@usc.edu

#include <opencv.hpp> 
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>

using namespace std;
using namespace cv; 

//[variables]
Mat src, src_gray;
Mat dst, detected_edges;


const int max_lowThreshold = 100;

const int kernel_size = 3;
const char* window_name = "Edge Map";



static void CannyThreshold(int, void*)
{
    /// Reduce noise with a kernel 3x3
    blur(src, detected_edges, Size(3, 3));

    /// Canny detector
    const int ratio = 3;
    int lowThreshold = 65;
    Canny(detected_edges, detected_edges, lowThreshold, lowThreshold * ratio, kernel_size);

    /// Using Canny's output as a mask, we display our result
    dst = Scalar::all(0);

    //![copyto]
    src.copyTo(dst, detected_edges);
    //![copyto]

    //![display]
    imshow(window_name, dst);
    //![display]
}


int main(int argc, char** argv)
{
    CommandLineParser parser(argc, argv, "{@input | fruits.jpg | input image}");
    src = imread("GrayImage2.jpg", IMREAD_GRAYSCALE); // Load an image

    if (src.empty())
    {
        cout << "Could not open or find the image!\n" << endl;
        cout << "Usage: " << argv[0] << " <Input image>" << endl;
        return -1;
    }

    // Create a matrix of the same type and size as src (for dst)
    dst.create(src.size(), src.type());

    //Create_window
    namedWindow(window_name, WINDOW_AUTOSIZE);

    // Show the image
    CannyThreshold(0, 0);

    // Save the image
    imwrite("CannyImage2_3_65.png", dst);
    
    // Wait until user exit program by pressing a key
    waitKey(0);

    return 0;
}