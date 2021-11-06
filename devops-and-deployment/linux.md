# Linux

## General Commands

- `history` and then `![number]`
- `echo`

- `apt update`
- `apt install`
- `one command | second command` - second command uses output from the first command
- `which command_name` - checks whether given command is installed and if so it prints its location


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
- `mv file_name file_name2_and_location`
- `rm file_name`, supports wildcards `rm file*`
- `rm -r directory_name`

## Text Commands

- `cat file_name`, when long file `more file_name`, use this to scroll both ways `less file_name`
- `head -n 5 file_name`, `tail -n 5 file_name`
- `cat file.txt > file2.txt`, `echo blabla > file.txt`, `ls -l > files.txt`

### grep

- **nano** is a basic linux editor
- `grep 'word' file_name`
- `grep -i 'bar' file1` for case insensitive search
- `grep -R 'httpd'` for recursive search in all of the files in the current directory and all of the subdirectories
- `grep -c 'nixcraft' frontpage.m` displays count of hits for given word
- `grep -w 'word'` forces to search for entire words

## Bash

- grep, sed, tr, awk, cut, paste, join, head, tail.

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

### chmod

- owner (u), group (g), others (o)
- `chmod a+x file_name`
- `chmod ugo=rwx filename`
- `chmod go-wx,u=rwx file_name`
