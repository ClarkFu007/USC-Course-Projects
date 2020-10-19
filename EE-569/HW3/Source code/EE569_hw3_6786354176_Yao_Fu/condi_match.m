% EE569 Homework Assignment #3:Problem2_part(a) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the conditional match

function value=condi_match(input_matrix,pattern)
flag=0;
for m=1:1:3
    for n=1:1:3
        if input_matrix(m,n)==pattern(m,n)
            flag=flag+1;
        else
            break
        end
    end
end
if flag==9
    value=1;
else
    value=0;
end