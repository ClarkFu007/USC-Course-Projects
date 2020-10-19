// EE569 Homework Assignment #2 Problem2_c: Color Halftoning with Error Diffusion
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


// Define file variables

constexpr auto Byte_Per_Pixel_Gray = 1; // 1 byte=8 bits
constexpr auto Byte_Per_Pixel_RGB = 3;
constexpr auto Height = 480;            // The "Rose" image's height
constexpr auto Width = 640;             // The "Rose" image's width
constexpr auto KernelSize = 3;          // The Kernel's size of the Floyd-Steinberg's error diffusion
constexpr auto ext_num = 6;             // The number of extension

constexpr auto CMYW = 1;               // Let 1 denote "CMYW"
constexpr auto MYGC = 2;               // Let 2 denote "MYGC"
constexpr auto RGMY = 3;               // Let 3 denote "RGMY"
constexpr auto KRGB = 4;               // Let 4 denote "KRGB"
constexpr auto RGBM = 5;               // Let 5 denote "RGBM"
constexpr auto CMGB = 6;               // Let 6 denote "CMGB"

constexpr auto K = 10;                // Let 10 denote "black"
constexpr auto R = 20;                // Let 20 denote "red"
constexpr auto G = 30;                // Let 30 denote "green"
constexpr auto B = 40;                // Let 40 denote "blue"
constexpr auto C = 50;                // Let 50 denote "cyan"
constexpr auto M = 60;                // Let 60 denote "megenta"
constexpr auto Y = 70;                // Let 70 denote "yellow"
constexpr auto W = 80;                // Let 80 denote "white"


// My functions's prototypes

void read_image(unsigned char image_data[][Width][Byte_Per_Pixel_RGB], const char* str);
          // Read images 

void seperate_rgb(unsigned char RGB_data[][Width][Byte_Per_Pixel_RGB],
	              unsigned char R_data[][Width][Byte_Per_Pixel_Gray],
	              unsigned char G_data[][Width][Byte_Per_Pixel_Gray],
	              unsigned char B_data[][Width][Byte_Per_Pixel_Gray]);
          // Transform RGB raw data into three channels seperately

void Change_cmy_rgb(unsigned char R_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char G_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char B_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char C_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char M_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char Y_data[][Width][Byte_Per_Pixel_Gray]);
          // Transform RGB channels into CMY channels seperately

void merge_rgb(unsigned char RGB_data[][Width][Byte_Per_Pixel_RGB],
	           unsigned char R_data[][Width][Byte_Per_Pixel_Gray],
	           unsigned char G_data[][Width][Byte_Per_Pixel_Gray],
	           unsigned char B_data[][Width][Byte_Per_Pixel_Gray]);
          // Merge R,G,and B channels into RGB raw data 

void merge_rgb_ext(unsigned char RGB_data[][Width + 2 * ext_num][Byte_Per_Pixel_RGB],
	               unsigned char R_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	               unsigned char G_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	               unsigned char B_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray]);

void ext_bound(unsigned char image_data[][Width][Byte_Per_Pixel_Gray],
	           unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray]);
          // Extend the boundaries of images

void fixed_thresh_demo_Gray(double image_data1[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	double image_data2[][Width + 2 * ext_num][Byte_Per_Pixel_Gray]);
          // Binarize images

void Separable_ED_demo(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	           unsigned char filtering_im[][Width][Byte_Per_Pixel_Gray],
	double kernel_r[][KernelSize], double kernel_l[][KernelSize], double sum);
          // The function to implement the correllation for half-toning with error diffusion

int Get_MBVQ(double R, double G, double B);
          // Determine MBVQ

int Get_Vertex(double R, double G, double B, int quadruple);
	      // Determine the closest vertex

double get_v(double vertex, int channel);
          // Get v values

void MBVQ_ED_demo(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_RGB],
	              unsigned char filtering_im[][Width][Byte_Per_Pixel_RGB],
	double kernel_r[][KernelSize], double kernel_l[][KernelSize], double sum);
          // Compute the quantization error and distribute the error to "future" pixels

void save_image(unsigned char output_image[][Width][Byte_Per_Pixel_RGB], const char* str);
          // Save the resulting images 

double pixel_round(double temp_pixel);
          // Handle the single pixel when it's greater than 1 or less than 0

double pixel_thresh(double temp_pixel);
          // Threshold the single pixel 


// Allocate image data array

unsigned char ImageDataRGB[Height][Width][Byte_Per_Pixel_RGB];
unsigned char ImageData_R[Height][Width][Byte_Per_Pixel_Gray];
unsigned char ImageData_G[Height][Width][Byte_Per_Pixel_Gray];
unsigned char ImageData_B[Height][Width][Byte_Per_Pixel_Gray];

// Data array for seperable error diffusion
unsigned char ImageData_C[Height][Width][Byte_Per_Pixel_Gray];
unsigned char ImageData_M[Height][Width][Byte_Per_Pixel_Gray];
unsigned char ImageData_Y[Height][Width][Byte_Per_Pixel_Gray];

unsigned char ext_ImageData_C[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];
unsigned char ext_ImageData_M[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];
unsigned char ext_ImageData_Y[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];

unsigned char FS_Image_C[Height][Width][Byte_Per_Pixel_Gray];
unsigned char FS_Image_M[Height][Width][Byte_Per_Pixel_Gray];
unsigned char FS_Image_Y[Height][Width][Byte_Per_Pixel_Gray];

unsigned char SED_ImageData_R[Height][Width][Byte_Per_Pixel_Gray];
unsigned char SED_ImageData_G[Height][Width][Byte_Per_Pixel_Gray];
unsigned char SED_ImageData_B[Height][Width][Byte_Per_Pixel_Gray];
unsigned char SED_ImageDataRGB[Height][Width][Byte_Per_Pixel_RGB];

// Data array for MBVQ-based error diffusion
unsigned char ext_ImageData_R[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];
unsigned char ext_ImageData_G[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];
unsigned char ext_ImageData_B[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray];
unsigned char ext_ImageData_RGB[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_RGB];

unsigned char MBVQ_ImageDataRGB[Height][Width][Byte_Per_Pixel_RGB];

int main()
{
	// Notice: I will divide every element by their sum later.

	double FS_Matrix_R[KernelSize][KernelSize] =
	{
		{0, 0, 0},
		{0, 0, 7},
		{3, 5, 1}
	};
	double FS_Matrix_L[KernelSize][KernelSize] =
	{
		{0, 0, 0},
		{7, 0, 0},
		{1, 5, 3}
	};

	// Read image into image data matrix
	const char* name_input = "Rose.raw";
	read_image(ImageDataRGB, name_input);

	// Transform RGB raw data into three channels seperately
	seperate_rgb(ImageDataRGB, ImageData_R, ImageData_G, ImageData_B);

	                    ///////////////////////////////////////////////////////////
	///////////////////////          Separable Error Diffusion (Below)          ///////////////////////

	// Transform RGB raw data into CMY channels seperately
	Change_cmy_rgb(ImageData_R, ImageData_G, ImageData_B, 
		           ImageData_C, ImageData_M, ImageData_Y);

	// Extend the boundary of the image
	ext_bound(ImageData_C, ext_ImageData_C);
	ext_bound(ImageData_M, ext_ImageData_M);
	ext_bound(ImageData_Y, ext_ImageData_Y);

	// Implement the correllation to realize Error Diffusion
	Separable_ED_demo(ext_ImageData_C, FS_Image_C, FS_Matrix_R, FS_Matrix_L, 16);  // For C channel
	Separable_ED_demo(ext_ImageData_M, FS_Image_M, FS_Matrix_R, FS_Matrix_L, 16);  // For M channel
	Separable_ED_demo(ext_ImageData_Y, FS_Image_Y, FS_Matrix_R, FS_Matrix_L, 16);  // For Y channel

	// Transform CMY raw data into RGB channels seperately
	Change_cmy_rgb(FS_Image_C, FS_Image_M, FS_Image_Y,
		           SED_ImageData_R, SED_ImageData_G, SED_ImageData_B);

	// Merge R,G,and B channels into RGB raw data 
	merge_rgb(SED_ImageDataRGB, SED_ImageData_R, SED_ImageData_G, SED_ImageData_B);
	
    ///////////////////////          Separable Error Diffusion (Above)          ///////////////////////
	                    ///////////////////////////////////////////////////////////


						///////////////////////////////////////////////////////////
	///////////////////////         MBVQ-based Error Diffusion (Below)         ///////////////////////

	// Extend the boundary of the image
	ext_bound(ImageData_R, ext_ImageData_R);
	ext_bound(ImageData_G, ext_ImageData_G);
	ext_bound(ImageData_B, ext_ImageData_B);
	
	merge_rgb_ext(ext_ImageData_RGB, ext_ImageData_R, ext_ImageData_G, ext_ImageData_B);
	
	// Step1: Determine MBVQ
	// Step2: Determine the closest vertex
	// Step3: Compute the quantization error and distribute the error to "future" pixels 
	MBVQ_ED_demo(ext_ImageData_RGB, MBVQ_ImageDataRGB, FS_Matrix_R, FS_Matrix_L, 16);

	///////////////////////         MBVQ-based Error Diffusion (Above)          ///////////////////////
						///////////////////////////////////////////////////////////


	// Write image data from image data matrix
	
	const char* name_SED_thresh = "Sep_ErrDif_Image.raw";
	save_image(SED_ImageDataRGB, name_SED_thresh);

	const char* name_MBVQ_thresh = "MBVQ_ErrDif_Image.raw";
	save_image(MBVQ_ImageDataRGB, name_MBVQ_thresh);

	return 0;
}


// My functions's definitions
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


void seperate_rgb(unsigned char RGB_data[][Width][Byte_Per_Pixel_RGB],
	              unsigned char R_data[][Width][Byte_Per_Pixel_Gray],
	              unsigned char G_data[][Width][Byte_Per_Pixel_Gray],
	              unsigned char B_data[][Width][Byte_Per_Pixel_Gray])
{
	using namespace std;

	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			R_data[m][n][Byte_Per_Pixel_Gray] = RGB_data[m][n][0];  // The R channel
			G_data[m][n][Byte_Per_Pixel_Gray] = RGB_data[m][n][1];  // The G channel
			B_data[m][n][Byte_Per_Pixel_Gray] = RGB_data[m][n][2];  // The B channel
		}
}


void merge_rgb(unsigned char RGB_data[][Width][Byte_Per_Pixel_RGB],
	           unsigned char R_data[][Width][Byte_Per_Pixel_Gray],
	           unsigned char G_data[][Width][Byte_Per_Pixel_Gray],
	           unsigned char B_data[][Width][Byte_Per_Pixel_Gray])
{
	using namespace std;

	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			RGB_data[m][n][0] = R_data[m][n][Byte_Per_Pixel_Gray];
			RGB_data[m][n][1] = G_data[m][n][Byte_Per_Pixel_Gray];
			RGB_data[m][n][2] = B_data[m][n][Byte_Per_Pixel_Gray];
		}
}


void merge_rgb_ext(unsigned char RGB_data[][Width + 2 * ext_num][Byte_Per_Pixel_RGB],
	               unsigned char R_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	               unsigned char G_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	               unsigned char B_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray])
{
	using namespace std;

	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{
			RGB_data[m][n][0] = R_data[m][n][Byte_Per_Pixel_Gray];
			RGB_data[m][n][1] = G_data[m][n][Byte_Per_Pixel_Gray];
			RGB_data[m][n][2] = B_data[m][n][Byte_Per_Pixel_Gray];
		}
}

void Change_cmy_rgb(unsigned char R_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char G_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char B_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char C_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char M_data[][Width][Byte_Per_Pixel_Gray],
	                unsigned char Y_data[][Width][Byte_Per_Pixel_Gray])
{
	using namespace std;

	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			C_data[m][n][0] = 255 - R_data[m][n][0];
			M_data[m][n][0] = 255 - G_data[m][n][0];
			Y_data[m][n][0] = 255 - B_data[m][n][0];
		}
}



void save_image(unsigned char output_image[][Width][Byte_Per_Pixel_RGB], const char* str)
{
	using namespace std;

	FILE* file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_image, sizeof(unsigned char), Height * Width * Byte_Per_Pixel_RGB, file);
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


void fixed_thresh_demo_Gray(double image_data1[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	double image_data2[][Width + 2 * ext_num][Byte_Per_Pixel_Gray])
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


void fixed_thresh_demo_RGB(double image_data1[][Width + 2 * ext_num][Byte_Per_Pixel_RGB],
	double image_data2[][Width + 2 * ext_num][Byte_Per_Pixel_RGB])
{
	using namespace std;

	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{
			if (image_data1[m][n][0] >= 0.5)
				image_data2[m][n][0] = 1;
			if (image_data1[m][n][0] <= 0)
				image_data2[m][n][0] = 0;

			if (image_data1[m][n][1] >= 0.5)
				image_data2[m][n][1] = 1;
			if (image_data1[m][n][1] <= 0)
				image_data2[m][n][1] = 0;

			if (image_data1[m][n][2] >= 0.5)
				image_data2[m][n][2] = 1;
			if (image_data1[m][n][2] <= 0)
				image_data2[m][n][2] = 0;
		}
}

double pixel_round(double temp_pixel)
{
	if (temp_pixel >= 1)
		return 1;
	else if (temp_pixel <= 0)
		return 0;
	else
		return temp_pixel;
}

double pixel_thresh(double temp_pixel)
{
	if (temp_pixel >= 0.5)
		return 1;
	else
		return 0;
}


void Separable_ED_demo(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_Gray],
	                   unsigned char filtering_im[][Width][Byte_Per_Pixel_Gray],
	                   double kernel_r[][KernelSize], double kernel_l[][KernelSize], double sum)
{
	using namespace std;

	double temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray] = { 0 };
	double binary_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_Gray] = { 0 };
	double binary_value = 0;
	double quan_error = 0;

	int index_i = (KernelSize - 1) / 2;
	int index_j = (KernelSize - 1) / 2;
	int k_i = 0;
	int k_j = 0;

	// Initialize a temporary image from the original image
	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
			temp_ext_image[m][n][0] = (double)ext_image_data[m][n][0] / 255;

	// Get the binarized image
	fixed_thresh_demo_Gray(temp_ext_image, binary_image);

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
	fixed_thresh_demo_Gray(temp_ext_image, binary_image);
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
			filtering_im[m][n][0] = (unsigned char)255 * binary_image[m + ext_num][n + ext_num][0];
}

int Get_MBVQ(double R, double G, double B)
{
	using namespace std;
	
	int quadruple = 0;
	if ((R + G) > 1)
	{
		if ((G + B) > 1)
		{
			if ((R + G + B) > 2)
				quadruple = 1;  // Return "CMYW"
			else
				quadruple = 2;	// Return "MYGC"
		}
		else
			quadruple = 3;      // Return "RGMY"
	}
	else
	{
		if (!((G + B) > 1))
		{ 
			if (!((R + G + B) > 1))
				quadruple = 4;  // Return "KRGB"
			else
				quadruple = 5;  // Return "RGBM"
		}
		else
			quadruple = 6;      // Return "CMGB"
	}
	return quadruple;
}

int Get_Vertex(double R, double G, double B, int quadruple)
{
	using namespace std;
	
	int vertex = 0;

	// No.1: For the CMYW Quadruple
	if (quadruple == 1)                 // CMYW = 1
	{
		vertex = 80;                    // The vertex is "white"

		if (B < 0.5)                    // B < 127
			if (B <= R)                 // B <= R
				if (B <= G)             // B <= G
					vertex = 70;        // The vertex is "yellow"

		if (G < 0.5)                    // G < 127
			if (G <= B)                 // G <= B
				if (G <= R)             // G <= R
					vertex = 60;        // The vertex is "magenta"

		if (R < 0.5)                    // R < 127
			if (R <= B)                 // R <= B
				if (R <= G)             // R <= G
					vertex = 50;        // The vertex is "cyan"
		
		return vertex;
	}

	// No.2: For the MYGC Quadruple
	if (quadruple == 2)                 // MYGC = 2
	{
		vertex = 60;                    // The vertex is "magenta"

		if (G >= B)                     // G >= B 
			if (R >= B)                 // R >= B
				if (R >= 0.5)           // R >= 127
					vertex = 70;        // The vertex is "yellow"
				else
					vertex = 30;        // The vertex is "green"

		if (G >= R)                     // G >= R 
			if (B >= R)                 // B >= R
				if (B >= 0.5)           // B >= 127
					vertex = 50;        // The vertex is "cyan"
				else
					vertex = 30;        // The vertex is "green"

		return vertex;
	}

	// No.3: For the RGMY Quadruple
	if (quadruple == 3)                 // RGMY = 3
	{
		if (B > 0.5)                    // B > 127 
		{
			if (R > 0.5)                // R > 127
			{
				if (B >= G)             // B >= G
					vertex = 60;        // The vertex is "magenta"
				else
					vertex = 70;        // The vertex is "yellow"
			}
			else
			{
				if (G > (B + R))        // G > B + R
					vertex = 30;        // The vertex is "green"
				else
					vertex = 60;        // The vertex is "magenta"
			}
		}
		else
		{
			if (R >= 0.5)               // R >= 127
			{
				if (G >= 0.5)           // G >= 127
					vertex = 70;        // The vertex is "yellow"
				else
					vertex = 20;        // The vertex is "red"
			}
			else
			{
				if (R >= G)             // R >= G
					vertex = 20;        // The vertex is "red"
				else
					vertex = 30;        // The vertex is "green"
			}
		}

		return vertex;
	}

	// No.4: For the KRGB Quadruple
	if (quadruple == 4)                 // KRGB = 4
	{
		vertex = 10;                    // The vertex is "black"

		if (B > 0.5)                    // B > 127
			if (B >= R)                 // B >= R
				if (B >= G)             // B >= G
					vertex = 40;        // The vertex is "blue"

		if (G > 0.5)                    // G > 127
			if (G >= B)                 // G >= B
				if (G >= R)             // G >= R
					vertex = 30;        // The vertex is "green"

		if (R > 0.5)                    // R > 127
			if (R >= B)                 // R >= B
				if (R >= G)             // R >= G
					vertex = 20;        // The vertex is "red"

		return vertex;
	}

	// No.5: For the RGBM Quadruple
	if (quadruple == 5)                 // MYGC = 5
	{
		vertex = 30;                    // The vertex is "green"

		if (R > G)                      // R > G 
			if (R >= B)                 // R >= B
				if (B < 0.5)            // B < 0.5
					vertex = 20;        // The vertex is "red"
				else
					vertex = 60;        // The vertex is "magenta"

		if (B > G)                      // B > G 
			if (B >= R)                 // B >= R
				if (R < 0.5)            // R < 0.5
					vertex = 40;        // The vertex is "blue"
				else
					vertex = 60;        // The vertex is "magenta"

		return vertex;
	}

	// No.6: For the CMGB Quadruple
	if (quadruple == 6)                 // CMGB = 6
	{
		if (B > 0.5)                    // B > 127 
		{
			if (R > 0.5)                // R > 127
			{
				if (G >= R)             // G >= R
					vertex = 50;        // The vertex is "cyan"
				else
					vertex = 60;        // The vertex is "magenta"
			}
			else
			{
				if (G > 0.5)            // G > 127
					vertex = 50;        // The vertex is "cyan"
				else
					vertex = 40;        // The vertex is "blue"
			}
		}
		else
		{
			if (R > 0.5)                // R > 127
			{
				float temp = R + B - G;
				if (temp >= 0.5)        // R - G + B >= 127
					vertex = 60;        // The vertex is "magenta"
				else
					vertex = 30;        // The vertex is "green"
			}
			else
			{
				if (G >= B)             // G >= B
					vertex = 30;        // The vertex is "green"
				else
					vertex = 40;        // The vertex is "blue"
			}
		}

		return vertex;
	}
}


double get_v(double vertex, int channel)
{
	using namespace std;

	float v = 0;

	if (channel == 0)              // The R channel
	{
		if (vertex == 10)          // The vertex is "black"
			v = 0;
		else if (vertex == 20)     // The vertex is "red"
			v = 1;
		else if (vertex == 30)     // The vertex is "green"
			v = 0;
		else if (vertex == 40)     // The vertex is "blue"
			v = 0;
		else if (vertex == 50)     // The vertex is "cyan"
			v = 0;
		else if (vertex == 60)     // The vertex is "magenta"
			v = 1;
		else if (vertex == 70)     // The vertex is "yellow"
			v = 1;
		else if (vertex == 80)     // The vertex is "white"
			v = 1;
		else
		{
			cout << "Vertex data error!";
			cout << endl;
		}
		return v;
	}
	if (channel == 1)              // The G channel
	{
		if (vertex == 10)          // The vertex is "black"
			v = 0;
		else if (vertex == 20)     // The vertex is "red"
			v = 0;
		else if (vertex == 30)     // The vertex is "green"
			v = 1;
		else if (vertex == 40)     // The vertex is "blue"
			v = 0;
		else if (vertex == 50)     // The vertex is "cyan"
			v = 1;
		else if (vertex == 60)     // The vertex is "magenta"
			v = 0;
		else if (vertex == 70)     // The vertex is "yellow"
			v = 1;
		else if (vertex == 80)     // The vertex is "white"
			v = 1;
		else
		{
			cout << "Vertex data error!";
			cout << endl;
		}
		return v;
	}
	if (channel == 2)              // The B channel
	{
		if (vertex == 10)          // The vertex is "black"
			v = 0;
		else if (vertex == 20)     // The vertex is "red"
			v = 0;
		else if (vertex == 30)     // The vertex is "green"
			v = 0;
		else if (vertex == 40)     // The vertex is "blue"
			v = 1;
		else if (vertex == 50)     // The vertex is "cyan"
			v = 1;
		else if (vertex == 60)     // The vertex is "magenta"
			v = 1;
		else if (vertex == 70)     // The vertex is "yellow"
			v = 0;
		else if (vertex == 80)     // The vertex is "white"
			v = 1;
		else
		{
			cout << "Vertex data error!";
			cout << endl;
		}
		return v;
	}
}


void MBVQ_ED_demo(unsigned char ext_image_data[][Width + 2 * ext_num][Byte_Per_Pixel_RGB],
	              unsigned char filtering_im[][Width][Byte_Per_Pixel_RGB],
	double kernel_r[][KernelSize], double kernel_l[][KernelSize], double sum)
{
	using namespace std;

	double temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_RGB] = { 0 };
	double binary_image[Height + 2 * ext_num][Width + 2 * ext_num][Byte_Per_Pixel_RGB] = { 0 };
	
	double quan_error[Byte_Per_Pixel_RGB] = { 0 };
	double R_value = 0, G_value = 0, B_value = 0;
	int quadruple_index = 0;
	int vertex_index = 0;
	double R_v = 0, G_v = 0, B_v = 0;


	int index_i = (KernelSize - 1) / 2;
	int index_j = (KernelSize - 1) / 2;
	int k_i = 0;
	int k_j = 0;

	// Initialize a temporary image from the original image
	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{ 
			temp_ext_image[m][n][0] = (double)ext_image_data[m][n][0] / 255;
			temp_ext_image[m][n][1] = (double)ext_image_data[m][n][1] / 255;
			temp_ext_image[m][n][2] = (double)ext_image_data[m][n][2] / 255;
		}

	// Diffuse error forward using the serpentine parsing
	for (int m = ext_num; m < Height + ext_num; m++)
	{
		if (m % 2 == 0)
		{
			for (int n = ext_num; n < Width + ext_num; n++)
			{
				// Step1: Determine MBVQ
				R_value = temp_ext_image[m][n][0];
				G_value = temp_ext_image[m][n][1];
				B_value = temp_ext_image[m][n][2];
				quadruple_index = Get_MBVQ(R_value, G_value, B_value);

				// Step2: Determine the closest vertex
				vertex_index = Get_Vertex(R_value, G_value, B_value, quadruple_index);
				R_v = get_v(vertex_index, 0);
				G_v = get_v(vertex_index, 1);
				B_v = get_v(vertex_index, 2);

				// Compute the quantization error
				quan_error[0] = temp_ext_image[m][n][0]  - R_v;
				quan_error[1] = temp_ext_image[m][n][1]  - G_v;
				quan_error[2] = temp_ext_image[m][n][2]  - B_v;

				// Step3: Compute the quantization error and distribute the error to "future" pixels 
				for (int i = -index_i; i <= index_i; i++)
					for (int j = -index_j; j <= index_j; j++)
					{
						k_i = i + index_i;
						k_j = j + index_j;

						// Distribute the error to "future" pixels
						temp_ext_image[m + i][n + j][0] =
							temp_ext_image[m + i][n + j][0] +
							kernel_r[k_i][k_j] * quan_error[0] / sum;
						temp_ext_image[m + i][n + j][1] =
							temp_ext_image[m + i][n + j][1] +
							kernel_r[k_i][k_j] * quan_error[1] / sum;
						temp_ext_image[m + i][n + j][2] =
							temp_ext_image[m + i][n + j][2] +
							kernel_r[k_i][k_j] * quan_error[2] / sum;
					}
				temp_ext_image[m][n][0] = R_v;
				temp_ext_image[m][n][1] = G_v;
				temp_ext_image[m][n][2] = B_v;
			}
		}
		else
		{
			for (int n = Width + ext_num - 1; n >= ext_num; n = n - 1)
			{
				// Step1: Determine MBVQ
				R_value = temp_ext_image[m][n][0];
				G_value = temp_ext_image[m][n][1];
				B_value = temp_ext_image[m][n][2];
				quadruple_index = Get_MBVQ(R_value, G_value, B_value);

				// Step2: Determine the closest vertex
				vertex_index = Get_Vertex(R_value, G_value, B_value, quadruple_index);
				R_v = get_v(vertex_index, 0);
				G_v = get_v(vertex_index, 1);
				B_v = get_v(vertex_index, 2);

				// Compute the quantization error
				quan_error[0] = temp_ext_image[m][n][0]  - R_v;
				quan_error[1] = temp_ext_image[m][n][1]  - G_v;
				quan_error[2] = temp_ext_image[m][n][2]  - B_v;

				// Step3: Compute the quantization error and distribute the error to "future" pixels 
				for (int i = -index_i; i <= index_i; i++)
					for (int j = -index_j; j <= index_j; j++)
					{
						k_i = i + index_i;
						k_j = j + index_j;

						// Distribute the error to "future" pixels
						temp_ext_image[m + i][n + j][0] =
							temp_ext_image[m + i][n + j][0] +
							kernel_l[k_i][k_j] * quan_error[0] / sum;
						temp_ext_image[m + i][n + j][1] =
							temp_ext_image[m + i][n + j][1] +
							kernel_l[k_i][k_j] * quan_error[1] / sum;
						temp_ext_image[m + i][n + j][2] =
							temp_ext_image[m + i][n + j][2] +
							kernel_l[k_i][k_j] * quan_error[2] / sum;
					}
				temp_ext_image[m][n][0] = R_v;
				temp_ext_image[m][n][1] = G_v;
				temp_ext_image[m][n][2] = B_v;
			}
		}
	}

	for (int m = ext_num; m < Height + ext_num; m++)
		for (int n = ext_num; n < Width + ext_num; n++)
		{
			if (temp_ext_image[m][n][0] >= 1)
				temp_ext_image[m][n][0] = 1;
			if (temp_ext_image[m][n][0] <= 0)
				temp_ext_image[m][n][0] = 0;

			if (temp_ext_image[m][n][1] >= 1)
				temp_ext_image[m][n][1] = 1;
			if (temp_ext_image[m][n][1] <= 0)
				temp_ext_image[m][n][1] = 0;

			if (temp_ext_image[m][n][2] >= 1)
				temp_ext_image[m][n][2] = 1;
			if (temp_ext_image[m][n][2] <= 0)
				temp_ext_image[m][n][2] = 0;
		}
		

	// Get the binarized image
	fixed_thresh_demo_RGB(temp_ext_image, binary_image);

	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			filtering_im[m][n][0] = (unsigned char)255 * binary_image[m + ext_num][n + ext_num][0];
			filtering_im[m][n][1] = (unsigned char)255 * binary_image[m + ext_num][n + ext_num][1];
			filtering_im[m][n][2] = (unsigned char)255 * binary_image[m + ext_num][n + ext_num][2];
		}
}


