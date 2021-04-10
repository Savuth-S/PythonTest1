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
    
    def ETA(start = 0, end = 0, show = False, total = 0, progress = 0, reset = False):
        global e_time, g_start, gs_start
        if reset:
            e_time = 0
            gs_start = start
            return None
        
        if start > 0:
            g_start = start
        
        if end > 0:
            e_time += (end-start)
            e_time *= ((end-gs_start)/e_time)
        
        if show and progress != 0:
            h = m = 0
            s = (e_time*(total/progress))-e_time
            #print(e_time)
            #print(e_time * (total/progress))
            #print(total/progress)
            #print( e_time - (e_time * (total/progress) ) )
            
            m = s//60
            s = s%60
            h = m//60
            m = m%60
            return "ETA "+str(int(h))+"h "+str(int(m))+"m "+str(int(s))+"s"
        return None