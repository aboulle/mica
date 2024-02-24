import cmd

class MyShell(cmd.Cmd):
    prompt = "[prompt] >>> "
    
    def __init__(self,function,object):                                                                       
            super().__init__()
            self.history = []
            self.function = function
            self.object = object

    def default(self, args):
        self.function(args, self.object)
        self.history.append(args)
   
    def do_history(self, args):
        for command in self.history:
            print(command) 
    
    def do_exit(self, line):
        return True
    
    def do_EOF(self, line):                    
        return True
    
    def do_help(self, args):
        print("===========================================")
        print("Available commands:")
        print("===========================================")
        print("  enter - passes the prompt through the LLM")                                                                                                                                                      
        print("  history - show the history of commands")
        print("  exit - exit the shell")                                                                                                                                                     
        print("  ctrl+d - exit the shell")
        print("  help - show this help message")
        print("===========================================")

    do_hist = do_history
