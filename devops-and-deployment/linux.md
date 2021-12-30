# Linux

## General Commands

- `history` and then `![number]`
- `echo`

- `apt update`
- `apt install`
- `one command | second command` - second command uses output from the first command
- `which command_name` - checks whether given command is installed and if so it prints its location
- `history` - shows history of commands that were run.

## Directory Navigation

- `ls`, `ls -1`, `ls -l`, `ls -a`
- `pwd`
- `cd`, `cd ~`
- `pushd /new_directory` - pushes current directory into the directory stack and switches to the provided path; saved directory can be retrieved using `popd`
- `locate file_name` searches recursively for files with given keyword in their name and lists them (uses Linux file DB)
- `updatedb` - updates Linux file DB

## File and Directory Commands

- `mkdir`
- `touch file_name`
- `mv file_name file_name2_and_location` or `mv file_name1 file_name2 file_name3 location/' which will move all of the specified files into a given location
- `rm file_name`, supports wildcards `rm file*`
- `rm -r directory_name`

### chmod

- owner (u), group (g), others (o)
- `chmod a+x file_name`
- `chmod ugo=rwx filename`
- `chmod go-wx,u=rwx file_name`

### find

- Allows for finding files and folders based on a wide variety of criteria.
- `find folder_to_start_search -name 'phrase'` - searches by files/folders names. `-iname` flag performs case insensitive search.
- `-type d` searches for directories only.

### du

- `du` - disk usage of the current directory.
- `-h` - file size in human-readable format.

### df

- `df` - provides disk usage information on mounted volumes.

## Text Commands

- `cat file_name`, when long file `more file_name`, use this to scroll both ways `less file_name`
- `head -n 5 file_name`, `tail -n 5 file_name`
- `tail -f` shows last part of a text file, but keeps it open and prints any new lines that appear in it (good for looking at the logs)
- `cat file.txt > file2.txt`, `echo blabla > file.txt`, `ls -l > files.txt`
- `cat file1.txt file2.txt` concatenates the files and outputs the result

### Redirect Standard Input

- `>` redirects standard input overwriting a file
- `>>` redirects standard input appending content to a file

### grep

- **nano** is a basic linux editor
- `grep 'word' file_name`
- `grep -i 'bar' file1` for case insensitive search
- `grep -R 'httpd'` for recursive search in all of the files in the current directory and all of the subdirectories
- `grep -c 'nixcraft' frontpage.m` displays count of hits for given word
- `grep -w 'word'` forces to search for entire words

### wc

- `wc file_name` returns 3 values: new lines count, words count and bytes count for a given file.

### sed

- take middle range of lines from the text file: `sed -n '12-22p'` alternatively it would be `tail -n+12 | head -n11`.

### tr

- translation/replacement using sets: `tr "abc" "cba"
- deletion of the characters in the set: `tr -d "a"`
- squeezing repeated characters from the set: `tr -s " "`

### cut

- cut certain number of characters from each line from the file: `cut -c10`, range: `cut -c10-20`, till the end `cut -c10-`

- cut delimited sequence (default delimiter is tab): `cut -d " " -f2-5`

### sort

- `sort file_name` sorts in lexicographical order
- `-r` flag to reverse
- `-n` flag to perform numerical sort
- `sort -t$'\t' -k2 -n -r` to sort numerically based on second column using tab as a delimiter

### uniq

- `uniq` removes any line consecutive repetitions of a line
- `uniq -c` provides counts for each repetition
- `uniq -u` returns only those lines that do not repeat

### paste

- `paste -s` by default tab delimiters are used
- `paste -sd $'\t\t\n'` can also use arbitrary sequence of delimiters

### diff

- `diff first_file second_file` - compares files and outputs their difference.
- `-y` flag shows files side by side.
- `-u` flag shows file differences in a git-like way.

## Expansions

- Shell expands certain characters or syntax that can be used in other commands.
- `~` - home folder.
- '*' - represents entire string.
- `?` - represents a single character.
- `{a,b,c}.txt` - creates a carthesian product with a string outside of curly braces. In this example it would output 3 strings: `a.txt b.txt c.txt`.
- `{1..10}` - creates a count from the first number to the last one (inclusive).
