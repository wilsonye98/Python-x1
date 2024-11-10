# Please write a program to generate all sentences where subject is
# in ["I", "You"] and verb is in ["Play", "Love"] and the object is
# in ["Hockey","Football"].

subject = ["I", "You"]
verbs = ["Play", "Love"]
objs = ["Hockey","Football"]

for sub in subject:
    for verb in verbs:
        for obj in objs:
            print(f"{sub} {verb} {obj}")
