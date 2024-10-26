# Learning | Linux Journey | soneruen

This document contains answers to quizzes and exercises from [Linux Journey](https://linuxjourney.com/lesson/the-shell).

---

## 1. The Shell

### Quiz Questions and Answers:
- **Question**: Whatz should be outputted to the display when you type `echo Hello World`?
  - **Answer**: Hello World

### Exercises:

```bash
$ date
# Output:
# [The current date and time will be displayed]

$ whoami
# Output:
# [Your username will be displayed]
```

## 2. pwd (Print Working Directory)

### Quiz Questions and Answers: 

- **Question:** How do I find what directory you are currently in?
  - **Answer:** Use the `pwd` command.


## 3. cd (Change Directory)

### Quiz Questions and Answers:

- **Questions:** If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use?
  - **Answer:** Use the `cd ..` command that takes you to the directory above your current one.

### Exercises:

```bash
$ cd .
# Output:
# [Takes you to the current directory.]

$ cd ..
# Output:
# [Takes you to the directory above your current.]

$ cd ~
# Output:
# [This directory defaults to your “home directory”. Such as /home/pete.]

$ cd -
# Output:
# [This will take you to the previous directory you were just at.]
```

## 4. ls (List Directories)

### Quiz Questions and Answers:

- **Questions:** What command would you use to see hidden files?
  - **Answer:** Use the `ls -a` command to view the hidden files.

### Exercises:

- **Exercise 1:** Run the `ls -R` command (recursively list directory contents).

```bash
$ ls -R
# Output:
# [This will display all files and directories recursively, starting from the current directory.]

$ ls -r
# Output:
# [This will display files and directories in reverse order.]

$ ls -t
# Output:
# [This will display files sorted by modification time, with the newest files listed first.]
```

## 5. touch
### Quiz Questions and Answers:

- **Question:** How do you create a file called `myfile`?
  - **Answer:** Use the `touch myfile` command

### Exercises:

- **Exercise 1:** Create a new file.

```bash
$ touch mynewfile
# Output:
# [file will be created]
```

- **Exercise 2:** Note the timestamp.
```bash
$ ls -l mynewfile
# Output:
# -rw-r--r-- 1 user user 0 [new timestamp] mynewfile
# (The timestamp will be updated to reflect the time the `touch` command was run.)
```

## 6. file
### Quiz Questions and Answers:

- **Questions:** What command can you use to find the file type of a file?
  - **Answer:** Use the `file` command.
 
### Exercises: 

- **Exercise:** Run the `file` command on a few different directories and files.

```bash
$ file banana.jpg
# Output:
# banana.jpg [banana.jpg is identified as a JPEG image.]

$ file setup.exe
# Output:
# [This is an executable for example 64-bit file that is mostly used to install applications.]
```

## 7. cat

### Quiz Questions and Answers:

- **Question:** What's a good way to see the contents of a file?
  - **Answer:** Use the `cat` command.

### Exercises:

- **Exercise 1:** Run `cat` on a single file.

```bash
$ cat mynewfile
# Output:
# (This file is empty, so there will be no output.)

$ cat /etc/hostname
# Output:
# [Your system’s hostname will be displayed.]
```

- **Exercise 2:** Run `cat` on multiple files.
```bash
$ cat file1 file2
# Output:
# [This will concatenate the contents of `file1` and `file2`, displaying them in the terminal.]
```

## 8. less

### Quiz Questions and Answers:

- **Question:** How do you quit out of a `less` command?
  - **Answer:** Press `q` to quit out of `less` and return to the shell.

### Exercises:

- **Exercise 1:** Run `less` on a file and navigate through it.

```bash
$ less /home/pete/Documents/text1
# Output:
# (Displays the contents of `text1` file page by page.)
```

## 9. history

- `history`: Displays a list of recent commands.
- `!!`: Runs the last command again.
- `ctrl-R`: Activates reverse search, allowing you to search for a previous command by typing part of it.
- `clear`: Clears the terminal screen, making it easier to view new outputs.
- **Tab Completion**: Start typing a command, file, or directory name, then press `Tab`. The shell will attempt to autocomplete based on available matches.

### Quiz Questions and Answers:

- **Question:** What is the command to clear the terminal?
  - **Answer:** The command to clear the terminal is `clear`.

### Exercises:

- **Exercise 1:** View your command history.

  ```bash
  $ history
  # Output:
  # 1  date
  # 2  whoami
  # 3  pwd
  # 4  cd /home
  # 5  ls -l
  # ...
  ```

## 10. cp (Copy)

### Key Options and Usage:

- **Syntax:** `cp [options] source destination`
- **Wildcards:**
  - `*` - Matches any sequence of characters.
  - `?` - Matches a single character.
  - `[]` - Matches any character within the brackets.
- **Flags:**
  - `-r` (recursive): Copy directories and their contents.
  - `-i` (interactive): Prompt before overwriting files.

### Quiz Questions and Answers:

- **Question:** What flag do you need to specify to copy over a directory?
  - **Answer:** The `-r` flag is required to copy directories recursively.

### Exercises:

- **Exercise 1:** Copy a single file to a different directory.

  ```bash
  $ cp mycoolfile /home/pete/Documents/cooldocs
  # Output:
  # (Copies `mycoolfile` to `/home/pete/Documents/cooldocs`)
  ```

## 11. mv (Move)

### Key Options and Usage:

- **Syntax:** `mv [options] source destination`
- **Basic Usage:**
  - **Rename a file:** `mv oldfile newfile`
  - **Move a file to a different directory:** `mv file /target_directory`
  - **Move multiple files:** `mv file1 file2 /target_directory`
  - **Rename a directory:** `mv old_directory new_directory`
- **Flags:**
  - `-i` (interactive): Prompts before overwriting files.
  - `-b` (backup): Creates a backup of the destination file by renaming it with a `~` at the end.

### Quiz Questions and Answers:

- **Question:** How do you rename a file called `cat` to `dog`?
  - **Answer:** Use `mv cat dog` to rename the file `cat` to `dog`.

### Exercises:

- **Exercise 1:** Rename a file.

  ```bash
  $ mv oldfile newfile
  # Output:
  # (Renames `oldfile` to `newfile`)
  ```

## 12. mkdir (Make Directory)

### Key Options and Usage:

- **Syntax:** `mkdir [options] directory_name`
- **Basic Usage:**
  - **Create multiple directories:** `mkdir books paintings`
  - **Create subdirectories:** `mkdir -p books/hemingway/favorites`
  
### Quiz Questions and Answers:

- **Question:** What command is used to make a directory?
  - **Answer:** The command used to make a directory is `mkdir`.

### Exercises:

- **Exercise 1:** Create a couple of directories and move some files into that directory.

  ```bash
  $ mkdir documents images
  # Output:
  # (Creates `documents` and `images` directories)

  $ mv file1.txt documents/
  # Output:
  # (Moves `file1.txt` into the `documents` directory)

  $ mv photo.jpg images/
  # Output:
  # (Moves `photo.jpg` into the `images` directory)
  ```


- **Force removal:** 
  ```bash
  rm -f file1
  ```

## 13. rm (Remove)

### Quiz Questions and Answers:

- **Question:** How do you remove a file called `myfile`?
  - **Answer:** Use `rm myfile` to remove the file called `myfile`.

### Exercises:

- **Exercise 1:** Create a file called `-file` (don't forget the dash!).
  
  ```bash
  $ touch -file
  # Output:
  # (Creates a file named `-file`)
  ```

## 14. find

### Quiz Questions and Answers:

- **Question:** What option should I specify for `find` if I want to search by name?
  - **Answer:** Use the `-name` option to search by name.

### Exercises:

- **Exercise 1:** Find a file from the root directory that has the word `net` in it.

  ```bash
  $ find / -name "*net*"
  # Output:
  # (Displays files containing "net" in their name)
  ```

## 15. help

### Quiz Questions and Answers:

- **Question:** How do you get quick command line help for built-in bash commands?
  - **Answer:** Use the `help` command followed by the command name, e.g., `help echo`.

### Exercises:

- **Exercise 1:** Run help on the `echo` command.

  ```bash
  $ help echo
  # Output:
  # (Displays help information for the echo command)
  ```

  ```bash
  $ help logout
  # Output:
  # (Displays help information for the logout command)
  ```

  ```bash
  $ help pwd
  # Output:
  # (Displays help information for the pwd command)
  ```

## 16. man

### Quiz Questions and Answers:

- **Question:** How do you see the manuals for a command?
  - **Answer:** Use the `man` command.

### Exercises:

- **Exercise 1:** Run the `man` command on the `ls` command.

  ```bash
  $ man ls
  # Output:
  # (Displays the manual page for the ls command)
  ```

  ## 17. whatis

### Quiz Questions and Answers:

- **Question:** What command can you use to see a small description of a command?
  - **Answer:** Use the `whatis` command followed by the command name, e.g., `whatis cat`.

### Exercises:

- **Exercise 1:** Run the `whatis` command on the `less` command.

  ```bash
  $ whatis less
  # Output:
  # (Displays a brief description of the less command)
  ```

## 18. alias

### Quiz Questions and Answers:

- **Question:** What command is used to make an alias?
  - **Answer:** Use the `alias` command followed by the alias name and command, e.g., `alias foobar='ls -la'`.

### Exercises:

- **Exercise 1:** Create a couple of aliases.

  ```bash
  $ alias list='ls -la'
  $ alias greet='echo Hello, World!'
  # Output:
  # (Creates aliases 'list' and 'greet')
  ```

- **Exercise 2:** Remove the aliases.

  ```bash
  $ unalias list
  $ unalias greet
  # Output:
  # (Removes the aliases 'list' and 'greet')
  ```

## 19. exit

### Quiz Questions and Answers:

- **Question:** How can you exit from the shell?
  - **Answer:** Use the `exit` command or the `logout` command to exit from the shell.

### Exercises:

- **Exercise 1:** Exit out of the shell and see what happens.

  ```bash
  $ exit
  # Output:
  # (Closes the shell session)
  ```

  ```bash
  $ logout
  # Output:
  # (Closes the shell session)
  ```
