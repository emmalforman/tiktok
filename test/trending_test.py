import os
import pytest
from TikTokApi import TikTokApi

from app.trending import get_trending

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_trending():
    output = get_trending()
    assert(len(output)==10)
