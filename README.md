# General Description:

This projects generates 10 million tokens in a file then reads those tokens and populates a Postgres RDBMS with those tokens ignring duplicates. This projects implements a few data structures to handle these operaions as efficiently as possible

Programing Language: ***Python***

Relational Database: ***PostgreSQL***

Implemented Approaches: ***2***

Potential Approaches: ***4***


## Approach #1: (Implemented)

In this approach, I use a Hash Set, since a ***HashSet*** has a constant access time
***O(1)***, and only stores each element once, so it would automatically get rid of duplicates. Along with that, I use a dictionary to store all duplicate tokens,
an their corresponding frequencies.

**Space Complexity:** Linear Space ----> ***O(n)*** where n is the number of tokens.

**Time Complexity:** Linear Time   ----> ***O(n)*** where we have to traverse every token and add it to the HashSet. Worst case sceneario is that we have a lt of chaining for each HashSet entry and we need to traverse each linked list while populating
the database.

**Network I/O:** We populate the database with the 10,000,000 tokens all at once, that permits the database to only focus on data processing, rather that spending more time on connection management, transaction overhead, and SQL parsing.

*Time for program to execute (start to finish):* ***70 seconds***


## Approach #2: (Implemented)


In this approach, I ***sort the tokens***, because with sorting, all duplicates will be after one another, and it is very easy to remove them.

**Space Complexity:** Linear Space ----> ***O(n)*** where n is the number of tokens.

**Time Complexity:** Linear Time   ----> ***O(nlog(n))*** for the sorting, then O(n) to
traverse the sorted list, remove the duplicates and populate the database. So worst case scenario is O(nlog(n)). 

**Network I/O:** We populate the database with the 10,000,000 tokens all at once, that permits the database to only focus on data processing, rather that spending more time on connection management, transaction overhead, and SQL parsing.

*Time for program to execute (start to finish):* ***86 seconds***	

### Retrospective:

The sorting approach would have competed with Approch 1 if it had not used any space, but unfortunately we have to build a list to store the sorted tokens, as we can't sort the tokens in the file in place, so in this case, approach 1 is better because of its smaller time complexity.



## Approach #3: (Theoretical)


In this approach, we build an ***N-ary tree***, where each child node is an array of ***26 children nodes***. The depth of the tree is ***7 levels***, because each token is only 7 characters. In this approach we can populate the tree at the same time as we remove duplicates, because the leaf nodes will contain a binary boolean (0/1) which means either we have populated the given token before or we haven't.

**Space Complexity:** ***exponential*** ---> O(26^7) {this is why I couldn't implement it}

**Time Complexity:** ***O(nlog(n))*** ---> where n is the number of tokens we need to traverse to populate the tree with, and the logarithmic time "log(n)" is to check whether the tree already stores that value.


## Approach #4: (optimized Approach #3)


In this approach, we ***optimize approach #3***, by first **sorting the elements**, then **splitting the tree** in approach #3 into 5 trees, each tree has only 5 children at each level, and then we can **parallelize** the whole approach by making ***5 threads***, each responsible for populating the then contiguous 4 starting characters into each tree. Here we won't need to worry about **synchronization** at all and there will never be two threads operating on the same token or the same tree.



## Database Schema:


This was very simple, the database only has one column called 'token' and it stores out tokens. There was no need for me to overcomplicate things.
