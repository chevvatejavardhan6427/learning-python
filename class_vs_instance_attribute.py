class cars:
	a=1         # class attribute
	@classmethod
	def show(cls):
		print(f"The class attribute of a={cls.a}")
l=cars()
l.a=7          # instance attibute
l.show()
