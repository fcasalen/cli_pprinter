from src.cli_pprinter.colors_terminal import CLIPPrinter
import io
import sys


def test_all():
    assert CLIPPrinter.__adjust_msg__("ha") == "ha\n"
    for func in [
        CLIPPrinter.red,
        CLIPPrinter.red_underline,
        CLIPPrinter.green,
        CLIPPrinter.green_underline,
        CLIPPrinter.yellow,
        CLIPPrinter.yellow_underline,
        CLIPPrinter.cyan,
        CLIPPrinter.cyan_underline,
        CLIPPrinter.white,
        CLIPPrinter.white_underline,
    ]:
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func("ha", end="")
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue() == "ha\n"
    captured_output = io.StringIO()
    sys.stdout = captured_output
    CLIPPrinter.line_breaker()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "*" * 100 + "\n\n"
