'''Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.'''



def change(s):
	r1 = [s[0].lower()]
    r2= [s[0].lower()]
	for c in s[1:]:
		if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
			r1.append('_')
            r2.append('-')
			r1.append(c.lower())
            r2.append(c.lower())
        else:
			r1.append(c)
            r2.append(c)

	snake=''.join(r1)
    kebab=''.join(r2)
    return([snake,kebab])

str = "MyNameIsDipesh"
print(change(str))
