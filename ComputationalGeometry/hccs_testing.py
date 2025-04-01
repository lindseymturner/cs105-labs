# Infrastructure for knowing of we are testing or not.
# Sometimes we want to print out extra debugging info if we are
#  doing a graphics test

are_we_doing_a_graphics_test = False   # dynamically set this to true when doing a graphics test

def doing_a_graphics_test():
    return are_we_doing_a_graphics_test

def starting_a_graphics_test():
    global are_we_doing_a_graphics_test
    are_we_doing_a_graphics_test = True
    
def finished_a_graphics_test():
    global are_we_doing_a_graphics_test
    are_we_doing_a_graphics_test = False