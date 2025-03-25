from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from user_sessions.models import Senhas
import platform
import win32print

def print_to_printer(content):
    with open("senha.txt", "w", encoding="utf-8") as f:
            f.write(content)
    """if platform.system() == "Windows":
        hprinter = win32print.OpenPrinter(win32print.GetDefaultPrinter())
        try:
            #começa  o documento
            print(content)
            win32print.StartDocPrinter(hprinter, 1, ("Senha", None, "RAW"))
            #inicia uma página
            win32print.StartPagePrinter(hprinter)
            #escreve na página o conteudo neste caso a ultima senha (que depois vai ser a senha que quisermos???)
            win32print.WritePrinter(hprinter, content.encode("utf-8"))
            win32print.EndPagePrinter(hprinter)
            #termina o documento
            win32print.EndDocPrinter(hprinter)
        finally:
            #então começa o print
            win32print.ClosePrinter(hprinter) 

        #se não for windows usa pycups
    elif platform.system() in ["Linux", "Darwin"]:  # macOS é "Darwin"
        import subprocess
        #tem de criar um ficheiro e vai começar a ocupar espaço por isso adicionar algo para eliminar os ficheiros
        #no produto final deviamos só usar linux duvido que os quiosques de imprimir senhas estejam a rodar qualquer versão de windows
        
        with open("debug_print_content.txt", "w", encoding="utf-8") as f:
            f.write(content)
    else:
        raise Exception("Unsupported Operating System for printing")"""

@login_required
def print_senha(request):
    # Ir buscar a senha
    latest_senha = Senhas.objects.filter(user=request.user).order_by('-created_at').first()

    if not latest_senha:
        
        print("[DEBUG] No codes found for user:", request.user.username)
        return redirect('senhas_page')

    # Mandar imprimir a ultima senha
    try:
        print_to_printer(latest_senha.number)
        print(f"[DEBUG] Printed code: {latest_senha.number}")
    except Exception as e:
        print(f"[DEBUG] Printing failed: {e}")
        #falhou volta para a página das senhas
        return redirect('senhas_page')

    # volta para a página das senhas
    return redirect('senhas_page')
