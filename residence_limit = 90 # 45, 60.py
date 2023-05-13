residence_limit = 90  # 45, 60
schengen_constraint = 180
visits = [[1, 10], [61, 90], [101, 140], [141, 160], [271, 290]]

def date_difference (leave, arrive):
    result = leave - arrive + 1
    return result

