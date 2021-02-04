# リストに重複した要素があるか判定（要素にリストがない場合）
def has_duplicates(seq):
    return len(seq) != len(set(seq))

# リストに重複した要素があるか判定（要素にリストがある場合）
def has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)