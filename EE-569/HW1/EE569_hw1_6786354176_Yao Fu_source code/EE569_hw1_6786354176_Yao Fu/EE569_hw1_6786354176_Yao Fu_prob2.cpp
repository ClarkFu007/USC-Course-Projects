// EE569 Homework Assignment # 1Problem_2
// Submission Date: January 28, 2020
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
constexpr auto BYTE_PER_PIXEL_GRAY = 1; // 1 byte=8 bits;
constexpr auto BYTE_PER_PIXEL_RGB = 3;
constexpr auto Height = 320;          // The "Corn.raw" image's height;
constexpr auto Width = 320;           // The "Corn.raw" image's width;
constexpr auto KernelSize = 5;        // The Kernel's size;
constexpr auto ext_num = 6;           // The number of extension

// My functions's prototypes
void read_image(unsigned char image_data[][Width][BYTE_PER_PIXEL_GRAY], const char* str);
                    // Read the "Corn_noisy" image 
void ext_bound(unsigned char image_data[][Width][BYTE_PER_PIXEL_GRAY],
	           unsigned char ext_image_data[][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY]);
                    // Extend the boundaries of images
void get_noise(unsigned char image_data1[][Width][BYTE_PER_PIXEL_GRAY],
	           unsigned char image_data2[][Width][BYTE_PER_PIXEL_GRAY],
	           int image_data_d[][Width][BYTE_PER_PIXEL_GRAY]);
                    // Get noise data in order to estimate its PDF
void corr_demo(unsigned char ext_image_data[][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	           unsigned char filtering_im[][Width][BYTE_PER_PIXEL_GRAY],
	           float kernel[][KernelSize]);
                    // The function to implement the correllation
void gau_filtering(unsigned char ext_image_data[][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	               unsigned char filtering_im[][Width][BYTE_PER_PIXEL_GRAY]);
                    // The function to realize Gaussian filtering whose parameters can be modified
void save_image(unsigned char output_image[][Width][BYTE_PER_PIXEL_GRAY], const char* str);
                    // Save the resulting denoised images 
void save_data(int output_data[][Width][BYTE_PER_PIXEL_GRAY], const char* str);
                    // Save noise data 
unsigned char pixel_round(float temp_pixel);
                    // To handle situations when intensity > 255 or intensity < 0
float sum_matrix(float matrix_data[][KernelSize]);
                    // Get the sum of elements of a certain matrix
void bilal_filtering(unsigned char ext_image_data[][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	                 unsigned char filtering_im[][Width][BYTE_PER_PIXEL_GRAY]);
                    // The function to realize bilateral filtering whose parameters can be modified

int main()
{

	// Allocate image data array
	unsigned char ImageData[Height][Width][BYTE_PER_PIXEL_GRAY];
	unsigned char ext_ImageData[Height + 2 * ext_num][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY];
	int NoiseData[Height][Width][BYTE_PER_PIXEL_GRAY];
	unsigned char InputImageData[Height][Width][BYTE_PER_PIXEL_GRAY];
	unsigned char UniFil_Image[Height][Width][BYTE_PER_PIXEL_GRAY];
	unsigned char GauFil1_Image[Height][Width][BYTE_PER_PIXEL_GRAY];
	unsigned char GauFil2_Image[Height][Width][BYTE_PER_PIXEL_GRAY];
	unsigned char BilFil_Image[Height][Width][BYTE_PER_PIXEL_GRAY];
	float Uni_Kernel[KernelSize][KernelSize] =
	{
		{1, 1, 1, 1, 1},
		{1, 1, 1, 1, 1},
	    {1, 1, 1, 1, 1},
	    {1, 1, 1, 1, 1},
	    {1, 1, 1, 1, 1}
	};
	float Gau_Kernel[KernelSize][KernelSize] =
	{
		{1,  4,  7,  4, 1},
		{4, 16, 26, 16, 4},
		{7, 26, 41, 26, 7},
		{4, 16, 26, 16, 4},
		{1,  4,  7,  4, 1}
	};

	// Read image into image data matrix
	const char* name_input1 = "Corn_noisy.raw";
	read_image(InputImageData, name_input1);
	const char* name_input2 = "Corn_gray.raw";
	read_image(ImageData, name_input2);

	// Extend the boundary of the image
	ext_bound(InputImageData, ext_ImageData);

	// Get noise data
	get_noise(InputImageData,ImageData,NoiseData);
	
	// Use the uniform weight function
    corr_demo(ext_ImageData, UniFil_Image, Uni_Kernel);
	// Use the Gaussian weight function
	corr_demo(ext_ImageData, GauFil1_Image, Gau_Kernel);
	gau_filtering(ext_ImageData, GauFil2_Image);
	
	// Implement the bilateral filtering
	bilal_filtering(ext_ImageData, BilFil_Image);
	
	// Write image data from image data matrix
	const char* name_noise = "Noise_data.raw";
	save_data(NoiseData, name_noise);
	const char * name_Uni = "UniFil_Image.raw";
	save_image(UniFil_Image, name_Uni);
	const char* name_Gau1 = "GauFil1_Image.raw";
	save_image(GauFil1_Image, name_Gau1);
	const char* name_Gau2 = "GauFil2_Image.raw";
	save_image(GauFil2_Image, name_Gau2);
	const char* name_Bil = "BilFil_Image.raw";
	save_image(BilFil_Image, name_Bil);

	return 0;
}


// My functions's definitions
void read_image(unsigned char image_data[][Width][BYTE_PER_PIXEL_GRAY], const char* str)
{
	using namespace std;

	FILE* file;
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
	fread(image_data, sizeof(unsigned char), Height * Width * BYTE_PER_PIXEL_GRAY, file);
	fclose(file);
}


void save_image(unsigned char output_image[][Width][BYTE_PER_PIXEL_GRAY], const char* str)
{
	using namespace std;

	FILE* file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_image, sizeof(unsigned char), Height * Width * BYTE_PER_PIXEL_GRAY, file);
	fclose(file);
}


void save_data(int output_data[][Width][BYTE_PER_PIXEL_GRAY], const char* str)
{
	using namespace std;

	FILE* file;
	// Write image data from image data matrix
	if (!(file = fopen(str, "wb")))
	{
		cout << "Cannot open file" << str << "!" << endl;
		exit(0);
	}
	fwrite(output_data, sizeof(int), 320 * 320*1, file);
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


void ext_bound(unsigned char image_data[][Width][BYTE_PER_PIXEL_GRAY],
	           unsigned char ext_image_data[][Width+ 2 * ext_num][BYTE_PER_PIXEL_GRAY])
{
	using namespace std;
	
	// Copy the center
	for (int m = ext_num; m < ext_num + Height; m++)
		for (int n = ext_num; n < ext_num + Width; n++)
			ext_image_data[m][n][BYTE_PER_PIXEL_GRAY - 1] =
			image_data[m - ext_num][n - ext_num][BYTE_PER_PIXEL_GRAY - 1];
	// Reflect the two vertical parts
	int index_l = 2 * ext_num - 1;
	int index_r = 2 * (Width + 2 * ext_num - 1) - index_l;
	for (int m = ext_num; m < ext_num + Height; m++)
		for (int n = 0; n < ext_num; n++)
		{
			ext_image_data[m][n][BYTE_PER_PIXEL_GRAY - 1] =
				image_data[m - ext_num][index_l - n - ext_num][BYTE_PER_PIXEL_GRAY - 1];
			ext_image_data[m][Width + 2 * ext_num - 1 - n][BYTE_PER_PIXEL_GRAY - 1] =
				image_data[m - ext_num][index_r -
				(Width + 2 * ext_num - 1 - n) - ext_num][BYTE_PER_PIXEL_GRAY - 1];
		}
	// Reflect the two horizontal parts
	int index_u = 2 * ext_num - 1;
	int index_b = 2 * (Height + 2 * ext_num - 1) - index_u;
	for (int m = 0; m < ext_num; m++)
		for (int n = ext_num; n < ext_num + Width; n++)
		{
			ext_image_data[m][n][BYTE_PER_PIXEL_GRAY - 1] =
				image_data[index_u - m - ext_num][n - ext_num][BYTE_PER_PIXEL_GRAY - 1];
			ext_image_data[Height + 2 * ext_num - 1 - m][n][BYTE_PER_PIXEL_GRAY - 1] =
				image_data[index_b - (Height + 2 * ext_num - 1 - m) - ext_num]
				[n - ext_num][BYTE_PER_PIXEL_GRAY - 1];
		}
	// Reflect the four corners
	for (int m = 0; m < ext_num; m++)
		for (int n = 0; n < ext_num; n++)
		{
			ext_image_data[m][n][BYTE_PER_PIXEL_GRAY - 1] = ext_image_data[index_u - m][n][BYTE_PER_PIXEL_GRAY - 1];
			ext_image_data[m + Height + ext_num][n][BYTE_PER_PIXEL_GRAY - 1] =
				ext_image_data[index_b - (m + Height + ext_num)][n][BYTE_PER_PIXEL_GRAY - 1];
			ext_image_data[m][n + Width + ext_num][BYTE_PER_PIXEL_GRAY - 1] =
				ext_image_data[m][index_r - (n + Width + ext_num)][BYTE_PER_PIXEL_GRAY - 1];
			ext_image_data[m + Height + ext_num][n + Width + ext_num][BYTE_PER_PIXEL_GRAY - 1] =
				ext_image_data[index_b - (m + Height + ext_num)][n + Width + ext_num]
				[BYTE_PER_PIXEL_GRAY - 1];
		}
}


void get_noise(unsigned char image_data1[][Width][BYTE_PER_PIXEL_GRAY],
	           unsigned char image_data2[][Width][BYTE_PER_PIXEL_GRAY],
	           int image_data_d[][Width][BYTE_PER_PIXEL_GRAY])
{
	using namespace std;
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			image_data_d[m][n][0] = (int)image_data1[m][n][0] - (int)image_data2[m][n][0];
		}
}


void corr_demo(unsigned char ext_image_data[][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	           unsigned char filtering_im[][Width][BYTE_PER_PIXEL_GRAY],
	           float kernel[][KernelSize])
{
	using namespace std;
		
	float temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY] = { 0 };
	float temp_fil_image[Height][Width][BYTE_PER_PIXEL_GRAY] = { 0 };
	int index_i = (KernelSize - 1) / 2;
	int index_j = (KernelSize - 1) / 2;

	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{
			temp_ext_image[m][n][0] = (float)ext_image_data[m][n][0];
		}

	for (int m = ext_num; m < Height + ext_num; m++)
		for (int n = ext_num; n < Width + ext_num; n++)
		{
			for (int i = -index_i; i <= index_i; i++)
				for (int j = -index_j; j <= index_j; j++)
				{
					temp_fil_image[m - ext_num][n - ext_num][0] =
						(temp_fil_image[m - ext_num][n - ext_num][0] +
							kernel[i + index_i][j + index_j] * temp_ext_image[m + i][n + j][0]);

				}
			float weight_sum = sum_matrix(kernel);
			temp_fil_image[m - ext_num][n - ext_num][0] =
				temp_fil_image[m - ext_num][n - ext_num][0] / weight_sum;
		}
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			filtering_im[m][n][0] = pixel_round(temp_fil_image[m][n][0]);
		}
}


float sum_matrix(float matrix_data[][KernelSize])
{
	using namespace std;
	float sum = 0;
	for (int m=0;m < KernelSize;m++)
		for (int n = 0; n < KernelSize; n++)
		{
			sum = sum + matrix_data[m][n];
		}
	return sum;
}


void gau_filtering(unsigned char ext_image_data[][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	               unsigned char filtering_im[][Width][BYTE_PER_PIXEL_GRAY])
{
	using namespace std;

	float temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY] = { 0 };
	float temp_fil_image[Height][Width][BYTE_PER_PIXEL_GRAY] = { 0 };
	float spatial_kernel[KernelSize][KernelSize] = { 0 };
	double sigma_c = 1.5;        //  Spatial parameter

	int index_i = (KernelSize - 1) / 2;
	int index_j = (KernelSize - 1) / 2;

	// Converge image data type "unsigned char" into "float"
	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{
			temp_ext_image[m][n][0] = (float)ext_image_data[m][n][0];
		}

	// Get spatial weighting coefficients
	for (int i = -index_i; i <= index_i; i++)
		for (int j = -index_j; j <= index_j; j++)
		{
			spatial_kernel[i + index_i][j + index_j] = 
				         (float)exp(-(pow((double)i - 0, 2) + pow((double)j - 0, 2)) / (2 * pow(sigma_c, 2)));
		}

	// Implement the correlation algorithm			
	for (int m = ext_num; m < Height + ext_num; m++)
		for (int n = ext_num; n < Width + ext_num; n++)
		{
			for (int i = -index_i; i <= index_i; i++)
				for (int j = -index_j; j <= index_j; j++)
				{

					float temp_value = (temp_fil_image[m - ext_num][n - ext_num][0] +
						spatial_kernel[i + index_i][j + index_j]
						* temp_ext_image[m + i][n + j][0]);
					temp_fil_image[m - ext_num][n - ext_num][0] = temp_value;
				}
			float weight_sum = sum_matrix(spatial_kernel);
			temp_fil_image[m - ext_num][n - ext_num][0] =
				temp_fil_image[m - ext_num][n - ext_num][0] / weight_sum;

		}
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			filtering_im[m][n][0] = pixel_round(temp_fil_image[m][n][0]);
		}

}


void bilal_filtering(unsigned char ext_image_data[][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY],
	                 unsigned char filtering_im[][Width][BYTE_PER_PIXEL_GRAY])
{
	using namespace std;

	float temp_ext_image[Height + 2 * ext_num][Width + 2 * ext_num][BYTE_PER_PIXEL_GRAY] = { 0 };
	float temp_fil_image[Height][Width][BYTE_PER_PIXEL_GRAY] = { 0 };
	double sigma_c = 1.5;        //  Spatial parameter
	double sigma_s = 300;        //  Range parameter
	float final_kernel[KernelSize][KernelSize] = { 0 };
	int index_i = (KernelSize - 1) / 2;
	int index_j = (KernelSize - 1) / 2;

	// Converge image data type "unsigned char" into "float"
	for (int m = 0; m < Height + 2 * ext_num; m++)
		for (int n = 0; n < Width + 2 * ext_num; n++)
		{
			temp_ext_image[m][n][0] = (float)ext_image_data[m][n][0];
		}

	// Implement the correlation algorithm			
	for (int m = ext_num; m < Height + ext_num; m++)
		for (int n = ext_num; n < Width + ext_num; n++)
		{
			for (int i = -index_i; i <= index_i; i++)
				for (int j = -index_j; j <= index_j; j++)
				{
					final_kernel[i+index_i][j + index_j]= 
						(float)exp(-(pow((double)i - 0, 2) + pow((double)j - 0, 2)) / (2 * pow(sigma_c, 2)))*
						(float)exp(-(pow(temp_ext_image[m + ext_num][n + ext_num][0] -
							temp_ext_image[m + ext_num + i][n + ext_num + j][0], 2)) /
							(2 * pow(sigma_s, 2)));

					float temp_value= (temp_fil_image[m - ext_num][n - ext_num][0] +
						final_kernel[i + index_i][j + index_j] 
						* temp_ext_image[m + i][n + j][0]);
					temp_fil_image[m - ext_num][n - ext_num][0] = temp_value;
				}
		    float weight_sum = sum_matrix(final_kernel);
			temp_fil_image[m - ext_num][n - ext_num][0] =
				temp_fil_image[m - ext_num][n - ext_num][0] / weight_sum;

		}
	for (int m = 0; m < Height; m++)
		for (int n = 0; n < Width; n++)
		{
			filtering_im[m][n][0] = pixel_round(temp_fil_image[m][n][0]);
		}
}






