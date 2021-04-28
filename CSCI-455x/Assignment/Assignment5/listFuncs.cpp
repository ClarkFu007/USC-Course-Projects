// Name: Yao Fu
// USC NetID: yaof
// CSCI 455 PA5
// Spring 2021


#include <iostream>
#include <cassert>

#include "listFuncs.h"

using namespace std;

// Representation invariant:
// list should always be a well-formed list.

// Tew constructors:
Node::Node(const string &theKey, int theValue) {
   key = theKey;
   value = theValue;
   next = NULL;
}

Node::Node(const string &theKey, int theValue, Node *n) {
   key = theKey;
   value = theValue;
   next = n;
}


//*************************************************************************
// Below are function definitions for my list functions:

// insert a new pair into the list
// returns false iff this key was already present 
// PRE: list is a well-formed list
bool listInsert(ListType &list, const std:: string &theKey, int theValue){
   Node *p = list;

   if (p == NULL) {
      list = new Node(theKey, theValue);
      return true;
   }

   while (p->next != NULL) {
      if (p->key == theKey){
         return false;
      }
      p = p->next;
   }
   
   p->next = new Node(theKey, theValue);
   return true;

}

// return the address of the value that goes with this key
// or NULL if key is not present.
//   Thus, this method can be used to either lookup the value or
//   update the value that goes with this key.
// PRE: list is a well-formed list
// POST: list is NULL
int *listLookup (ListType &list, const std::string &theKey){
   Node *p = list;

   while (p!= NULL) {
      if (p->key == theKey){
         return &(p->value);
      }
      p = p->next;
   }
   return NULL;
}


// remove a node pair given its key
// return false iff key wasn't present
//         (and no change made to list)
// PRE: list is a well-formed list
bool listRemove(ListType &list, const std::string &theKey){
   Node *p = list;
   
   // The list has no elements:
   if (p == NULL) {
      return false;
   }
   
   // The list has only one element:
   if (p->next == NULL) {
      if (p->key == theKey){
         list->next = NULL;
         delete p;
         return true;
      }
      else{
         return false;
      }
   }
   
   // The list has more than one elements: 
   if (p->key == theKey){ // the first one is theKey.
      list = list->next;
      delete p;
      return true;
   }
   while (p->next->next != NULL) { // the first one isn't theKey.
      Node *last = p;
      p = p->next;
      if (p->key == theKey){
         last->next = p->next;
         delete p;
         return true;
      }
   }
   Node *temp = p->next; // To check the last one。
   if (temp->key == theKey){
      p->next = NULL;
      delete temp;
      return true;
   }
   else{
      return false;
   }

}


// print out all the entries in the list, one per line.
// PRE: list is a well-formed list
void listPrintAll(ListType &list){
   Node *p = list;
   while (p != NULL) {
      std::cout << p->key << " " << p->value << endl;
      p = p->next;
   }
   
}


// number of entries in the list
// PRE: list is a well-formed list
int getListNum(ListType &list){
   Node *p = list;
   int listNum = 0;
   while (p != NULL) {
      listNum++;
      p = p->next;
   }
   
   return listNum;
}
