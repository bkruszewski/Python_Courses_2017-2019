import io
from contextlib import redirect_stdout

def get_print_output(testowana_funkcja):

    bufor_pamieci = io.StringIO()

    with redirect_stdout(bufor_pamieci):

        testowana_funkcja()

        return bufor_pamieci.getvalue()
