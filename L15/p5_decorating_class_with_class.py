# DON'T DO THIS

class Tracer:

    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args, **kwargs):
        self.wrapped = self.aClass(*args, **kwargs)
        return self

    def __getattr__(self, item):
        print(f"Trace: {item}")
        return getattr(self.wrapped, item)


@Tracer
class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

# Person = Tracer(Person)

john = Person("John")
john.print_name()

print()

anna = Person("Anna")  # here method __call__ is called and field self.wrapped is re-assinged to Anna. John will be lost
anna.print_name()

john.print_name()
