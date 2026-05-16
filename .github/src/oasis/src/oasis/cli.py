from oasis.cli import main def test_main(capsys): main() captured = capsys.readouterr() assert "OASIS is running." in captured
