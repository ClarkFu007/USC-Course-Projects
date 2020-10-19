% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the principle component analysis(PCA)

function Y_r=PCA_demo_test(feature_matrix,feature_test,height,width,d)

% Compute mean
m_X=zeros(width,1);
sum=0;
for n=1:1:width
    for m=1:1:height
        sum=sum+feature_matrix(m,n);
    end
    m_X(n,1)=sum/height;
    sum=0;
end

% Subtract mean to get zero data matrix Y
Y=zeros(height,width);
for m=1:1:height
    for n=1:1:width
        Y(m,n)=feature_matrix(m,n)-m_X(n);
    end
end

% Computen SVD of Y: Y=U*S*V' 
[U,S,V]=svd(Y);

% Dimensionality reduction
S_r=S(:,1:d);
V_r=V(:,1:d);
Y_r=feature_test*V_r;