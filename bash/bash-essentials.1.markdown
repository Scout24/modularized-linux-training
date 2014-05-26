bash-essentials(1) -- Bash Essential Tricks - ImmobilienScout24 Linux Training
==============================================================================

## LICENSE
Creative Commons (CC BY-SA 3.0)

## DESCRIPTION
This material should help you to improve your abilities to write good bash scripts. Better
scripts means less maintenace, faster execution of your tasks and therefore a time saving for you.
This man page contains a starting point for:

    01.) REDIRECTIONS
    02.) PIPELINES
    03.) JOB CONTROL
    04.) QUOTES
    05.) COMMAND SUBSTITUTION
    06.) COMMAND LISTS
    07.) EXIT STATUS
    08.) USEFULL SYSTEM COMMANDS
    09.) SED
    10.) AWK
    11.) REGULAR EXPRESSIONS (REGEX)
    12.) PATTERN MATCHING
    13.) BRACE EXPANSION
    14.) EXECUTION OF BASH SCRIPTS
    15.) COMMENTS
    16.) VARIABLES
    17.) USER INPUT
    18.) POSITIONAL PARAMETERS
    19.) CONDITIONAL EXPRESSIONS
    20.) COMPOUND COMMANDS
    21.) LOOPS
    22.) ARITHMETIC EVALUATION
    23.) FUNCTIONS
    24.) HERE DOCUMENTS
    25.) PROCESS SUBSTITUTION
    26.) SHELL BUILDIN COMMANDS
    27.) SIGNALS
    28.) CODING GUIDELINE

## REDIRECTIONS
### STDOUT

Here is an example for redirecting STDOUT:

	$ cat /var/log/messages > ~/tmp/own.log

### STDERR

Here is an example for redirecting STDERR:

	$ cat /var/log/foobar 2> ~/tmp/own.err

### STDIN

Here is an example for redirecting STDIN:

	$ mail -s "My logfile" my@domain.org < ~/tmp/my.log

### Combination
You can combine the different channels as well. For example an redirection from STDOUT and STDERR:

	$ service apache2 reload &> /dev/null

Note: Very old versions of bash did not support __&>__, use >/dev/null 2>&1 instead.

## PIPELINES
Beside the redirection you can concatenate the different channels. For example __STDOUT__ with __STDIN__:

	$ grep ERROR /var/log/syslog | wc -l

## JOB CONTROL
Job control refers to the ability to selectively stop (suspend) the execution of processes
and continue (resume) their execution at a later point. The following work in interactive Bash sessions:

* __fg__: Command for putting a job in foreground
* __bg__: Command for putting a job in background
* __Ctrl+Z__: Stop/suspend the current running process

Here is an simple example:

    $ top
    ...
    Ctrl+Z
    [1]+  Stopped              top

The process is now suspended. To resume this process (the id is 1) use __fg__ to
resume it to foreground or __bg__ for continuing this process in the background:

    $ fg 1

If you want to start a program as a background job immediately append __&__ after the command:

    $ top &

## QUOTES
__Example 1:__

With the help of echo you can generate any output you want to STDOUT. Whitespaces will be converted to one whitespace. To avoid this, surround your output with "" or '':

    $ echo one   two
    one two

    $ echo "one   two"
    one   two

__Example 2:__

With single quotes ('...') you loose the meaning of meta characters:

    $ echo 'This is the content from $VAR: $VAR'
    This is the content from $VAR: $VAR

To avoid this use nesting:

    $ echo 'This is the content from $VAR: "'$VAR'"'
    This is the content from $VAR: "value"

__Example 3:__

If you to not want to use nesting use double quotes ("..."):

* Meta characters will be kept
* You can use command substitutions
* Meta characters in strings have to be masked

    $ echo "This is the content from \$VAR: \"$VAR\""
    This is the content from $VAR: "value"

## COMMAND SUBSTITUTION
Commands will be executed within other commands and their output will be used in the surrounding command:

	$ echo "Directory has $(ls -l | wc -l) entries"

The syntax is as seen $(...):

* \`...\` is bourne shell format and __not recommended__.
* $(...) is bash-format and more robust and also allows nesting.

## COMMAND LISTS
In bash you can concatenate a list of commands and build command lists. For example:

	$ cat /var/log/messages ; echo done
	$ cat /var/log/messages || echo fail
	$ cat /var/log/messages && echo done

Further you can group commands with (...) or {...}:

	$ ( tail /var/log/messages ; echo hello world ; date )

The main difference between (...) and {...} is that (...) spawns a sub-shell.

## EXIT STATUS
Every command (should) exit with an appropriate exit status:

* Equals 0 means success
* Unlike 0 means error
* Values over 125 indicate special errors
* 127 means "command not found"
* 126 means "not executable"
* Fatal errors are in bash 128+SIGNUM

For example you can combine commands like this:

	$ cat /var/log/messages && echo "the log exists"
	$ cat /var/log/foobar || echo "the log does not exist"

Armed with this and the knowledge above, you are able to build more complex command structures:

	$ test : && ( echo "this is true"; echo "the test was executed on $(date +%d.%m.%Y)" ; echo "done" )

ATTENTION: Please use this sparingly, because you can create very unreadable command structures with this!

## USEFUL SYSTEM COMMANDS
### cat
Concatenate - Read given files or standard input and print all of it on the standard output

### wc
Word Cound - Print count of newlines, words or bytes for each file

### grep
Print lines matching a pattern

### tr
Translate or delete characters

### cut
Print out columns from files

### sort
Sort lines of text files

### awk
Pattern scanning and processing language

### sed
Stream editor for filtering and transforming text

### less
Simple text file viewer ("less is more")

### time
Run programs and summarize system resource usage

### date
Print or set the system date and time. An example:

	$ date --date="20091111 +1 day"
	$ date --date="20080110 + 7 hours"

ATTENTION! Be careful when using date as root as you can accidentially set the system clock

### mktemp
Create a temporary file or directory

### uniq
Filter out duplicate lines. Input must be sorted. The same can be achieved with sort -u

### tee
Read from standard input and write to standard output and given files

### logger
A shell command interface to the syslog(3) system log module:

    $ logger -p user.err -t "myscript" "ERROR: Script cannot be completed!"

## SED
### General
Is a stream editor for filtering and transforming text in an non interactive manner.

* Processing is done via commands
* The input will be processed line by line
* You can execute different editor commands with the use of __-e__ (not needed for a single command)
* Per default the result is printed to STDOUT (Use __-i__ if you want to edit a file directly)
* You can select the part to be edited via line numbers or regular expressions
* The regex is following the rules you might already know from grep (PCRE are also possible with __-r__)
* Regex have to be enclosed by __/__ or __\#__

Here are some examples. The data file contains (boolean.dat):

    TRUE,FALSE
    FALSE,FALSE
    TRUE,TRUE
    MARKER
    FALSE,FALSE
    TRUE,TRUE

Replaces in BOOL.file the first occurence of FALSE with TRUE and __ONLY__ the first occurence:

    $ sed 's/FALSE/TRUE/' boolean.dat

Replaces in line 5 exactly the first occurence of FALSE with TRUE:

    $ sed '5s/FALSE/TRUE/' boolean.dat

Replaces in line 1-3 exactly the first occurence of FALSE (per line):

    $ sed '1,3s/FALSE/TRUE/' boolean.dat

Replaces from line 1 on to the first occurence of MARKER, FALSE with TRUE:

    $ sed '1,/MARKER/s/FALSE/TRUE/' boolean.dat

### Multiple replacements per line
If you want to replace more than one occurences per line, you can use the following:

    $ sed 's/FALSE/TRUE/g' boolean.dat

Or if you want edit the first occurence and the second one:

    $ sed -e 's/FALSE/TRUE/' -e 's/FALSE/DUNNO/' boolean.dat

### Using bash variables
Because $ is used in regex as the line end for example you have to use bash variables in the following way:

    $ VAR=DUNNO; sed 's/FALSE$/'"$VAR"'/g' boolean.dat

Or (if you need the real regex $ then you have to escape it):

    $ VAR=DUNNO; sed "s/FALSE\$/$VAR/g" boolean.dat

### Add text parts
If you want to add text parts, see the following examples. Here the content of file1 is pasted after line 6 of file2:

    $ sed '6 r file1' file2

Or add an extra line with "HIT" after each line with a FALSE:

    $ sed '/FALSE/a HIT' boolean.dat

### Deleting elements
Delete all line with the occurence of FALSE:

    $ sed '/FALSE/d' boolean.dat

Or delete lines directly (here line 6):

    $ sed '6 d' boolean.dat

## AWK
Pattern scanning and processing language.
It applies a list of conditions and commands to every line of the input files.
The structure of __awk__ is very simple:

* awk 'Pattern { Commands }'
* Example data (employees.txt):

		100  Thomas  Manager    Sales       100
		200  Jason   Developer  Technology  500
		300  Sanjay  Sysadmin   Tehcnology  300
		400  Nisha   Manager    Marketing   200
		500  Randy   DBA        Technology  400

Calculate with fields:

		$ awk '$1 > $5 { print $2 }' employees.txt
		Nisha
		Randy

Or filter by pattern:

		$ awk '/Te[ch]+nology/ { print $2 }' employees.txt
		Jason
		Sanjay
		Randy

* The pattern and action are not really necessary, a missing pattern matches every line:

		$ awk '$1 > $5' employees.txt
		400  Nisha   Manager    Marketing   200
		500  Randy   DBA        Technology  400

		$ awk '{ print $2 }' employees.txt
		Thomas
		Jason
		Sanjay
		Nisha
		Randy

Without an input file, STDIN will be used:

	$ echo 100 | awk '$1 > 0 {print $1, " is multiplied with two point five ", $1*2.5}'

Per default the field separator is an whitespace or tabulator. If you want to use an alternative
field separator use the __-F__ commandline option.

### Awk Scripts
Alternatively you can write an awk script:

	$ cat minicalc.awk
	#!/usr/bin/awk -f
	{
	    $1 > 0 {print $1, " is multiplied with two point five ", $1*2.5}
	}

	$ echo 100 | ./minicalc.awk

The general format of an awk script is like this:

	BEGIN { Commands }
	Condition { Commands }
	{ Commands }
	END { Commands }

The entire script is run repeatedly for each line of the text file that awk processes.
All command blocks with matching conditions are executed. Conditions can be Regular Expressions
in /.../ or conditional expressions.

BEGIN and END are special conditions which match exactly once and allow doing stuff before any line from the input files is read or after all the input files have been processed. With BEGIN and END it is very simple to initialize some variables, e.g. a counter, process the input files and then print a summary at the end.

### Predefined variables
Beside the possibility of using user defined variables, awk has a set of built-in variables:

    * __$0__: Gives the entire active line
    * __$1__: Gives the first field, $2 the second field and so on ...
    * __$2__: Gives the second field etc.
    * __NF__: Gives you the total number of fields in a record
    * __NR__: Gives you the total number of records being processed or line number

An example for showing the last field of the data above:

    $ awk '{print $2," -> ",$NF}' employees.txt
    Thomas  ->  100
    Jason  ->  500
    Sanjay  ->  300
    Nisha  ->  200
    Randy  ->  400

## REGULAR EXPRESSIONS (REGEX)
The following describes regular expressions in general. grep/sed/awk/... have some special notations which are not covered in this section.

### Special characters
* . - Any character
* ^ - Beginning of the line
* $ - Line end

__Example:__

"L.n.x" matches to "Linux" or "Lunix" but not to "Liinux"

### Quantifiers
* ? - No or exactly one repeat of the previous character
* \+ - One or several repeats of the previous character
* \* - No or several repeats of the previous character
* {m,n} - Minimum of m to maximum n repeats of the previous character

### Grouping
With [...] you can group characters. There are some additional rules:

* ^ in [...] negates the grouped characters
* [abc] means an a or b or c (e.g. abcdedf)
* If you want to use more than one sign you have to use (?:...)
* You can use ranges like: [a-z] or [a-zA-Z] or [0-9]

### Predefined character sets
Beside the grouping above you can use predefined character sets. Here some examples:

* __\t__: A tabulator
* __\n__: A line break
* __\s__: A whitespace, line break, tabulator or carriage return
* __\d__: A sign of type number
* __\w__: A letter, number or underline

__ATTENTION:__ sed don't understand the above escapes by default! Use the __-r__ switch for extended regex in that case!

### Greedy vs. non greedy
Regex can be greedy and non greedy. What does this mean? A greedy regex will match as
much as it can, while a non greedy regex will match the first possibility.
An example string would be __bcdabdcbabcd__:

* __(.*)ab__ will remember __bcdabdcb__ and is therefore greedy
* __(.*?)ab__ will remember __bcd__

__HINT:__ This don't work with __sed__ use __perl -pe__ instead! If you want to use the remember function in __sed__ , escape the __()__ characters with __\__.

__HINT:__ There are good online tools for fast testing of your regex. E.g.: http://regex101.com/

## PATTERN MATCHING
You can use pattern in the bash command line as well:

* \* - No or several characters
* ? - A single sign
* [abc] - Any sign inside the bracket
* [a-z] - Any sign within the given range
* [!ab] - Any sign, which isn't in the bracket
* [:class:] - Character classes - e.g. alnum alpha ascii blank cntrl digit graph lower print punct space upper word xdigit. Example: [:ascii:]+ matches 1 or more ascii characters

## BRACE EXPANSION
Converts lists into separate strings. Helps a lot to combine repetitive parts of a command line. For example the following are the same:

	$ mkdir /tmp/example_{1,2,3}
    $ mkdir /tmp/example_1 /tmp/example_2 /tmp/example_3

And the following are also the same, even when using a pattern as part of the brace expansion:

	$ ls /lib/modules/3.2.0-{48,5?}-*
    $ ls /lib/modules/3.2.0-48-* /lib/modules/3.2.0-5?-*

Note that this is a feature of the shell. Therefore it does not work in quotes: __"{1,2}"__ is just that without expansion.

## EXECUTION OF BASH SCRIPTS
You can put single commands into one file and they will be executed in a batch like manner. But bash
scripts are much more like this. With the right ingredients, you can create very powerful scripts, 
which are able to automate annoying complex tasks. There are several ways for calling an bash script.
The first one is to directly load it with the interpreter:

	$ bash script

Or if you put the so called shebang (\#\!/bin/bash) in the first line (more details in the __SHEBANG__ section) and change the execution
rights appropriately:

	$ ./script

To change the file permissions you have to add the execute flag:

	$ chmod 755 script.sh
	$ chmod u+x script.sh

The script name is freely selectable, but avoid the names of system commands!
Best use the __type__ command to find out if the new name for a script is still available.

For Bash the file suffix (e.g. .sh) is irrelevant. However, it might help some editors or IDEs to correctly format the source code. A useful compromise between easing the development and the usage of a script is to use the .sh suffix in the source code and then install the script without the .sh suffix.

## COMMENTS
To create an maintainable bash script you have to use comments, which describes the things you are 
doing inside the script. A command begins with an __\#__ and goes till the end of line.

### SHEBANG
A special comment is the first line, if it begins with __\#!__. This defines the program, with which this file needs to be run. The kernel checks executable files for such a line and runs the named program with the file as first argument. That way a Bash, Perl, Awk ... script does not need a special suffix to be executed by the correct interpreter. Typical examples are:

* \#!/bin/bash to use Bash
* \#!/bin/sh to specifically use any SH-compatible shell. This increases portability to other systems, but one must make sure not to use any Bash-specific statements.
* \#!/usr/bin/perl to run a Perl script
* \#!/usr/bin/env python to run a Python script. Note the use of the env helper which will search for python in $PATH.

One can also give further command line arguments to the interpreter to influence the behaviour. Common Examples are setting the interpreter to a strict mode:

* \#!/bin/bash -e -u to abort on uncought errors or unset variables
* \#!/usr/bin/perl -w to set strict mode
* \#!/usr/bin/awk -f to tell awk to read this file as script file

## VARIABLES
In general you have to differ between two situations. Assign a value to a variable and read the value
of the variable. When you assign a variable __DO NOT__ use a $ in front (except where you want to read the name of the variable to assing from another variable). When you use a $ in front you read
out the assigned value. To assign a value use __=__ and no whitespaces between key/value and __=__\!

Variable names are case sensitive. A common practice is to use all caps for variables that have a larger scope or that are used for something constant or user-configurable. Lowercase is used for local variables.

__Example:__

    $ VAR="value"
    $ echo $VAR
    
### Regular Variables
For regular variables you can use different variable expansions (parameter expansions):

* __${#VAR}__: Length of the string
* __${parameter#word}__, __${parameter##word}__: Remove matching prefix pattern, ## is greedy

        $ DIR=/var/log/apache2
		$ echo "Result: ${DIR#*/}, ${DIR##*/}"
		Result: var/log/apache2, apache2
        

* __${parameter%word}__, __${parameter%%word}__: Remove matching suffix pattern, %% is greedy
* __${parameter:offset}__, __${parameter:offset:length}__: Substring expansion.
* __${parameter//pattern/string}__: Pattern substitution, use single / to replace only first occurance
* __${parameter^^pattern}__: Convert in uppercase, use single ^ to convert only first char. Omit patter to match any
* __${parameter,,pattern}__: Convert in lowercase, use single , to convert only first char. Omit pattern to match any

Or be able to react on undefined variables:

* __${parameter:-string}__: If parameter is not set or null, use string
* __${parameter:=string}__: If parameter is not set or null, set to string and use string
* __${parameter:+string}__: If parameter is not set or null, do nothing. If it is set, use string instead of actual value.

### Arrays
Beside the normal scalar variables, you can use arrays in bash scripts. Multidimensional arrays are not supported.
Here is how you can assign values:

    $ VAR=( val1 val2 val3 )
    $ VAR[3]=val

Further you can use different variable expansions (parameter expansions):

* __${#var[@]}__ or __${#var[*]}__: Count of array elements
* __${var[@]}__ or __${var[*]}__: Gives the content of all array elements. The [@] form does correct word expansion on the values if used in "" quotes. Mostt common example is iterating over command line arguments while respecting arguments with blanks and other special chars:
        
        for param in "$@" ; do
            echo "Param: >>$param<<"
        done

If you go with an loop through an array you might want to know which index is currently active:

    for ((i=0 ; i<${#NAMES[@]} ; i++)) ; do
        echo ${NAMES[$i]}
        # Other stuff here
    done

### Special Variables
Beside user defined variables bash has so called SHELL VARIABLES or SPECIAL PARAMETERS. 
The most importent are listed below:

* __$HOME__: Contain the absolute path of the home dir from the current active user
* __$PWD__: Contain the absolute path of the current directory (__pwd__ is the appropriate shell command)
* __$SHELL__: Which is the current active shell. Useful to restrict the execution e.g. only in __bash__ and not __sh__
* __$IFS__: Represents the internal field seperator. For example if you want to read the list "one:two:three" in a loop, you have to set __IFS__ to __:__
* __$PPID__: Contain the process id of the parent process
* __$UID__: Contain the UID of the current active user
* __$RANDOM__: Use this to get a random integer value
* __$#__: Contain the amount of parameters, with wich the script was launched. In functions the amount of function parameters is contained.
* __$@__: Expands the positianal parameters. When the expansion occurs within double quotes, each parameter expands to a separate word.
* __$*__: Expands the positianal parameters. When the expansion occurs within double quotes, all parameters expand to a single word.
* __$?__: Contain the exit code of the last executed command
* __PIPESTATUS__: Is a Bash Array containing the exit codes of the last command pipe. This is the only way to access the exit code of the first (or any other non-last) element in the command pipe
* __$$__: Expands to the process ID of the shell
* __$0__: Expands  to the name of the shell or shell script

### Environment Variables

Shell variables can be exported to called commands as environment variables with the __export__ builtin. Note that Subshells always inherit plain Shell variables while external commands only inherit variables exported to the environment:

    $ unset foo ; foo=bar ; ( echo $foo ; env | grep foo ) ; declare -p foo
    bar
    declare -- foo="bar"

    $ unset foo ; export foo=bar ; ( echo $foo ; env | grep foo )
    bar
    foo=bar
    declare -x foo="bar"

The __env__ command, if used without arguments, simply prints all environment variables. Its main purpose is to manipulate the environment before running another command.

### declare
Variables can be even created without a value assignment. For this purpose the builtin command __declare__ is used. Here a simple typification occurs.
Here are some of the options:

* __-a__: Each name is an indexed array variable
* __-i__: The variable is treated as an integer. Arithmetic evaluation is performed when the variable is assigned a value.
* __-l__ or __-u__: When the variable is assigned a value, all upper-case characters are converted to lower-case.
* __-x__: Mark names for export to subsequent commands via the environment
* __-r__: Make names readonly.  These names cannot then be assigned values by subsequent assignment statements or unset.

### unset
With __unset__ you can remove a variable, if it is not set readonly. The following example demonstrate this behaviour:

	$ declare -r foo=bar
	$ declare -p foo
	declare -r foo="bar"
	$ foo=baz
	bash: foo: readonly variable
	$ unset foo
	$ declare -p foo
	declare -r foo="bar"
	
Reference variable names with __$__ when using __unset__!

### Debugging Variables
Use the __declare -p__ builtin command to get a canonical representation of a variable which could be also used to recreate that variable with the same content:

    $ a=foo
    $ let b=2+4
    $ c=( $a $b )
    $ declare -p a b c
    declare -- a="foo"
    declare -- b="6"
    declare -a c='([0]="foo" [1]="6")'


## USER INPUT
Scripts can interact through STDIN with the user. To read from STDIN you can use the following:

    read -p "What is your name: " NAME
    echo $NAME

## POSITIONAL PARAMETERS
Scripts can be called with command line arguments. These are available in the script through the special variables __$1__, __$2__ etc.

* __$0__ contains the script name as it was called
* Cannot be overwritten with a normal assignment
* You can write to these variables with the use of __set__
* To acces values higher than __$9__ use e.g. __${12}__
* The __shift__ builtin command removes the first value from this list. This is used to iterate over an unknown number of command line argments:

        while [[ "$1" ]] ; do
            # do something with $1
            shift
        done

## CONDITIONAL EXPRESSIONS
The last two examples contained conditions. Such conditions can be used in the following constructs:

* __[[__...__]]__ builtin
* __test__ and __[__ builtins

For a complete list of the test parameters use __man test__. Examples for conditions are:

* __-f__ file: True, if the file exist
* __-d__ dir: True, if the directory exist
* __-z__ string: The length of STRING is zero
* __==__ or __=__: True, if both strings are equal
* __\<__: True, if string1 is less string2
* __\>__: True, if string1 is greater string2
* Arythmetic comparisons with -eq, -ne, -lt, -le, -gt und -ge

__[[__ is the extended version of test. == and != uses Pattern Expansion, and &&, ||, () is used to group conditions and create logical expressions. As a best practice we use [[ and not test or [ unless it is a very simple condition.

### The if statement
The __if__ statement is followed by an conditional expression, as described above. Alternatively you can use a
command. If the command succeeds the _if_ is true, if it fails the _if_ is false. Here is an example:

    if grep -q word /var/log/messages ; then
        echo HIT
    fi

An example with an conditional expression:

    if [[ -z $VAR && -z $VAR1 ]] ; then
        echo "Variable1 and variable2 is empty"
    fi

test and [ use -a for && and -o for || and do not support grouping with ().

### The case statement
Beside the use of __if__ for conditional comparisons, the __case__ statement is
another option. Here is an example:

    case "$1" in
        start) do_start
               ;;
         stop) do_stop
               ;;
            *) echo "$0 start|stop"
               ;;
    esac

## COMPOUND COMMANDS
Compound commands are a group or list of several commands. 

* (...) executes the commands in a subshell, variables assignments are lost:

        $ unset g ; echo XX$g ; ( g=foo ; ) ; echo XX$g
        XX
        XX

* {...} executes the commands in the active shell, variables remain set:
        
        $ unset g ; echo XX$g ; { g=foo ; } ; echo XX$g
        XX
        XXfoo

Both forms can be used to group commands together and redirect their I/O together, for example:

    {
        echo Dear Admin
        echo
        echo please check the backup. It ran last time on
        echo
        stat -c "%y" backup-file.tar.gz
        echo
        echo Yours sincererly,
        echo $HOSTNAME
    } | mail -s "Backup Warning" root

Conditions with the __if__ statement or loops with __while__ or __for__ are compound commands. For example:

    if [[ "$HOME" == "/home/user" ]] ; then
        echo "Your home directory is $HOME"
    fi

Or the test command itself:

    $ test -f /var/log/messages && echo "file exists"

## LOOPS
### for
Two examples for using a for loop in bash scripts:

    for i in 1 2 3 4 5 ; do
        echo $i
    done

Or a bit more complex:

    for (( i=1; i \<= 5; i\+\+ )) ; do
        echo $i
    done

### while
Executes the commands inside the loop, until the condition is false:

    i=1
    while ((i <= 5)) ; do
	    echo $i
        ((i++))
    done

### until
Execute the commands inside the loop, until the condition is true:

    i=1
    until ((i > 5)) ; do
        echo $i
        ((i++))
    done

## ARITHMETIC EVALUATION
### Arithmetic Expansion
You can create an arithmetic expression with __((__expression__))__ or with __let__:

* The expression follows the rules of ARITHMETIC EVALUATION
* Bash can only work with integer values. For floating evaluations use __bc(1)__

        $ echo "2.5 + 7.5 " |bc -l
        10.0

* Is the expression wrong, you get an error message and no expansion takes place

        $ echo $((1 / 1))
        1
        $ echo $((1 / 0))
        bash: 1 / 0: division by 0 (error token is "0")

* Use __((__...__))__ around a statement to enable arithmetic evaluation:

        (( b=2 ))
        if (( b>1 )) ; then
            echo b is large
        fi

* Use __$((__...__))__ for arithmetic expansion, e.g. inline calculations:

        $ backup_time=54263
        $ printf "Backup took %d:%02d:%02d\n" $((backup_time/3600)) $(((backup_time%3600)/60)) $((backup_time%60))
        Backup took 15:04:23

* __let__ can be also used, but then the arguments must be quoted.
* Beware of the exit value of an arithmetic expression: If it evaluates to 0 then the exit code is 1. Otherwise it is 0. The reason for that behaviour is that that way an arithmetic expression like (( 1=1 )) has an exit code of 0 which means "true".

### Operators
It is possible to do various mathematical operations. But floating point operations are not supported directly (use other languages like lua, perl, ... for that):

* __id++__, __id--__: POST (assign first and then increment) increment and decrement

        y=1
        z=$((y++))
        
        Result: y=2 and z=1

* __++id__, __--id__: PRE (increment first and then assign) increment und -decrement

        y=1
        z=$((++y))
        
        Result: y=2 and z=2

* __-__, __+__: Addition and substraction
* __\*__, __/__, __%__, __\*\*__ : Multiplication, division, modulo, exponentiation
* ...

## FUNCTIONS
### General
Outsource parts of your script in functions, if you want to reuse the functionality. Function looks like the following rules:

* __[ function ] name [()] { commands ... }__
* You must use either __function__ or __()__ to denote a function
* The function body __{...}__ is a list of commands or block
* The function body must not be empty
* Functions return an exit code which is determined by the exit code of the last command
* Use __return__ to explicitly set the exit code and return from the function
* To return strings, work with stdout or use global variables

### Function arguments
When a function is called the __positional parameters__ contain the function arguments locally (__$0__ keeps its value):

	function t_func {
		echo "\$0 : $0"
		echo "\$1 : $1"
	}
	t_func foo

	Result: $0 : script.sh
			$1 : foo

### Local variables
Sometimes you need to reduce the visibility of variables to the specific function:

* Define local variables with __local__ (SHELL BUILTIN COMMAND)
* The visibility scope is for the function itself and their called functions
* If you try to use __local__ outside a function, you get an error message
* As possible options you can use the options from __declare__

## HERE DOCUMENTS
### General
It is possible to redirect STDIN to a string, which is quoted at the actual position (here)  of the script:

    <<[-]delimiter
        here-document
    delimiter

You can use tabulators (not whitespaces) in front of the delimiter (to keep your intention e.g. in functions) if you use __-__ after __<<__. You cannot use expansions in the delimiter, but in the here document you can use expansion. Here is an more explanatory example:

        cat <<- HERE
		    foo
		    $HOME
		    baz
            $(( RANDOM * 100 ))
		HERE

### Here strings
Another variant of an here document is an so called here string (__<<<word__). word will be expanded and used as STDIN. An example:

    if grep -q "txt" <<< "$VAR" ; then
	    echo "$VAR contains the substring sequence \"txt\""
    fi

Here strings are very useful to avoid useless use of cat or echo.

## PROCESS SUBSTITUTION
Another form of redirects is the process substitution:

* __>(list)__: Data is piped as input to command list
* __<(list)__: Data is read from the output of the command list

Note that the expression is replaced by a temporary FIFO file, you still need to add < or > to actually redirect the I/O from or to the subprocess:

    lines=0
	while read LINE ; do
        echo $LINE
        (( lines++ ))
    done < <(ls /tmp | grep foo )
    echo $lines

If written as ls /tmp | grep foo | while read LINE ; do ... then the incremented version variable lines would not be visible outside the while loop due to variable scoping.

## SHELL BUILTIN COMMANDS
### set & shopt
With shell options you can change the behaviour of the bash. Use __set__ or __shopt__ for this.

* __set__ only accesses a part of the available options
* __shopt__ uses all options
* __set -o__ or __shopt -o__ shows all options which could be used by __set__
* __shopt__ shows the status of the extended shell options

Below a list with option examples (first for __set__, second for __shopt__):

* __-a__, __-o allexport__: Exports all variable defined after the command
* __-b__, __-o notify__: Displays the ending of jobs immediately and don't wait for the next prompt
* __-C__, __-o noclobber__: Not allow > redirections to files
* __-e__, __-o errexit__: Exit immediately if an error occured
* __-f__, __-o noglob__: Deactivate wildcard expansion
* __-o nullglob__ (Only with shopt): If set, bash allows patterns which match no files to expand to a null string, rather than themselves

See _bash(1)_ under __SHELL BUILTIN COMMANDS__ and search then for __shopt__ for a complete list.

## SIGNALS
Signals are important for inter-process communication. You can send signals to running programs with __kill__. With __trap__ it is possible to control the behaviour of a shell script when it receives a signal (see _signal(7)_ for more informations). Only SIGKILL and SIGSTOP cannot be caught. Here is an example for catching Ctrl+C:

	trap "echo -e '\nI have received the SIGINT signal\n' ; exit 0" SIGINT
	while true ; do 
		echo -n .
		sleep 2
	done

Instead of giving a command list, a function name is also possible (__trap function_name SIGNAL__). Use __trap__ for cleanup routines by catching the exit signal __EXIT__:

	trap exitfunc EXIT

## CODING GUIDELINE
To ensure readable and maintainable scripts it is useful to follow some general rules. This section show some collected issues you should consider:

* Indentation should be done with 4 whitespaces. Use Tabs for HERE documents.
* Use __trap__ with __EXIT__ to install an exit handler to cleanup temporary files etc. regardless of why the scripts exits.

