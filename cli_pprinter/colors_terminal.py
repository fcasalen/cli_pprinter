from termcolor import cprint

class CLIPPrinter:
    def __adjust_msg__(msg:str):
        return msg + '\n'
    
    @staticmethod
    def cyan_underline(msg: str, **kwargs):
        'cyan, bold, underline, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'cyan', attrs = ['bold', 'underline', 'reverse'], **kwargs)

    @staticmethod
    def cyan(msg: str, **kwargs):
        'cyan, bold, underline, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'cyan', attrs = ['bold', 'reverse'], **kwargs)

    @staticmethod
    def green(msg: str, **kwargs):
        'green, bold, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'green', attrs = ['bold', 'reverse'], **kwargs)
    
    @staticmethod
    def green_underline(msg: str, **kwargs):
        'green, bold, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'green', attrs = ['bold', 'reverse', 'underline'], **kwargs)

    @staticmethod
    def red(msg: str, **kwargs):
        'red, bold, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'red', attrs = ['bold', 'reverse'], **kwargs)

    @staticmethod
    def red_underline(msg: str,**kwargs):
        'red, bold, underline, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'red', attrs = ['bold', 'underline', 'reverse'], **kwargs)

    @staticmethod
    def yellow(msg: str, **kwargs):
        'yellow, bold, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'yellow', attrs = ['bold', 'reverse'], **kwargs)

    @staticmethod
    def yellow_underline(msg: str, **kwargs):
        'yellow, bold, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'yellow', attrs = ['bold', 'reverse', 'underline'], **kwargs)

    @staticmethod
    def white(msg: str, **kwargs):
        'white, bold, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'white', attrs = ['bold', 'reverse'], **kwargs)
    
    @staticmethod
    def white_underline(msg: str, **kwargs):
        'white, bold, reverse'
        cprint(text = CLIPPrinter.__adjust_msg__(msg), color = 'white', attrs = ['bold', 'reverse',' underline'], **kwargs)