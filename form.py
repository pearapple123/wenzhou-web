


class SearchForm(FlaskForm):
    term = StringField('Search for:', validators=[DataRequired()])
    submit = SubmitField('Search')