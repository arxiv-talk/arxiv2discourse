

# Discourse API
API_KEY = 'e3d20e29465a164c40b065d37ba1a24d920ae59303ab67ae48e479fe6b116019'

from pydiscourse import DiscourseClient
client = DiscourseClient(
        'https://arxiv-talk-test.discourse.group/',
        api_username='arxivbot',
        api_key=API_KEY)

import seaborn as sns

palette = sns.color_palette("Spectral", 20).as_hex()
colors = [color.removeprefix('#') for color in palette]

categories = [
    {'name': 'A - Computer Science', 'color': colors[0]},
    {'name': 'A - Economics', 'color': colors[1]},
    {'name': 'A - Electrical Engineering and Systems Science','color': colors[2]},
    {'name': 'A - Mathematics','color': colors[3]},
    {'name': 'A - Astrophysics','color': colors[4]},
    {'name': 'A - Condensed Matter','color': colors[5]},
    {'name': 'A - General Relativity and Quantum Cosmology', 'color': colors[6]},
    {'name': 'A - High Energy Physics - Experiment', 'color': colors[7]},
    {'name': 'A - High Energy Physics - Lattice', 'color': colors[8]},
    {'name': 'A - High Energy Physics - Phenomenology', 'color': colors[9]},
    {'name': 'A - High Energy Physics - Theory', 'color': colors[10]},
    {'name': 'A - Mathematical Physics', 'color': colors[11]},
    {'name': 'A - Nonlinear Sciences', 'color': colors[12]},
    {'name': 'A - Nuclear Experiment', 'color': colors[13]},
    {'name': 'A - Nuclear Theory', 'color': colors[14]},
    {'name': 'A - Physics', 'color': colors[15]},
    {'name': 'A - Quantum Physics', 'color': colors[16]},
    {'name': 'A - Quantitative Biology', 'color': colors[17]},
    {'name': 'A - Quantitative Finance', 'color': colors[18]},
    {'name': 'A - Statistics', 'color': colors[19]}
]

symbols = ['cs', 'econ', 'eess', 'math', 'astro-ph', 'cond-mat', 'gr-qc', 'hep-ex', 'hep-lat', 'hep-ph', 'hep-th', 'math-ph', 'nlin', 'nucl-ex', 'nucl-th', 'physics', 'quant-ph', 'q-bio', 'q-fin', 'stat']

categories_dict = dict(zip(symbols, categories))

client.create_category(name = 'Preprints', color = None)

for category in categories_dict.values():
    try: 
        client.create_category(name = category['name'], color = category['color'], parent = 'Preprints')
    except Exception as e:
        print(e)
    