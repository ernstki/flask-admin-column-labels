from flask_admin.contrib.sqla import ModelView


class ColumnPropertiesView(ModelView):
    column_list = ['name', 'proper_name', 'comment']
    column_sortable_list = column_list


class TestView(ModelView):
    column_display_pk = True
    column_list = ['id', 'name', 'description']
    column_sortable_list = column_list