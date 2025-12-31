from about.models import About

def run():
    About.objects.create(
        title='About Me',
        content='This is the about page content.',
        profile_image='images/nobody.jpg'
    )
    print('About object created.')
