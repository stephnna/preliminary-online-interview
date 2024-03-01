# Preliminary Online Interview Test for Python
 
# Thank you for your application. Our recruitment process is in 3 stages. We have decided to carry out the first stage online. The other 2 stages will be physical interviews at our Offices in Lagos.
 
# Find below the Technical Interview Questions.  Before commencing, kindly acknowledge receipt of this Email.
 
# Thank you for your Interest in the Bincom ICT Solutions.
# Note: You will need to complete the test within 6 hours of getting this notification.
 
# STEP 1
# Kindly answer the attached Questions using python

# STEP 2
# Upload your .py file to any Temporary hosting for Assessment e.g. Google Drive.


# STEP 3

# When you have completed the test,  Complete the following form to confirm that you have completed the Test. 
# https://blog.bincom.net/bincomforms/bincom-recruitment-online-interview-submission-form/ 

# The submission should contain:
# 1.      An attachment of your working code files (preferably a link to an online repository or storage)
 
 
# Wishing You All the best
 



# Python Basic Developer Test
# Background:
# You have been provided with a web page showing the colors of dresses put on by Bincom staffs for the week. We are planning to produce Tshirts for staffs and we have issues deciding the colors to be used. We want to make our decision based on the analysis of the data presented in the web page.

# Kindly go through the web page and write a python program that answers the questions below:
 
# Requirements:
# ·         You may use python2 or python3
# ·         You may use any IDE of your choice
# ·         You may use regular expression
 
# Key Features:
# 1.      Which color of shirt is the mean color?
# 2.      Which color is mostly worn throughout the week?
# 3.      Which color is the median?
# 4.      BONUS Get the variance of the colors
# 5.      BONUS if a colour is chosen at random, what is the probability that the color is red?
# 6.      Save the colours and their frequencies in postgresql database
# 7.      BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
# 8.      Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
# 9.      Write a program to sum the first 50 fibonacci sequence.
 
# Hints:
# Bonus Questions are not Required but are recommended.
# We are Testing your Basic Programming Ability.
# You may browse any website of your choice to get code snippets and tutorials if necessary.
# Follow this link to get the html page https://drive.google.com/open?id=1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf
 
import re
from collections import Counter
import random
import psycopg2
import numpy as np

# HTML data
html_data = """
<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
    
    body{
        width:1000px;
        margin: auto;
    }
    table,tr,td{
        border:solid;
        padding: 5px;
    }
    table{
        border-collapse: collapse;
        width:100%;
    }
    h3{
        font-size: 25px;
        color:green;
        text-align: center;
        margin-top: 100px;
    }
    p{
        font-size: 18px;
        font-weight: bold;
    }
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
    
    <thead>
        <th>DAY</th><th>COLOURS</th>
    </thead>
    <tbody>
        <tr>
            <td>MONDAY</td>
            <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
        </tr>
        <tr>
            <td>TUESDAY</td>
            <td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
        </tr>
        <tr>
            <td>WEDNESDAY</td>
            <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
        </tr>
        <tr>
            <td>THURSDAY</td>
            <td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
        </tr>
        <tr>
            <td>FRIDAY</td>
            <td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
        </tr>

    </tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
</body>
</html>
"""

# Extract colors from HTML table
colors_match = re.findall(r'[A-Za-z]+', html_data)
colors = [color.upper() for color in colors_match]

# Calculate mean color
mean_color = max(set(colors), key=colors.count)

# Calculate mode (most frequent color)
mode_color = Counter(colors).most_common(1)[0][0]

# Calculate median color
colors.sort()
n = len(colors)
median_color = colors[n // 2] if n % 2 != 0 else (colors[n // 2 - 1], colors[n // 2])

# Calculate variance
color_counts = Counter(colors)
variance = np.var(list(color_counts.values()))

# Probability of choosing red randomly
red_probability = color_counts.get('RED', 0) / len(colors)

# Saving colors and their frequencies in PostgreSQL database
def save_to_database(colors):
    conn = psycopg2.connect("dbname=test user=postgres password=postgres")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS colors (color VARCHAR(255), frequency INT)")
    for color, freq in color_counts.items():
        cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, freq))
    conn.commit()
    conn.close()

# Recursive searching algorithm
def recursive_search(lst, num, start=0):
    if start >= len(lst):
        return False
    if lst[start] == num:
        return True
    return recursive_search(lst, num, start + 1)

# Generate random 4-digit binary number and convert to base 10
random_binary = ''.join(str(random.randint(0, 1)) for _ in range(4))
base_10 = int(random_binary, 2)

# Sum of first 50 Fibonacci numbers
def fibonacci_sum(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return sum(fib_sequence)

fib_sum = fibonacci_sum(50)

# Results
print("Mean color:", mean_color)
print("Mode color:", mode_color)
print("Median color:", median_color)
print("Variance of colors:", variance)
print("Probability of choosing red randomly:", red_probability)
save_to_database(colors)
print("Colors saved to database.")
print("Recursive search result for 5 in [1, 2, 3, 4, 5]:", recursive_search([1, 2, 3, 4, 5], 5))
print("Random 4-digit binary number:", random_binary)
print("Converted to base 10:", base_10)
print("Sum of first 50 Fibonacci numbers:", fib_sum)
