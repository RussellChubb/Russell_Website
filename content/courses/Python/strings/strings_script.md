# Strings Script

Strings in Python are sequences of characters enclosed in either single quotes (') or double quotes ("). Strings are one of the most commonly used data types in Python, and understanding how to manipulate and work with strings is essential for any programmer.

You can access individual characters of a string using square brackets with an index. NOTE: Python uses zero-based indexing, so the first character has an index of 0.

You can loop through each character in a string using a for loop. This can be useful for performing operations on each character individually.

The len() function returns the length of a string, i.e., the number of characters it contains.
The in keyword is used to check if a substring exists within a string. It returns True if the substring is found, otherwise False.

The if not keyword is used to check if a substring does not exist within a string. It returns True if the substring is not found, otherwise False.

Slicing is a technique used to extract a portion of a string. The syntax for slicing is string[start:stop:step].The start index is inclusive, while the stop index is exclusive. You can also omit the start, stop, or step values to use their defaults (beginning of the string, end of the string, and step of 1, respectively).

Strings in Python are immutable, which means they cannot be changed after they are created. However, you can create new strings based on modifications of existing ones using various methods:

The upper method converts all characters in a string to uppercase.

The lower method converts all characters in a string to lowercase.

The strip method removes leading and trailing whitespace.

The replace method replaces occurrences of a substring with another substring.

String concatenation is the process of joining two or more strings together. You can concatenate strings using the + operator - However, you can also use the join() method for concatenation:
f-Strings (formatted string literals) are a way to embed expressions inside string literals using curly braces {}.

F-strings offer a concise and readable way to format strings:

Escape characters are used to include special characters in strings that would otherwise be difficult or impossible to represent directly. They are preceded by a backslash:

Understanding these aspects of strings in Python allows you to effectively manipulate and format text in your programs, making your code more versatile and powerful.

Thank you for watching
