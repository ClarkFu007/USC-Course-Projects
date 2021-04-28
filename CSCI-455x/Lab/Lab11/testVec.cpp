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


int main(){
   vector<int> v = readVals();
   printVals(v);
   return 0;
}
