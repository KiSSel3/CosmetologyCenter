from main.models import FAQ, Review
import pytest

@pytest.fixture
def sample_faq():
    return FAQ.objects.create(
        question="What is the FAQ?",
        answer="This is a frequently asked question."
    )


@pytest.fixture
def sample_review():
    return Review.objects.create(
        text="Great product!",
        rating=9,
        author="John Doe"
    )