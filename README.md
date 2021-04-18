# unithash
Unithash hashing algorithm - a variable length segmentable hashing algorithm calculated by recursively adding the digits in a number till the sum is a single digit.

![image](https://user-images.githubusercontent.com/20480325/115152356-5feb7a00-a08e-11eb-99f8-b438da323e5f.png)

# Hashing algorithm
Given a large number, break up the number into equal length segments. Then apply the unit-sum function recursively on each segment and combine all segments to form a single hash value. The length of the segments can also depending on the type of content being hashed. An important aspect here is handling of alphabetic and non-alphanumeric characters. In order to handle these, the algorithm converts the character to their ASCII values and then converts them to corresponding mappings to the positions in the alphabets series and use them to create the hash. Thus the mappings become a = 0, z = 26 and likewise for the other characters.

# Functions usage
There are 2 major functions defined in this library -
           
            + find.get_unithash (arg1: integer)
           
            + find.set_unithash (arg1: string, arg2: integer)

The first function is used to get the unit sum value of a given number. It expects only 1 argument of type integer as input, which would be the number for which we wish to calculate the unit sum.

![image](https://user-images.githubusercontent.com/20480325/115152651-88c03f00-a08f-11eb-9c84-0531218e768b.png)

The second function is actual hashing algorithm implementation. It takes in 2 arguments. Argument 1 is the content to be hashed in the form of a string. Argument 2 is used to set the segment distribution length. Varying the segmentation length, would generate varying hash digests for the same text.

![image](https://user-images.githubusercontent.com/20480325/115152660-8f4eb680-a08f-11eb-9ffd-010c992b7eb1.png)
![image](https://user-images.githubusercontent.com/20480325/115152664-92e23d80-a08f-11eb-8c8e-1aa25778fde4.png)

# Using the Library
In order to use this hashing algorithm in your code, do a pip install for the library.

  > pip install unithash

Then in the python code import the library and its corresponding functions and that's it! Here's a sample code -

![image](https://user-images.githubusercontent.com/20480325/115152694-bad1a100-a08f-11eb-981b-663469efb596.png)
