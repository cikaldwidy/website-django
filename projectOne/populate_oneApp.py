import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectOne.settings')  # Make sure this path is correct

import django
django.setup()

# Import required modules and models
import random
from oneApp.models import Topic, Webpage, AccesRecord
from faker import Faker

fakegen = Faker()
topics = ["Social", "Search", "Marketplace", "News", "Games"]

def add_topic():
    # Create or get a topic
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    # Populate N entries
    for entry in range(N):
        # Get or create a topic
        top = add_topic()
        
        # Generate fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # Create a new Webpage entry (avoid using 'Webpage' as a variable name)
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        
        # Optionally, create an AccessRecord entry if needed
        acc_rec = AccesRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

# Call the populate function to add data
if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Populating complete")
    
