import re
from model.group import Group

def test_add_group(app):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(Group(name="фывфвыв"))
    new_list = app.groups.get_group_list()
    new_list.append(Group(name="фывфвыв"))
    assert len(old_list) + 2 == len(new_list)



def clear(s):
    return re.sub(r"^\s+|\s+$+:", "", s)