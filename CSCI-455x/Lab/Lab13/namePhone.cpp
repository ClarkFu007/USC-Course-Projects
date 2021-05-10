/*

  CSCI 455 C String lab

  See lab description for what it should do.  
  C++ tools allowed: cout, call by reference, ostream output, new / delete

*/


// for C input functions (e.g., fgets used here)
#include <cstdio>

// C string functions
#include <cstring>

#include <iostream>


using namespace std;

const char NAME_DELIM = ':';
const int AREA_CODE_SIZE = 3;
const int PREFIX_SIZE = 3;
const int LINE_NO_SIZE = 4;
const int MAX_LINE_SIZE = 1024;  // including newline and terminating null char


int readName(char *buffer, char *destChar) { 
   int i = 0;
   if (*(buffer + i) == ':'){
      *(destChar) = '\0';
      return i;
   }
   while (*(buffer + i) != ':') { 
      *(destChar + i) = *(buffer + i); 
      i++; 
   } 
   *(destChar + i + 1) = '\0'; 
   return i;
} 


void readField(char *buffer, int startLoc, int fieldLen, char *destChar) { 
   int j = 0; 
   // char *sm = destChar; 
   for (int i = startLoc; i < startLoc + fieldLen; i++) { 
      *(destChar + j) = *(buffer + i); 
      j++; 
   } 
   *(destChar+fieldLen) = '\0'; 
   // sm[0] = 0; 
} 

int main() {

   char buffer[MAX_LINE_SIZE];


   // fgets reads a line of input and puts it in a C string.  If the line of input
   // is longer than the buffer array only gets enough chars that fit (and ignores the
   // rest); this prevents it from overwriting the end of the array.
   // Unlike Java Scanner nextLine(), fgets also saves the newline in the buffer.
   // So after call, buffer will have 0 or more chars read from the line, 
   // then a newline char ('\n'), and then the null char ('\0')
   // note: the sizeof function below does not work with dynamic arrays.
   // fgets returns 0 (false) when it hits EOF
   // Note: stdin (third paremeter below) is the C version of cin or System.in


   while (fgets(buffer, sizeof(buffer), stdin)) { 
      //xxx-xxx-xxxx 
      cout << "--------------------" << endl; 
      cout << "LINE READ: " << buffer; 
   
      char *name = new char[MAX_LINE_SIZE + 1]; 
      char *areacodePT = new char[AREA_CODE_SIZE + 1]; 
      char *prefixPT = new char[PREFIX_SIZE + 1]; 
      char *linenoPT = new char[LINE_NO_SIZE + 1]; 

      int strLoc = readName(buffer, name);
      readField(buffer, strLoc, AREA_CODE_SIZE, areacodePT);
      readField(buffer, strLoc + 4, PREFIX_SIZE, prefixPT);
      readField(buffer, strLoc + 8, LINE_NO_SIZE, linenoPT);
   
      cout << "name read: '" << name << "'" << endl; 
      cout << "area code " << areacodePT << endl; 
      cout << "prefix code " << prefixPT << endl; 
      cout << "line Number " << linenoPT << endl;
      
      delete name;
      delete areacodePT;
      delete prefixPT;
      delete linenoPT;
   } 
}