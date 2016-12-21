formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % 
    ("I had this thing.",
    "That you could type up right.",
	"But is didn't sing.",
    "So I said goodnight."
    )
    )

#我把最后一个print中的formatter& 删掉，运行，发现输出的内容不一样，明白了formatter是用来定义格式的，可以将后main的四句话以formatter中的格式输出。