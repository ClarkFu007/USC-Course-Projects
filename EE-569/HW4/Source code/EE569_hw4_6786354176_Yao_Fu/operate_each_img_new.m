% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the texture segmentation

function vector=operate_each_img_new(input_img,height,width,ext_num,w_size)

% Step1:Subtract image mean(reduce illumination effects)
sum=0;
for m=1:1:height
    for n=1:1:width
        sum=sum+input_img(m,n);
    end
end
img_mean=sum/(height*width);
for m=1:1:height
    for n=1:1:width
        input_img(m,n)=input_img(m,n)-img_mean;
    end
end

% Step2: Apply 25 5*5 Laws filers to get 25 filtered images
% Get the 2-D Laws Filters
size=5;
L5=[1,4,6,4,1];E5=[-1,-2,0,2,1];S5=[-1,0,2,0,-1];W5=[-1,2,0,-2,1];R5=[1,-4,6,-4,1];

L5L5=tensor_product(L5,L5,5);L5E5=tensor_product(L5,E5,5);L5S5=tensor_product(L5,S5,5);
L5W5=tensor_product(L5,W5,5);L5R5=tensor_product(L5,R5,5);

E5L5=tensor_product(E5,L5,5);E5E5=tensor_product(E5,E5,5);E5S5=tensor_product(E5,S5,5);
E5W5=tensor_product(E5,W5,5);E5R5=tensor_product(E5,R5,5);

S5L5=tensor_product(S5,L5,5);S5E5=tensor_product(S5,E5,5);S5S5=tensor_product(S5,S5,5);
S5W5=tensor_product(S5,W5,5);S5R5=tensor_product(S5,R5,5);

W5L5=tensor_product(W5,L5,5);W5E5=tensor_product(W5,E5,5);W5S5=tensor_product(W5,S5,5);
W5W5=tensor_product(W5,W5,5);W5R5=tensor_product(W5,R5,5);

R5L5=tensor_product(R5,L5,5);R5E5=tensor_product(R5,E5,5);R5S5=tensor_product(R5,S5,5);
R5W5=tensor_product(R5,W5,5);R5R5=tensor_product(R5,R5,5);


% Do the convolution
output1=conv_demo(input_img,height,width,ext_num,L5L5,size);
output2=conv_demo(input_img,height,width,ext_num,L5E5,size);
output3=conv_demo(input_img,height,width,ext_num,L5S5,size);
output4=conv_demo(input_img,height,width,ext_num,L5W5,size);
output5=conv_demo(input_img,height,width,ext_num,L5R5,size);
output6=conv_demo(input_img,height,width,ext_num,E5L5,size);
output7=conv_demo(input_img,height,width,ext_num,E5E5,size);
output8=conv_demo(input_img,height,width,ext_num,E5S5,size);
output9=conv_demo(input_img,height,width,ext_num,E5W5,size);
output10=conv_demo(input_img,height,width,ext_num,E5R5,size);
output11=conv_demo(input_img,height,width,ext_num,S5L5,size);
output12=conv_demo(input_img,height,width,ext_num,S5E5,size);
output13=conv_demo(input_img,height,width,ext_num,S5S5,size);
output14=conv_demo(input_img,height,width,ext_num,S5W5,size);
output15=conv_demo(input_img,height,width,ext_num,S5R5,size);
output16=conv_demo(input_img,height,width,ext_num,W5L5,size);
output17=conv_demo(input_img,height,width,ext_num,W5E5,size);
output18=conv_demo(input_img,height,width,ext_num,W5S5,size);
output19=conv_demo(input_img,height,width,ext_num,W5W5,size);
output20=conv_demo(input_img,height,width,ext_num,W5R5,size);
output21=conv_demo(input_img,height,width,ext_num,R5L5,size);
output22=conv_demo(input_img,height,width,ext_num,R5E5,size);
output23=conv_demo(input_img,height,width,ext_num,R5S5,size);
output24=conv_demo(input_img,height,width,ext_num,R5W5,size);
output25=conv_demo(input_img,height,width,ext_num,R5R5,size);


% Step3: Average energy to form a 25-D feature vector
element1=aver_energy_new(output1,height,width,w_size);element2=aver_energy_new(output2,height,width,w_size);
element3=aver_energy_new(output3,height,width,w_size);element4=aver_energy_new(output4,height,width,w_size);
element5=aver_energy_new(output5,height,width,w_size);
element6=aver_energy_new(output6,height,width,w_size);element7=aver_energy_new(output7,height,width,w_size);
element8=aver_energy_new(output8,height,width,w_size);element9=aver_energy_new(output9,height,width,w_size);
element10=aver_energy_new(output10,height,width,w_size);
element11=aver_energy_new(output11,height,width,w_size);element12=aver_energy_new(output12,height,width,w_size);
element13=aver_energy_new(output13,height,width,w_size);element14=aver_energy_new(output14,height,width,w_size);
element15=aver_energy_new(output15,height,width,w_size);
element16=aver_energy_new(output16,height,width,w_size);element17=aver_energy_new(output17,height,width,w_size);
element18=aver_energy_new(output18,height,width,w_size);element19=aver_energy_new(output19,height,width,w_size);
element20=aver_energy_new(output20,height,width,w_size);
element21=aver_energy_new(output21,height,width,w_size);element22=aver_energy_new(output22,height,width,w_size);
element23=aver_energy_new(output23,height,width,w_size);element24=aver_energy_new(output24,height,width,w_size);
element25=aver_energy_new(output25,height,width,w_size);

% Step4: Define 15-D feature vector as follows
vecotr1=element1;
vecotr2=(element2+element6)/2;
vecotr3=(element3+element11)/2;
vecotr4=(element4+element16)/2;
vecotr5=(element5+element21)/2;
vecotr6=element7;
vecotr7=(element8+element12)/2;
vecotr8=(element9+element17)/2;
vecotr9=(element10+element22)/2;
vecotr10=element13;
vecotr11=(element14+element18)/2;
vecotr12=(element15+element23)/2;
vecotr13=element19;
vecotr14=(element20+element24)/2;
vecotr15=element25;
vector=[vecotr2./vecotr1;
        vecotr3./vecotr1;
        vecotr4./vecotr1;
        vecotr5./vecotr1;
        vecotr6./vecotr1;
        vecotr7./vecotr1;
        vecotr8./vecotr1;
        vecotr9./vecotr1;
        vecotr10./vecotr1;
        vecotr11./vecotr1;
        vecotr12./vecotr1;
        vecotr13./vecotr1;
        vecotr14./vecotr1;
        vecotr15./vecotr1];

end