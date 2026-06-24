try:
	import pyjokes
	def _get_joke(): # type: ignore
		return pyjokes.get_joke()
except Exception:
	# Fallback when pyjokes is not installed or cannot be resolved
	def _get_joke():
		return "Why did the programmer quit? Because he didn't get arrays."

joke = _get_joke()
print(joke)
print("Hello World")

# there are 2 types of modules built in modules and external modules
# python supports REPEL i mean calculations ho sakti daba kr 3sre pe esa act krta hai jese calculator