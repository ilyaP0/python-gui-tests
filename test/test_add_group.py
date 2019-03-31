def test_add_group(app):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(name="dsaddasad")
    new_list = app.groups.add_new_group(name="dsaddasad")
    new_list.append(name="dsaddasad")
    assert sorted(old_list) == sorted(new_list)