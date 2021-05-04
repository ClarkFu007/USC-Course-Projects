/*  Name: Yao Fu
 *  USC NetID: yaof
 *  CS 455 Sping 2021
 *  Extra credit assignment
 *
 *  ectest.cpp
 *
 *  a non-interactive test program to test the functions described in ecListFuncs.h
 *
 *    to run it use the command:   ectest
 *
 *  Note: this uses separate compilation.  You put your list code ecListFuncs.cpp
 *  Code in this file should call those functions.
 */


#include <iostream>
#include <string>
#include <sstream>

#include "ecListFuncs.h"

using namespace std;
typedef Node* ListType;


/*
 * checkResult
 *
 * PRE: list is a well-formed list
 *
 * Checks whether the expected result is the same as the ouput
 * from specific functions.
 */
void checkResult(string exp, ListType list){
   string expOutput = exp;
   string yourOutput = listToString(list);
   if (yourOutput == expOutput){
      cout << "SUCCESSFUL!"<< endl;
   }
   else{
      cout << "FAILED!" << endl;
   }
   cout << "The expected result is "<< expOutput + "." << endl;
   cout << "Your result is " << yourOutput + "." << endl;
   cout << endl;
}



int main (){
   
   // Check the "listToString" function.
   ListType theList;
   theList = NULL;
   checkResult("()", theList);
   theList = new Node(1);
   theList->next = new Node(3);
   theList->next->next = new Node(5);
   theList->next->next->next = NULL;
   checkResult("(1 3 5)", theList);
   delete theList;
   ListType empList = buildList("   ");
   checkResult("()", empList);
   delete empList;
   
   // Check the "buildList" function.
   ListType list1 = buildList(" 1  2  1  2  1  2  ");
   checkResult("(1 2 1 2 1 2)", list1);
   
   // Check the "removeLastInstance" function.
   removeLastInstance(list1, 2);
   checkResult("(1 2 1 2 1)", list1);
   removeLastInstance(list1, 2);
   checkResult("(1 2 1 1)", list1);
   removeLastInstance(list1, 1);
   checkResult("(1 2 1)", list1);
   removeLastInstance(list1, 1);
   checkResult("(1 2)", list1);
   removeLastInstance(list1, 2);
   checkResult("(1)", list1);
   removeLastInstance(list1, 1);
   checkResult("()", list1);
   delete list1;
   
   // Check the "splitAtIndex" function.
   ListType list2;
   ListType a;
   ListType b;
   
   list2 = buildList("   ");
   splitAtIndex(list2, 4, a, b);
   checkResult("()", a);
   checkResult("()", b);
   
   list2 = buildList(" 3  -5  -3  9");
   splitAtIndex(list2, 0, a, b);
   checkResult("()", a);
   checkResult("(-5 -3 9)", b);
   
   list2 = buildList(" 3  -5  -3  9");
   splitAtIndex(list2, 1, a, b);
   checkResult("(3)", a);
   checkResult("(-3 9)", b);
   
   list2 = buildList(" 3  -5  -3  9");
   splitAtIndex(list2, 2, a, b);
   checkResult("(3 -5)", a);
   checkResult("(9)", b);
   
   list2 = buildList(" 3  -5  -3  9");
   splitAtIndex(list2, 3, a, b);
   checkResult("(3 -5 -3)", a);
   checkResult("()", b);
   
   list2 = buildList(" 3  -5  -3  9");
   splitAtIndex(list2, 4, a, b);
   checkResult("()", a);
   checkResult("()", b);
   
   delete list2;

   return 0;
}

