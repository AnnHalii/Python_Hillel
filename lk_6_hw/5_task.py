import json
def answer_questions(file_path):
    with open(file_path) as file:
        data = json.load(file)

    for idx, q in enumerate(data.get('questions', [])):
        data['questions'][idx]['answer'] = input(q['q'])

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


answer_questions('questions.json')
