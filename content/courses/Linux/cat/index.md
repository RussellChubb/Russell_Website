---
title: "Cat Command"
description: ""
summary: "Introduction to the Cat Command in Linux"
showAuthor: true
date: 2026-05-09
featureimage: "featured.jpg"
tags: ["Linux"]
series: ["Learn Linux"]
series_order: 3
---

The 'cat' command, short for 'concatenate', is a versatile tool that reads files sequentially, writing them to standard output. This makes it ideal for viewing and concatenating files.
Whether you're a beginner or an experienced Linux user, the 'cat' command is an essential tool for quickly viewing and manipulating text files.

Before we begin, the Linux environment I’m using is the CoCalc Linux Terminal (Running BASH). This environment provides a consistent, easy to access way for myself and others to use Linux, without the need to install any custom programmes, or spend time configuring your own OS. (This isn’t a sponsored message, even though it kind of sounds like it)

The syntax for the 'cat' command is as follows: cat, followed by any optional flags, and then the file or files you want to work with.

Here’s an example of when you can use the 'cat' command to answer a business problem, specifically “Yo dude… can you please display the contents of the file 'yo.txt'?”

To answer this, type cat yo.txt. This command will output the entire content of the file 'example.txt' to your terminal.

The 'cat' command can be enhanced with various flags, which I’ll explain now.

NOTE: If you don’t know what flags are, be sure to watch my previous video, where I provide an explanation of this concept.

The 'cat' command has several useful flags, with the flags I’ll focus on today being: -n, -b, and -s.

The -n flag is useful for adding line numbers to the output. For example, cat -n yo.txt will display the content of 'yo.txt' with each line numbered.

The -b flag is similar but only numbers non-empty lines. For example, cat -b yo.txt will number only the lines with content, skipping the blank lines.

In addition to viewing file contents, the 'cat' command can also be used to concatenate multiple files into one. For example, cat one.txt two.txt > combined.txt will combine the contents of 'one.txt' and 'two.txt' into a new file called 'combined.txt'.

So there you have it: an introduction to the Linux 'cat' command! Mastering the 'cat' command will help you become more proficient in managing text files in Linux, making it an indispensable tool in your command-line toolkit.

Thank you for watching!
