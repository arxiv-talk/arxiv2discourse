
# Discourse API
API_KEY = 'e3d20e29465a164c40b065d37ba1a24d920ae59303ab67ae48e479fe6b116019'

from pydiscourse import DiscourseClient
client = DiscourseClient(
        'https://arxiv-talk-test.discourse.group/',
        api_username='arxivbot',
        api_key=API_KEY)

categories = [
    'Computer Science',
    'Economics',
    'Electrical Engineering and Systems Science',
    'Mathematics',
    'Physics',
    'Quantitative Biology',
    'Quantitative Finance',
    'Statistics'
]

physics_subcategories = [
    'Astrophysics',
    'Condensed Matter',
    'General Relativity and Quantum Cosmology',
    'High Energy Physics - Experiment',
    'High Energy Physics - Lattice',
    'High Energy Physics - Phenomenology',
    'High Energy Physics - Theory',
    'Mathematical Physics',
    'Nonlinear Sciences',
    'Nuclear Experiment',
    'Nuclear Theory',
    'Physics',
    'Quantum Physics'
]

for category in categories:
    try: 
        client.create_category(name = category, color = None)
    except Exception as e:
        print(e)
    
for subcategory in physics_subcategories:
    try:
        client.create_category(name = subcategory, parent = 'Physics', color = None)
    except Exception as e:
        print(e)