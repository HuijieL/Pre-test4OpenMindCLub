#Example 1
age = raw_input("How old are you?")
height = raw_input("how height are you?")
weight = raw_input("how weight are you?")
# %r 
print "So you are %r years old, %r tall and %r weight." % \
	(age, height, weight)
# %s
print "So you are %s years old, %s tall and %s weight." % (
	age, height, weight)

# Example 2 shows the difference between %s and %r
like = '50'
hate = 46.667

print "%s %r" % (like, like)
print "%s %r" % (hate, hate)
print like
print hate
print like, hate

#Example 3 shows why we use %r than %s.
apple = raw_input("please type the first number?")
orange = raw_input("please type the second number?")
print apple + orange      #connect two strings because the output type of "raw_input" is string.
# !Attention: int() does not work.
#print int(apple) + int(orange)  #add two (int) numbers 
print float(apple) + float(orange) # add two (float) numbers
print float(apple), int(float(apple)) #int() only change the number 

