from testread import test


def white_high_risk_no_re_offend(records: list) -> float:
    """
   Analyzes list from read_data and counts occurrences where the first element is "Caucasian" and the seventh element is "0".
   :param records: A list of records, where each record is a list of strings.
   :return:
   """
    bottom_count = 0
    top_count = 0
    print(records)
    for record in records:
        #print(record[1])
        #print(record[6])
        #print(record[5])
        if record[1] == "Caucasian" and record[6] == "0":
            bottom_count += 1
        if record[1] == "Caucasian" and record[6] == "0" and record[5] != "Low":
            top_count += 1
    print(top_count)
    print(bottom_count)
    percentage = top_count / bottom_count * 100
    print(percentage)
    return percentage


white_high_risk_no_re_offend(test())