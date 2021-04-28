// Name: Yao Fu
// USC NetID: yaof
// CSCI 455 PA5
// Spring 2021

// Table.cpp  Table class implementation


#include "Table.h"

#include <iostream>
#include <string>
#include <cassert>

// for hash function called in private hashCode method defined below
#include <functional>

using namespace std;


// listFuncs.h has the definition of Node and its methods.  -- when
// you complete it it will also have the function prototypes for your
// list functions.  With this #include, you can use Node type (and
// Node*, and ListType), and call those list functions from inside
// your Table methods, below.
//
// Representation invariants:
// 1: hashSize should be always greater than 0;
// 2: each bucket is a linked list with some node elements containing
// string, integer and a pointer.

#include "listFuncs.h"


//*************************************************************************

// Two constructor functions:
Table::Table() {
   hashSize = Table::HASH_SIZE;
   theTable = new ListType[hashSize]();

}
Table::Table(unsigned int hSize) {
   hashSize = hSize;
   theTable = new ListType[hashSize]();
}

// inserts a new pair into the table.
// return false iff this key was already present 
// (and no change made to table).
bool Table::insert(const string &key, int value) {
   if (Table::lookup(key) != NULL){
      return false;
   }
   else{
      unsigned int tableIndex = Table::hashCode(key);
      return listInsert(theTable[tableIndex], key, value);  
   }
}

// return the address of the value that goes with this key
// or NULL if key is not present.
// Thus, this method can be used to either lookup the value or
// update the value that goes with this key.
int * Table::lookup(const string &key) {
   for (unsigned int i = 0; i < hashSize; i++){
      if (theTable[i] != NULL){
         if (listLookup(theTable[i], key) != NULL){
            return listLookup(theTable[i], key);
         }
      }
   }
   return NULL;   
}

// remove a pair given its key.
// return false iff key wasn't present
// (and no change made to table).
bool Table::remove(const string &key) {
   if (Table::lookup(key) == NULL){
      return false;
   }
   else{
      for (unsigned int i = 0; i < hashSize; i++){
         if (listLookup(theTable[i], key) != NULL){
            if (getListNum(theTable[i]) == 1){
               bool temp = listRemove(theTable[i], key);
               theTable[i] = NULL;
               return temp;
            }
            else{
               return listRemove(theTable[i], key); 
            }
         }
      }
      return false;
   }
}

// print out all the entries in the table, one per line.
void Table::printAll() const {
   for (unsigned int i=0; i < hashSize; i++){
      if (theTable[i] != NULL){
         listPrintAll(theTable[i]);
      }
   }

}

// return the number of entries in the table.
int Table::numEntries() const {
   int entryNum = 0;
   for (unsigned int i=0; i < hashSize; i++){
      if (theTable[i] != NULL){
         entryNum = entryNum + getListNum(theTable[i]);
      }
   }
   
   return entryNum;      
}

// hashStats: for diagnostic purposes only
// prints out info to let us know if we're getting a good distribution
// of values in the hash table.
void Table::hashStats(ostream &out) const {
   int noEmBuktNum = 0;
   int longestChain = 0;
   
   for (unsigned int i=0; i < hashSize; i++){
      if (theTable[i] != NULL){
         noEmBuktNum++;
         if (longestChain < getListNum(theTable[i])){
            longestChain = getListNum(theTable[i]);
         }
      }
   }
   
   out << "number of buckets: " << hashSize << endl;
   out << "number of entries: " <<  Table::numEntries() << endl;
   out << "number of non-empty buckets: " << noEmBuktNum << endl;
   out << "longest chain: " << longestChain << endl;

}


// hash function for a string
// (we defined it for you)
// returns a value in the range [0, hashSize)
unsigned int Table::hashCode(const string &word) const {

   // Note: calls a std library hash function for string (it uses the good hash
   //   algorithm for strings that we discussed in lecture).
   return hash<string>()(word) % hashSize;

}



