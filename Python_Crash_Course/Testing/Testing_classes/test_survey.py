import pytest
from survey import AnonymousSurvey


# def test_store_single_response():
#     """Test that a single response is stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response("English")
#     assert "English" in language_survey.responses
    
# def test_store_three_responses():
#     """Test that three responses are stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     responses = ["English", "Mandarin", "German"]
    
#     for response in responses:
#         language_survey.store_response(response)
    
#     assert response in language_survey.responses

@pytest
def language_survey():
    """A survey that will be available to all functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response():
    """Test that a single response is stored properly."""
    language_survey.store_response("English")
    assert "English" in language_survey.responses
    
def test_store_three_responses():
    """Test that three responses are stored properly."""
    responses = ["English", "Mandarin", "German"]
    
    for response in responses:
        language_survey.store_response(response)
    
    assert response in language_survey.responses