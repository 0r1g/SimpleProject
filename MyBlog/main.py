import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyBlog.settings")
django.setup()

from blog.models import Post

v1 = Post.objects.create(
    title='Title',
    content='Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты.'
)
v1.save()
