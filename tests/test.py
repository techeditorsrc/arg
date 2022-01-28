from arg import arg

args=arg()

print(args.read_arg({
    "case-sensitive":True,
    "args":"-x -X"
}))

print(args.read_arg())