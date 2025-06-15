 FLAMES Game in Python

This is a simple Python project that implements the popular childhood game FLAMES to determine the relationship between two people based on their names.


 What is FLAMES?

FLAMES stands for:

- F – Friends  
- L – Love  
- A – Affection  
- M – Marriage  
- E – Enemies  
- S – Siblings  

Based on the number of non-common letters between two names, this game eliminates letters from the word "FLAMES" to predict the relationship.


 How It Works

1. Takes two names as input.
2. Removes common characters between both names.
3. Counts the total number of remaining characters.
4. Uses this count to eliminate letters from FLAMES in a circular manner.
5. The last remaining letter represents the relationship.

 Code Usage
python
 Run the script
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

relationship = flames_game(name1, name2)
print("Relationship is:", relationship)
