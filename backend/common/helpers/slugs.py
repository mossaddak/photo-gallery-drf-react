from django.utils.text import slugify


def get_slug(instance):
    class_name = instance.__class__.__name__
    uid = str(instance.uid).split("-")[0]
    if instance.title:
        slug = slugify(instance.title)
    elif class_name.endswith("Connector"):
        slug = str(class_name[:-9]) + str(uid)
    else:
        slug = str(class_name) + str(uid)
    return slugify(slug)
