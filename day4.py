import re


def main():
    file = open("day4.txt", "r")
    text = file.read()

    documents = text.split("\n\n")
    documents = [doc.replace("\n", " ") for doc in documents]

    day1docs = check_existence(documents)
    day2docs = check_valid(documents)

    print(f"numdocs={len(documents)}")
    print(f"{day1docs=}")
    print(f"{day2docs=}")


def check_existence(documents):  # part 1
    doc_count = 0
    for doc in documents:
        doc_count += exist_doc(doc)

    return doc_count


def check_valid(documents):  # part 2
    doc_count = 0
    for doc in documents:
        doc_count += validate_doc(doc)

    return doc_count


def validate_doc(doc):
    if check_byr(doc) and check_iyr(doc) and check_eyr(doc) and check_hgt(doc) and check_hcl(doc) and check_ecl(doc) and check_pid(doc):
        return 1

    return 0


def check_byr(doc):
    byr = re.search(r"byr:(\d{4})\b", doc)
    if byr:
        byr = int(byr.group(1))
        if byr >= 1920 and byr <= 2002:
            return True
    return False


def check_iyr(doc):
    iyr = re.search(r"iyr:(\d{4})\b", doc)
    if iyr:
        iyr = int(iyr.group(1))
        if iyr >= 2010 and iyr <= 2020:
            return True
    return False


def check_eyr(doc):
    eyr = re.search(r"eyr:(\d{4})\b", doc)
    if eyr:
        eyr = int(eyr.group(1))
        if eyr >= 2020 and eyr <= 2030:
            return True
    return False


def check_hgt(doc):
    hgt = re.search(r"hgt:(\d+)(\w{2})\b", doc)

    if hgt:
        hgtnum = int(hgt.group(1))
        cmorin = hgt.group(2)
        if cmorin == 'cm':
            if hgtnum >= 150 and hgtnum <= 193:
                return True
        elif cmorin == 'in':
            if hgtnum >= 59 and hgtnum <= 76:
                return True
        else:
            return False

    return False


def check_hcl(doc):
    hcl = re.search(r"hcl:#([0-9a-f]{6})\b", doc)
    if hcl:
        return True
    return False


def check_ecl(doc):
    ecl = re.search(r"ecl:(\w{3})\b", doc)
    if ecl and ecl.group(1) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def check_pid(doc):
    pid = re.search(r"pid:(\d{9})\b", doc)
    if pid:
        return True
    return False


def exist_doc(doc):
    if 'byr:' not in doc:
        return 0
    if 'iyr:' not in doc:
        return 0
    if 'eyr:' not in doc:
        return 0
    if 'hgt:' not in doc:
        return 0
    if 'hcl:' not in doc:
        return 0
    if 'ecl:' not in doc:
        return 0
    if 'pid:' not in doc:
        return 0
    return 1


if __name__ == "__main__":
    main()
