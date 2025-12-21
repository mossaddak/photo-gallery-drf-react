def get_media_path_prefix(instance, filename):
    class_name = instance.__class__.__name__
    if class_name.endswith("Connector"):
        class_name = class_name[:-9]
    return f"{class_name.lower()}/{filename}"
