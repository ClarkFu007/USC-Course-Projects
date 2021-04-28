#include <iostream>
#include <vector>
using namespace std;

vector<int> readVals(){
   vector<int> nums;
   int uInput;
   cout << "Vector: ";
   while (cin >> uInput) {
      nums.push_back(uInput);   
   }
   return nums;
}

void printVals(vector<int> v){
   for (unsigned i = 0; i < v.size(); i++){
      cout << v[i] << " ";
   }
   cout << endl;
}

vector<int> isEvenFilter(vector<int> v){
   vector<int> filterNums;
   for (unsigned i = 0; i < v.size(); i++){
      if(v[i] % 2 ==0 ){
         filterNums.push_back(v[i]);
      }
   }
   return filterNums;
}

int main(){
   
   vector<int> v = readVals();
   printVals(v);
   
   vector<int> filteredV = isEvenFilter(v);
   cout << "Filtered vector: ";
   printVals(filteredV);
   
   cout << "Original vector: ";
   printVals(v);
   return 0;
}
