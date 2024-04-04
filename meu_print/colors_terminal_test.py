from .colors_terminal import CLIPPrinter

def test_all():
    assert CLIPPrinter.__adjust_msg__('ha')
    assert not CLIPPrinter.red('ha', end = '')