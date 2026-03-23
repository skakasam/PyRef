"""Python Booleans Practice Module"""

###############################################################################
# Booleans represent thruth values. The bool type has exactly two constant
# instances: True or False.
# Note that bool is a subclass of int, and False and True behave like integers
# 0 and 1 in many numeric contexts. However, relying on this is discouraged!
###############################################################################

read_perms, write_perms, execute_perms = "Y", "Y", "N"
readable, writeable, executable = (
    read_perms.upper() == "Y",
    write_perms.upper() == "Y",
    execute_perms.upper() == "Y",
)

print(f"type(readable) = {type(readable)}")
print(f"type(writeable) = {type(writeable)}")
print(f"type(executable) = {type(executable)}")

print(f"readable = {readable}")
print(f"writeable = {writeable}")
print(f"executable = {executable}")

# Treating bool as int is discouraged, use int() instead
# final_perms = (readable * 2**2) + (writeable * 2**1) + (executable * 2**0)
final_perms = (int(readable) * 2**2) + (int(writeable) * 2**1) + (int(executable) * 2**0)
print(f"type(final_perms) = {type(final_perms)}")
print(f"final_perms = {final_perms}")
