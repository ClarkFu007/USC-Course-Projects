// Name: Yao Fu
// USC NetID: yaof
// CSCI 455 PA5
// Spring 2021


//*************************************************************************
// Node class definition 
// and declarations for functions on ListType

// Note1: we don't need Node in Table.h
// because it's used by the Table class; not by any Table client code.

// Note2: it's good practice to not put "using" statement in *header* files.  Thus
// here, things from std libary appear as, for example, std::string

#ifndef LIST_FUNCS_H
#define LIST_FUNCS_H

#include <string>
  

struct Node {
   std::string key;
   int value;
   Node *next;
   
   Node(const std::string &theKey, int theValue);
   Node(const std::string &theKey, int theValue, Node *n);
};

typedef Node * ListType;

//*************************************************************************
//add function headers (aka, function prototypes) for your functions
//that operate on a list here (i.e., each includes a parameter of type
//ListType or ListType&).  No function definitions go in this file.


// insert a new pair into the list.
// return false iff this key was already present. 
// PRE: list is a well-formed list
bool listInsert(ListType &list, const std:: string &key, int val);

// return the address of the value that goes with this key
// or NULL if key is not present.
//   Thus, this method can be used to either lookup the value or
//   update the value that goes with this key.
// PRE: list is a well-formed list
// POST: list is NULL
int *listLookup (ListType &list, const std::string &key);


// remove a node pair given its key.
// return false iff key wasn't present
//         (and no change made to list)
// PRE: list is a well-formed list
bool listRemove(ListType &list, const std::string &key);

// print out all the entries in the list, one per line.
// Sample output:
//   zhou 283
//   sam 84
//   babs 99
// PRE: list is a well-formed list
void listPrintAll(ListType &list);

// number of entries in the list.
// PRE: list is a well-formed list
int getListNum(ListType &list);


// keep the following line at the end of the file
#endif
