from termcolor import cprint

attrs_br = ["bold", "reverse"]
attrs_bru = ["bold", "reverse", "underline"]


class CLIPPrinter:
    def __adjust_msg__(msg: str):
        return msg + "\n"

    @staticmethod
    def cyan_underline(msg: str, **kwargs):
        "cyan, bold, underline, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg),
            color="cyan",
            attrs=attrs_bru,
            **kwargs,
        )

    @staticmethod
    def cyan(msg: str, **kwargs):
        "cyan, bold, underline, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg), color="cyan", attrs=attrs_br, **kwargs
        )

    @staticmethod
    def green(msg: str, **kwargs):
        "green, bold, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg),
            color="green",
            attrs=attrs_br,
            **kwargs,
        )

    @staticmethod
    def green_underline(msg: str, **kwargs):
        "green, bold, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg),
            color="green",
            attrs=attrs_bru,
            **kwargs,
        )

    @staticmethod
    def red(msg: str, **kwargs):
        "red, bold, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg), color="red", attrs=attrs_br, **kwargs
        )

    @staticmethod
    def red_underline(msg: str, **kwargs):
        "red, bold, underline, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg), color="red", attrs=attrs_bru, **kwargs
        )

    @staticmethod
    def yellow(msg: str, **kwargs):
        "yellow, bold, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg),
            color="yellow",
            attrs=attrs_br,
            **kwargs,
        )

    @staticmethod
    def yellow_underline(msg: str, **kwargs):
        "yellow, bold, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg),
            color="yellow",
            attrs=attrs_bru,
            **kwargs,
        )

    @staticmethod
    def white(msg: str, **kwargs):
        "white, bold, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg),
            color="white",
            attrs=attrs_br,
            **kwargs,
        )

    @staticmethod
    def white_underline(msg: str, **kwargs):
        "white, bold, reverse"
        cprint(
            text=CLIPPrinter.__adjust_msg__(msg),
            color="white",
            attrs=attrs_bru,
            **kwargs,
        )

    @staticmethod
    def line_breaker(breaker: str = "*", breaker_count: int = 100):
        cprint(text=breaker * breaker_count + "\n", color="white", attrs=attrs_bru)
