# The Linux CLI Commands Handbook

## Table of Contents

- Preface
- The Linux Handbook (Overview)
- Conclusion

### Commands covered (quick list)

1. Introduction to Linux
2. man
3. ls
4. cd
5. pwd
6. mkdir
7. rmdir
8. mv
9. cp
10. open
11. touch
12. find
13. ln
14. gzip
15. gunzip
16. tar
17. alias
18. cat
19. less
20. tail
21. wc
22. grep
23. sort
24. uniq
25. diff
26. echo
27. chown
28. chmod
29. umask
30. du
31. df
32. basename
33. dirname
34. ps
35. top
36. kill
37. killall
38. jobs
39. bg
40. fg
41. type
42. which
43. nohup
44. xargs
45. vim
46. emacs
47. nano
48. whoami
49. who
50. su
51. sudo
52. passwd
53. ping
54. traceroute
55. clear
56. history
57. export
58. crontab
59. uname
60. env
61. printenv

---

## Preface

The Linux Handbook follows the 80/20 rule: learn in 20% of the time the 80% of a topic.

In particular, the goal is to get you up to speed quickly with Linux. This book is written by Flavio. I publish programming tutorials on my blog flaviocopes.com and I organize a yearly bootcamp at bootcamp.dev. You can reach me on Twitter @flaviocopes.

Enjoy!

---

## The Linux Handbook

### 1. Introduction to Linux

Linux is an operating system, like macOS or Windows. It is also the most popular Open Source and free, as in freedom, operating system. It powers the vast majority of the servers that compose the Internet. It's the base upon which everything is built upon. Android is based on (a modified version of) Linux.

The Linux "core" (called kernel) was born in 1991 in Finland. It went on to be the kernel of the GNU Operating System, creating the duo GNU/Linux. There's not just "one Linux" — we have distributions (distros) like Debian, Red Hat, and Ubuntu.

macOS is a UNIX-like OS and shares many commands with GNU/Linux. Windows has WSL (Windows Subsystem for Linux). Most cloud servers run Linux (VPS providers like DigitalOcean).

A shell is a command interpreter (Bash, Zsh, Fish, etc.) that lets you run programs and write scripts. In this handbook we'll cover common commands you'll use frequently.

### 2. man

The `man` command shows the manual page for other commands.

Example:

```sh
man <command>
```

Man pages are comprehensive; for quick examples use the tldr pages project (`tldr <command>`).

### 3. ls

List files in a directory:

```sh
ls
ls /bin
ls -al /bin
```

The `-l` option shows detailed info (permissions, links, owner, group, size, modified date, name). The `-a` option shows hidden files (those starting with `.`).

### 4. cd

Change directory:

```sh
cd <directory>
cd ..    # parent directory
cd /etc  # absolute path
```

Example:

```sh
mkdir fruits
cd fruits
```

### 5. pwd

Print working directory:

```sh
pwd
```

### 6. mkdir

Create directories:

```sh
mkdir fruits
mkdir dogs cars
mkdir -p fruits/apples
```

### 7. rmdir

Remove empty directories:

```sh
rmdir fruits
rmdir fruits cars
```

To remove directories with contents, use `rm -rf` (dangerous):

```sh
rm -rf fruits cars
```

### 8. mv

Move or rename files:

```sh
touch pear
mv pear new_pear
mv pear apple fruits   # move multiple files into folder
```

### 9. cp

Copy files and directories:

```sh
cp apple another_apple
cp -r fruits cars
```

### 10. open (macOS)

Open files or directories on macOS (opens Finder or apps):

```sh
open <filename>
open <directory>
open .
open <application name>
```

### 11. touch

Create an empty file or update its timestamp:

```sh
touch apple
```

### 12. find

Search for files/dirs recursively. Examples:

```sh
find . -name '*.js'
find . -type d -name src
find folder1 folder2 -name filename.txt
find . -type d -name '*.md' -not -path 'node_modules/*'
find . -type f -size +100c
find . -type f -mtime -1
find . -type f -mtime -1 -delete
find . -type f -exec cat {} \;
```

Notes: use quotes around `*` to avoid shell expansion. Use `-iname` for case-insensitive name matching.

### 13. ln

Create links (hard or symbolic):

Hard link:

```sh
ln original link
ln recipes.txt newrecipes.txt
```

Symbolic (soft) link:

```sh
ln -s original link
ln -s recipes.txt newrecipes.txt
```

### 14. gzip

Compress files with gzip:

```sh
gzip filename
gzip -c filename > filename.gz   # keep original
gzip -k filename                 # keep original (if supported)
gzip -1 filename                 # compression level 1..9
gzip -r a_folder                 # recursive
gzip -d filename.gz              # decompress
```

### 15. gunzip

Equivalent to `gzip -d`:

```sh
gunzip filename.gz
gunzip -c filename.gz > anotherfilename
```

### 16. tar

Create and extract archives:

```shn
tar -cf archive.tar file1 file2
tar -xf archive.tar
tar -xf archive.tar -C directory
# gzipped tar
tar -czf archive.tar.gz file1 file2
tar -xf archive.tar.gz
```

### 17. alias

Create shell aliases:

```sh
alias ll='ls -al'
alias lsthis="ls $PWD"
alias lscurrent='ls $PWD'
```

To make aliases permanent, add them to `~/.bashrc`, `~/.profile`, `~/.bash_profile`, or your shell config file.

### 18. cat

Print or concatenate files:

```sh
cat file
cat file1 file2
cat file1 file2 > file3   # overwrite
cat file1 file2 >> file3  # append
cat -n file1              # show line numbers
```

### 19. less

View files interactively:

```sh
less file
# navigation: q to quit, / to search, ? to search backward, v to open editor, F to follow (like tail -f)
```

### 20. tail

Show end of file; follow for live updates:

```sh
tail -f /var/log/system.log
tail -n 10 file
tail -n +10 file
```

### 21. wc

Count lines, words, bytes:

```sh
wc file
wc -l file    # lines
wc -w file    # words
wc -c file    # bytes
wc -m file    # characters (multibyte aware)
```

### 22. grep

Search text using patterns/regex:

```sh
grep 'pattern' file
grep -n 'pattern' file         # show line numbers
grep -nC 2 'pattern' file      # show 2 lines of context
less file | grep -n 'pattern'  # pipe to grep
grep -i 'pattern' file         # case insensitive
grep -v 'pattern' file        # invert match
```

### 23. sort

Sort lines of text:

```sh
sort file
sort -r file        # reverse
sort -n file        # numeric
sort -u file        # unique
ls | sort
```

### 24. uniq

Filter adjacent duplicate lines; often used with `sort`:

```sh
sort dogs.txt | uniq
sort dogs.txt | uniq -d    # show duplicates
sort dogs.txt | uniq -u    # show unique lines
sort dogs.txt | uniq -c | sort -nr   # frequency sort
```

### 25. diff

Show differences between files:

```sh
diff dogs.txt moredogs.txt
diff -y file1 file2    # side-by-side
diff -u file1 file2    # unified format (git-friendly)
diff -r dir1 dir2      # recursive directories
```

### 26. echo

Print arguments or variables:

```sh
echo "hello"
echo "hello" >> output.txt
echo "The path variable is $PATH"
echo $(ls -al)
echo {1..5}
```

Escape special characters as needed (e.g. `\`, `$`, `.`).

### 27. chown

Change file owner and group:

```sh
chown <owner> <file>
chown flavio test.txt
chown -R <owner> <dir>         # recursive
chown owner:group file
chgrp <group> file
```

### 28. chmod

Change file permissions (symbolic or numeric):

Symbolic examples:

```sh
chmod a+r filename
chmod a+rw filename
chmod o-rwx filename
chmod og-r filename
chmod -R u+rw folder
```

Numeric examples:

```sh
chmod 777 filename
chmod 755 filename
chmod 644 filename
```

Permission bits: read=4, write=2, execute=1 (sum to form digits 0..7).

### 29. umask

Set default file creation mask:

```sh
umask       # show current mask
umask -S    # human readable
umask 002
umask g+r
```

### 30. du

Estimate directory sizes:

```sh
du
du -h <directory>            # human readable
du -a                        # include files
du -h <directory> | sort -nr | head
```

### 31. df

Show disk free/usage:

```sh
df
df -h   # human readable
df <path>  # show filesystem for path
```

### 32. basename

Extract final component of a path:

```sh
basename /Users/flavio/test.txt   # -> test.txt
```

### 33. dirname

Extract directory part of a path:

```sh
dirname /Users/flavio/test.txt   # -> /Users/flavio
```

### 34. ps

List processes:

```sh
ps
ps ax
ps axww | grep "Visual Studio Code"
```

Columns include PID, TT, STAT, TIME, and command. Use `ps axww` to avoid truncation.

### 35. top

Interactive real-time process viewer:

```sh
top
top -o mem   # sort by memory
```

Quit with `q` or `Ctrl-C`.

### 36. kill

Send signals to processes:

```sh
kill <PID>
kill -HUP <PID>
kill -INT <PID>
kill -KILL <PID>
kill -TERM <PID>
kill -CONT <PID>
kill -STOP <PID>
```

Signals can also be sent by number (e.g. `kill -9 <PID>` for KILL).

### 37. killall

Send a signal to processes by name:

```sh
killall top
killall -HUP top
```

### 38. jobs

List background jobs started from the shell:

```sh
top &
jobs
fg %1
```

Use `jobs -l` to show PIDs.

### 39. bg

Resume a stopped job in the background:

```sh
bg %1
bg
```

### 40. fg

Bring a background job to the foreground:

```sh
fg %1
fg
```

### 41. type

Show how a command will be interpreted by the shell (executable, builtin, function, alias):

```sh
type ls
```

### 42. which

Show the full path of an executable on `PATH` (does not work for aliases/builtins):

```sh
which ls
```

### 43. nohup

Run a command immune to hangups, so it continues after logout:

```sh
nohup <command> &
```

### 44. xargs

Build and execute command lines from standard input:

```sh
command1 | xargs command2
cat todelete.txt | xargs rm
xargs -p    # prompt before execution
xargs -n1 -p
xargs -I % /bin/bash -c 'command2 %; command3 %'
```

### 45. vim

Modal text editor. Basics:

```sh
vi test.txt
# i to enter insert mode, esc to exit insert mode
# :w to save, :q to quit, :wq to save and quit, :q! to quit without saving
# undo: u, redo: Ctrl-r
```

Use `vimtutor` to learn interactively.

### 46. emacs

Powerful editor; start with:

```sh
emacs
emacs <filename>
# Exit: Ctrl-x Ctrl-c
# Tutorial: Ctrl-h t
```

macOS users: consider installing a modern Emacs via Homebrew (`brew install emacs`).

### 47. nano

Simple beginner editor:

```sh
nano <filename>
# Quit: Ctrl-X
```

### 48. whoami

Print current user:

```sh
whoami
```

### 49. who

Show users logged in:

```sh
who
who -aH
who am i
```

### 50. su

Switch user:

```sh
su <username>
# su (without args) switches to root and asks for root password
exit   # return to previous user
```

### 51. sudo

Run commands as another user (commonly root):

```sh
sudo <command>
sudo -i        # start root shell
sudo -u flavio ls /Users/flavio
```

### 52. passwd

Change user's password:

```sh
passwd          # change your own password interactively
passwd <username>   # as root, set another user's password
```

### 53. ping

Send ICMP echo requests to test reachability:

```sh
ping google.com
ping -c 2 google.com
```

Stop with `Ctrl-C`.

### 54. traceroute

Trace network route to a host:

```sh
traceroute flaviocopes.com
traceroute -q 1 flaviocopes.com
```

### 55. clear

Clear the terminal screen (shortcut `Ctrl-L`):

```sh
clear
clear -x   # clears screen but allows scrollback
```

### 56. history

Show command history:

```sh
history
history | grep docker
!121   # repeat command number 121
history -c   # clear history
```

### 57. export

Export environment variables to child processes:

```sh
TEST="test"
echo $TEST
export TEST="test"
./script.sh  # script sees exported TEST
export PATH=$PATH:/new/path
export -n TEST   # unset exported flag for TEST
```

### 58. crontab

Edit scheduled cron jobs:

```sh
crontab -l
EDITOR=nano crontab -e
# Example cron line: * */12 * * * /Users/flavio/test.sh >/dev/null 2>&1
```

### 59. uname

Show system information:

```sh
uname
uname -a
uname -s
uname -r
uname -m
```

macOS: `sw_vers` shows macOS-specific version details.

### 60. env

Run a command with modified environment or print environment:

```sh
env USER=flavio node app.js
env -i /usr/local/bin/node app.js
env -i NAME=flavio node app.js
env -u HOME node app.js
env   # list env
```

### 61. printenv

Print environment variables or a specific variable:

```sh
printenv
printenv PATH
```

---
