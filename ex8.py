formatter = "%r %s %s %s"

print formatter % (1,2,3,4)
print formatter % ("하나", "둘", "셋", "넷")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
          "I had this thing.",
		  "That you could type up right.",
		  "But it didn't sing.",
		  "So I said goodnight."
)
