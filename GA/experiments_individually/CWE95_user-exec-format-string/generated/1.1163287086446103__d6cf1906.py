def code_execution(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        #BAD -- Allow user to define code to be run.
        ex = "ex"
        ex += "ec"
        def get_cmd():
            return "setname('{}')".format(first_name)
        eval('{}({})'.format(ex, repr(get_cmd())))