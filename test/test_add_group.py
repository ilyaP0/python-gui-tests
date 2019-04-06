from generator import gengroups

def test_add_group(app):
    old_list = app.groups.get_group_list()
    item = app.gengroups.read_excel()
    app.groups.add_new_group(item)
    new_list = app.groups.get_group_list()
    old_list.append(item)
    assert  sorted(old_list) == sorted(new_list)