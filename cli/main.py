from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint


questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'You first name ma Brotha'
    }
]
answers = prompt(questions)
pprint(answers)

