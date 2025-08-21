# A Passing Test
# The test function will call the function we're testing, and we'll make an assertion
# about the value that's returned. If our assertion is correct, the test will pass;
# if the assertion is incorrect the test will fail

from name_function import get_formatted_name

def test_first_last_name():
    """Do names like Janis Joplin work?"""
    formatted_name = get_formatted_name("Janis", "Joplin")
    assert formatted_name == "Janis Joplin"
    
def test_first_last_middle_name():
    """Do names like Janis Mary Joplin work?"""
    formatted_name = get_formatted_name("Janis", "Joplin", "Mary")
    assert formatted_name == "Janis Mary Joplin"