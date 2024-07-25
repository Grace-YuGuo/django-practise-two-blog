from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test the comment form in blog app
    """

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'The blog content is A'})
        self.assertTrue(comment_form.is_valid(), msg='Blog form is not valid')

#     def test_form_is_invalid(self):
#         comment_form = CommentForm({'body': ''})
#         self.assertFalse(comment_form.is_valid(), msg='Form is valid')