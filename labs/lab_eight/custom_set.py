"""

Hello World

Rules:
* cant use built in set
* cant use built in dictionary
"""

class CustomSet(set):
    """ Doc string for CustomSet Class"""

    def __init__(self, *args):
        super(CustomSet, self).__init__(*args)
        pass