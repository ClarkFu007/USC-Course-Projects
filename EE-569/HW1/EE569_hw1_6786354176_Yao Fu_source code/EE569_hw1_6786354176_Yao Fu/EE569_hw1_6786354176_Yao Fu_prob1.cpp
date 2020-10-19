// EE569 Homework Assignment #1 Problem_1
// Submission Date: January 28, 2020
// Name : Yao Fu
// USC ID : 6786354176
// Email : yaof@usc.edu

#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <sal.h> 
#include <math.h>
#include <algorithm>
#pragma warning(disable:4996)


// Define file variables
constexpr auto BYTE_PER_PIXEL_GRAY = 1;  // 1 byte=8 bits
constexpr auto BYTE_PER_PIXEL_RGB = 3;
constexpr auto Height_1ab = 532;         // The "Dog.raw" image's height
constexpr auto Width_1ab = 600;          // The "Dog.raw" image's width
constexpr auto Height_1c = 400;          // The "Toy.raw" image's height
constexpr auto Width_1c = 560;           // The "Toy.raw" image's width
constexpr auto ext_num = 5;              // The number of extension

// Pixel's structure
typedef struct pixel
{
	unsigned char intensity;             // The intensity value of each pixel
	int index;                           // The index value of each pixel
}p;
p R_Channel[Height_1c * Width_1c] = { 0 };
p G_Channel[Height_1c * Width_1c] = { 0 };
p B_Channel[Height_1c * Width_1c] = { 0 };
// A function to sort the pixels in terms of their intensity values
bool Compare(const p& pixel1, const p& pixel2)
{
	return pixel1.intensity < pixel2.intensity;
}

// My functions's prototypes
void ext_bound(unsigned char image_data[][Width_1ab][BYTE_PER_PIXEL_GRAY],
	           unsigned char ext_image_data[][Width_1ab + 2 * ext_num][BYTE_PER_PIXEL_GRAY]);
                   // Extend the boundaries of images
void bili_demo(unsigned char ext_image_data[][Width_1ab + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	           unsigned char bili_demo_image[][Width_1ab][BYTE_PER_PIXEL_RGB]);
                   // Bilinear Demosaicing
void MHC_demo(unsigned char ext_image_data[][Width_1ab + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	          unsigned char MHC_demo_image[][Width_1ab][BYTE_PER_PIXEL_RGB]);
                   // Malvar-He-Cutler (MHC) Demosaicing     
void im_hist(unsigned char image_data[][Width_1c][BYTE_PER_PIXEL_RGB], 
	         int channel_rgb_data[][3]);
                   // To plot the histograms of the red, green and blue channels of the original image  
void hist_maniA(unsigned char image_data[][Width_1c][BYTE_PER_PIXEL_RGB],
	            unsigned char img_equA[][Width_1c][BYTE_PER_PIXEL_RGB]);
                   // The method A: the transfer-function-based histogram equalization method

void hist_maniB(unsigned char image_data[],
	            unsigned char img_equB[]);
                   // The method B: the cumulative-probability-based histogram equalization method
unsigned char pixel_round(float temp_pixel);
                   // To handle situations when intensity > 255 or intensity < 0
void read_image_1ab(unsigned char image_data[][Width_1ab][BYTE_PER_PIXEL_GRAY], const char *str);
                   // Read the "Dog" image in part (a) and part (b) 
void read_image_1c_a(unsigned char image_data[][Width_1c][BYTE_PER_PIXEL_RGB], const char *str);
                   // Read the "Toy" image method A of part (c) to make raw data three-dimensional
void read_image_1c_b(unsigned char image_data[], const char* str);
                   // Read the "Toy" image method B of part (c) to make raw data one-dimensional
void save_image_1ab(unsigned char output_image[][Width_1ab][BYTE_PER_PIXEL_RGB], const char *str);
                   // Save the resulting "Dog" images in part (a) and part (b) 
void save_image_1c_a(unsigned char output_image[][Width_1c][BYTE_PER_PIXEL_RGB], const char* str);
                   // Read the "Toy" image method A of part (c) to make raw data three-dimensional
void save_image_1c_b(unsigned char output_image[], const char* str);
                   // Read the "Toy" image method A of part (c) to make raw data three-dimensional
void save_data_1c1(int output_data[][3], const char *str);
                   // Save data in to plot the histograms of the red, green and blue channels 
                   // of the original image
void save_data_1c2(unsigned char output_data[][3], const char* str);
                   // Save data in method A to plot transfer functions for each channel
                   // I will use data in Matlab to plot cumlative histograms for each channel in method B
int main()
{
	using namespace std;

	// Allocate image data array
	unsigned char ImageData_1ab[Height_1ab][Width_1ab][BYTE_PER_PIXEL_GRAY];
	unsigned char ext_ImageData[Height_1ab + 2 * ext_num][Width_1ab + 2 * ext_num][BYTE_PER_PIXEL_GRAY];
	unsigned char BiliDemoImage[Height_1ab][Width_1ab][BYTE_PER_PIXEL_RGB];
	unsigned char MHC_DemoImage[Height_1ab][Width_1ab][BYTE_PER_PIXEL_RGB];
	unsigned char ImageData_1c_a[Height_1c][Width_1c][BYTE_PER_PIXEL_RGB];
	unsigned char ImageData_1c_b[Height_1c * Width_1c * BYTE_PER_PIXEL_RGB];
	int ChannelRGB_Data[256][3] = { 0 };
	unsigned char EnhanA_RGB_Data[Height_1c][Width_1c][BYTE_PER_PIXEL_RGB];
	unsigned char EnhanB_RGB_Data[Height_1c * Width_1c * BYTE_PER_PIXEL_RGB];

	// Read image into image data matrix
	const char *name_1ab = "Dog.raw";
	read_image_1ab(ImageData_1ab, name_1ab);
	const char* name_1c = "Toy.raw";
	read_image_1c_a(ImageData_1c_a, name_1c);
	read_image_1c_b(ImageData_1c_b, name_1c);

	// Extend the boundary of the image
	ext_bound(ImageData_1ab,ext_ImageData);

	// Operate the bilinear demosaicing
	bili_demo(ext_ImageData,BiliDemoImage);

	// Operate the MHC demosaicing
	MHC_demo(ext_ImageData,MHC_DemoImage);

	// Write image data from image data matrix
	const char *name_1a = "Dog_rgb_bili.raw";
	save_image_1ab(MHC_DemoImage, name_1a);
	const char *name_1b = "Dog_rgb_MHC.raw";
	save_image_1ab(MHC_DemoImage, name_1b);

	// To plot the histograms of the red, green and blue channels of the original image  
	im_hist(ImageData_1c_a, ChannelRGB_Data);
	const char *name_1c1 = "Prob_1c1_data.raw";
	save_data_1c1(ChannelRGB_Data, name_1c1);
	
	// The method A: the transfer-function-based histogram equalization method
	hist_maniA(ImageData_1c_a, EnhanA_RGB_Data);
	const char* name_1cA = "EnhanA_RGB.raw";
	save_image_1c_a(EnhanA_RGB_Data, name_1cA);
	
	// The method B: the cumulative-probability-based histogram equalization method
	hist_maniB(ImageData_1c_b, EnhanB_RGB_Data);
	const char* name_1cB = "EnhanB_RGB.raw";
	save_image_1c_b(EnhanB_RGB_Data, name_1cB);

	return 0;
}


// My functions's definitions
void read_image_1ab(unsigned char image_data[][Width_1ab][BYTE_PER_PIXEL_GRAY], const char *str)
{
	using namespace std;

	FILE *file;
	// Check if image is grayscale or color
	if (BYTE_PER_PIXEL_GRAY == 1)
	{
		cout << "You image is gray-scale" << endl;
	}
	else
	{
		cout << "You input BytesPerPixel is wrong. Please input again!" << endl;
	}
	// Read images into image data matrix
	if (!(file = fopen(str, "rb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fread(image_data, sizeof(unsigned char), Height_1ab * Width_1ab * BYTE_PER_PIXEL_GRAY, file);
	fclose(file);
}


void read_image_1c_a(unsigned char image_data[][Width_1c][BYTE_PER_PIXEL_RGB], const char* str)
{
	using namespace std;

	FILE* file;
	// Check if image is grayscale or color
	if (BYTE_PER_PIXEL_RGB == 3)
	{
		cout << "You image is color-scale" << endl;
	}
	else
	{
		cout << "You input BytesPerPixel is wrong. Please input again!" << endl;
	}
	// Read images into image data matrix
	if (!(file = fopen(str, "rb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fread(image_data, sizeof(unsigned char), Height_1c * Width_1c * BYTE_PER_PIXEL_RGB, file);
	fclose(file);
}


void read_image_1c_b(unsigned char image_data[], const char* str)
{
	using namespace std;

	FILE* file;
	// Read images into image data matrix
	if (!(file = fopen(str, "rb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fread(image_data, sizeof(unsigned char), Height_1c * Width_1c * BYTE_PER_PIXEL_RGB, file);
	fclose(file);
}


void save_image_1ab(unsigned char output_image[][Width_1ab][BYTE_PER_PIXEL_RGB], const char *str)
{
	using namespace std;

	FILE *file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_image, sizeof(unsigned char), Height_1ab * Width_1ab * BYTE_PER_PIXEL_RGB, file);
	fclose(file);
}


void save_image_1c_a(unsigned char output_image[][Width_1c][BYTE_PER_PIXEL_RGB], const char* str)
{
	using namespace std;

	FILE* file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_image, sizeof(unsigned char), Height_1c * Width_1c * BYTE_PER_PIXEL_RGB, file);
	fclose(file);
}


void save_image_1c_b(unsigned char output_image[], const char* str)
{
	using namespace std;

	FILE* file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_image, sizeof(unsigned char), Height_1c * Width_1c * BYTE_PER_PIXEL_RGB, file);
	fclose(file);
}


// Save data
void save_data_1c1(int output_data[][3], const char* str)
{
	using namespace std;

	FILE* file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_data, sizeof(int), 256 * 3, file);
	fclose(file);
}


void save_data_1c2(unsigned char output_data[][3], const char* str)
{
	using namespace std;

	FILE* file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_data, sizeof(unsigned char), 256 * 3, file);
	fclose(file);
}


void ext_bound(unsigned char image_data[][Width_1ab][BYTE_PER_PIXEL_GRAY],
	           unsigned char ext_image_data[][Width_1ab + 2 * ext_num][BYTE_PER_PIXEL_GRAY])
{
	using namespace std;

	// Copy the center
	for (int m = ext_num; m < ext_num + Height_1ab; m++)
		for (int n = ext_num; n < ext_num + Width_1ab; n++)
			ext_image_data[m][n][BYTE_PER_PIXEL_GRAY-1] = 
			                  image_data[m - ext_num][n - ext_num][BYTE_PER_PIXEL_GRAY-1];
	// Reflect the two vertical parts
	int index_l = 2 * ext_num - 1;
	int index_r = 2 * (Width_1ab+2*ext_num-1)-index_l;
	for (int m = ext_num; m < ext_num + Height_1ab; m++)
		for (int n = 0; n < ext_num; n++)
		   {
			ext_image_data[m][n][BYTE_PER_PIXEL_GRAY-1] = 
				              image_data[m - ext_num][index_l - n - ext_num][BYTE_PER_PIXEL_GRAY-1];
			ext_image_data[m][Width_1ab+2*ext_num-1-n][BYTE_PER_PIXEL_GRAY-1] = 
				              image_data[m - ext_num][index_r -
				                    (Width_1ab + 2 * ext_num - 1 - n) - ext_num][BYTE_PER_PIXEL_GRAY-1];
		   }
	// Reflect the two horizontal parts
	int index_u = 2 * ext_num - 1;
	int index_b = 2 * (Height_1ab+2*ext_num-1)-index_u;
	for (int m = 0; m < ext_num ; m++)
		for (int n = ext_num; n < ext_num+Width_1ab; n++)
		{
			ext_image_data[m][n][BYTE_PER_PIXEL_GRAY-1] = 
				              image_data[index_u - m - ext_num][n-ext_num][BYTE_PER_PIXEL_GRAY-1];
			ext_image_data[Height_1ab + 2 * ext_num - 1 - m][n][BYTE_PER_PIXEL_GRAY-1] = 
				              image_data[index_b -(Height_1ab + 2 * ext_num - 1 - m) - ext_num]
				                        [n-ext_num][BYTE_PER_PIXEL_GRAY-1];
		}
	// Reflect the four corners
	for (int m = 0; m < ext_num; m++)
		for (int n = 0; n < ext_num; n++)
		{
			ext_image_data[m][n][BYTE_PER_PIXEL_GRAY-1] = ext_image_data[index_u - m][n][BYTE_PER_PIXEL_GRAY-1];
			ext_image_data[m+Height_1ab+ext_num][n][BYTE_PER_PIXEL_GRAY-1] =
				             ext_image_data[index_b-(m + Height_1ab + ext_num)][n][BYTE_PER_PIXEL_GRAY-1];
			ext_image_data[m][n+Width_1ab+ext_num][BYTE_PER_PIXEL_GRAY-1] = 
				             ext_image_data[m][index_r - (n + Width_1ab + ext_num)][BYTE_PER_PIXEL_GRAY-1];
			ext_image_data[m + Height_1ab + ext_num][n + Width_1ab + ext_num][BYTE_PER_PIXEL_GRAY-1] =
				             ext_image_data[index_b - (m + Height_1ab + ext_num)][n + Width_1ab + ext_num]
				                                                             [BYTE_PER_PIXEL_GRAY-1];
		}
}


void bili_demo(unsigned char ext_image_data[][Width_1ab + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	           unsigned char bili_demo_image[][Width_1ab][BYTE_PER_PIXEL_RGB])
{
	using namespace std;

	float temp_value;
	for (int m = 0; m < Height_1ab; m++)
		for (int n = 0; n < Width_1ab; n+=2)
		{ 
			if (m % 2 == 0)
			{
				// G's values in G
				temp_value = (float)ext_image_data[m + ext_num][n + ext_num][0];
				bili_demo_image[m][n][1] = pixel_round(temp_value);
				// R's values in G
				temp_value = (float)(ext_image_data[m + ext_num][n + ext_num - 1][0]+
					                        ext_image_data[m + ext_num][n + ext_num + 1][0]) / 2;
				bili_demo_image[m][n][0] = pixel_round(temp_value);
				// B's values in G
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + ext_num][0] +
					                        ext_image_data[m + ext_num + 1][n + ext_num][0]) / 2;
				bili_demo_image[m][n][2] = pixel_round(temp_value);
				// R's values in R
				temp_value = (float)ext_image_data[m + ext_num][n + ext_num][0];
				bili_demo_image[m][n + 1][0] = pixel_round(temp_value);
				// B's values in R
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + 1 + ext_num - 1][0] +
					                            ext_image_data[m + ext_num - 1][n + 1 + ext_num + 1][0] +
					                            ext_image_data[m + ext_num + 1][n + 1 + ext_num - 1][0] +
					                            ext_image_data[m + ext_num + 1][n + 1 + ext_num + 1][0]) / 4;
				bili_demo_image[m][n + 1][2] = pixel_round(temp_value);
				// G's values in R
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + 1 + ext_num][0] +
					                            ext_image_data[m + ext_num + 1][n + 1 + ext_num][0] +
					                            ext_image_data[m + ext_num][n + 1 + ext_num - 1][0] +
					                            ext_image_data[m + ext_num][n + 1 + ext_num + 1][0]) / 4;
				bili_demo_image[m][n + 1][1] = pixel_round(temp_value);
			}
			else
			{
				// B's values in B
				temp_value = (float)ext_image_data[m + ext_num][n + ext_num][0];
				bili_demo_image[m][n][2] = pixel_round(temp_value);
				// G's values in B
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + ext_num][0] +
					                        ext_image_data[m + ext_num + 1][n + ext_num][0] +
					                        ext_image_data[m + ext_num][n + ext_num - 1][0] +
					                        ext_image_data[m + ext_num][n + ext_num + 1][0]) / 4;
				bili_demo_image[m][n][1] = pixel_round(temp_value);
				// R's values in B
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + ext_num - 1][0] +
					                        ext_image_data[m + ext_num - 1][n + ext_num + 1][0] +
					                        ext_image_data[m + ext_num + 1][n + ext_num - 1][0] +
					                        ext_image_data[m + ext_num + 1][n + ext_num + 1][0]) / 4;
				bili_demo_image[m][n][0] = pixel_round(temp_value);
				// G's values in G
				temp_value = (float)ext_image_data[m + ext_num][n + ext_num][0];
				bili_demo_image[m][n][1] = pixel_round(temp_value);
				// R's values in G
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + 1 + ext_num][0] +
					                          ext_image_data[m + ext_num + 1][n + 1 + ext_num][0]) / 2;
				bili_demo_image[m][n + 1][0] = pixel_round(temp_value);
				// B's values in G
				temp_value = (float)(ext_image_data[m + ext_num][n + 1 + ext_num - 1][0] +
					                          ext_image_data[m + ext_num][n + 1 + ext_num + 1][0]) / 2;
				bili_demo_image[m][n + 1][2] = pixel_round(temp_value);
			}
        }
}


void MHC_demo(unsigned char ext_image_data[][Width_1ab + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	          unsigned char MHC_demo_image[][Width_1ab][BYTE_PER_PIXEL_RGB])
{
	using namespace std;

	float temp_value;
	for (int m = 0; m < Height_1ab; m++)
		for (int n = 0; n < Width_1ab; n += 2)
		{
			if (m % 2 == 0)
			{
				// G's values in G
				temp_value = (float) ext_image_data[m + ext_num][n + ext_num][0];
				MHC_demo_image[m][n][1] = pixel_round(temp_value);
				// R's values in G
				temp_value = (float)(ext_image_data[m + ext_num][n + ext_num - 1][0] +
					ext_image_data[m + ext_num][n + ext_num + 1][0]) / 2 +
					 (0.625 * 5 * ext_image_data[m + ext_num][n + ext_num][0]  -
						 0.625 * ext_image_data[m + ext_num - 1][n + ext_num - 1][0] +
						 0.625 * 0.5 * ext_image_data[m + ext_num - 2][n + ext_num][0] -
						 0.625 * ext_image_data[m + ext_num - 1][n + ext_num + 1][0] -
						 0.625 * ext_image_data[m + ext_num][n + ext_num + 2][0] -
						 0.625 * ext_image_data[m + ext_num + 1][n + ext_num + 1][0] +
						 0.625 * 0.5 * ext_image_data[m + ext_num + 2][n + ext_num][0] -
						 0.625 * ext_image_data[m + ext_num + 1][n + ext_num - 1][0] -
						 0.625 * ext_image_data[m + ext_num][n + ext_num - 2][0]);
				MHC_demo_image[m][n][0] = pixel_round(temp_value);
				// B's values in G
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + ext_num][0] +
					ext_image_data[m + ext_num + 1][n + ext_num][0]) / 2 +
					 (0.625 * 5 * ext_image_data[m + ext_num][n + ext_num][0]  -
						 0.625 * ext_image_data[m + ext_num - 1][n + ext_num - 1][0] -
						 0.625 * ext_image_data[m + ext_num - 2][n + ext_num][0] -
						 0.625 * ext_image_data[m + ext_num - 1][n + ext_num + 1][0] +
						 0.625 * 0.5 * ext_image_data[m + ext_num][n + ext_num + 2][0] -
						 0.625 * ext_image_data[m + ext_num + 1][n + ext_num + 1][0] -
						 0.625 * ext_image_data[m + ext_num + 2][n + ext_num][0] -
						 0.625 * ext_image_data[m + ext_num + 1][n + ext_num - 1][0] +
						 0.625 * 0.5 * ext_image_data[m + ext_num][n + ext_num - 2][0]);
				MHC_demo_image[m][n][2] = pixel_round(temp_value);
				// R's values in R
				temp_value = (float)ext_image_data[m + ext_num][n + ext_num][0];
				MHC_demo_image[m][n + 1][0] = pixel_round(temp_value);
				// B's values in R
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + 1 + ext_num - 1][0] +
					ext_image_data[m + ext_num - 1][n + 1 + ext_num + 1][0] +
					ext_image_data[m + ext_num + 1][n + 1 + ext_num - 1][0] +
					ext_image_data[m + ext_num + 1][n + 1 + ext_num + 1][0]) / 4 +
					 (0.75 * 6 * ext_image_data[m + ext_num][n + ext_num][0] -
						 0.75 * 1.5 * ext_image_data[m + ext_num - 2][n + ext_num][0] -
						 0.75 * 1.5 * ext_image_data[m + ext_num + 2][n + ext_num][0] -
						 0.75 * 1.5 * ext_image_data[m + ext_num][n + ext_num - 2][0] -
						 0.75 * 1.5 * ext_image_data[m + ext_num][n + ext_num + 2][0]);
				MHC_demo_image[m][n + 1][2] = pixel_round(temp_value);
				// G's values in R
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + 1 + ext_num][0] +
					ext_image_data[m + ext_num + 1][n + 1 + ext_num][0] +
					ext_image_data[m + ext_num][n + 1 + ext_num - 1][0] +
					ext_image_data[m + ext_num][n + 1 + ext_num + 1][0]) / 4 +
					 (0.5 * ext_image_data[m + ext_num][n + 1 + ext_num][0]
						-  0.25 * 0.5 * ext_image_data[m + ext_num - 2][n + 1 + ext_num][0] -
						   0.25 * 0.5 * ext_image_data[m + ext_num + 2][n + 1 + ext_num][0] -
						   0.25 * 0.5 * ext_image_data[m + ext_num][n + 1 + ext_num - 2][0] -
						   0.25 * 0.5 * ext_image_data[m + ext_num][n + 1 + ext_num + 2][0]);
				MHC_demo_image[m][n + 1][1] = pixel_round(temp_value);
			}
			else
			{
				// B's values in B
				temp_value = (float)ext_image_data[m + ext_num][n + ext_num][0];
				MHC_demo_image[m][n][2] = pixel_round(temp_value);
				// G's values in B
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + ext_num][0] +
					ext_image_data[m + ext_num + 1][n + ext_num][0] +
					ext_image_data[m + ext_num][n + ext_num - 1][0] +
					ext_image_data[m + ext_num][n + ext_num + 1][0]) / 4 +
					 (0.5 * ext_image_data[m + ext_num][n + ext_num][0]
						- 0.25 * 0.5 * ext_image_data[m + ext_num - 2][n + ext_num][0] -
						  0.25 * 0.5 * ext_image_data[m + ext_num + 2][n + ext_num][0] -
						  0.25 * 0.5 * ext_image_data[m + ext_num][n + ext_num - 2][0] -
						  0.25 * 0.5 * ext_image_data[m + ext_num][n + ext_num + 2][0]);
				MHC_demo_image[m][n][1] = pixel_round(temp_value);
				// R's values in B
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + ext_num - 1][0] +
					ext_image_data[m + ext_num - 1][n + ext_num + 1][0] +
					ext_image_data[m + ext_num + 1][n + ext_num - 1][0] +
					ext_image_data[m + ext_num + 1][n + ext_num + 1][0]) / 4 +
					 (0.75 * 6 * ext_image_data[m + ext_num][n + ext_num][0] -
						 0.75 * 1.5 * ext_image_data[m + ext_num - 2][n + ext_num][0] -
						 0.75 * 1.5 * ext_image_data[m + ext_num + 2][n + ext_num][0] -
						 0.75 * 1.5 * ext_image_data[m + ext_num][n + ext_num - 2][0] -
						 0.75 * 1.5 * ext_image_data[m + ext_num][n + ext_num + 2][0]);
				MHC_demo_image[m][n][0] = pixel_round(temp_value);
				// G's values in G
				temp_value = (float)ext_image_data[m + ext_num][n + ext_num][0];
				MHC_demo_image[m][n][1] = pixel_round(temp_value);
				// R's values in G
				temp_value = (float)(ext_image_data[m + ext_num - 1][n + 1 + ext_num][0] +
					ext_image_data[m + ext_num + 1][n + 1 + ext_num][0]) / 2 +
					 (0.625 * 5 * ext_image_data[m + ext_num][n + 1 + ext_num][0] -
						 0.625 * ext_image_data[m + ext_num][n + 1 + ext_num - 2][0] -
						 0.625 * ext_image_data[m + ext_num - 1][n + 1 + ext_num - 1][0] +
						 0.625 * 0.5 * ext_image_data[m + ext_num - 2][n + 1 + ext_num][0] -
						 0.625 * ext_image_data[m + ext_num - 1][n + 1 + ext_num + 1][0] -
						 0.625 * ext_image_data[m + ext_num][n + 1 + ext_num + 2][0] -
						 0.625 * ext_image_data[m + ext_num + 1][n + 1 + ext_num + 1][0] +
						 0.625 * 0.5 * ext_image_data[m + ext_num + 2][n + 1 + ext_num][0] -
						 0.625 * ext_image_data[m + ext_num + 1][n + 1 + ext_num - 1][0]);
				MHC_demo_image[m][n + 1][0] = pixel_round(temp_value);
				// B's values in G
				temp_value = (float)(ext_image_data[m + ext_num][n + 1 + ext_num - 1][0] +
					ext_image_data[m + ext_num][n + 1 + ext_num + 1][0]) / 2 +
					 (0.625 * 5 * ext_image_data[m + ext_num][n + 1 + ext_num][0] -
						 0.625 * ext_image_data[m + ext_num][n + 1 + ext_num - 2][0] -
						 0.625 * ext_image_data[m + ext_num - 1][n + 1 + ext_num - 1][0] +
						 0.625 * 0.5 * ext_image_data[m + ext_num][n + 1 + ext_num - 2][0] -
						 0.625 * ext_image_data[m + ext_num - 1][n + 1 + ext_num + 1][0] -
						 0.625 * ext_image_data[m + ext_num][n + 1 + ext_num + 2][0] -
						 0.625 * ext_image_data[m + ext_num + 1][n + 1 + ext_num + 1][0] +
						 0.625 * 0.5 * ext_image_data[m + ext_num][n + 1 + ext_num + 2][0] -
						 0.625 * ext_image_data[m + ext_num + 1][n + 1 + ext_num - 1][0]);
				MHC_demo_image[m][n + 1][2] = pixel_round(temp_value);
			}
		}
}


unsigned char pixel_round(float temp_pixel)
{
	if (temp_pixel >= 255)
		return 255;
	else if (temp_pixel <= 0)
		return 0;
	else
		return (unsigned char)temp_pixel;
}


void im_hist(unsigned char image_data[][Width_1c][BYTE_PER_PIXEL_RGB],
	         int channel_rgb_data[][3])
{
	using namespace std;

	for (int m = 0; m < Height_1c ; m++)
		for (int n = 0; n < Width_1c ; n++)
		{
			unsigned char temp0 = image_data[m][n][0];
			unsigned char temp1 = image_data[m][n][1];
			unsigned char temp2 = image_data[m][n][2];
			channel_rgb_data[temp0][0] ++;     // R channel
			channel_rgb_data[temp1][1] ++;     // G channel
			channel_rgb_data[temp2][2] ++;     // B channel
		}
}


void hist_maniA(unsigned char image_data[][Width_1c][BYTE_PER_PIXEL_RGB], 
	            unsigned char img_equA[][Width_1c][BYTE_PER_PIXEL_RGB])
{
	using namespace std;
	
	// Step1: Obtain the histograms
	float nor_channel_rgb_data[256][3] = { 0 };
	for (int m = 0; m < Height_1c; m++)
		for (int n = 0; n < Width_1c; n++)
		{
			unsigned char temp0 = image_data[m][n][0];
			unsigned char temp1 = image_data[m][n][1];
			unsigned char temp2 = image_data[m][n][2];
			nor_channel_rgb_data[temp0][0] ++;     // R channel
			nor_channel_rgb_data[temp1][1] ++;     // G channel
			nor_channel_rgb_data[temp2][2] ++;     // B channel
		}
	// Step2: Calculate the normalized probability histograms
	int total = Height_1c * Width_1c;
	for (int i = 0; i < 256; i++)
	{
		nor_channel_rgb_data[i][0] /= total;
		nor_channel_rgb_data[i][1] /= total;
		nor_channel_rgb_data[i][2] /= total;
	}
	// Step3: Calculate the Cumulative Distribution Probability
	float cdf_channel_rgb[256][3] = { 0 };
	cdf_channel_rgb[0][0] = nor_channel_rgb_data[0][0];
	cdf_channel_rgb[0][1] = nor_channel_rgb_data[0][1];
	cdf_channel_rgb[0][2] = nor_channel_rgb_data[0][2];
	for (int i = 1; i < 256; i++)
	{
		cdf_channel_rgb[i][0] = cdf_channel_rgb[i - 1][0] + nor_channel_rgb_data[i][0];
		cdf_channel_rgb[i][1] = cdf_channel_rgb[i - 1][1] + nor_channel_rgb_data[i][1];
		cdf_channel_rgb[i][2] = cdf_channel_rgb[i - 1][2] + nor_channel_rgb_data[i][2];
	}
	// Step4: Create the mapping table
	unsigned char equi_channel_rgb[256][3] = { 0 };
	for (int i = 0; i < 256; i++)
	{
		equi_channel_rgb[i][0] = floor(255 * cdf_channel_rgb[i][0]);
		equi_channel_rgb[i][1] = floor(255 * cdf_channel_rgb[i][1]);
		equi_channel_rgb[i][2] = floor(255 * cdf_channel_rgb[i][2]);
	}
	const char* name_1c1_data = "Prob_1c1_data.raw";
	save_data_1c2(equi_channel_rgb, name_1c1_data);
	// Step5: Get the enhanced image using the Method A
	for (int m = 0; m < Height_1c; m++)
		for (int n = 0; n < Width_1c; n++)
			for (int i = 0; i < 256; i++)
			{
				if (image_data[m][n][0] == i)
				{
					img_equA[m][n][0] = equi_channel_rgb[i][0];
				}
				if (image_data[m][n][1] == i)
				{
					img_equA[m][n][1] = equi_channel_rgb[i][1];
				}
				if (image_data[m][n][2] == i)
				{
					img_equA[m][n][2] = equi_channel_rgb[i][2];
				}
			}
}


void hist_maniB(unsigned char image_data[],
	unsigned char img_equB[])

{
	using namespace std;

	// Step1: Find out how many pixels go into each bucket ?
	int num = 400 * 560 / 256;

	// Step2: Assign pixels in the original image to corresponding buckets
	for (int i = 0; i < Height_1c * Width_1c * BYTE_PER_PIXEL_RGB; i = i + 3)
	{
		R_Channel[i / 3].intensity = image_data[i];
		R_Channel[i / 3].index = i;


		G_Channel[(i - 1) / 3].intensity = image_data[i + 1];
		G_Channel[(i - 1) / 3].index = i + 1;


		B_Channel[(i - 2) / 3].intensity = image_data[i + 2];
		B_Channel[(i - 2) / 3].index = i + 2;
	}
	// Sort the pixels according to their intensity values
	sort(R_Channel, R_Channel + Height_1c * Width_1c, Compare);
	sort(G_Channel, G_Channel + Height_1c * Width_1c, Compare);
	sort(B_Channel, B_Channel + Height_1c * Width_1c, Compare);
	int pixel_value = 0;
	for (int i = 0; i < Height_1c * Width_1c; i++)
	{
		R_Channel[i].intensity = pixel_value;

		G_Channel[i].intensity = pixel_value;

		B_Channel[i].intensity = pixel_value;

		if (i % num == num - 1)
			pixel_value++;
	}
	int location_r; int location_g; int location_b;
	for (int i = 0; i < Height_1c * Width_1c; i++)
	{
		location_r = R_Channel[i].index;
		img_equB[location_r] = R_Channel[i].intensity;

		location_g = G_Channel[i].index;
		img_equB[location_g] = G_Channel[i].intensity;

		location_b = B_Channel[i].index;
		img_equB[location_b] = B_Channel[i].intensity;
	}
}






