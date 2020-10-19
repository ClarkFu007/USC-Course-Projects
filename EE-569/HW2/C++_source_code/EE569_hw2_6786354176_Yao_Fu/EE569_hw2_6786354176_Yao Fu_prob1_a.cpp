// EE569 Homework Assignment #2 Problem1_a
// Submission Date: February 16, 2020
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


// Part(1): Define file variables

constexpr auto Byte_Per_Pixel_Gray = 1; // 1 byte=8 bits;
constexpr auto Byte_Per_Pixel_RGB = 3;
constexpr auto Height = 321;          // The two images' height;
constexpr auto Width = 481;           // The two images' width;
constexpr auto KernelSize = 3;        // The Kernel's size;
constexpr auto ext_num = 3;           // The number of extension


// Part(2): My functions's prototypes

void read_image(unsigned char image_data[][Width][Byte_Per_Pixel_RGB], const char* str);
          // Read images 
void conver_rgb_gray(unsigned char RGB_data[][Width][Byte_Per_Pixel_RGB],
	                 unsigned char Gray_data[][Width][Byte_Per_Pixel_Gray]);
	      // RGB to grayscale conversion
void ext_bound(unsigned char image_data[][Width][Byte_Per_Pixel_Gray],
	           unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray]);
          // Extend the boundaries of images
void corr_demo(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	           unsigned char filtering_im[][Width][Byte_Per_Pixel_Gray],
	           float kernel[][KernelSize]);
          // The function to implement the correllation
void nor_grad_mag_map(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	                  unsigned char nor_grad_mag_im[][Width][Byte_Per_Pixel_Gray],
	                  float kernel_x[][KernelSize], float kernel_y[][KernelSize]);
	      // Calculate the normalized gradient magnitude map
void thresh_demo(unsigned char image_data1[][Width][Byte_Per_Pixel_Gray],
	             unsigned char image_data2[][Width][Byte_Per_Pixel_Gray],
	             int threshold);
          // Threshold the normalized gradient magnitude map
void save_image(unsigned char output_image[][Width][Byte_Per_Pixel_Gray], const char* str);
          // Save the resulting images 
unsigned char pixel_round(float temp_pixel);
          // To handle situations when intensity > 255 or intensity < 0


// Part(3): Allocate image data array

unsigned char ImageDataRGB1[Height][Width][Byte_Per_Pixel_RGB];    // RGB for "Dogs"
unsigned char ImageDataRGB2[Height][Width][Byte_Per_Pixel_RGB];    // RGB for "Gallery"

unsigned char ImageDataGray1[Height][Width][Byte_Per_Pixel_Gray];  // Gray for "Dogs"
unsigned char ImageDataGray2[Height][Width][Byte_Per_Pixel_Gray];  // Gray for "Gallery"

unsigned char ext_ImageData1[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];
unsigned char ext_ImageData2[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];

unsigned char SobFil_Image1_x[Height][Width][Byte_Per_Pixel_Gray];  // X-gradient for "Dogs"
unsigned char SobFil_Image2_x[Height][Width][Byte_Per_Pixel_Gray];  // X-gradient for "Gallery"
unsigned char SobFil_Image1_y[Height][Width][Byte_Per_Pixel_Gray];  // Y-gradient for "Dogs"
unsigned char SobFil_Image2_y[Height][Width][Byte_Per_Pixel_Gray];  // Y-gradient for "Gallery"

unsigned char NorGrad_Image1[Height][Width][Byte_Per_Pixel_Gray];   // Normalized gradient for "Dogs"
unsigned char NorGrad_Image2[Height][Width][Byte_Per_Pixel_Gray];   // Normalized gradient for "Gallery"

unsigned char Thresh_Image1[Height][Width][Byte_Per_Pixel_Gray];    // The final edge map for "Dogs"
unsigned char Thresh_Image2[Height][Width][Byte_Per_Pixel_Gray];    // The final edge map for "Gallery"


// Part(4): The main function

int main()
{
	float Sobel_x[KernelSize][KernelSize] =
	{
		{-1,  0,  1},
		{-2,  0,  2},
		{-1,  0,  1}
	};
	float Sobel_y[KernelSize][KernelSize] =
	{
		{ 1,  2,  1},
		{ 0,  0,  0},
		{-1, -2, -1}
	};
	int Thresh_Value1 = floor(255 * 0.34);   // The threshold for the best visual performance for "Dogs"
	int Thresh_Value2 = floor(255 * 0.22);   // The threshold for the best visual performance for "Gallery"

	// Read image into image data matrix
	const char* name_input1 = "Dogs.raw";
	read_image(ImageDataRGB1, name_input1);
	const char* name_input2 = "Gallery.raw";
	read_image(ImageDataRGB2, name_input2);

	// RGB to grayscale conversion
	conver_rgb_gray(ImageDataRGB1, ImageDataGray1);
	conver_rgb_gray(ImageDataRGB2, ImageDataGray2);

	// Extend the boundary of the image
	ext_bound(ImageDataGray1, ext_ImageData1);
	ext_bound(ImageDataGray2, ext_ImageData2);

	// Use the Sobel_x kernel
	corr_demo(ext_ImageData1, SobFil_Image1_x, Sobel_x);
	corr_demo(ext_ImageData2, SobFil_Image2_x, Sobel_x);
	// Use the Sobel_y kernel
	corr_demo(ext_ImageData1, SobFil_Image1_y, Sobel_y);
	corr_demo(ext_ImageData2, SobFil_Image2_y, Sobel_y);
	
	// Calculate the normalized gradient magnitude map
	nor_grad_mag_map(ext_ImageData1, NorGrad_Image1, Sobel_x, Sobel_y);
	nor_grad_mag_map(ext_ImageData2, NorGrad_Image2, Sobel_x, Sobel_y);
	
	// Threshold the normalized gradient magnitude map
	thresh_demo(NorGrad_Image1, Thresh_Image1, Thresh_Value1);
	thresh_demo(NorGrad_Image2, Thresh_Image2, Thresh_Value2);

	// Write image data from image data matrix
	const char* name_gray1 = "GrayImage1.raw";
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

	return 0;
}


// // Part(5): My functions's definitions
void read_image(unsigned char image_data[][Width][Byte_Per_Pixel_RGB], const char* str)
{
	using namespace std;

	FILE* file;
	// Check if image is grayscale or color
	if (Byte_Per_Pixel_Gray == 1)
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
	fread(image_data, sizeof(unsigned char), Height * Width * Byte_Per_Pixel_RGB, file);
	fclose(file);
}


void save_image(unsigned char output_image[][Width][Byte_Per_Pixel_Gray], const char* str)
{
	using namespace std;

	FILE* file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_image, sizeof(unsigned char), Height * Width * Byte_Per_Pixel_Gray, file);
	fclose(file);
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


void conver_rgb_gray(unsigned char image_rgb_data[][Width][Byte_Per_Pixel_RGB],
	                 unsigned char image_gray_data[][Width][Byte_Per_Pixel_Gray])
{
	using namespace std;

	float temp_rgb_image[Height][Width][Byte_Per_Pixel_RGB] = { 0 };
	float temp_gray_image[Height][Width][Byte_Per_Pixel_Gray] = { 0 };
	
	// Convert unsigned char into float
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)		
		{
			temp_rgb_image[m][n][0] = (float)image_rgb_data[m][n][0];
			temp_rgb_image[m][n][1] = (float)image_rgb_data[m][n][1];
			temp_rgb_image[m][n][2] = (float)image_rgb_data[m][n][2];
		}
	// Convert RGB into grayscale 
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			temp_gray_image[m][n][0] = 0.2989 * temp_rgb_image[m][n][0] +
				                       0.5870 * temp_rgb_image[m][n][1] +
				                       0.1140 * temp_rgb_image[m][n][2];
		}
	// Convert float into unsigned char
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			image_gray_data[m][n][0] = pixel_round(temp_gray_image[m][n][0]); 
		}
}


void ext_bound(unsigned char image_data[][Width][Byte_Per_Pixel_Gray],
	           unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray])
{
	using namespace std;

	// Copy the center
	for (int m = ext_num; m < ext_num + Height; m++)
		for (int n = ext_num; n < ext_num + Width; n++)
			ext_image_data[m][n][Byte_Per_Pixel_Gray - 1] =
			image_data[m - ext_num][n - ext_num][Byte_Per_Pixel_Gray - 1];
	// Reflect the two vertical parts
	int index_l = 2 * ext_num - 1;
	int index_r = 2 * (Width + 2 * ext_num - 1) - index_l;
	for (int m = ext_num; m < ext_num + Height; m++)
		for (int n = 0; n < ext_num; n++)
		{
			ext_image_data[m][n][Byte_Per_Pixel_Gray - 1] =
				image_data[m - ext_num][index_l - n - ext_num][Byte_Per_Pixel_Gray - 1];
			ext_image_data[m][Width + 2 * ext_num - 1 - n][Byte_Per_Pixel_Gray - 1] =
				image_data[m - ext_num][index_r -
				(Width + 2 * ext_num - 1 - n) - ext_num][Byte_Per_Pixel_Gray - 1];
		}
	// Reflect the two horizontal parts
	int index_u = 2 * ext_num - 1;
	int index_b = 2 * (Height + 2 * ext_num - 1) - index_u;
	for (int m = 0; m < ext_num; m++)
		for (int n = ext_num; n < ext_num + Width; n++)
		{
			ext_image_data[m][n][Byte_Per_Pixel_Gray - 1] =
				image_data[index_u - m - ext_num][n - ext_num][Byte_Per_Pixel_Gray - 1];
			ext_image_data[Height + 2 * ext_num - 1 - m][n][Byte_Per_Pixel_Gray - 1] =
				image_data[index_b - (Height + 2 * ext_num - 1 - m) - ext_num]
				[n - ext_num][Byte_Per_Pixel_Gray - 1];
		}
	// Reflect the four corners
	for (int m = 0; m < ext_num; m++)
		for (int n = 0; n < ext_num; n++)
		{
			ext_image_data[m][n][Byte_Per_Pixel_Gray - 1] = ext_image_data[index_u - m][n][Byte_Per_Pixel_Gray - 1];
			ext_image_data[m + Height + ext_num][n][Byte_Per_Pixel_Gray - 1] =
				ext_image_data[index_b - (m + Height + ext_num)][n][Byte_Per_Pixel_Gray - 1];
			ext_image_data[m][n + Width + ext_num][Byte_Per_Pixel_Gray - 1] =
				ext_image_data[m][index_r - (n + Width + ext_num)][Byte_Per_Pixel_Gray - 1];
			ext_image_data[m + Height + ext_num][n + Width + ext_num][Byte_Per_Pixel_Gray - 1] =
				ext_image_data[index_b - (m + Height + ext_num)][n + Width + ext_num]
				[Byte_Per_Pixel_Gray - 1];
		}
}


void corr_demo(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	           unsigned char filtering_im[][Width][Byte_Per_Pixel_Gray],
	           float kernel[][KernelSize])
{
	using namespace std;

	float temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray] = { 0 };
	float temp_fil_image[Height][Width][Byte_Per_Pixel_Gray] = { 0 };
	int index_i = (KernelSize - 1) / 2;
	int index_j = (KernelSize - 1) / 2;

	// Change the data type from "unsigned char" to "float" 
	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{
			temp_ext_image[m][n][0] = (float)ext_image_data[m][n][0];
		}

	// Implement the correlation
	for (int m = ext_num; m < Height + ext_num; m++)
		for (int n = ext_num; n < Width + ext_num; n++)
		{
			for (int i = -index_i; i <= index_i; i++)
				for (int j = -index_j; j <= index_j; j++)
				{
					temp_fil_image[m - ext_num][n - ext_num][0] =
						temp_fil_image[m - ext_num][n - ext_num][0] +
							kernel[i + index_i][j + index_j] * temp_ext_image[m + i][n + j][0];
				}
			temp_fil_image[m - ext_num][n - ext_num][0] =
				abs(temp_fil_image[m - ext_num][n - ext_num][0]);
		}
	double max_pixel = 0;
    double min_pixel = 0;

    // Find maximum and minimum values of pixels
    for (int m = 0; m < Height; m++)
	    for (int n = 0; n < Width; n++)
	{
		max_pixel = max((double)temp_fil_image[m][n][0], max_pixel);
		min_pixel = min((double)temp_fil_image[m][n][0], min_pixel);
	}

    // Normalize the images
    for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			temp_fil_image[m][n][0] = 255 * (temp_fil_image[m][n][0] - (float)min_pixel) /
				((float)max_pixel - (float)min_pixel);
	    }

	// Get final results
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			filtering_im[m][n][0] = pixel_round(temp_fil_image[m][n][0]);
		}
}


void nor_grad_mag_map(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	                  unsigned char nor_grad_mag_im[][Width][Byte_Per_Pixel_Gray],
	                  float kernel_x[][KernelSize], float kernel_y[][KernelSize])
{
	using namespace std;

	float temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray] = { 0 };
	float temp_fil_x_image[Height][Width][Byte_Per_Pixel_Gray] = { 0 };
	float temp_fil_y_image[Height][Width][Byte_Per_Pixel_Gray] = { 0 };
	float temp_fil_mag_image[Height][Width][Byte_Per_Pixel_Gray] = { 0 };
	int index_i = (KernelSize - 1) / 2;
	int index_j = (KernelSize - 1) / 2;

	// Change the data type from "unsigned char" to "float" 
	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{
			temp_ext_image[m][n][0] = (float)ext_image_data[m][n][0];
		}

	// Implement the correlation in X and Y direction seperately
	for (int m = ext_num; m < Height + ext_num; m++)
		for (int n = ext_num; n < Width + ext_num; n++)
		{
			for (int i = -index_i; i <= index_i; i++)
				for (int j = -index_j; j <= index_j; j++)
				{
					temp_fil_x_image[m - ext_num][n - ext_num][0] =
						temp_fil_x_image[m - ext_num][n - ext_num][0] +
						kernel_x[i + index_i][j + index_j] * temp_ext_image[m + i][n + j][0];
					temp_fil_y_image[m - ext_num][n - ext_num][0] =
						temp_fil_y_image[m - ext_num][n - ext_num][0] +
						kernel_y[i + index_i][j + index_j] * temp_ext_image[m + i][n + j][0];
				}
			temp_fil_x_image[m - ext_num][n - ext_num][0] =
				abs(temp_fil_x_image[m - ext_num][n - ext_num][0]);
			temp_fil_y_image[m - ext_num][n - ext_num][0] =
				abs(temp_fil_y_image[m - ext_num][n - ext_num][0]);
		}

	// Get the normalized gradient magnitude 
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			temp_fil_mag_image[m][n][0] = (float)sqrt((pow((double)temp_fil_x_image[m][n][0], 2) +
				pow((double)temp_fil_y_image[m][n][0], 2))); 
		}

	// Find maximum and minimum values of pixels
	double max_pixel = 0;                                                                                                                                                        
	double min_pixel = 0;
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			max_pixel = max((double)temp_fil_mag_image[m][n][0], max_pixel);
			min_pixel = min((double)temp_fil_mag_image[m][n][0], min_pixel);
		}

	// Normalize the images
	for (int m = 0; m < Height; m++)
		for (int n =0; n < Width; n++)
		{
			temp_fil_mag_image[m][n][0] = 255 * (temp_fil_mag_image[m][n][0] - (float)min_pixel) /
				((float)max_pixel - (float)min_pixel);
		}

	 // Get final results
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			nor_grad_mag_im[m][n][0] = pixel_round(temp_fil_mag_image[m][n][0]);
		}
		 
}


void thresh_demo(unsigned char image_data1[][Width][Byte_Per_Pixel_Gray], 
	             unsigned char image_data2[][Width][Byte_Per_Pixel_Gray],
	             int threshold)
{
	using namespace std;

	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			if (image_data1[m][n][0] >= threshold)
				image_data2[m][n][0] = 255;
			else
				image_data2[m][n][0] = 0;
		}
}






