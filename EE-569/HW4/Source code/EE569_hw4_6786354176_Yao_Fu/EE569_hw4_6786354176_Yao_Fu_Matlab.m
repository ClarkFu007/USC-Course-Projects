% EE569 Homework Assignment # 4 
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu

%% Problem 1: Texture Analysis and Segmentation

%% Part(a):Texture Classification --- Feature Extraction
%% Display the original images
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

%% Get the 15-D feature vector for each texture image
blanket1_vector=operate_each_img(blanket1,128,128,2);
blanket2_vector=operate_each_img(blanket2,128,128,2);
blanket3_vector=operate_each_img(blanket3,128,128,2);
blanket4_vector=operate_each_img(blanket4,128,128,2);
blanket5_vector=operate_each_img(blanket5,128,128,2);
blanket6_vector=operate_each_img(blanket6,128,128,2);
blanket7_vector=operate_each_img(blanket7,128,128,2);
blanket8_vector=operate_each_img(blanket8,128,128,2);
blanket9_vector=operate_each_img(blanket9,128,128,2);

brick1_vector=operate_each_img(brick1,128,128,2);
brick2_vector=operate_each_img(brick2,128,128,2);
brick3_vector=operate_each_img(brick3,128,128,2);
brick4_vector=operate_each_img(brick4,128,128,2);
brick5_vector=operate_each_img(brick5,128,128,2);
brick6_vector=operate_each_img(brick6,128,128,2);
brick7_vector=operate_each_img(brick7,128,128,2);
brick8_vector=operate_each_img(brick8,128,128,2);
brick9_vector=operate_each_img(brick9,128,128,2);

grass1_vector=operate_each_img(grass1,128,128,2);
grass2_vector=operate_each_img(grass2,128,128,2);
grass3_vector=operate_each_img(grass3,128,128,2);
grass4_vector=operate_each_img(grass4,128,128,2);
grass5_vector=operate_each_img(grass5,128,128,2);
grass6_vector=operate_each_img(grass6,128,128,2);
grass7_vector=operate_each_img(grass7,128,128,2);
grass8_vector=operate_each_img(grass8,128,128,2);
grass9_vector=operate_each_img(grass9,128,128,2);

rice1_vector=operate_each_img(rice1,128,128,2);
rice2_vector=operate_each_img(rice2,128,128,2);
rice3_vector=operate_each_img(rice3,128,128,2);
rice4_vector=operate_each_img(rice4,128,128,2);
rice5_vector=operate_each_img(rice5,128,128,2);
rice6_vector=operate_each_img(rice6,128,128,2);
rice7_vector=operate_each_img(rice7,128,128,2);
rice8_vector=operate_each_img(rice8,128,128,2);
rice9_vector=operate_each_img(rice9,128,128,2);

test1_vector=operate_each_img(test1,128,128,2);
test2_vector=operate_each_img(test2,128,128,2);
test3_vector=operate_each_img(test3,128,128,2);
test4_vector=operate_each_img(test4,128,128,2);
test5_vector=operate_each_img(test5,128,128,2);
test6_vector=operate_each_img(test6,128,128,2);
test7_vector=operate_each_img(test7,128,128,2);
test8_vector=operate_each_img(test8,128,128,2);
test9_vector=operate_each_img(test9,128,128,2);
test10_vector=operate_each_img(test10,128,128,2);
test11_vector=operate_each_img(test11,128,128,2);
test12_vector=operate_each_img(test12,128,128,2);

% Get the feature set
train_feature_set=zeros(36,15);
train_feature_set(1,1:15)=blanket1_vector;train_feature_set(2,1:15)=blanket2_vector;
train_feature_set(3,1:15)=blanket3_vector;train_feature_set(4,1:15)=blanket4_vector;
train_feature_set(5,1:15)=blanket5_vector;train_feature_set(6,1:15)=blanket6_vector;
train_feature_set(7,1:15)=blanket7_vector;train_feature_set(8,1:15)=blanket8_vector;
train_feature_set(9,1:15)=blanket9_vector;

train_feature_set(10,1:15)=brick1_vector;train_feature_set(11,1:15)=brick2_vector;
train_feature_set(12,1:15)=brick3_vector;train_feature_set(13,1:15)=brick4_vector;
train_feature_set(14,1:15)=brick5_vector;train_feature_set(15,1:15)=brick6_vector;
train_feature_set(16,1:15)=brick7_vector;train_feature_set(17,1:15)=brick8_vector;
train_feature_set(18,1:15)=brick9_vector;

train_feature_set(19,1:15)=grass1_vector;train_feature_set(20,1:15)=grass2_vector;
train_feature_set(21,1:15)=grass3_vector;train_feature_set(22,1:15)=grass4_vector;
train_feature_set(23,1:15)=grass5_vector;train_feature_set(24,1:15)=grass6_vector;
train_feature_set(25,1:15)=grass7_vector;train_feature_set(26,1:15)=grass8_vector;
train_feature_set(27,1:15)=grass9_vector;

train_feature_set(28,1:15)=rice1_vector;train_feature_set(29,1:15)=rice2_vector;
train_feature_set(30,1:15)=rice3_vector;train_feature_set(31,1:15)=rice4_vector;
train_feature_set(32,1:15)=rice5_vector;train_feature_set(33,1:15)=rice6_vector;
train_feature_set(34,1:15)=rice7_vector;train_feature_set(35,1:15)=rice8_vector;
train_feature_set(36,1:15)=rice9_vector;

test_feature_set=zeros(12,15);
test_feature_set(1,1:15)=test1_vector;test_feature_set(2,1:15)=test2_vector;
test_feature_set(3,1:15)=test3_vector;test_feature_set(4,1:15)=test4_vector;
test_feature_set(5,1:15)=test5_vector;test_feature_set(6,1:15)=test6_vector;
test_feature_set(7,1:15)=test7_vector;test_feature_set(8,1:15)=test8_vector;
test_feature_set(9,1:15)=test9_vector;test_feature_set(10,1:15)=test10_vector;
test_feature_set(11,1:15)=test11_vector;test_feature_set(12,1:15)=test12_vector;

%% Evaluate the discriminant power of those features
% The overall average:
y_aver=sum(train_feature_set)/36; % 1 by 15

% The average within class i:
y_i=zeros(4,15); % 4 by 15
y_i(1,:)=sum(train_feature_set(1:9,:))/9;
y_i(2,:)=sum(train_feature_set(10:18,:))/9;
y_i(3,:)=sum(train_feature_set(19:27,:))/9;
y_i(4,:)=sum(train_feature_set(28:36,:))/9;

% The intra-class sum of squares:
intra_class1=zeros(1,15);
intra_class2=zeros(1,15);
intra_class3=zeros(1,15);
intra_class4=zeros(1,15);
for i=1:1:9
    intra_class1=intra_class1+(train_feature_set(i,:)-y_i(1,:)).^2;
    intra_class2=intra_class2+(train_feature_set(i+9,:)-y_i(2,:)).^2;
    intra_class3=intra_class3+(train_feature_set(i+18,:)-y_i(3,:)).^2;
    intra_class4=intra_class4+(train_feature_set(i+27,:)-y_i(4,:)).^2;
end
intra_class_sum=intra_class1+intra_class2+intra_class3+intra_class4;

% The inter-class sum of squares:
inter_class1=9*((y_i(1,:)-y_aver).^2);
inter_class2=9*((y_i(2,:)-y_aver).^2);
inter_class3=9*((y_i(3,:)-y_aver).^2);
inter_class4=9*((y_i(4,:)-y_aver).^2);
inter_class_sum=inter_class1+inter_class2+inter_class3+inter_class4;

% The discriminant power
dc_power=inter_class_sum./intra_class_sum;
dc_power=dc_power';

%% Feature Reduction:Reduce the feature dimension from 15 to 3 using the PCA
Y_r_train=PCA_demo(train_feature_set,36,15,3);
X1_train=Y_r_train(1:9,1);Y1_tarin=Y_r_train(1:9,2);Z1_train=Y_r_train(1:9,3);
X2_train=Y_r_train(10:18,1);Y2_train=Y_r_train(10:18,2);Z2_train=Y_r_train(10:18,3);
X3_train=Y_r_train(19:27,1);Y3_train=Y_r_train(19:27,2);Z3_train=Y_r_train(19:27,3);
X4_train=Y_r_train(28:36,1);Y4_train=Y_r_train(28:36,2);Z4_train=Y_r_train(28:36,3);
figure;
plot3(X1_train,Y1_tarin,Z1_train,'m.','MarkerSize',15)
hold on
plot3(X2_train,Y2_train,Z2_train,'b.','MarkerSize',15)
plot3(X3_train,Y3_train,Z3_train,'r.','MarkerSize',15)
plot3(X4_train,Y4_train,Z4_train,'g.','MarkerSize',15)
grid on
xlabel('feature1')
ylabel('feature2')
zlabel('feature3')
title('The reduced 3-D feature vector in the feature space')
legend('blanket','brick','grass','rice','Location','NorthEast');
hold off

Y_r_test=PCA_demo_test(train_feature_set,test_feature_set,36,15,3);

%% Part(b):Advanced Texture Classification --- Classifier Explore
%% k-Nearest Neighbor
%% 3-dimension
Y_r_test1=PCA_demo(test_feature_set,12,15,3); % 36by3
% Initialize the cluster centroids
C2=zeros(4,3);
C2(1,1)=Y_r_test1(1,1);C2(1,2)=Y_r_test1(1,2);C2(1,3)=Y_r_test1(1,3);     % 1-9
C2(2,1)=Y_r_test1(2,1);C2(2,2)=Y_r_test1(2,2);C2(2,3)=Y_r_test1(2,3);  % 10-18
C2(3,1)=Y_r_test1(6,1);C2(3,2)=Y_r_test1(6,2);C2(3,3)=Y_r_test1(6,3);  % 19-27
C2(4,1)=Y_r_test1(9,1);C2(4,2)=Y_r_test1(9,2);C2(4,3)=Y_r_test1(9,3);  % 28-36
 
for num=1:1:10000
% Calculate the distance between samples and centroids
distance=zeros(12,4);
for i=1:1:12
    distance(i,1)=square((C2(1,1)-Y_r_test1(i,1))^2+(C2(1,2)-Y_r_test1(i,2))^2+...
                         (C2(1,3)-Y_r_test1(i,3))^2);
    distance(i,2)=square((C2(2,1)-Y_r_test1(i,1))^2+(C2(2,2)-Y_r_test1(i,2))^2+...
                         (C2(2,3)-Y_r_test1(i,3))^2);
    distance(i,3)=square((C2(3,1)-Y_r_test1(i,1))^2+(C2(3,2)-Y_r_test1(i,2))^2+...
                         (C2(3,3)-Y_r_test1(i,3))^2);
    distance(i,4)=square((C2(4,1)-Y_r_test1(i,1))^2+(C2(4,2)-Y_r_test1(i,2))^2+...
                         (C2(4,3)-Y_r_test1(i,3))^2);
end

clusters_label=zeros(12,1);
for i=1:1:12
    min_distance=min(distance(i,:));
    for j=1:1:4
        if distance(i,j)==min_distance
            clusters_label(i)=j;
        end
    end
end

C2_11=0;C2_12=0;C2_13=0;num_C2_1=0;
C2_21=0;C2_22=0;C2_23=0;num_C2_2=0;
C2_31=0;C2_32=0;C2_33=0;num_C2_3=0;
C2_41=0;C2_42=0;C2_43=0;num_C2_4=0;
for i=1:1:12
    if clusters_label(i)==1
        C2_11=C2_11+Y_r_test1(i,1);
        C2_12=C2_12+Y_r_test1(i,2);
        C2_13=C2_13+Y_r_test1(i,3);
        num_C2_1=num_C2_1+1;
    end
    if clusters_label(i)==2
        C2_21=C2_21+Y_r_test1(i,1);
        C2_22=C2_22+Y_r_test1(i,2);
        C2_23=C2_23+Y_r_test1(i,3);
        num_C2_2=num_C2_2+1;
    end
    if clusters_label(i)==3
        C2_31=C2_31+Y_r_test1(i,1);
        C2_32=C2_32+Y_r_test1(i,2);
        C2_33=C2_33+Y_r_test1(i,3);
        num_C2_3=num_C2_3+1;
    end
    if clusters_label(i)==4
        C2_41=C2_41+Y_r_test1(i,1);
        C2_42=C2_42+Y_r_test1(i,2);
        C2_43=C2_43+Y_r_test1(i,3);
        num_C2_4=num_C2_4+1;
    end
end
C2(1,1)=C2_11/num_C2_1;C2(1,2)=C2_12/num_C2_1;C2(1,3)=C2_13/num_C2_1;  
C2(2,1)=C2_21/num_C2_2;C2(2,2)=C2_22/num_C2_2;C2(2,3)=C2_23/num_C2_2;
C2(3,1)=C2_31/num_C2_3;C2(3,2)=C2_32/num_C2_3;C2(3,3)=C2_33/num_C2_3; 
C2(4,1)=C2_41/num_C2_4;C2(4,2)=C2_42/num_C2_4;C2(4,3)=C2_43/num_C2_4; 
end

idx2=zeros(12,1);
for i=1:1:12
    D1=(Y_r_test1(i,1)-C2(1,1))^2+(Y_r_test1(i,2)-C2(1,2))^2;
    D2=(Y_r_test1(i,1)-C2(2,1))^2+(Y_r_test1(i,2)-C2(2,2))^2;
    D3=(Y_r_test1(i,1)-C2(3,1))^2+(Y_r_test1(i,2)-C2(3,2))^2;
    D4=(Y_r_test1(i,1)-C2(4,1))^2+(Y_r_test1(i,2)-C2(4,2))^2;
    D=[D1,D2,D3,D4];
    min_D=min(D);
    if min_D==D1
        idx2(i)=1;
    end
    if min_D==D2
        idx2(i)=2;
    end
    if min_D==D3
        idx2(i)=3;
    end
    if min_D==D4
        idx2(i)=4;
    end
end

%% 15-dimension
test_feature_set; % 12by15

% Initialize the cluster centroids
C2=zeros(4,15);
for i=1:1:15
    C2(1,i)=test_feature_set(1,i);     % 1-9
    C2(2,i)=test_feature_set(2,i);  % 10-18
    C2(3,i)=test_feature_set(6,i);  % 19-27
    C2(4,i)=test_feature_set(9,i);  % 28-36
end
 
for num=1:1:9000
% Calculate the distance between samples and centroids
distance=zeros(12,4);
for i=1:1:12
    sum1=0;sum2=0;sum3=0;sum4=0;
    for j=1:1:15
        sum1=sum1+(C2(1,j)-test_feature_set(i,j))^2;
        sum2=sum2+(C2(2,j)-test_feature_set(i,j))^2;
        sum3=sum3+(C2(3,j)-test_feature_set(i,j))^2;
        sum4=sum4+(C2(4,j)-test_feature_set(i,j))^2;
    end
    distance(i,1)=square(sum1);
    distance(i,2)=square(sum2);
    distance(i,3)=square(sum3);
    distance(i,4)=square(sum4);
end

clusters_label=zeros(12,1);
for i=1:1:12
    min_distance=min(distance(i,:));
    for j=1:1:4
        if distance(i,j)==min_distance
            clusters_label(i)=j;
        end
    end
end

C2_1=zeros(15,1);num_C2_1=0;
C2_2=zeros(15,1);num_C2_2=0;
C2_3=zeros(15,1);num_C2_3=0;
C2_4=zeros(15,1);num_C2_4=0;

for i=1:1:12
    if clusters_label(i)==1
        for j=1:1:15
            C2_1(j,1)=C2_1(j,1)+test_feature_set(i,j);
        end
        num_C2_1=num_C2_1+1;
    end
    if clusters_label(i)==2
        for j=1:1:15
            C2_2(j,1)=C2_2(j,1)+test_feature_set(i,j);
        end
        num_C2_2=num_C2_2+1;
    end
    if clusters_label(i)==3
        for j=1:1:15
            C2_3(j,1)=C2_3(j,1)+test_feature_set(i,j);
        end
        num_C2_3=num_C2_3+1;
    end
    if clusters_label(i)==4
        for j=1:1:15
            C2_4(j,1)=C2_4(j,1)+test_feature_set(i,j);
        end
        num_C2_4=num_C2_4+1;
    end
end
for i=1:1:15
    C2(1,i)=C2_1(i,1)/num_C2_1;
    C2(2,i)=C2_2(i,1)/num_C2_2;
    C2(3,i)=C2_3(i,1)/num_C2_3;
    C2(4,i)=C2_4(i,1)/num_C2_4;
end

idx3=zeros(12,1);
for i=1:1:12
    D=zeros(4,1);
    for k=1:1:4
        for j=1:1:15
            D(k,1)=D(k,1)+(C2(k,j)-test_feature_set(i,j))^2;
        end
    end

    min_D=min(D);
    if min_D==D(1,1)
        idx3(i)=1;
    end
    if min_D==D(2,1)
        idx3(i)=2;
    end
    if min_D==D(3,1)
        idx3(i)=3;
    end
    if min_D==D(4,1)
        idx3(i)=4;
    end
end
end
%%
right_answers=zeros(12,1);
right_answers(1,1)=2;right_answers(2,1)=0;right_answers(3,1)=0;right_answers(4,1)=1;
right_answers(5,1)=3;right_answers(6,1)=2;right_answers(7,1)=1;right_answers(8,1)=3;
right_answers(9,1)=4;right_answers(10,1)=1;right_answers(11,1)=0;right_answers(12,1)=2;
label=zeros(36,1);
label(1:9,1)=1;label(10:18,1)=2;label(19:27,1)=3;label(28:36,1)=4;
%% Random Forest
B=TreeBagger(120,Y_r_train,label);
Yfit=predict(B,Y_r_test);

%% Support Vecor Machine
%   You can use a support vector machine (SVM) when your data has 
% exactly two classes. An SVM classifies data by finding the best 
% hyperplane that separates all data points of one class from those 
% of the other class. The best hyperplane for an SVM means the one 
% with the largest margin between the two classes. Margin means the maximal 
% width of the slab parallel to the hyperplane that has no interior data points

% bimary classification problem
Y_r_train=PCA_demo(train_feature_set,36,15,3); % 36 by 2(features)
    
label=zeros(36,1);  % 36 by 1
label(1:9,1)=1;label(10:18,1)=2;label(19:27,1)=3;label(28:36,1)=4;
label1=zeros(36,1);label2=zeros(36,1);label3=zeros(36,1);label4=zeros(36,1);
label1(1:9,1)=label(1:9,1);label2(10:18,1)=label(10:18,1);
label3(19:27,1)=label(19:27,1);label4(28:36,1)=label(28:36,1);


Y_r_test=PCA_demo_test(train_feature_set,test_feature_set,36,15,3);% 12 by 2(features)
label_new=zeros(12,1);

Md1=fitcsvm(Y_r_train,label1,'Standardize',true,'KernelFunction','rbf');
Md2=fitcsvm(Y_r_train,label2,'Standardize',true,'KernelFunction','rbf');
Md3=fitcsvm(Y_r_train,label3,'Standardize',true,'KernelFunction','rbf');
Md4=fitcsvm(Y_r_train,label4,'Standardize',true,'KernelFunction','rbf');

test_value1=predict(Md1,Y_r_test);
test_value2=predict(Md2,Y_r_test);
test_value3=predict(Md3,Y_r_test);
test_value4=predict(Md4,Y_r_test);
test_value=test_value1+test_value2+test_value3+test_value4;

%% Part(c):Texture Segmentation
%% Display the original image
fid=fopen('comp.raw','r');
comp=fread(fid,[600,450]);fclose(fid);
comp=comp';
imshow(uint8(comp));
imwrite(uint8(comp),'comp.png');
%% Segmentation
% energy feature computation
w_size=51;
comp_vector=operate_each_img_new(comp,450,600,2,w_size);
comp_vector=comp_vector';

% Use the K-means
[idx3,C3] =kmeans(comp_vector,6,'MaxIter',12000);
img_new1=reshape(idx3,450,600);
img_new1=uint8(img_new1*40);
imshow(img_new1)
imwrite(img_new1,'The segmented result.png');

%% Advanced Texture Segmentation
% Post-processing
img_new1_m=img_new1;
for m=1:1:230
    for n=1:1:100
        img_new1_m(m,n)=img_new1(10,200);
    end
end
for m=1:1:170
    for n=1:1:150
        img_new1_m(m,n)=img_new1(10,200);
    end
end
for m=1:1:100
    for n=430:1:600
        img_new1_m(m,n)=img_new1(5,350);
    end
end
for m=1:1:190
    for n=480:1:600
        img_new1_m(m,n)=img_new1(5,350);
    end
end
for m=370:1:450
    for n=1:1:250
        img_new1_m(m,n)=img_new1(300,5);
    end
end
for m=250:1:290
    for n=1:1:100
        img_new1_m(m,n)=img_new1(300,5);
    end
end
for m=225:1:450
    for n=510:1:600
        img_new1_m(m,n)=img_new1(450,590);
    end
end
imshow(img_new1_m)
imwrite(img_new1_m,'The modified segmented result.png');


%% Problem 2:Image Feature Extractors
%% Part(a):Salient Point Descriptor
%% Display the original images
img_Husky1=imread('Husky_1.jpg');
img_Husky2=imread('Husky_2.jpg');
img_Husky3=imread('Husky_3.jpg');
img_Puppy1=imread('Puppy_1.jpg');
%% Part(b):Image Matching
%% Question(1)
img1=single(rgb2gray(img_Husky1));
img3=single(rgb2gray(img_Husky3));
[f1,d1]=vl_sift(img1,'Levels',5,'PeakThresh',4);
[f3,d3]=vl_sift(img3,'Levels',5,'PeakThresh',4);
% Pick the largest scale in Husky_3
figure;
image(img_Husky3);   
axis image
hold on
max_scale3=max(f3(3,:));
for i=1:1:size(f3,2)
    if f3(3,i)==max_scale3
        x3_value=f3(1,i);
        y3_value=f3(2,i);
        f3_location=i;
        f3_angel=atan(f3(4,i));
        break
    end 
end
plot(x3_value,y3_value,'o','color','r','MarkerSize',max_scale3,'LineWidth',1.5);
line([x3_value,x3_value+max_scale3*cos(f3_angel)],[y3_value,y3_value+max_scale3*sin(f3_angel)],...
     'linestyle','-','color','r','LineWidth',1.5);
saveas(gcf, 'The key point with the largest scale in H3.png')
hold off
%%
com_fig=zeros(size(img3,1),size(img3,2)+size(img1,2),3);  
com_fig(:,1:size(img3,2),:)=img_Husky3;
com_fig(1:size(img1,1),(size(img3,2)+1):end,:)=img_Husky1;
com_fig=uint8(com_fig);
[matches3,scores3]=vl_ubcmatch(d3,d1,1);

for i=1:1:size(matches3,2)
    if matches3(1,i)==f3_location
        f1_location=matches3(2,i);
    end
end
for i=1:1:size(f1,2)
    if i==f1_location
        x1_value=f1(1,i)+size(img3,2);
        y1_value=f1(2,i);
        scale1=f1(3,i);
        angel1=atan(f1(4,i));
        break
    end 
end

%% Find its cloest neighboring keypoint in Husky_1
figure;
image(com_fig);   
axis image
hold on
plot(x3_value,y3_value,'o','color','r','MarkerSize',max_scale3,'LineWidth',1.5);
line([x3_value,x3_value+max_scale3*cos(f3_angel)],[y3_value,y3_value+max_scale3*sin(f3_angel)],...
     'linestyle','-','color','r','LineWidth',1.5);
plot(x1_value,y1_value,'o','color','r','MarkerSize',scale1,'LineWidth',1.5);
line([x1_value,x1_value+scale1*cos(angel1)],[y1_value,y1_value+scale1*sin(angel1)],...
     'linestyle','-','color','r','LineWidth',1.5);
line([x1_value,x3_value],[y1_value,y3_value],...
     'linestyle','-','color','g','LineWidth',1.5);
saveas(gcf, 'The cloest neighboring keypoint in H1.png')
hold off
%%
m1=img_match(img_Husky1,img_Husky3);

%%
m2=img_match(img_Husky3,img_Husky2);
%%
m3=img_match(img_Husky3,img_Puppy1);
%%
m4=img_match(img_Husky1,img_Puppy1);

%% Part(c):Bag of Words
%% Create codewrods for all four images
% For the image "Husky_1"
img_H1=single(rgb2gray(img_Husky1));
[f1,d1]=vl_sift(img_H1,'Levels',5,'PeakThresh',4);
d1=double(d1);
[idx1,C1] =kmeans(d1',8,'MaxIter',8000);

min_class1=min(idx1);
max_class1=max(idx1);
feature_vector_numb1=zeros(max_class1,1);
for i=1:1:length(idx1)
    class1=idx1(i);
    feature_vector_numb1(class1)=feature_vector_numb1(class1)+1;
end
figure(1)
b1=bar(feature_vector_numb1,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);
xlabel('The different kinds of feature vectors')
ylabel('The frequency of different kinds of feature vectors')
title({'The histogram of codewords for the image "Husky1"'})

% For the image "Husky_2"
img_H2=single(rgb2gray(img_Husky2));
[f2,d2]=vl_sift(img_H2,'Levels',5,'PeakThresh',4);
d2=double(d2);
[idx2,C2] =kmeans(d2',8,'MaxIter',8000);

min_class2=min(idx2);
max_class2=max(idx2);
feature_vector_numb2=zeros(max_class2,1);
for i=1:1:length(idx2)
    class2=idx2(i);
    feature_vector_numb2(class2)=feature_vector_numb2(class2)+1;
end
figure(2)
b2=bar(feature_vector_numb2,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);
xlabel('The different kinds of feature vectors')
ylabel('The frequency of different kinds of feature vectors')
title({'The histogram of codewords for the image "Husky2"'})

% For the image "Husky_3"
img_H3=single(rgb2gray(img_Husky3));
[f3,d3]=vl_sift(img_H3,'Levels',5,'PeakThresh',4);
d3=double(d3);
[idx3,C3] =kmeans(d3',8,'MaxIter',8000);

min_class3=min(idx3);
max_class3=max(idx3);
feature_vector_numb3=zeros(max_class3,1);
for i=1:1:length(idx3)
    class3=idx3(i);
    feature_vector_numb3(class3)=feature_vector_numb3(class3)+1;
end
figure(3)
b3=bar(feature_vector_numb3,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);
xlabel('The different kinds of feature vectors')
ylabel('The frequency of different kinds of feature vectors')
title({'The histogram of codewords for the image "Husky3"'})

% For the image "Puppy_1"
img_P1=single(rgb2gray(img_Puppy1));
[f4,d4]=vl_sift(img_P1,'Levels',5,'PeakThresh',4);
d4=double(d4);
[idx4,C4] =kmeans(d4',8,'MaxIter',8000);

min_class4=min(idx4);
max_class4=max(idx4);
feature_vector_numb4=zeros(max_class4,1);
for i=1:1:length(idx4)
    class4=idx4(i);
    feature_vector_numb4(class4)=feature_vector_numb4(class4)+1;
end
figure(4)
b4=bar(feature_vector_numb4,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);
xlabel('The different kinds of feature vectors')
ylabel('The frequency of different kinds of feature vectors')
title({'The histogram of codewords for the image "Puppy1"'})
    
%% Match Husky_3's codewords with other images
img_H1=single(rgb2gray(img_Husky1));
[f1,d1]=vl_sift(img_H1,'Levels',5,'PeakThresh',4);
d1=double(d1);
[idx1,C1] =kmeans(d1',8,'MaxIter',8000);

img_H2=single(rgb2gray(img_Husky2));
[f2,d2]=vl_sift(img_H2,'Levels',5,'PeakThresh',4);
d2=double(d2);
[idx2,C2] =kmeans(d2',8,'MaxIter',8000);

img_H3=single(rgb2gray(img_Husky3));
[f3,d3]=vl_sift(img_H3,'Levels',5,'PeakThresh',4);
d3=double(d3);
[idx3,C3] =kmeans(d3',8,'MaxIter',8000);

img_P1=single(rgb2gray(img_Puppy1));
[f4,d4]=vl_sift(img_P1,'Levels',5,'PeakThresh',4);
d4=double(d4);
[idx4,C4] =kmeans(d4',8,'MaxIter',8000);
%%
idx1_comp=img_comp(d1',C3);
min_class1_comp=min(idx1_comp);
max_class1_comp=max(idx1_comp);
feature_vector_numb1_comp=zeros(max_class1_comp,1);
for i=1:1:length(idx1_comp)
    class1_comp=idx1_comp(i);
    feature_vector_numb1_comp(class1_comp)=feature_vector_numb1_comp(class1_comp)+1;
end
figure;
b1_comp=bar(feature_vector_numb1_comp,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);
xlabel('The different kinds of feature vectors')
ylabel('The frequency of different kinds of feature vectors')
title({'The histogram of codewords for "Husky1" to match "Husky3"'})
%%
idx2_comp=img_comp(d2',C3);
min_class2_comp=min(idx2_comp);
max_class2_comp=max(idx2_comp);
feature_vector_numb2_comp=zeros(max_class2_comp,1);
for i=1:1:length(idx2_comp)
    class2_comp=idx2_comp(i);
    feature_vector_numb2_comp(class2_comp)=feature_vector_numb2_comp(class2_comp)+1;
end
figure;
b2_comp=bar(feature_vector_numb2_comp,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);
xlabel('The different kinds of feature vectors')
ylabel('The frequency of different kinds of feature vectors')
title({'The histogram of codewords for "Husky2" to match "Husky3"'})

%%
idx4_comp=img_comp(d4',C3);
min_class4_comp=min(idx4_comp);
max_class4_comp=max(idx4_comp);
feature_vector_numb4_comp=zeros(max_class4_comp,1);
for i=1:1:length(idx4_comp)
    class4_comp=idx4_comp(i);
    feature_vector_numb4_comp(class4_comp)=feature_vector_numb4_comp(class4_comp)+1;
end
figure;
b4_comp=bar(feature_vector_numb4_comp,'FaceColor',[0 .6 .6],'EdgeColor',[0 .8 .8],'LineWidth',1.5);
xlabel('The different kinds of feature vectors')
ylabel('The frequency of different kinds of feature vectors')
title({'The histogram of codewords for "Puppy1" to match "Husky3"'})


%% For the image "Husky_1" and the image "Husky_3"
r1=img_Husky1;r2=img_Husky3;
x=0:1:255;
 
R1 = r1(:,:,1);
G1 = r1(:,:,2);  
B1 = r1(:,:,3);
H_R1=imhist(R1);
H_G1=imhist(G1);
H_B1=imhist(B1);
 
R2 = r2(:,:,1);  
G2 = r2(:,:,2);  
B2 = r2(:,:,3);  
H_R2=imhist(R2);
H_G2=imhist(G2);
H_B2=imhist(B2);
 
t1=0;n1=0;m1=0;
t2=0;n2=0;m2=0;
t3=0;n3=0;m3=0;
for i=1:length(H_R1)
    y1=[];                % R
    if H_R1(i)~=H_R2(i)
        y1=min([H_R1(i),H_R2(i)]);
    else
        y1=H_R1(i);
    end
    L1(i)=y1;
    t1=t1+L1(i);
    n1=n1+H_R1(i);
    m1=m1+H_R2(i);
    
    y2=[];                % G
    if H_G1(i)~=H_G2(i)
        y2=min([H_G1(i),H_G2(i)]);
    else
        y2=H_G1(i);
    end
    L2(i)=y2;
    t2=t2+L2(i);
    n2=n2+H_G1(i);
    m2=m2+H_G2(i);
    
    y3=[];                % B
    if H_B1(i)~=H_B2(i)
        y3=min([H_B1(i),H_B2(i)]);
    else
        y3=H_B1(i);
    end
    L3(i)=y3;
    t3=t3+L2(i);
    n3=n3+H_B1(i);
    m3=m3+H_B2(i);
    
end
s1=min([n1,m1]);
fin1=(t1/s1);% The similarity between R
 
s2=min([n2,m2]);
fin2=(t2/s2);% The similarity between G
 
s3=min([n3,m3]);
fin3=(t3/s3); % The similarity between B
 
fin=mean([fin1,fin2,fin3]); % The finial similarity


subplot(231);imshow(r1);title('The image "Husky1"');
subplot(232);imshow(r2);title('The image "Husky3');
subplot(233);text(0.5,.5,{'The degrees of similarity is',num2str(fin)},...
                          'FontSize',7,'HorizontalAlignment','center');

subplot(234);plot(x,H_R1,'b',x,H_R2,'r:');
             title('The R channel');...
             legend('Husky1','Husky3');
subplot(235);plot(x,H_G1,'b',x,H_G2,'r:');
             title('The G channel');
             legend('Husky1','Husky3');
subplot(236);plot(x,H_B1,'b',x,H_B2,'r:');
             title('The B channel');
             legend('Husky1','Husky3');
%% For the image "Husky_2" and the image "Husky_3"
r1=img_Husky2;r2=img_Husky3;
x=0:1:255;
 
R1 = r1(:,:,1);
G1 = r1(:,:,2);  
B1 = r1(:,:,3);
H_R1=imhist(R1);
H_G1=imhist(G1);
H_B1=imhist(B1);
 
R2 = r2(:,:,1);  
G2 = r2(:,:,2);  
B2 = r2(:,:,3);  
H_R2=imhist(R2);
H_G2=imhist(G2);
H_B2=imhist(B2);
 
 
t1=0;n1=0;m1=0;
t2=0;n2=0;m2=0;
t3=0;n3=0;m3=0;
for i=1:length(H_R1)
    y1=[];                % R
    if H_R1(i)~=H_R2(i)
        y1=min([H_R1(i),H_R2(i)]);
    else
        y1=H_R1(i);
    end
    L1(i)=y1;
    t1=t1+L1(i);
    n1=n1+H_R1(i);
    m1=m1+H_R2(i);
    
     y2=[];                % G
    if H_G1(i)~=H_G2(i)
        y2=min([H_G1(i),H_G2(i)]);
    else
        y2=H_G1(i);
    end
    L2(i)=y2;
    t2=t2+L2(i);
    n2=n2+H_G1(i);
    m2=m2+H_G2(i);
    
    y3=[];                % B
    if H_B1(i)~=H_B2(i)
        y3=min([H_B1(i),H_B2(i)]);
    else
        y3=H_B1(i);
    end
    L3(i)=y3;
    t3=t3+L2(i);
    n3=n3+H_B1(i);
    m3=m3+H_B2(i);
    
end
s1=min([n1,m1]);
fin1=(t1/s1);% The similarity between R
 
s2=min([n2,m2]);
fin2=(t2/s2);% The similarity between G
 
s3=min([n3,m3]);
fin3=(t3/s3);% The similarity between B

fin=mean([fin1,fin2,fin3]);% The finial similarity 


subplot(231);imshow(r1);title('The image "Husky2"');
subplot(232);imshow(r2);title('The image "Husky3');
subplot(233);text(0.5,.5,{'The degrees of similarity is',num2str(fin)},...
                          'FontSize',7,'HorizontalAlignment','center');

subplot(234);plot(x,H_R1,'b',x,H_R2,'r:');
             title('The R channel');...
             legend('Husky2','Husky3');
subplot(235);plot(x,H_G1,'b',x,H_G2,'r:');
             title('The G channel');
             legend('Husky2','Husky3');
subplot(236);plot(x,H_B1,'b',x,H_B2,'r:');
             title('The B channel');
             legend('Husky2','Husky3');
             
%% For the image "Puppy_1" and the image "Husky_3"
r1=img_Puppy1;r2=img_Husky3;
x=0:1:255;
 
R1 = r1(:,:,1);
G1 = r1(:,:,2);  
B1 = r1(:,:,3);
H_R1=imhist(R1);
H_G1=imhist(G1);
H_B1=imhist(B1);
 
R2 = r2(:,:,1);  
G2 = r2(:,:,2);  
B2 = r2(:,:,3);  
H_R2=imhist(R2);
H_G2=imhist(G2);
H_B2=imhist(B2);
 
 
t1=0;n1=0;m1=0;
t2=0;n2=0;m2=0;
t3=0;n3=0;m3=0;
for i=1:length(H_R1)
    y1=[];                % R
    if H_R1(i)~=H_R2(i)
        y1=min([H_R1(i),H_R2(i)]);
    else
        y1=H_R1(i);
    end
    L1(i)=y1;
    t1=t1+L1(i);
    n1=n1+H_R1(i);
    m1=m1+H_R2(i);
    
     y2=[];                % G
    if H_G1(i)~=H_G2(i)
        y2=min([H_G1(i),H_G2(i)]);
    else
        y2=H_G1(i);
    end
    L2(i)=y2;
    t2=t2+L2(i);
    n2=n2+H_G1(i);
    m2=m2+H_G2(i);
    
    y3=[];                % B
    if H_B1(i)~=H_B2(i)
        y3=min([H_B1(i),H_B2(i)]);
    else
        y3=H_B1(i);
    end
    L3(i)=y3;
    t3=t3+L2(i);
    n3=n3+H_B1(i);
    m3=m3+H_B2(i);
    
end
s1=min([n1,m1]);
fin1=(t1/s1);% The similarity between R
 
s2=min([n2,m2]);
fin2=(t2/s2);% The similarity between G
 
s3=min([n3,m3]);
fin3=(t3/s3);% The similarity between B
 
fin=mean([fin1,fin2,fin3]);% The finial similarity 


subplot(231);imshow(r1);title('The image "Puppy1"');
subplot(232);imshow(r2);title('The image "Husky3');
subplot(233);text(0.5,.5,{'The degrees of similarity is',num2str(fin)},...
                          'FontSize',7,'HorizontalAlignment','center');

subplot(234);plot(x,H_R1,'b',x,H_R2,'r:');
             title('The R channel');...
             legend('Puppy1','Husky3');
subplot(235);plot(x,H_G1,'b',x,H_G2,'r:');
             title('The G channel');
             legend('Puppy1','Husky3');
subplot(236);plot(x,H_B1,'b',x,H_B2,'r:');
             title('The B channel');
             legend('Puppy1','Husky3');






