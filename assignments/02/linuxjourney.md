# Learning | Linux Journey

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
