# mathQuestions
Generate math questions from templates

served on heroku

https://reviewquestions.herokuapp.com/questions/7/15

Using the URLconf defined in mathQuestions.urls, Django tried these URL patterns, in this order:

```
questions/ <int:year>/ [name='qa_stats']
questions/ <int:year>/<int:nof_questions> [name='qa_questions_answers']
questions/ <int:year>/<int:nof_questions>/<int:start_from> [name='qa_index_start_from']
questions/ <int:year>/<int:nof_questions>/<int:start>/<int:end> [name='qa_index_start_end']
questions/ <int:year>/type [name='qa_stats_by_type']
questions/ <int:year>/complexity [name='qa_stats_by_complexity']
questions/ <int:year>/type/<str:qtype>/<int:nof_questions> [name='qa_by_type']
questions/ <int:year>/complexity/<str:complexity>/<int:nof_questions> [name='qa_by_complexity']
questions/ <int:year>/<str:qtype>/<str:complexity>/<int:nof_questions> [name='qa_by_type_complexity']
admin/
```
