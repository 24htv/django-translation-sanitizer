Django Translation Sanitizer
============================

**Django Translation Sanitizer** is a simple Django app to sanitize the output of `makemessages`
 command by disabling fuzzy matching and sorting it's output.

Rationale
---------
When one first create the `*.po` files with the original `makemessages` command everything seems
nice -- Django makes clean file that one can easily edit via text editor. 

The actual "mess" comes after command has been running several times -- 
when Django tries to match previous translations of a changed original it often fails to do it correctly. 
 
The thing is that it fails *silently*. It takes enormous amounts of time to find and 
fix the translation issues django had made.

So instead of changing the previous translations this module simply adds the new ones, 
leaving everything else untouched.


How to use it
-------------

1. Install the package from [https://pypi.org/project/django-tranlation-sanitizer/][PyPI] like this:
    ```bash
    pip install django-translation-sanitizer
    ```

2. Add "translation_sanitizer" to your INSTALLED_APPS setting like this
    ```python
    INSTALLED_APPS = [
            ...
            'translation_sanitizer',
        ]
    ```
3. That's it! Now `makemessages` command will produce clean, sorted and fuzzy-free output.


[PyPI]: https://pypi.org/project/django-tranlation-sanitizer/PyPI
