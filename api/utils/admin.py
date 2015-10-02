class WYSIWYG(object):
    """
    A mixin that adds the scripts necessary for TinyMCE admin integration.
    """

    class Media:
        js = [
            "/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js",
            "/static/grappelli/tinymce_setup/tinymce_setup.js"]
