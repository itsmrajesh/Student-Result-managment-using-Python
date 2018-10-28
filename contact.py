#contact
from collections import namedtuple

Contact = namedtuple("Contact", ["name","usn", "sem", "dept","numb"])
result = namedtuple("result",["name","usn","subc","subn","marks","res"])
res=namedtuple("res",["usn","name","cgpa"])
update=namedtuple("update",["name","sem","dept","numb","usn"])
