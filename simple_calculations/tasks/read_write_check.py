"""
This program tests itself. Function gets the textfile name as input (file is in the same folder),
writes down most mentioned symbol and number of uses in the file with same name+'_1'+extension and returns same values
as tuple

    Most mentioned symbol (mms):

    :arg file_name

    :returns tuple(char, int) -- MMS and number of uses
>>> mms("text1.txt")
(' ', 260)
>>> mms("text2.txt")
(' ', 136)
>>> mms("text3.txt")
('e', 6)
"""


def mms(file_name: str) -> tuple[str, int]:
    char_dict = {}
    mx = None
    with open(file_name, 'r', encoding='utf-8') as inf:
        text = inf.readline()
        while text:
            for char in text:
                if char in char_dict:
                    char_dict[char] += 1
                    if char_dict[char] > mx[1]:
                        mx = (char, char_dict[char])
                else:
                    char_dict[char] = 1
                    if mx is None:
                        mx = (char, char_dict[char])
            text = inf.readline()
    (name, extension) = file_name.split(".")
    with open(name+"_1."+extension, 'w') as outf:
        outf.write(str(mx))
    return mx


if __name__ == "__main__":
    print(mms("text1.txt"))
