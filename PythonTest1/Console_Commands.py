import os, sys

class Console(object):
    """Comandos de consola porque python /shrugh"""
    
    def clear():
        if os.name in ("nt", "dos"):
            os.system('cls')
        else:
            os.system('clear')

    def progressBar(total, progress, prefix="\t", suffix=""):
        percent = ("{0:.1f}").format(100*(progress/float(total)))
        filledLength = int(50 * progress//total)
        bar = '█' * filledLength + ' ' * (50-filledLength)
        print(f"\r{prefix} |{bar}| {percent}% {suffix}", end="")

        if progress == total:
            print()
    
    global g_start, g_end, g_count
    g_start = g_end = g_anchor = g_end = g_count = 0
    def ETA(start, end, total, progress, reset=False):
        global g_start, g_end, g_count, g_anchor
        if reset:
            g_start = 0
            g_end = 0
            g_count = 0
            g_anchor = start
            return None
            
        g_start += start
        g_end += end
        g_count += 1.1
        total = total-total*(progress/total)
        
        
        
        h, m, s=(0,0,(((g_end-g_start)/g_count)*total))
        
        if s > 60:  
            m = s//60
            s = s%60
        if m > 60:
            h = m//60
            m = m%60
        
        if h < 1:
            h = ""
        else:
            h = str(int(h))+"h "
        if m < 1:
            m = ""
        else:
            m = str(int(m))+"m "
        
        s = str(int(s))+"s"
        return "ETA "+h+m+s

