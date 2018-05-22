from flask_admin.contrib.sqla import ModelView


class ColumnPropertiesView(ModelView):
    """
    Shows table metadata gleaned from a view that's based on the MySQL
    information_schema.TABLES table, scoped to just tables that exist in
    the current database.
    """
    column_list = ['parent_table', 'name', 'proper_name', 'comment']
    column_sortable_list = column_list


class TestView(ModelView):
    column_display_pk = True
    list_template = 'admin/model/list_header_tooltips.html'

    def __init__(self, model, session, **kwargs):
        from models import ColumnProperty as cp

        clabels = {}
        cdescriptions = {}
        q = session.query(cp).filter(cp.parent_table==model.__tablename__)

        for row in q.all():
            clabels[row.name] = row.proper_name
            cdescriptions[row.name] = row.comment

        self.column_labels = clabels
        self.column_descriptions = cdescriptions

        super(TestView, self).__init__(model, session, **kwargs)
