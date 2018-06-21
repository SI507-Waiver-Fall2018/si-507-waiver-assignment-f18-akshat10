# 507WaiverFall2017

Waiver exam for University of Michigan UMSI course, SI 507. You must complete all 4 parts, and the code for each part must be checked in to github with the name specified for that part. Any other filenames will break our grading system and will be rejected.

**Any questions about waiving, credits, or course registration should go to UMSI advisors and not to the proctors of this waiver.**

## To complete and submit
You should accept this assignment via GitHub Classroom and commit all of the files already included here, edited to include the solutions, PLUS two more files: the `noun_data.csv` you will create in Part 1, and the `part4_viz_image.png` file you will create in Part 4.


**Note**
This waiver assignment is composed of activity parts that cover many, but not all, of the learning objectives from SI 507, including using source control like Git, learning to use new libraries for data manipulation for UX or analysis like NLTK or BeautifulSoup, organizing and dealing with complex data problems, and using libraries to access, process, and explore data, along with using/investigating any tools and/or programming knowledge that you need to complete these tasks. SI 507 is not limited to these things, but if you can complete this assignment in less than several weeks, you are ready to go on to more advanced programming courses and learn other aspects of SI 507 as you need if you do not already know them.

## Part 1: Create a program to analyze the twitter timeline of a selected user.

FILENAME: `part1.py`

ARGUMENTS: the program takes two arguments--a twitter username and the number of tweets to analyze.

OUTPUT: the program outputs the following:
* the user name
* the number of tweets analyzed
* the five most frequent verbs that appear in the analyzed tweets
* the five most frequent nouns that appear in the analyzed tweets
* the five most frequent adjectives that appear in the analyzed tweets
* the number of _original_ tweets (i.e., not retweets)
* the number of times that the _original_ tweets in the analyzed set were favorited
* the number of times that the _original_ tweets in the analyzed set were retweeted by others

**To determine the five most frequent**, ties should be broken alphabetically, capitals before lowercase. (Check out Python stable sorting for a relatively easy way to handle this.)

The program **should also save a CSV file of the 5 most frequent nouns in the analyzed tweets**, called `noun_data.csv`. You'll use this in Part 4!

NOTES:
* use `tweepy` for accessing the Twitter API
* Use NLTK for analyzing parts of speech. Use NLTK's default POS tagger and tagset (this will use the [UPenn treebank tagset](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html))--you do NOT need to install any taggers or tagsets into NLTK.
* "stop words": ignore any words that do not start with an alphabetic character `[a-zA-Z`], and also ignore 'http', 'https', and 'RT' (these show up a lot in Twitter)
* a "verb" is anything that is tagged VB*
* a "noun" is anything that is tagged NN*
* an "adjective" is anything that is tagged JJ*



SAMPLE OUTPUT:

```bash
mwnewman$ python3 get_tweets.py umsi 12
USER: umsi
TWEETS ANALYZED: 12
VERBS: are(4) being(3) is(3) improve(2) Join(2)
NOUNS: umsi(8) UMSI(8) students(5) Join(5) amp(5)
ADJECTIVES more(5) umsi(4) doctoral(2) new(2) social(2)
ORIGINAL TWEETS: 8
TIMES FAVORITED (ORIGINAL TWEETS ONLY): 26
TIMES RETWEETED (ORIGINAL TWEETS ONLY): 18
```

SAMPLE CSV FILE OUTPUT **inside a .csv file**
```txt
Noun,Number
umsi,8
UMSI,8
students,5
Join,5
amp,5
```


## Part 2: Create a Simple Database application

For part 2, you will create a program to access information in the Northwind database (included in the repository)

FILENAME: `part2.py`

USAGE: the program does different things based on the arguments passed in.  
**part2.py customers**: prints the list of all customers

**part2.py employees**: prints the list of all employees

**part2.py orders cust=&lt;customer id&gt;**: prints the list of _order dates_ for all orders placed for the specified customer. Use the _customer ID_ for this command.

**part2.py orders emp=&lt;employee last name&gt;**: prints the list of _order dates_ for all orders managed by the specified employee. Use the _employee last name_ for this command.

SAMPLE OUTPUT:
The sample output is large, so it's on another page: [Sample Output](https://github.com/aerenchyma/507WaiverFall2017/blob/master/part2_output.md)

NOTE: Use sqlite3.

## Part 3: Scrape the Michigan Daily

FILENAME: `part3.py`

In part 3, you will use Beautiful Soup to scrape the Most Read stories from the Michigan Daily site (http://michigandaily.com), and will crawl one level deeper to find the author of each Most Read story.

SAMPLE OUTPUT:
```
dhcp3-213:507waiver2 mwnewman$ python3 part3.py   
Michigan Daily -- MOST READ  
Darkness and the Occult: A brief history of doom metal  
  by Selena Aguilera
"The white rice was excellent. Followed the directions on the bag perfectly. Way to go."  
  by Hunter Zhao
Schlissel: "I try not to have a personal opinion" on potential C.C. Little renaming, awaiting further review  
  by Alexa St. John
A guide to Michigan's 2018 gubernatorial race
  by Colin Beresford
```

NOTES: If there is more than one reporter, you only need to print the first name on the byline.

## Part 4: Visualize some data

FILENAME: `part4.py`

Write code that uses **plot.ly** to create a bar chart representing the data you got in **Part 1** about the most common *nouns* only in the Twitter data. More information about using plot.ly for bar chart creation can be found here: https://plot.ly/python/bar-charts/

You should use `part4.py` to do so.

You should create, as a result of `part4.py`, an image file of the bar chart: `part4_viz_image.png`.

Any bar chart representing your data about nouns is acceptable.
