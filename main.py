from UsefulDecorator import NotNone

@NotNone
def test(test, **kwargs):
    print(kwargs)

test() #raise Exception