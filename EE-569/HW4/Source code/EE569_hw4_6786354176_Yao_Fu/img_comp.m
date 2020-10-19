% EE569 Homework Assignment #4
% Submission Date: March 22, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to compare images' similarity

function idx_new=img_comp(d1,C2)
row_num=size(d1,1);
column_num=size(d1,2);

distance=zeros(row_num,8);
for m=1:1:row_num
    for n=1:1:8
        for i=1:1:column_num
            distance(m,n)=distance(m,n)+(d1(m,i)-C2(n,i))^2;
        end
    end
end

idx_new=zeros(row_num,1);
for m=1:1:row_num
    min_dist=min(distance(m,:));
    for n=1:1:8
        if distance(m,n)==min_dist
            idx_new(m,1)=n;
            break
        end   
    end
end

end
