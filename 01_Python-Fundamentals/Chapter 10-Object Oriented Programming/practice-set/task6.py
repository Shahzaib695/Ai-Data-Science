# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
# yes any name is compatible excluding self too
class Test:
    def show(self):
        print(self)
t1 = Test()
t1.show()