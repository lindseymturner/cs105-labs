from tabulate import tabulate
from read_data import read_data
from analyze_data import white_high_risk_no_re_offend, white_low_risk_reoffended, african_american_high_risk_no_re_offend, african_american_low_risk_reoffended


top_left = str(white_high_risk_no_re_offend(read_data()))
top_right = str(african_american_high_risk_no_re_offend(read_data()))
bottom_left = str(white_low_risk_reoffended(read_data()))
bottom_right = str(african_american_low_risk_reoffended(read_data()))

def print_table():
    table_list = [["Labeled higher risk, but didn't re-offend", top_left, top_right],
                  ["Labeled lower risk, yet did re-offend", bottom_left, bottom_right]]
    col_names = ["", "White", "African-American"]
    print(tabulate(table_list, headers=col_names))
print_table()


