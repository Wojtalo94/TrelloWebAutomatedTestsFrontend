import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("login")
class TestCreateTable:
    def test_create_table_verification(self):
        assert "Trello" in self.driver.title