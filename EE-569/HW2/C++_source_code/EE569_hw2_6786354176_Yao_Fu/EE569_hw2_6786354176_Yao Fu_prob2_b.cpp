// EE569 Homework Assignment #2 Problem2_b 
// Submission Date: February 16, 2020
// Name : Yao Fu
// USC ID : 6786354176
// Email : yaof@usc.edu

#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <sal.h> 
#include <math.h>
#pragma warning(disable:4996)


// Define file variables
constexpr auto Byte_Per_Pixel_Gray = 1; // 1 byte=8 bits
constexpr auto Byte_Per_Pixel_RGB = 3;
constexpr auto Height = 500;           // The "LightHouse" image's height
constexpr auto Width = 750;            // The "LightHouse" image's width
constexpr auto KernelSize1 = 3;        // The Kernel's size of the Floyd-Steinberg's error diffusion
constexpr auto KernelSize2 = 5;        // The Kernel's size of the JJN's and Stucki's error diffusion
constexpr auto ext_num = 6;            // The number of extension

// My functions's prototypes
void read_image(unsigned char image_data[][Width][Byte_Per_Pixel_Gray], const char* str);
// Read images 
void ext_bound(unsigned char image_data[][Width][Byte_Per_Pixel_Gray],
	           unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray]);
// Extend the boundaries of images
void fixed_thresh_demo(float image_data1[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	                   float image_data2[][Width + 2 * ext_num][Byte_Per_Pixel_Gray]);
// Binarize images
void corr_demo_1(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	             unsigned char filtering_im[][Width][Byte_Per_Pixel_Gray],
	             float kernel_r[][KernelSize1], float kernel_l[][KernelSize1], float sum);
void corr_demo_2(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	             unsigned char filtering_im[][Width][Byte_Per_Pixel_Gray],
	             float kernel_r[][KernelSize2], float kernel_l[][KernelSize2], float sum);
// Two functions to implement the correllation for half-toning with error diffusion
void save_image(unsigned char output_image[][Width][Byte_Per_Pixel_Gray], const char* str);
// Save the resulting images 
float pixel_round(float temp_pixel);
// Handle the single pixel when it's greater than 1 or less than 0
float pixel_thresh(float temp_pixel);
// Threshold the single pixel 

// Allocate image data array
unsigned char ImageDataGray[Height][Width][Byte_Per_Pixel_Gray];
unsigned char ext_ImageData[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];

unsigned char FS_Image[Height][Width][Byte_Per_Pixel_Gray];
unsigned char JJN_Image[Height][Width][Byte_Per_Pixel_Gray];
unsigned char Stucki_Image[Height][Width][Byte_Per_Pixel_Gray];


int main()
{
	float FS_Matrix_R[KernelSize1][KernelSize1] =
	{
		{0, 0, 0},
		{0, 0, 7},
		{3, 5, 1}
	};
	float FS_Matrix_L[KernelSize1][KernelSize1] =
	{
		{0, 0, 0},
		{7, 0, 0},
		{1, 5, 3}
	};

	float JJN_Matrix_R[KernelSize2][KernelSize2] =
	{
		{0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0},
		{0, 0, 0, 7, 5},
		{1, 3, 5, 3, 1},
		{3, 5, 7, 5, 3}
	};
	float JJN_Matrix_L[KernelSize2][KernelSize2] =
	{
		{0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0},
		{7, 5, 0, 0, 0},
		{1, 3, 5, 3, 1},
		{3, 5, 7, 5, 3}
	};
	float Stucki_Matrix_R[KernelSize2][KernelSize2] =
	{
		{0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0},
		{0, 0, 0, 8, 4},
		{1, 2, 4, 2, 1},
		{2, 4, 8, 4, 2}
	};
	float Stucki_Matrix_L[KernelSize2][KernelSize2] =
	{
		{0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0},
		{4, 8, 0, 0, 0},
		{1, 2, 4, 2, 1},
		{2, 4, 8, 4, 2}
	};

	// Read image into image data matrix
	const char* name_input = "LightHouse.raw";
	read_image(ImageDataGray, name_input);

	// Extend the boundary of the image
	ext_bound(ImageDataGray, ext_ImageData);

	// Implement the correllation to realize Error Diffusion
	corr_demo_1(ext_ImageData, FS_Image, FS_Matrix_R, FS_Matrix_L, 16);
	corr_demo_2(ext_ImageData, JJN_Image, JJN_Matrix_R, JJN_Matrix_L, 48);
	corr_demo_2(ext_ImageData, Stucki_Image, Stucki_Matrix_R, Stucki_Matrix_L, 42);

	// Write image data from image data matrix

	const char* name_fs_thresh = "FS_ErrDif_Image.raw";
	save_image(FS_Image, name_fs_thresh);

	const char* name_jjn_thresh = "JJN_ErrDif_Image.raw";
	save_image(JJN_Image, name_jjn_thresh);

	const char* name_stucki_thresh = "Stucki_ErrDif_Image.raw";
	save_image(Stucki_Image, name_stucki_thresh);

	return 0;
}


// My functions's definitions
void read_image(unsigned char image_data[][Width][Byte_Per_Pixel_Gray], const char* str)
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
	fread(image_data, sizeof(unsigned char), Height * Width * Byte_Per_Pixel_Gray, file);
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
			ext_image_data[m][n][Byte_Per_Pixel_Gray - 1] = 0;
			ext_image_data[m][Width + 2 * ext_num - 1 - n][Byte_Per_Pixel_Gray - 1] = 0;
		}
	// Reflect the two horizontal parts
	int index_u = 2 * ext_num - 1;
	int index_b = 2 * (Height + 2 * ext_num - 1) - index_u;
	for (int m = 0; m < ext_num; m++)
		for (int n = ext_num; n < ext_num + Width; n++)
		{
			ext_image_data[m][n][Byte_Per_Pixel_Gray - 1] = 0;
			ext_image_data[Height + 2 * ext_num - 1 - m][n][Byte_Per_Pixel_Gray - 1] = 0;
		}
	// Reflect the four corners
	for (int m = 0; m < ext_num; m++)
		for (int n = 0; n < ext_num; n++)
		{
			ext_image_data[m][n][Byte_Per_Pixel_Gray - 1] = 0;
			ext_image_data[m + Height + ext_num][n][Byte_Per_Pixel_Gray - 1] = 0;
			ext_image_data[m][n + Width + ext_num][Byte_Per_Pixel_Gray - 1] = 0;
			ext_image_data[m + Height + ext_num][n + Width + ext_num][Byte_Per_Pixel_Gray - 1] = 0;
		}
}


void fixed_thresh_demo(float image_data1[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	                   float image_data2[][Width + 2 * ext_num][Byte_Per_Pixel_Gray])
{
	using namespace std;

	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{
			if (image_data1[m][n][0] >= 0.5)
				image_data2[m][n][0] = 1;
			else
				image_data2[m][n][0] = 0;
		}
}


float pixel_round(float temp_pixel)
{
	if (temp_pixel >= 1)
		return 1;
	else if (temp_pixel <= 0)
		return 0;
	else
		return temp_pixel;
}

float pixel_thresh(float temp_pixel)
{
	if (temp_pixel >= 0.5)
		return 1;
	else
		return 0;
}


void corr_demo_1(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	             unsigned char filtering_im[][Width][Byte_Per_Pixel_Gray],
	             float kernel_r[][KernelSize1], float kernel_l[][KernelSize1], float sum)
{
	using namespace std;

	float temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray] = { 0 };
	float binary_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray] = { 0 };
	float binary_value = 0;
	float quan_error = 0;
	int index_i = (KernelSize1 - 1) / 2;
	int index_j = (KernelSize1 - 1) / 2;
	int k_i = 0;
	int k_j = 0;
	// Initialize a temporary image from the original image
	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
			temp_ext_image[m][n][0] = (float)ext_image_data[m][n][0] / 255;

	// Get the binarized image
	fixed_thresh_demo(temp_ext_image, binary_image);

	// Diffuse error forward using the serpentine parsing
	for (int m = ext_num; m < Height + ext_num; m++)
	{
		if (m % 2 == 0)
		{
			for (int n = ext_num; n < Width + ext_num; n++)
			{
				temp_ext_image[m][n][0] = pixel_round(temp_ext_image[m][n][0]);
				binary_value = pixel_thresh(temp_ext_image[m][n][0]);
				// Compute the quantization error
				quan_error = temp_ext_image[m][n][0] - binary_value;

				for (int i = -index_i; i <= index_i; i++)
					for (int j = -index_j; j <= index_j; j++)
					{
						k_i = i + index_i;
						k_j = j + index_j;
						// Distribute the error to "future" pixels
						temp_ext_image[m + i][n + j][0] =
							temp_ext_image[m + i][n + j][0] +
							kernel_r[k_i][k_j] * quan_error / sum;
					}
			}
		}
		else
		{
			for (int n = Width + ext_num - 1; n >= ext_num; n = n - 1)
			{
				temp_ext_image[m][n][0] = pixel_round(temp_ext_image[m][n][0]);
				binary_value = pixel_thresh(temp_ext_image[m][n][0]);
				// Compute the quantization error
				quan_error = temp_ext_image[m][n][0] - binary_value;

				for (int i = -index_i; i <= index_i; i++)
					for (int j = -index_j; j <= index_j; j++)
					{
						k_i = i + index_i;
						k_j = j + index_j;
						// Distribute the error to "future" pixels
						temp_ext_image[m + i][n + j][0] =
							temp_ext_image[m + i][n + j][0] +
							kernel_l[k_i][k_j] * quan_error / sum;
					}
			}
		}
	}

	for (int m = ext_num; m < Height + ext_num; m++)
		for (int n = ext_num; n < Width + ext_num; n++)
		{
			if (temp_ext_image[m][n][0] >= 1)
				temp_ext_image[m][n][0] = 1;
			else if (temp_ext_image[m][n][0] <= 0)
				temp_ext_image[m][n][0] = 0;
			else
				continue;
		}

	// Get the binarized image
	fixed_thresh_demo(temp_ext_image, binary_image);
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
			filtering_im[m][n][0] = (unsigned char)255 * binary_image[m + ext_num][n + ext_num][0];
}


void corr_demo_2(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	             unsigned char filtering_im[][Width][Byte_Per_Pixel_Gray],
	             float kernel_r[][KernelSize2], float kernel_l[][KernelSize2], float sum)
{
	using namespace std;

	float temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray] = { 0 };
	float binary_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray] = { 0 };
	int index_i = (KernelSize2 - 1) / 2;
	int index_j = (KernelSize2 - 1) / 2;
	float binary_value = 0;
	float quan_error = 0;

	int k_i = 0;
	int k_j = 0;
	// Initialize a temporary image from the original image
	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
			temp_ext_image[m][n][0] = (float)ext_image_data[m][n][0] / 255;

	// Get the binarized image
	fixed_thresh_demo(temp_ext_image, binary_image);

	// Diffuse error forward using the serpentine parsing
	for (int m = ext_num; m < Height + ext_num; m++)
	{
		if (m % 2 == 0)
		{
			for (int n = ext_num; n < Width + ext_num; n++)
			{
				temp_ext_image[m][n][0] = pixel_round(temp_ext_image[m][n][0]);
				binary_value = pixel_thresh(temp_ext_image[m][n][0]);
				// Compute the quantization error
				quan_error = temp_ext_image[m][n][0] - binary_value;

				for (int i = -index_i; i <= index_i; i++)
					for (int j = -index_j; j <= index_j; j++)
					{
						k_i = i + index_i;
						k_j = j + index_j;
						// Distribute the error to "future" pixels
						temp_ext_image[m + i][n + j][0] =
							temp_ext_image[m + i][n + j][0] +
							kernel_r[k_i][k_j] * quan_error / sum;
					}
			}
		}
		else
		{
			for (int n = Width + ext_num - 1; n >= ext_num; n = n - 1)
			{
				temp_ext_image[m][n][0] = pixel_round(temp_ext_image[m][n][0]);
				binary_value = pixel_thresh(temp_ext_image[m][n][0]);
				// Compute the quantization error
				quan_error = temp_ext_image[m][n][0] - binary_value;

				for (int i = -index_i; i <= index_i; i++)
					for (int j = -index_j; j <= index_j; j++)
					{
						k_i = i + index_i;
						k_j = j + index_j;
						// Distribute the error to "future" pixels
						temp_ext_image[m + i][n + j][0] =
							temp_ext_image[m + i][n + j][0] +
							kernel_l[k_i][k_j] * quan_error / sum;
					}
			}
		}
	}

	for (int m = ext_num; m < Height + ext_num; m++)
		for (int n = ext_num; n < Width + ext_num; n++)
		{
			if (temp_ext_image[m][n][0] >= 1)
				temp_ext_image[m][n][0] = 1;
			else if (temp_ext_image[m][n][0] <= 0)
				temp_ext_image[m][n][0] = 0;
			else
				continue;
		}

	// Get the binarized image
	fixed_thresh_demo(temp_ext_image, binary_image);
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
			filtering_im[m][n][0] = (unsigned char)255 * binary_image[m + ext_num][n + ext_num][0];
}