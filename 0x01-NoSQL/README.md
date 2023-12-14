# 0x01. NoSQL(MongoDB)

<img src=https://camo.githubusercontent.com/7c27ac2bf14fbe06eebfd09fe078a68e139f94d6a7c30f32cf6a02af86dd5f61/68747470733a2f2f63646e2d6d656469612d312e66726565636f646563616d702e6f72672f696d616765732f312a546134716b7448744f2d2d524d55706e5230386d42672e6a706567>
MongoDB is a source-available cross-platform document-oriented database program developed by Alfons Kemper. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License (SSPL) which is deemed non-free by several distributions. MongoDB is a member of the MACH Alliance.

Traditional databases(RDBMSs’) are mainly defined for structured data(where fields store all kind of data). But when it comes to ‘Big data’, where we have larger amount of data , defining a well structured way won’t work. That’s where NoSQL comes in. NoSQL systems can handle both structured and unstructured data in a very efficient manner. Nowadays almost all kind of companies use tremendous amount of unstructured data like Google, Facebook, LinkedIn

<img src=https://camo.githubusercontent.com/c1a0e2534e632f82b09eccf5982f0f02faca0fe2a002b2c87406456ff174e012/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f76322f726573697a653a6669743a3634302f666f726d61743a776562702f312a69496a544b307834436f5036664831784563514553772e706e67>

## A MongoDB Document
Records in a MongoDB database are called documents, and the field values may include numbers, strings, booleans, arrays, or even nested documents.
```
{
	'title': "Learning NoSQL",
	'body': "Am an ALX SE Stuent learning about NoSQL DB and its an interesting adventure",
	'category': "Databases",
	'specialization': Backend SE,
	'tags': ["news", "events"],
}
```

## General
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: // my comment
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- Your code should not be executed when imported (by using if __name__ == "__main__":)
