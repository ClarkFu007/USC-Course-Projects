// Name: Yao Fu
// USC NetID: yaof
// CSCI 455 PA5
// Spring 2021
/*
 * grades.cpp
 * A program to test the Table class.
 * How to run it:
 *      grades [hashSize]
 * 
 * the optional argument hashSize is the size of hash table to use.
 * if it's not given, the program uses default size (Table::HASH_SIZE)
 *
 */

#include "Table.h"

// cstdlib needed for call to atoi
#include <cstdlib>
#include<ctype.h>
#include <string>
#include <sstream>

using namespace std;

// Clear all space characters to left or right of the string.
string clearHeadTailSpace(string str){
   if (str.empty()){
      return str;
   }
   
   str.erase(0, str.find_first_not_of(" "));
   str.erase(str.find_last_not_of(" ") + 1);
   return str;
}

// Extract the integer from the given string.
int extractIntegerWords(string str){
    stringstream ss; // Store the whole string into string stream    
    ss << str;       // Runn loop till the end of the stream
    string temp;
    int found = 0;
    while (!ss.eof()) {
        ss >> temp; // Extract word by word from stream
        
       // Check the given word is integer or not 
        if (stringstream(temp) >> found){  
           return found;   
        }
       
        //To save from space at the end of string 
        temp = "";
    }
   return found;
}

// Check if the operation is "insert":
bool checkInsert(string operation, Table * grades){
   string name = "";
   string opeaStr = "insert";
   if (operation.find(opeaStr) != std::string::npos) {
      unsigned int firstIndex = 0;
      unsigned int lastIndex = 0;
      for (unsigned int i = 0; i < operation.size(); i++){
         if (operation[i] == opeaStr.back()){
            firstIndex = i + 1;
         }
         if(isdigit(operation[i])){
            lastIndex = i;
            int nameNum = lastIndex - firstIndex;
            name = operation.substr(firstIndex, nameNum);
            name = clearHeadTailSpace(name); 
            break;
         }   
      }
      int score = extractIntegerWords(operation);
      bool result = grades-> insert(name, score);
      if (!result){
         cout << "Can't insert: " << name << " was already present!" << endl;
      }
      return true;
   }
   else{
      return false;
   }
}

// Check if the operation is "change":
bool checkChange(string operation, Table * grades){
   string name = "";
   string opeaStr = "change";
   if (operation.find(opeaStr) != std::string::npos) {
      unsigned int firstIndex = 0;
      unsigned int lastIndex = 0;
      for (unsigned int i = 0; i < operation.size(); i++){
         if (operation[i] == opeaStr.back()){
            firstIndex = i + 1;
         }
         if(isdigit(operation[i])){
            lastIndex = i;
            int nameNum = lastIndex - firstIndex;
            name = operation.substr(firstIndex, nameNum);
            name = clearHeadTailSpace(name); 
            break;
         }   
      }
      int newScore = extractIntegerWords(operation);
      int *value = grades-> lookup(name);
      if (value == NULL){
         cout << "Can't change: " << name << " was already present!" << endl;
      }
      else{
         *value = newScore;
      }
      return true;
   }
   else{
      return false;
   }
}

// Check if the operation is "lookup":
bool checkLookup(string operation, Table * grades){
   string name = "";
   string opeaStr = "lookup";
   if (operation.find(opeaStr) != std::string::npos) {
      unsigned int firstIndex = 0;
      unsigned int lastIndex = 0;
      for (unsigned int i = 0; i < operation.size(); i++){
         if (operation[i] == opeaStr.back()){
            firstIndex = i + 1;
            lastIndex = operation.size();
            int nameNum = lastIndex - firstIndex;
            name = operation.substr(firstIndex, nameNum);
            name = clearHeadTailSpace(name); 
            break;
         } 
      }
      int *value = grades-> lookup(name);
      if (value == NULL){
         cout << "Can't lookup: " << name << " isn't in the table!" << endl;
      }
      else{
         cout << name <<"'s score is " << *value << "." << endl;
      }
      return true;
   }
   else{
      return false;
   }
}

// Check if the operation is "remove":
bool checkRemove(string operation, Table * grades){
   string name = "";
   string opeaStr = "remove";
   if (operation.find(opeaStr) != std::string::npos) {
      unsigned int firstIndex = 0;
      unsigned int lastIndex = 0;
      int count = 1;
      for (unsigned int i = 0; i < operation.size(); i++){
         if (operation[i] == opeaStr.back()){
            if (count == 2){
               firstIndex = i + 1;
               lastIndex = operation.size();
               int nameNum = lastIndex - firstIndex;
               name = operation.substr(firstIndex, nameNum);
               name = clearHeadTailSpace(name); 
               break;
            }
            else{
            count++;
            }
         } 
      }
      bool result = grades-> remove(name);
      if (result == false){
         cout << "Can't remove: "<< name << " isn't in the table!" << endl;
      }
      return true;
   }
   else{
      return false;
   }
}

// Display the valid command line formats.
void printComdSummary(){
   cout << "Only command formats below are valid:" << endl;
   cout << "insert name score" << endl;
   cout << "change name newscore" << endl;
   cout << "lookup name" << endl;
   cout << "remove name" << endl;
   cout << "print" << endl;
   cout << "size" << endl;
   cout << "stats" << endl;
   cout << "help" << endl;
   cout << "quit" << endl;
}

// Do the operation from the client.
void dpOperation(string operation, Table * grades){
   if (checkInsert(operation, grades)){
      return;
   }
   
   if (checkChange(operation, grades)){
      return;
   }
   
   if (checkLookup(operation, grades)){
      return;
   }
   
   if (checkRemove(operation, grades)){
      return;
   }
   
   if (operation == "print"){
      grades->printAll();
      return;
   }
   
   if (operation == "size"){
      cout << "The number of entries in the table is " << grades->numEntries() << "." <<endl;
      return;
   }
   if (operation == "stats"){
      grades->hashStats(cout);
      return;
   }
   if (operation == "help"){
      printComdSummary();
      return;
   }
   cout << "ERROR: invalid command" <<endl;
   printComdSummary();
   return;
}


int main(int argc, char * argv[]) {

   // gets the hash table size from the command line
   int hashSize = Table::HASH_SIZE;

   Table * grades;  // Table is dynamically allocated below, so we can call
   // different constructors depending on input from the user.

   if (argc > 1) {
      hashSize = atoi(argv[1]);  // atoi converts c-string to int

      if (hashSize < 1) {
         cout << "Command line argument (hashSize) must be a positive number" 
              << endl;
         return 1;
      }

      grades = new Table(hashSize);

   }
   else {   // no command line args given -- use default table size
      grades = new Table();
   }


   grades->hashStats(cout);


   // Do the operation as the client asks.   
   string operation;
   cout << "cmd>";
   getline (cin, operation);
   while (operation != "quit"){
      dpOperation(operation, grades);
      cout << "cmd>";
      getline (cin, operation);
   }

   return 0;
}
