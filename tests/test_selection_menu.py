from src.cli import selection_menu


class TestSelectionMenu:

    """Tests for selection menu funcs."""

    def test_title(self):
        title = "Test Title"
        obj = selection_menu.SelectionMenu(title)
        assert obj._title == title.center(30, "~")
