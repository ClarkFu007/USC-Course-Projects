// EE569 Homework Assignment #2 Problem2_a
// Submission Date: February 16, 2020
// Name : Yao Fu
// USC ID : 6786354176
// Email : yaof@usc.edu

#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <sal.h> 
#include <math.h>
#include <time.h>
#pragma warning(disable:4996)


// Define file variables
constexpr auto Byte_Per_Pixel_Gray = 1; // 1 byte=8 bits
constexpr auto Byte_Per_Pixel_RGB = 3;
constexpr auto Height = 500;          // The "LightHouse" image's height
constexpr auto Width = 750;           // The "LightHouse" image's width


// My functions's prototypes
void read_image(unsigned char image_data[][Width][Byte_Per_Pixel_Gray], const char* str);
          // Read images 
void fixed_thresh_demo(unsigned char image_data1[][Width][Byte_Per_Pixel_Gray],
	                   unsigned char image_data2[][Width][Byte_Per_Pixel_Gray],
	                   int threshold);
          // Implement the operation of fixed thresholding
void random_thresh_demo(unsigned char image_data1[][Width][Byte_Per_Pixel_Gray],
	                    unsigned char image_data2[][Width][Byte_Per_Pixel_Gray]);
          // Implement the operation of random thresholding
void DM_thresh_demo(unsigned char image_data1[][Width][Byte_Per_Pixel_Gray],
	                    unsigned char image_data2[][Width][Byte_Per_Pixel_Gray], const int layer);
          // Implement the operation of using the Dithering matrix
void save_image(unsigned char output_image[][Width][Byte_Per_Pixel_Gray], const char* str);
          // Save the resulting denoised images 
unsigned char pixel_round(float temp_pixel);
          // To handle situations when intensity > 255 or intensity < 0


// Allocate image data array

unsigned char ImageDataGray[Height][Width][Byte_Per_Pixel_Gray];
unsigned char FixThresh_Image[Height][Width][Byte_Per_Pixel_Gray];
unsigned char RandomThresh_Image[Height][Width][Byte_Per_Pixel_Gray];
unsigned char DithMatrix_2_Image[Height][Width][Byte_Per_Pixel_Gray];
unsigned char DithMatrix_8_Image[Height][Width][Byte_Per_Pixel_Gray];
unsigned char DithMatrix_32_Image[Height][Width][Byte_Per_Pixel_Gray];

int main()
{
	int Thresh_Value =128;

	// Read image into image data matrix
	const char* name_input = "LightHouse.raw";
	read_image(ImageDataGray, name_input);

	// Implement the operation of fixed thresholding
	fixed_thresh_demo(ImageDataGray, FixThresh_Image, Thresh_Value);

	// Implement the operation of random thresholding
	random_thresh_demo(ImageDataGray, RandomThresh_Image);

	// Implement the operation of using the Dithering matrix	
	DM_thresh_demo(ImageDataGray, DithMatrix_2_Image, 1);
	DM_thresh_demo(ImageDataGray, DithMatrix_8_Image, 3);
	DM_thresh_demo(ImageDataGray, DithMatrix_32_Image, 5);

	// Write image data from image data matrix
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


unsigned char pixel_round(float temp_pixel)
{
	if (temp_pixel >= 255)
		return 255;
	else if (temp_pixel <= 0)
		return 0;
	else
		return (unsigned char)temp_pixel;
}


void fixed_thresh_demo(unsigned char image_data1[][Width][Byte_Per_Pixel_Gray],
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


void random_thresh_demo(unsigned char image_data1[][Width][Byte_Per_Pixel_Gray],
	                    unsigned char image_data2[][Width][Byte_Per_Pixel_Gray])
{
	using namespace std;

	srand((unsigned)time(NULL));

	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{			
			int threshold = rand() % 256;
			if (image_data1[m][n][0] >= threshold)
				image_data2[m][n][0] = 255;
			else
				image_data2[m][n][0] = 0;
		}
}


void DM_thresh_demo(unsigned char image_data1[][Width][Byte_Per_Pixel_Gray],
	                unsigned char image_data2[][Width][Byte_Per_Pixel_Gray], const int layer)
{
	using namespace std;

	const int size = pow(2, layer);
	//allocate the matrix
	int** Bayer_index_matrix = new int* [size];
	int** threshold_matrix = new int* [size];
	int** I = new int* [size];
	for (int ith_row = 0; ith_row < size; ith_row++)
	{
		Bayer_index_matrix[ith_row] = new int[size];
		threshold_matrix[ith_row] = new int[size];
		I[ith_row] = new int[size];
	}

	// use the matrix
	I[0][0] = (int)1; I[0][1] = (int)2;
	I[1][0] = (int)3; I[1][1] = (int)0;

	// Get the Bayer index matrix
	if (layer == 1)
	{
		for (int i = 0; i < size; i++)
			for (int j = 0; j < size; j++)
				Bayer_index_matrix[i][j] = I[i][j];
	}
	else
	{
		int index = 0;
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < 2; j++)
				Bayer_index_matrix[i][j] = (int)I[i][j];

		for (int ith_layer = 1; ith_layer < layer; ith_layer++)
		{
			index = pow(2, ith_layer);
			cout << index;
			cout << endl;
			for (int i = 0; i < index; i++)
				for (int j = 0; j < index; j++)
				{
					Bayer_index_matrix[i][j] = (int)4 * I[i][j] + 1;
					Bayer_index_matrix[i][j + index] = (int)4 * I[i][j] + 2;
					Bayer_index_matrix[i + index][j] = (int)4 * I[i][j] + 3;
					Bayer_index_matrix[i + index][j + index] = (int)4 * I[i][j];
				}
			for (int i = 0; i < 2 * index; i++)
				for (int j = 0; j < 2 * index; j++)
					I[i][j] = (int)Bayer_index_matrix[i][j];
		}
		for (int i = 0; i < size; i++)
		{
			for (int j = 0; j < size; j++)
				cout << Bayer_index_matrix[i][j] << ", ";
			cout << endl;
		}

	}

	for (int i = 0; i < size; i++)
		for (int j = 0; j < size; j++)
			threshold_matrix[i][j] = floor((Bayer_index_matrix[i][j] + 0.5) * 255 / pow(size, 2));

	int threshold = 0;
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			int pixel_m = m % size;
			int pixel_n = n % size;
			threshold = threshold_matrix[pixel_m][pixel_n];
			if (image_data1[m][n][0] >= threshold)
				image_data2[m][n][0] = 255;
			else
				image_data2[m][n][0] = 0;
		}

	//deallocate the matrix
	for (int ith_row = 0; ith_row < size; ith_row++)
	{
		delete[] Bayer_index_matrix[ith_row];
		delete[] threshold_matrix[ith_row];
		delete[] I[ith_row];
	}
	delete[] Bayer_index_matrix;
	delete[] threshold_matrix;
	delete[] I;
}