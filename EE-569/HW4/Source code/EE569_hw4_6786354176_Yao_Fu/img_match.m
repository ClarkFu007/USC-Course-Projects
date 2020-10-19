% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the image matching

function scores=img_match(img_RGB1,img_RGB2)

img1=single(rgb2gray(img_RGB1));
img2=single(rgb2gray(img_RGB2));

com_fig=zeros(size(img1,1),size(img1,2)+size(img2,2),3);  
com_fig(:,1:size(img1,2),:)=img_RGB1;
com_fig(1:size(img2,1),(size(img1,2)+1):end,:)=img_RGB2;
com_fig=uint8(com_fig);

[f1,d1]=vl_sift(img1,'Levels',5,'PeakThresh',4);
[f2,d2]=vl_sift(img2,'Levels',5,'PeakThresh',4);
[matches,scores]=vl_ubcmatch(d1,d2,1.5);

f1_location=matches(1,:);
f2_location=matches(2,:);

figure;
image(com_fig);   
axis image
hold on
for i=1:1:size(matches,2)
    x1_value=f1(1,f1_location(i));
    y1_value=f1(2,f1_location(i));
    scale1=f1(3,f1_location(i)); 
    angel1=atan(f1(4,f1_location(i)));
    plot(x1_value,y1_value,'o','color','r','MarkerSize',scale1,'LineWidth',1.5);
    line([x1_value,x1_value+scale1*cos(angel1)],[y1_value,y1_value+scale1*sin(angel1)],...
           'linestyle','-','color','r','LineWidth',1.5);
       
    x2_value=f2(1,f2_location(i))+size(img1,2);
    y2_value=f2(2,f2_location(i));
    scale2=f2(3,f2_location(i));
    angel2=atan(f2(4,f2_location(i)));
    plot(x2_value,y2_value,'o','color','r','MarkerSize',scale2,'LineWidth',1.5);
    line([x2_value,x2_value+scale2*cos(angel2)],[y2_value,y2_value+scale2*sin(angel2)],...
           'linestyle','-','color','r','LineWidth',1.5);
     
    line([x1_value,x2_value],[y1_value,y2_value],...
     'linestyle','-','color','g','LineWidth',1.5);
end
hold off
end