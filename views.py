from flask_admin.contrib.sqla import ModelView


class ColumnPropertiesView(ModelView):
    column_list = ['name', 'proper_name', 'comment']
    column_sortable_list = column_list


class TestView(ModelView):
    column_display_pk = True

    def __init__(self, model, session, **kwargs):
        from models import ColumnProperty

        cl = {}

        for row in session.query(ColumnProperty):
            cl[row.name] = row.proper_name

        self.column_labels = cl

        super(TestView, self).__init__(model, session, **kwargs)

