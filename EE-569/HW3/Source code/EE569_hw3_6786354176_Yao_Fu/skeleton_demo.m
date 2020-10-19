% EE569 Homework Assignment #3:Problem2_part(a) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the skeletonizing

function output_img=skeleton_demo(input_img,height,width)

% get numbers of bounds at each pixel as a matrix
bound_nums=bound_matrix(input_img,height,width);

% Extend the boundaries of images by padding zeros
ext_num=1;
ext_input_img=zeros(height+ext_num*2,width+ext_num*2);
for m=1:1:height
    for n=1:1:width
        ext_input_img(m+ext_num,n+ext_num)=input_img(m,n);
    end
end

% Look up the conditional mark patterns
mark_matrix=zeros(height,width); % '1' means marking the pixel,'0' means not. 
for m=1:1:height
    for n=1:1:width
        if ext_input_img(m+ext_num,n+ext_num)==1
            E11=ext_input_img(m+ext_num-1,n+ext_num-1);
            E12=ext_input_img(m+ext_num-1,n+ext_num);
            E13=ext_input_img(m+ext_num-1,n+ext_num+1);
            E21=ext_input_img(m+ext_num,n+ext_num-1);
            E22=ext_input_img(m+ext_num,n+ext_num);
            E23=ext_input_img(m+ext_num,n+ext_num+1);
            E31=ext_input_img(m+ext_num+1,n+ext_num-1);
            E32=ext_input_img(m+ext_num+1,n+ext_num);
            E33=ext_input_img(m+ext_num+1,n+ext_num+1);
            input_matrix=[E11,E12,E13;E21,E22,E23;E31,E32,E33];
            if bound_nums(m,n)==4
                pattern1=[0,0,1;0,1,1;0,0,1];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[1,1,1;0,1,0;0,0,0];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,0,0;1,1,0;1,0,0];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[0,0,0;0,1,0;1,1,1];
                value4=condi_match(input_matrix,pattern4);
                pattern5=[0,1,0;0,1,1;0,0,0];
                value5=condi_match(input_matrix,pattern5);
                pattern6=[0,1,0;1,1,0;0,0,0];
                value6=condi_match(input_matrix,pattern6);
                pattern7=[0,0,0;1,1,0;0,1,0];
                value7=condi_match(input_matrix,pattern7);
                pattern8=[0,0,0;0,1,1;0,1,0];
                value8=condi_match(input_matrix,pattern8);
                
                if value1||value2||value3||value4||...
                   value5||value6||value7||value8==1
                    mark_matrix(m,n)=1;
                end
            end
            if bound_nums(m,n)==6
                pattern1=[1,1,1;0,1,1;0,0,0];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[0,1,1;0,1,1;0,0,1];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,1,1;1,1,0;0,0,0];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[1,1,0;1,1,0;1,0,0];
                value4=condi_match(input_matrix,pattern4);
                pattern5=[1,0,0;1,1,0;1,1,0];
                value5=condi_match(input_matrix,pattern5);
                pattern6=[0,0,0;1,1,0;1,1,1];
                value6=condi_match(input_matrix,pattern6);
                pattern7=[0,0,0;0,1,1;1,1,1];
                value7=condi_match(input_matrix,pattern7);
                pattern8=[0,0,1;0,1,1;0,1,1];
                value8=condi_match(input_matrix,pattern8);
                if value1||value2||value3||value4||value5||value6||value7||value8==1
                    mark_matrix(m,n)=1;
                end 
            end
            if bound_nums(m,n)==7
                pattern1=[1,1,1;0,1,1;0,0,1];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[1,1,1;1,1,0;1,0,0];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,0,0;1,1,0;1,1,1];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[0,0,1;0,1,1;1,1,1];
                value4=condi_match(input_matrix,pattern4);
                if value1||value2||value3||value4==1
                    mark_matrix(m,n)=1;
                end
            end
            if bound_nums(m,n)==8
                pattern1=[0,1,1;0,1,1;0,1,1];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[1,1,1;1,1,1;0,0,0];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,1,0;1,1,0;1,1,0];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[0,0,0;1,1,1;1,1,1];
                value4=condi_match(input_matrix,pattern4);
                if value1||value2||value3||value4==1
                    mark_matrix(m,n)=1;
                end
            end
            if bound_nums(m,n)==9
                pattern1=[1,1,1;0,1,1;0,1,1];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[0,1,1;0,1,1;1,1,1];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,1,1;1,1,1;1,0,0];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[1,1,1;1,1,1;0,0,1];
                value4=condi_match(input_matrix,pattern4);
                pattern5=[1,1,1;1,1,0;1,1,0];
                value5=condi_match(input_matrix,pattern5);
                pattern6=[1,1,0;1,1,0;1,1,1];
                value6=condi_match(input_matrix,pattern6);
                pattern7=[1,0,0;1,1,1;1,1,1];
                value7=condi_match(input_matrix,pattern7);
                pattern8=[0,0,1;1,1,1;1,1,1];
                value8=condi_match(input_matrix,pattern8);
                if value1||value2||value3||value4||value5||value6||value7||value8==1
                    mark_matrix(m,n)=1;
                end 
            end
            if bound_nums(m,n)==10
                pattern1=[1,1,1;0,1,1;1,1,1];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[1,1,1;1,1,1;1,0,1];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,1,1;1,1,0;1,1,1];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[1,0,1;1,1,1;1,1,1];
                value4=condi_match(input_matrix,pattern4);
                if value1||value2||value3||value4==1
                    mark_matrix(m,n)=1;
                end
            end
            if bound_nums(m,n)==11
                pattern1=[1,1,1;1,1,1;0,1,1];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[1,1,1;1,1,1;1,1,0];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,1,0;1,1,1;1,1,1];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[0,1,1;1,1,1;1,1,1];
                value4=condi_match(input_matrix,pattern4);
                if value1||value2||value3||value4==1
                    mark_matrix(m,n)=1;
                end
            end
        end
    end
end


% Look up the unconditional mark patterns
% Extend the boundaries of mark matrix by padding zeros
ext_num=1;
ext_mark_matrix=zeros(height+ext_num*2,width+ext_num*2);
for m=1:1:height
    for n=1:1:width
        ext_mark_matrix(m+ext_num,n+ext_num)=mark_matrix(m,n);
    end
end

for m=1+ext_num:1:height+ext_num
    for n=1+ext_num:1:width+ext_num
        temp_value=0;
        if ext_mark_matrix(m,n)==1
            E11=ext_mark_matrix(m-1,n-1);
            E12=ext_mark_matrix(m-1,n);
            E13=ext_mark_matrix(m-1,n+1);
            E21=ext_mark_matrix(m,n-1);
            E22=ext_mark_matrix(m,n);
            E23=ext_mark_matrix(m,n+1);
            E31=ext_mark_matrix(m+1,n-1);
            E32=ext_mark_matrix(m+1,n);
            E33=ext_mark_matrix(m+1,n+1);
            input_matrix=[E11,E12,E13;E21,E22,E23;E31,E32,E33];

            % Spur
            pattern1=[0,0,0;0,1,0;0,0,1];
            value1=condi_match(input_matrix,pattern1);
            pattern2=[0,0,0;0,1,0;1,0,0];
            value2=condi_match(input_matrix,pattern2);
            pattern3=[0,0,1;0,1,0;0,0,0];
            value3=condi_match(input_matrix,pattern3);
            pattern4=[1,0,0;0,1,0;0,0,0];
            value4=condi_match(input_matrix,pattern4);
            
            temp_value=temp_value||value1||value2||value3||value4;
            
          % Single 4-connection
            pattern5=[0,0,0;0,1,0;0,1,0];
            value5=condi_match(input_matrix,pattern5);
            pattern6=[0,0,0;0,1,1;0,0,0];
            value6=condi_match(input_matrix,pattern6);
            pattern7=[0,0,0;1,1,0;0,0,0];
            value7=condi_match(input_matrix,pattern7);
            pattern8=[0,1,0;0,1,0;0,0,0];
            value8=condi_match(input_matrix,pattern8);
            
            temp_value=temp_value||value5||value6||value7||value8;
            
            % L Corner
            pattern9=[0,1,0;0,1,1;0,0,0];
            value9=condi_match(input_matrix,pattern9);
            pattern10=[0,1,0;1,1,0;0,0,0];
            value10=condi_match(input_matrix,pattern10);
            pattern11=[0,0,0;0,1,1;0,1,0];
            value11=condi_match(input_matrix,pattern11);
            pattern12=[0,0,0;1,1,0;0,1,0];
            value12=condi_match(input_matrix,pattern12);
            
            temp_value=temp_value||value9||value10||value11||value12;

            % Corner Cluster
            value13=0;
            if and(and(E11,E12),and(E21,E22))==1
                value13=1;
            end
            value14=0;
            if and(and(E22,E23),and(E32,E33))==1
                value14=1;
            end
            temp_value=temp_value||value13||value14;
            
            % Tee Branch
            value15=0;
            if E12&&E21&&E22&&E23==1
                value15=1;
            end
            value16=0;
            if E12&&E21&&E22&&E32==1
                value16=1;
            end
            value17=0;
            if E21&&E22&&E23&&E32==1
                value17=1;
            end
            value18=0;
            if E12&&E22&&E23&&E32==1
                value18=1;
            end

            temp_value=temp_value||value15||value16||value17||value18;
            
            % Vee Branch
            value19=0;value20=0;value21=0;value22=0;
            if E11==1 && E13==1
                if E31==1 || E32==1 || E33==1
                    value19=1;
                end
            end
            if E11==1 && E31==1
                if E13==1 || E23==1 || E33==1
                    value20=1;
                end
            end
            if E31==1 && E33==1
                if E11==1 || E12==1 || E13==1
                    value21=1;
                end
            end
            if E13==1 && E33==1
                if E11==1 || E21==1 || E31==1
                    value22=1;
                end
            end
            
            temp_value=temp_value||value19||value20||value21||value22;

            % Digonal Branch
            pattern231=[1,1,0;0,1,1;1,0,1];
            value231=condi_match(input_matrix,pattern231);
            pattern232=[0,1,0;0,1,1;1,0,1];
            value232=condi_match(input_matrix,pattern232);
            pattern233=[1,1,0;0,1,1;1,0,0];
            value233=condi_match(input_matrix,pattern233);
            pattern234=[0,1,0;0,1,1;1,0,0];
            value234=condi_match(input_matrix,pattern234);
            
            temp_value=temp_value||value231||value232||value233||value234;
            
            pattern241=[0,1,1;1,1,0;1,0,1];
            value241=condi_match(input_matrix,pattern241);
            pattern242=[0,1,0;1,1,0;1,0,1];
            value242=condi_match(input_matrix,pattern242);
            pattern243=[0,1,1;1,1,0;0,0,1];
            value243=condi_match(input_matrix,pattern243);
            pattern244=[0,1,0;1,1,0;0,0,1];
            value244=condi_match(input_matrix,pattern244);
            
            temp_value=temp_value||value241||value242||value243||value244;
            
            pattern251=[1,0,1;1,1,0;0,1,1];
            value251=condi_match(input_matrix,pattern251);
            pattern252=[0,0,1;1,1,0;0,1,1];
            value252=condi_match(input_matrix,pattern252);
            pattern253=[1,0,1;1,1,0;0,1,0];
            value253=condi_match(input_matrix,pattern253);
            pattern254=[0,0,1;1,1,0;0,1,0];
            value254=condi_match(input_matrix,pattern254);
            
            temp_value=temp_value||value251||value252||value253||value254;
            
            pattern261=[1,0,1;0,1,1;1,1,0];
            value261=condi_match(input_matrix,pattern261);
            pattern262=[1,0,0;0,1,1;1,1,0];
            value262=condi_match(input_matrix,pattern262);
            pattern263=[1,0,1;0,1,1;0,1,0];
            value263=condi_match(input_matrix,pattern263);
            pattern264=[1,0,0;0,1,1;0,1,0];
            value264=condi_match(input_matrix,pattern264);
            
            temp_value=temp_value||value261||value262||value263||value264;
        end
        
        if temp_value==1
           mark_matrix(m-ext_num,n-ext_num)=0;
        end
            
    end
end       
            
% get the new output image
output_img=zeros(height,width);
for m=1:1:height
    for n=1:1:width
        if mark_matrix(m,n)==0
            output_img(m,n)=input_img(m,n);
        end
    end
end