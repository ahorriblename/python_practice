"""
Problem:

The virus attacked the filesystem of the supercomputer and broke the control
of access rights to the files. For each file there is a known set of operations
which may be applied to it:

write W,
read R,
execute X.

The first line contains the number N — the number of files contained in the
filesystem. The following N lines contain the file names and allowed
operations with them, separated by spaces. The next line contains an integer
M — the number of operations to the files. In the last M lines specify the
operations that are requested for files. One file can be requested many times.

You need to recover the control over the access rights to the files. For each
request your program should return OK if the requested operation is valid or
Access denied if the operation is invalid.

"""

# get num of keys-value pairs to initialize
num_of_keys = int(input())
# create dictionary of access_rights
access_rights = {}
# get file name and its access rights
for i in range(num_of_keys):
    file_name, rights = input().split(" ", 1)
    # remove whitespace
    rights = rights.replace(" ", "")
    # convert access rights to array
    rights = list(rights)

    # store key and value into dictionary
    access_rights[file_name] = rights

# get num of operations
num_of_operation = int(input())

for i in range(num_of_operation):
    operation, file = input().split()

    # convert word into char to match values in access_rights
    if operation == "execute":
        operation = "X"
    elif operation == "write":
        operation = "W"
    else:
        operation = "R"

    # check if the operation is in the rights array of the given file
    if operation in access_rights[file]:
        print("OK")
    else:
        print("Access denied")
