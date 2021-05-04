/*  Name: Yao Fu
 *  USC NetID: yaof
 *  CS 455 Sping 2021
 *
 *  See ecListFuncs.h for specification of each function.
 *
 *  NOTE: remove the print statements below as you implement each function
 *  or you will receive no credit for that function
 *
 */

#include <string>
#include <cassert>

// for istringstream
#include <sstream>

// iostream only needed for the "not implemented yet" messages in starter code
#include <iostream>

#include "ecListFuncs.h"

using namespace std;

// Representation invariant:
// list should always be a well-formed list.

// *********************************************************
// Node constructors: do not change
Node::Node(int item) { 
   data = item;
   next = NULL;
}

Node::Node(int item, Node *n) {
   data = item;
   next = n;
}

// *********************************************************
/*
 * insertLast
 *
 * PRE: list is a well-formed list
 *
 * Inserts an integer to the last position of the linked list.
 */
void insertLast(ListType &list, int val){
   Node *p = list;

   if (p == NULL) {
      list = new Node(val);
      return;
   }

   while (p->next != NULL) {
      p = p->next;
   }
   
   p->next = new Node(val);
}

/*
 * buildList
 * 
 * PRE: listString only contains numbers (valid integer format) and spaces
 *
 * creates and returns a linked list from a string of space separated numbers
 */
ListType buildList(const string & listString) {
   ListType list;
   list = NULL;
   stringstream ss;        // Store the whole string into string stream    
   ss << listString;       // Runn loop till the end of the stream
   string temp;
   int intElement;
   
   while (!ss.eof()){
      ss >> temp;
      if (stringstream(temp) >> intElement){
         insertLast(list, intElement);
      }
      temp = "";
   }
   return list; 
  
}

/*
 * listToString
 *
 * PRE: list is a well-formed list.
 *
 * converts the list to a string form that has the following format shown by example.
 * the list is unchanged by the function.
 */
string listToString(ListType list) {
   Node *p = list;
   if (p == NULL){
      return "()";
   }
   else{
      string output = "(";
      while (p != NULL) {
         output = output + std::to_string(p->data) + " ";
         p = p->next;
      }
      output.erase(output.find_last_not_of(" ") + 1);
      output = output + ")";
      return output;  
   }
}

/*
 * removeLastInstance
 *
 * PRE: list is a well-formed list
 *
 * removes the last instance of target in list. If target is not in list, list is unchanged.
 */
void removeLastInstance(ListType & list, int target) {
   Node *p = list;
   
   // The list has no elements:
   if (p == NULL) {
      return;
   }
   
   // The list has only one element:
   if (p->next == NULL) {
      if (p->data == target){
         list = NULL;
         delete p;
      }
      return;
   }
   
   // The list has more than one elements:
   Node *targetP = NULL;
   Node *targetLastP = NULL;
   bool isFirst = false;
   if (p->data == target){ // the first one is target.
      targetP = p;
      isFirst = true;
   }
   while (p->next->next != NULL) { 
      Node *lastNode = p;
      p = p->next;
      if (p->data == target){
         targetP = p;
         targetLastP = lastNode;
         isFirst =false;
      }
   }
   
   Node *finalNode = p->next; // To check the last one.
   if (finalNode->data == target){
      p->next = NULL;
      delete finalNode;
      return;
   }
   else{
      if (isFirst){
         list = list->next;
         delete targetP;
         return;
      }
      else{
         targetLastP->next = targetP->next;
         delete targetP;
         return;
      }
   }
   
}

/*
 * splitAtIndex
 *
 * PRE: list is a well-formed list and index >= 0
 *
 * Assuming nodes are numbered starting from 0, splits list into two sub-lists as follows: 
 * "a" will contain all the elements up to, but not including, the node at the given index 
 * from the original list.  And "b" will contain all the elements after
 * the node at the given index in the original list.  Otherwise the values in the new
 * lists will be in the same order as they were in the original list.  
 * If index >= the length of the list, all the elements will be in "a",
 * and "b" will be NULL.
 * After the operation, list will have the value NULL (the function destroys the list, because
 * it reuses nodes form the original list).
 */
void splitAtIndex(ListType &list, int index, ListType &a, ListType &b) {
   assert(index >= 0);
   
   a = NULL;
   b = NULL;
   bool isA = true;
   int currIndex = 0;
   if (list == NULL){
      return;
   }
   while (list!= NULL) { 
      if (currIndex == index){
         isA = false;
      }
      else{
         if (isA){
            if (list != NULL){
               insertLast(a, list-> data);
            }
         }
         else{
            if (list != NULL){
               insertLast(b, list-> data);
            }
         }
      }
      
      list = list->next;
      currIndex++;
   }
   
   if (isA){
      a = NULL;
      b = NULL;
   }

}

