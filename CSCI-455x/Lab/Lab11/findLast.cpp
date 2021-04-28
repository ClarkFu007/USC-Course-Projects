#include <iostream>
#include <vector>
using namespace std;

vector<int> readVals(){
   vector<int> nums;
   int uInput;
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

int findLast(vector<int> v, int target){
   if(v.size() == 0){
      return -1;
   }   
   for (int i = v.size()-1; i >= 0; i--){
      if(v[i] == target){
         return i;
      }
   }
   return -1;
}

void testFindLast(vector<int> v, int target){
   cout << "Vector: ";
   printVals(v);
   int lastIndex = findLast(v, target);
   cout << "The last instance of " << target << " is at position " << lastIndex << endl;   
}

int main(){   
   vector<int> v = readVals();
   testFindLast(v,10);
   return 0;
}
