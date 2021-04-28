// Name: Yao Fu
// USC NetID: yaof
// CSCI 455 PA5
// Spring 2021

// pa5list.cpp
// a program to test the linked list code necessary for a hash table chain

// You are not required to submit this program for pa5.

// We gave you this starter file for it so you don't have to figure
// out the #include stuff.  The code that's being tested will be in
// listFuncs.cpp, which uses the header file listFuncs.h

// The pa5 Makefile includes a rule that compiles these two modules
// into one executable.

#include <iostream>
#include <string>
#include <cassert>

using namespace std;

#include "listFuncs.h"


int main() {
   typedef Node* ListType;
   ListType *theList;
   theList = new ListType[5]();
   
   //ListType theList = NULL;
   listPrintAll(theList[0]);
   cout << "The size of the list is " << getListNum(theList[1]) <<"."<< endl;
   
   listInsert(theList[0], "TingTing", 98);
   listInsert(theList[1], "Joe", 74);
   listInsert(theList[2], "Gan", 94);
   listInsert(theList[3], "Clark", 88);
   
   listPrintAll(theList[0]);
   cout << "The size of the list is " << getListNum(theList[0]) <<"."<< endl;
   
   cout << listLookup(theList[0], "TingTing") << endl;
   cout << theList[0]->key << endl;
   cout << theList[1]->key << endl;
   cout << theList[2]->key << endl;
   cout << theList[3]->key << endl;

   
   bool isRemove;
   isRemove = listRemove(theList[1], "Clark");
   cout << isRemove << endl;
   cout << "The size of the list is " << getListNum(theList[1]) <<"."<< endl;
   listPrintAll(theList[1]);


   return 0;
}
