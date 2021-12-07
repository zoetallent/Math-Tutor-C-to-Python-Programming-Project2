#This program shows a user how a peice of code that was originally written in C++ can be written in Python
print("Welcome to this program.This canshow how a peice of code can be written differently.")
print("Here a user will see how a peice of code that was writtren in C++ can be written in Python.")
print("This program allows the user to imput different mathematical operations that the computer can solve.")
# This is a list of variables that will be used so that the program can run 
#Set constants for Minimum, maximum numbers and math problems
MIN_VALUE=0
MAX_VALUE=999
ADDITION=1
SUBTRACTION=2
MULTIPLICATION=3,
DIVISION=4,
QUIT_PROBLEM=5
          
# Below shows what the program would look like in the C++ coding language
#include <iostream>
#include <cstdlib>
#include <ctime>
#using namespace std;

int main()
{
    //Set constants for Minimum, maximum numbers and math problems
    const int MIN_VALUE=0,
              MAX_VALUE=999,
              ADDITION=1,
              SUBTRACTION=2,
              MULTIPLICATION=3,
              DIVISION=4,
              QUIT_PROBLEM=5;
              
    //Set Variables to enter number 1, 2 and the answer
    int userAnswer,
        rand_value_1,
        rand_value_2,
        rand_value_answer,
        menu_select;
    
    unsigned seed = time(0);          
    
    srand(seed);
    
    //Use if, if-else, do-while and switch statment to determine the type of math problem.
    do 
    {
        rand_value_1=(rand()%(MAX_VALUE-MIN_VALUE +1))+
                     MIN_VALUE;
        rand_value_2=(rand()%(MAX_VALUE-MIN_VALUE +1))+
                     MIN_VALUE;
        cout << "\nWhat type of math problem would\n"
             << "you like to solve? \n";
        cout << "1. Addition"       << endl;
        cout << "2. Subtraction"    << endl;
        cout << "3. Multiplication" << endl;
        cout << "4. Division"       << endl;
        cout << "5. Quit Program ";
      while(!(cin >> menu_select)  ||
               menu_select < ADDITION || 
               menu_select > QUIT_PROBLEM) 
               {
                    cout << "\nInvalid selection. Please enter\n"
                    << "a valid selection: \n";
                    cin.clear();
                    cin.ignore(1200, '\n');
                }
        if (menu_select != QUIT_PROBLEM)
        {
            switch(menu_select)
            {
                case 1:
                    cout<<rand_value_1<<" + "
                        <<rand_value_2<<" = ";
                    rand_value_answer = rand_value_1 +
                                        rand_value_2;
                    while(!(cin>>userAnswer))
                    {
                        cout<<"There is an error. The number must be"
                            <<"picked.";
                        cin.clear();
                        cin.ignore(1200, '\n');
                    }
                    break;
                case 2:
                    cout<<rand_value_1<<" - "
                        <<rand_value_2<<" = ";
                    rand_value_answer = rand_value_1 -
                                        rand_value_2;
                    while(!(cin>>userAnswer))
                    {
                        cout<<"There is an error. The number must be"
                            <<"picked.";
                        cin.clear();
                        cin.ignore(1200, '\n');
                    }
                    break;
                case 3:
                    cout<<rand_value_1<<" x "
                        <<rand_value_2<<" = ";
                    rand_value_answer = rand_value_1 *
                                        rand_value_2;
                    while(!(cin>>userAnswer))
                    {
                        cout<<"There is an error. The number must be"
                            <<"picked.";
                        cin.clear();
                        cin.ignore(1200, '\n');
                    }
                    break;
                case 4:
                    cout<<rand_value_1<<" / "
                        <<rand_value_2<<" = ";
                    rand_value_answer = rand_value_1 /
                                        rand_value_2;
                    while(!(cin>>userAnswer))
                    {
                        cout<<"There is an error. The number must be"
                            <<"picked.";
                        cin.clear();
                        cin.ignore(1200, '\n');
                    }
                    break;
            }
            
            if(userAnswer==rand_value_answer)
            {
                cout << "\nCongratulations!" 
                     << endl 
                     << endl;
            }
            else if(userAnswer!=rand_value_answer)
            {
                cout << "\nWrong answer. Correct answer is: " 
                     << rand_value_answer 
                     << endl 
                     << endl;
            }
        }
        else
            cout << "Program complete." << endl;

    }
    while (menu_select != QUIT_PROBLEM);
    cout << endl;
    
    return 0;
}

#Below shows the samer code from above written in Python  
#This shows how the numbers are imported at random so that the eqation will work
import random 
def random_numbers
num1= random.Random(99)
num2= random.Random(99) 
#This is the switch statement using a dictionary
    def dispatch_if(operator, num1, num2):
        if operator == 'add':
            return num1 + num2
        elif operator == 'subtract':
            return num1 -  num2
        elif operator == 'multiply':
            return num1 * num2
        elif operator == 'divid': 
            return num1 / num2
def dispatch_dict(operator, num1 ,num2):
    return 
{
    'add':lambda:  num1 + num2,
    'subtract':lambda:  num1 - num2,
    'multiply':lambda:  num1 * num2,
    'divid':lambda:  num1 / num2,    
}
#This is how the users will answer 
answer= int(input ("Enter the opperator that you want to do: "))
while num1, num2 == True:
    print "This is right"



#Here are the sources used
#https://www.youtube.com/watch?v=5AOfDuV6X30    
#https://www.youtube.com/watch?v=CasqhmeopnU
#https://www.youtube.com/watch?v=zWL3z7NMqAs
#https://www.youtube.com/watch?v=gllUwQnYVww