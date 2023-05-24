#def my_function(something):
    #Do This
    #Then do this
    #Finally do this

#def functions_with_outputs():
#    result = 3*2
#    return result

#output = functions_with_outputs()

#print(output)

# Functions with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("ChRisTopHer", "MCKLVEEN")
print(formated_string)


