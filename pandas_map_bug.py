import pandas as pd

def trim_whitespace_df_applymap(df: pd.DataFrame) -> pd.DataFrame:
    return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
def trim_whitespace_df_map(df: pd.DataFrame) -> pd.DataFrame:
    return df.map(lambda x: x.strip() if isinstance(x, str) else x)

if __name__ == "__main__":
    test_df = pd.DataFrame({"a": ["  a", "b  ", "  c  "]})

    output_applymap = trim_whitespace_df_applymap(trim_whitespace_df_applymap(test_df))
    output_map = trim_whitespace_df_map(trim_whitespace_df_map(test_df))

    print("applymap")
    print(output_applymap)
    print("map")
    print(output_map)
