# Strings
When using the "print" built-in function we have 3 arguments which we can be: the string, a separator and end, let's take a look down there
Obs: a separator will allow us to choose a character to split strings passed for the function, and the end will define what have at the end of each strings
By default, the separator is " "(a space) and the end its a "\n"(new line char)
```py
print("weslley","pablo","pietro",sep="-",end="END")
#Expected output: weslley-pablo-pietroEND
```
### Escape char
we can use "\" to spit out a char from a string

### Built-in functions for strings

- str_var.lower(): will return the whole string formatted as lower case
- str_var.upper(): will return the whole string formatted as upper case
- str_var.islower(): will return a True statement if the string as formatted as lower case and false if isnt
- str_var.isupper(): will return a True statemente if the string as formatted as upper case and false if isnt
- len(str_var): will return the lenght of the string(each character, spaces and special chars does count)i
- str_var.index(""): you can pass a char and he will return the index of this char if he does exist on the string
- str_var.replace("what_we_want_to_replace", "what_will_replace") 

### Strings as an Array
We can see a string as an Array which means every char have an Index, so if the word "Hello" its stored on a var, we can do something like:
```py
hello = "hello"
print(hello[4])
#Will return "o", because Arrays starts from zero
```
