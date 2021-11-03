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
