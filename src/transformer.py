# Apply transformation logic

import yaml
import pandas as pd

def apply_mappings(df, mapping_path):
    with open(mapping_path, 'r') as f:
        mappings = yaml.safe_load(f)['fields']
    return df.rename(columns=mappings)

def enrich_with_product_reference(df, reference_path):
    ref_df = pd.read_csv(reference_path)

    # Normalize nulls for join compatibility
    df = df.fillna("")
    ref_df = ref_df.fillna("")

    # Perform multi-key join
    enriched_df = df.merge(
        ref_df,
        how='left',
        on=['asset_class', 'base_product', 'sub_product', 'transaction_type']
    )

    missing = enriched_df[enriched_df['isda_taxonomy'].isnull()]
    if not missing.empty:
        print(f"[WARNING] {len(missing)} trades could not be matched to product reference.")

    return enriched_df
