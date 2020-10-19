% EE569 Homework Assignment #3:Problem2_part(a) 
% Submission Date: March 3, 2020
% Name: Yao Fu
% USC ID: 6786354176
% Email: yaof@usc.edu
% Goal: The function to do the shrinking

function output_img=shrink_demo(input_img,height,width)

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
            if bound_nums(m,n)==1
                mark_matrix(m,n)=1;
            end
            if bound_nums(m,n)==2
                pattern1=[0,0,0;0,1,1;0,0,0];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[0,1,0;0,1,0;0,0,0];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[0,0,0;1,1,0;0,0,0];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[0,0,0;0,1,0;0,1,0];
                value4=condi_match(input_matrix,pattern4);
                if value1||value2||value3||value4==1
                    mark_matrix(m,n)=1;
                end
            end
            if bound_nums(m,n)==3
                pattern1=[0,0,1;0,1,1;0,0,0];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[0,1,1;0,1,0;0,0,0];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,1,0;0,1,0;0,0,0];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[1,0,0;1,1,0;0,0,0];
                value4=condi_match(input_matrix,pattern4);
                pattern5=[0,0,0;1,1,0;1,0,0];
                value5=condi_match(input_matrix,pattern5);
                pattern6=[0,0,0;0,1,0;1,1,0];
                value6=condi_match(input_matrix,pattern6);
                pattern7=[0,0,0;0,1,0;0,1,1];
                value7=condi_match(input_matrix,pattern7);
                pattern8=[0,0,0;0,1,1;0,0,1];
                value8=condi_match(input_matrix,pattern8);
                if value1||value2||value3||value4||value5||value6||value7||value8==1
                    mark_matrix(m,n)=1;
                end 
            end
            if bound_nums(m,n)==4
                pattern1=[0,0,1;0,1,1;0,0,1];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[1,1,1;0,1,0;0,0,0];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[1,0,0;1,1,0;1,0,0];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[0,0,0;0,1,0;1,1,1];
                value4=condi_match(input_matrix,pattern4);
                if value1||value2||value3||value4==1
                    mark_matrix(m,n)=1;
                end
            end
            if bound_nums(m,n)==5
                pattern1=[1,1,0;0,1,1;0,0,0];
                value1=condi_match(input_matrix,pattern1);
                pattern2=[0,1,0;0,1,1;0,0,1];
                value2=condi_match(input_matrix,pattern2);
                pattern3=[0,1,1;1,1,0;0,0,0];
                value3=condi_match(input_matrix,pattern3);
                pattern4=[0,0,1;0,1,1;0,1,0];
                value4=condi_match(input_matrix,pattern4);
                pattern5=[0,1,1;0,1,1;0,0,0];
                value5=condi_match(input_matrix,pattern5);
                pattern6=[1,1,0;1,1,0;0,0,0];
                value6=condi_match(input_matrix,pattern6);
                pattern7=[0,0,0;1,1,0;1,1,0];
                value7=condi_match(input_matrix,pattern7);
                pattern8=[0,0,0;0,1,1;0,1,1];
                value8=condi_match(input_matrix,pattern8);
                if value1||value2||value3||value4||value5||value6||value7||value8==1
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
                pattern9=[1,1,0;0,1,1;0,0,1];
                value9=condi_match(input_matrix,pattern9);
                pattern10=[0,1,1;1,1,0;1,0,0];
                value10=condi_match(input_matrix,pattern10);
                if value1||value2||value3||value4||value5||value6||value7||value8||value9||value10==1
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
            pattern1=[0,0,1;0,1,0;0,0,0];
            value1=condi_match(input_matrix,pattern1);
            pattern2=[1,0,0;0,1,0;0,0,0];
            value2=condi_match(input_matrix,pattern2);
            
            % Single 4-connection
            pattern3=[0,0,0;0,1,0;0,1,0];
            value3=condi_match(input_matrix,pattern3);
            pattern4=[0,0,0;0,1,1;0,0,0];
            value4=condi_match(input_matrix,pattern4);
            
            temp_value=temp_value||value1||value2||value3||value4;
            
            % L Cluster
            pattern5=[0,0,1;0,1,1;0,0,0];
            value5=condi_match(input_matrix,pattern5);
            pattern6=[0,1,1;0,1,0;0,0,0];
            value6=condi_match(input_matrix,pattern6);
            pattern7=[1,1,0;0,1,0;0,0,0];
            value7=condi_match(input_matrix,pattern7);
            pattern8=[1,0,0;1,1,0;0,0,0];
            value8=condi_match(input_matrix,pattern8);
            pattern9=[0,0,0;1,1,0;1,0,0];
            value9=condi_match(input_matrix,pattern9);
            pattern10=[0,0,0;0,1,0;1,1,0];
            value10=condi_match(input_matrix,pattern10);
            pattern11=[0,0,0;0,1,0;0,1,1];
            value11=condi_match(input_matrix,pattern11);
            pattern12=[0,0,0;0,1,1;0,0,1];
            value12=condi_match(input_matrix,pattern12);
            
            temp_value=temp_value||value5||value6||value7||value8||...
                value9||value10||value11||value12;
            
            % 4-connected Offset
            pattern13=[0,1,1;1,1,0;0,0,0];
            value13=condi_match(input_matrix,pattern13);
            pattern14=[1,1,0;0,1,1;0,0,0];
            value14=condi_match(input_matrix,pattern14);
            pattern15=[0,1,0;0,1,1;0,0,1];
            value15=condi_match(input_matrix,pattern15);
            pattern16=[0,0,1;0,1,1;0,1,0];
            value16=condi_match(input_matrix,pattern16);
            
            temp_value=temp_value||value13||value14||value15||value16;
            
            % Spur corner Cluster
            pattern171=[0,1,1;0,1,1;1,0,0];
            value171=condi_match(input_matrix,pattern171);
            pattern172=[0,0,1;0,1,1;1,0,0];
            value172=condi_match(input_matrix,pattern172);
            pattern173=[0,1,1;0,1,0;1,0,0];
            value173=condi_match(input_matrix,pattern173);
            
            pattern181=[1,1,0;1,1,0;0,0,1];
            value181=condi_match(input_matrix,pattern181);
            pattern182=[1,0,0;1,1,0;0,0,1];
            value182=condi_match(input_matrix,pattern182);
            pattern183=[1,1,0;0,1,0;0,0,1];
            value183=condi_match(input_matrix,pattern183);
            
            pattern191=[0,0,1;1,1,0;1,1,0];
            value191=condi_match(input_matrix,pattern191);
            pattern192=[0,0,1;0,1,0;1,1,0];
            value192=condi_match(input_matrix,pattern192);
            pattern193=[0,0,1;1,1,0;1,0,0];
            value193=condi_match(input_matrix,pattern193);
            
            pattern201=[1,0,0;0,1,1;0,1,1];
            value201=condi_match(input_matrix,pattern201);
            pattern202=[1,0,0;0,1,0;0,1,1];
            value202=condi_match(input_matrix,pattern202);
            pattern203=[1,0,0;0,1,1;0,0,1];
            value203=condi_match(input_matrix,pattern203);
            
            temp_value=temp_value||value171||value172||value173||...
                                   value181||value182||value183||...
                                   value191||value192||value193||...
                                   value201||value202||value203;
            
            % Corner Cluster
            value21=0;
            if and(and(E11,E12),and(E21,E22))==1
                value21=1;
            end
            temp_value=or(temp_value,value21);
            
            % Tee Branch
            pattern221=[1,1,0;1,1,1;1,0,0];
            value221=condi_match(input_matrix,pattern221);
            pattern222=[0,1,0;1,1,1;1,0,0];
            value222=condi_match(input_matrix,pattern222);
            pattern223=[0,1,0;1,1,1;0,0,0];
            value223=condi_match(input_matrix,pattern223);
            pattern224=[1,1,0;1,1,1;0,0,0];
            value224=condi_match(input_matrix,pattern224);
            
            temp_value=temp_value||value221||value222||value223||value224;
            
            pattern231=[0,1,1;1,1,1;0,0,1];
            value231=condi_match(input_matrix,pattern231);
            pattern232=[0,1,0;1,1,1;0,0,1];
            value232=condi_match(input_matrix,pattern232);
            pattern233=[0,1,1;1,1,1;0,0,0];
            value233=condi_match(input_matrix,pattern233);
            pattern234=[0,1,0;1,1,1;0,0,0];
            value234=condi_match(input_matrix,pattern234);
            
            temp_value=temp_value||value231||value232||value233||value234;
            
            pattern241=[0,0,1;1,1,1;0,1,1];
            value241=condi_match(input_matrix,pattern241);
            pattern242=[0,0,1;1,1,1;0,1,0];
            value242=condi_match(input_matrix,pattern242);
            pattern243=[0,0,0;1,1,1;0,1,1];
            value243=condi_match(input_matrix,pattern243);
            pattern244=[0,0,0;1,1,1;0,1,0];
            value244=condi_match(input_matrix,pattern244);
            
            temp_value=temp_value||value241||value242||value243||value244;
            
            pattern251=[1,0,0;1,1,1;1,1,0];
            value251=condi_match(input_matrix,pattern251);
            pattern252=[0,0,0;1,1,1;1,1,0];
            value252=condi_match(input_matrix,pattern252);
            pattern253=[1,0,0;1,1,1;0,1,0];
            value253=condi_match(input_matrix,pattern253);
            pattern254=[0,0,0;1,1,1;0,1,0];
            value254=condi_match(input_matrix,pattern254);
                
            temp_value=temp_value||value251||value252||value253||value254;
            
            pattern261=[1,1,1;1,1,0;0,1,0];
            value261=condi_match(input_matrix,pattern261);
            pattern262=[1,1,0;1,1,0;0,1,0];
            value262=condi_match(input_matrix,pattern262);
            pattern263=[0,1,1;1,1,0;0,1,0];
            value263=condi_match(input_matrix,pattern263);
            pattern264=[0,1,0;1,1,0;0,1,0];
            value264=condi_match(input_matrix,pattern264);
            
            temp_value=temp_value||value261||value262||value263||value264;
            
            pattern271=[0,1,0;1,1,0;1,1,1];
            value271=condi_match(input_matrix,pattern271);
            pattern272=[0,1,0;1,1,0;1,1,0];
            value272=condi_match(input_matrix,pattern272);
            pattern273=[0,1,0;1,1,0;0,1,1];
            value273=condi_match(input_matrix,pattern273);
            pattern274=[0,1,0;1,1,0;0,1,0];
            value274=condi_match(input_matrix,pattern274);
            
            temp_value=temp_value||value271||value272||value273||value274;
            
            pattern281=[0,1,0;0,1,1;1,1,1];
            value281=condi_match(input_matrix,pattern281);
            pattern282=[0,1,0;0,1,1;0,1,1];
            value282=condi_match(input_matrix,pattern282);
            pattern283=[0,1,0;0,1,1;1,1,0];
            value283=condi_match(input_matrix,pattern283);
            pattern284=[0,1,0;0,1,1;0,1,0];
            value284=condi_match(input_matrix,pattern284);
            
            temp_value=temp_value||value281||value282||value283||value284;
            
            pattern291=[1,1,1;0,1,1;0,1,0];
            value291=condi_match(input_matrix,pattern291);
            pattern292=[0,1,1;0,1,1;0,1,0];
            value292=condi_match(input_matrix,pattern292);
            pattern293=[1,1,0;0,1,1;0,1,0];
            value293=condi_match(input_matrix,pattern293);
            pattern294=[0,1,0;0,1,1;0,1,0];
            value294=condi_match(input_matrix,pattern294);

            temp_value=temp_value||value291||value292||value293||value294;
            
            % Vee Branch
            value30=0;value31=0;value32=0;value33=0;
            if E11==1 && E13==1
                if E31==1 || E32==1 || E33==1
                    value30=1;
                end
            end
            if E11==1 && E31==1
                if E13==1 || E23==1 || E33==1
                    value31=1;
                end
            end
            if E31==1 && E33==1
                if E11==1 || E12==1 || E13==1
                    value32=1;
                end
            end
            if E13==1 && E33==1
                if E11==1 || E21==1 || E31==1
                    value33=1;
                end
            end
            
            temp_value=temp_value||value30||value31||value32||value33;

            % Digonal Branch
            pattern341=[1,1,0;0,1,1;1,0,1];
            value341=condi_match(input_matrix,pattern341);
            pattern342=[0,1,0;0,1,1;1,0,1];
            value342=condi_match(input_matrix,pattern342);
            pattern343=[1,1,0;0,1,1;1,0,0];
            value343=condi_match(input_matrix,pattern343);
            pattern344=[0,1,0;0,1,1;1,0,0];
            value344=condi_match(input_matrix,pattern344);
            
            temp_value=temp_value||value341||value342||value343||value344;
            
            pattern351=[0,1,1;1,1,0;1,0,1];
            value351=condi_match(input_matrix,pattern351);
            pattern352=[0,1,0;1,1,0;1,0,1];
            value352=condi_match(input_matrix,pattern352);
            pattern353=[0,1,1;1,1,0;0,0,1];
            value353=condi_match(input_matrix,pattern353);
            pattern354=[0,1,0;1,1,0;0,0,1];
            value354=condi_match(input_matrix,pattern354);
            
            temp_value=temp_value||value351||value352||value353||value354;
            
            pattern361=[1,0,1;1,1,0;0,1,1];
            value361=condi_match(input_matrix,pattern361);
            pattern362=[0,0,1;1,1,0;0,1,1];
            value362=condi_match(input_matrix,pattern362);
            pattern363=[1,0,1;1,1,0;0,1,0];
            value363=condi_match(input_matrix,pattern363);
            pattern364=[0,0,1;1,1,0;0,1,0];
            value364=condi_match(input_matrix,pattern364);
            
            temp_value=temp_value||value361||value362||value363||value364;
            
            pattern371=[1,0,1;0,1,1;1,1,0];
            value371=condi_match(input_matrix,pattern371);
            pattern372=[1,0,0;0,1,1;1,1,0];
            value372=condi_match(input_matrix,pattern372);
            pattern373=[1,0,1;0,1,1;0,1,0];
            value373=condi_match(input_matrix,pattern373);
            pattern374=[1,0,0;0,1,1;0,1,0];
            value374=condi_match(input_matrix,pattern374);
            
            temp_value=temp_value||value371||value372||value373||value374;
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

               