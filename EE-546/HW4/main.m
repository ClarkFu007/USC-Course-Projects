aca2_s = load('aca2_labels.mat').array;
aca2_array = load('total_results1.mat').array;
aca5_s = load('aca5_labels.mat').array;
aca5_array = load('total_results2.mat').array;
%%
aca2_miss_rate = Misclassification(aca2_array', aca2_s);
aca2_minimum = min(aca2_miss_rate)

aca5_miss_rate = Misclassification(aca5_array', aca5_s);
aca5_minimum = min(aca5_miss_rate)

save('aca2_miss_rate.mat','aca2_miss_rate')
save('aca5_miss_rate.mat','aca5_miss_rate')
%%
aca2_s_t = min(load('aca2_miss_rate.mat').aca2_miss_rate);
aca5_s_t = min(load('aca5_miss_rate.mat').aca5_miss_rate);
%%
A = [2,3,4,6,7;
     3,5,8,2,2;
     4,8,1,3,3;
     6,2,3,7,6;
     7,2,3,6,1];
[V, D] = eigs(A)
[V, D] = eigs(eye(5)-A)
