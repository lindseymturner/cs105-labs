from read_data import read_data

def white_high_risk_no_re_offend(records: list) -> float:
    """
   Analyzes list from read_data and counts occurrences where the first element is "Caucasian" and the seventh element is "0".
   :param records: A list of records, where each record is a list of strings.
   :return:

>>> white_high_risk_no_re_offend([['Male', 'Caucasian', '', '', '', 'High', '0', '', ''], ['', 'Caucasian', '', '', '', 'Low', '0', '', '']])
50.0

   """
    # precondition: if any record in the records list does not have a length of 9, then raise ValueError
    # precondition: the 6th element in each record should be either 0 or 1
    bottom_count = 0
    top_count = 0

    for record in records:
        assert len(record) == 9
        if record[1] == "Caucasian" and record[6] == "0":
            bottom_count += 1
        if record[1] == "Caucasian" and record[6] == "0" and record[5] != "Low":
            top_count += 1
    percentage = top_count / bottom_count * 100
    #print(percentage)
    return percentage


#white_high_risk_no_re_offend(read_data())


def african_american_high_risk_no_re_offend(records: list) -> float:
    """
   Analyzes list from read_data and counts occurrences where the first element is "African_American" and the seventh element is "0".
   :param records: A list of records, where each record is a list of strings.
   :return:

>>> african_american_high_risk_no_re_offend([['Male', 'African-American', '', '', '', 'High', '0', '', ''], ['', 'African-American', '', '', '', 'Low', '0', '', '']])
50.0

   """
    # precondition: if any record in the records list does not have a length of 9, then raise ValueError
    # precondition: the 6th element in each record should be either 0 or 1

    bottom_count = 0
    top_count = 0

    for record in records:
        if record[1] == "African-American" and record[6] == "0":
            bottom_count += 1
        if record[1] == "African-American" and record[6] == "0" and record[5] != "Low":
            top_count += 1
    percentage = top_count / bottom_count * 100
    #print(percentage)
    return percentage


#african_american_high_risk_no_re_offend(read_data())


def white_low_risk_reoffended(records: list) -> float:
    """
   Analyzes list from read_data and counts occurrences where the first element is "Caucasian" and the seventh element is "1".
   :param records: A list of records, where each record is a list of strings.
   :return:

>>> white_low_risk_reoffended([['Male', 'Caucasian', '', '', '', 'Low', '1', '', ''], ['', 'Caucasian', '', '', '', 'Low', '1', '', '']])
100.0

   """
    # precondition: if any record in the records list does not have a length of 9, then raise ValueError
    # precondition: the 6th element in each record should be either 0 or 1
    # precondition: at least 1 person meets the parameters for race and two-year-recid (the bottom count has to end up being greater than 0)
    bottom_count = 0
    top_count = 0

    for record in records:
        if record[1] == "Caucasian" and record[6] == "1":
            bottom_count += 1
        if record[1] == "Caucasian" and record[6] == "1" and record[5] == "Low":
            top_count += 1
    if bottom_count > 0:
        percentage = top_count / bottom_count * 100
    else:
        raise ValueError
    #print(percentage)
    return percentage


#white_low_risk_reoffended(read_data())


def african_american_low_risk_reoffended(records: list) -> float:
    """
   Analyzes list from read_data and counts occurrences where the first element is "African_American" and the seventh element is "1".
   :param records: A list of records, where each record is a list of strings.
   :return:

>>> african_american_low_risk_reoffended([['Male', 'African-American', '', '', '', 'Low', '1', '', ''], ['', 'African-American', '', '', '', 'Low', '1', '', '']])
100.0

   """
    # precondition: if any record in the records list does not have a length of 9, then raise ValueError
    # precondition: the 6th element in each record should be either 0 or 1

    bottom_count = 0
    top_count = 0

    for record in records:
        if record[1] == "African-American" and record[6] == "1":
            bottom_count += 1
        if record[1] == "African-American" and record[6] == "1" and record[5] == "Low":
            top_count += 1
    percentage = top_count / bottom_count * 100
    #print(percentage)
    return percentage


#african_american_low_risk_reoffended(read_data())