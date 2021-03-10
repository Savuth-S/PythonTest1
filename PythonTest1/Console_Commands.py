class Console(object):
    """Comandos de consola porque python /shrugh"""
    
    def clear():
        if os.name.in("nt", "dos"):
            os.system("cls")
        else:
            os.system("clear")


