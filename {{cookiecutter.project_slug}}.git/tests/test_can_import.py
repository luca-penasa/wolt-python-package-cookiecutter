def test_import_package():
    """Verify we can import the main package"""
    import {{ cookiecutter.package_name }}

def test_has_version():
    """Check that the package has an accesible __version__"""
    import {{ cookiecutter.package_name }}
    version = {{ cookiecutter.package_name }}.__version__