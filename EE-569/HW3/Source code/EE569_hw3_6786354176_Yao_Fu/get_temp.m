% EE569 Homework Assignment #3:Problem2_part(d) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to get the temporary value for comparison

function temp_value=get_temp(input_matrix,m,n)

a11=input_matrix(m-1,n-1);a12=input_matrix(m-1,n);a13=input_matrix(m-1,n+1);
a21=input_matrix(m,n-1);a22=input_matrix(m,n);a23=input_matrix(m,n+1);
a31=input_matrix(m+1,n-1);a32=input_matrix(m+1,n);a33=input_matrix(m+1,n+1);

temp_value=a11||a12||a13||a21||a22||a23||a31||a32||a33;
end