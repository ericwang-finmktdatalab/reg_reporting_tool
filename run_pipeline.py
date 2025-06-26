# Execution Pipeline

from src.loader import load_data
from src.transformer import apply_mappings, enrich_with_product_reference
from src.reporter import to_json, to_xml
from src.utils import validate_schema, log_event, dict_to_xml, parse_date, generate_uuid

continuation_flag = True

log_event('Loading trade data')
df = load_data('data/raw/sample_trades.csv')
if validate_schema(df, ['TradeID', 'TradeDate', 'Counterparty', 'AssetClass', 'BaseProduct', 'SubProduct', 'TransactionType', 'Notional', 'Currency', 'Maturity', 'Action']) > 0:
    continuation_flag = False

if continuation_flag:
    log_event('Applying mappings')
    df = apply_mappings(df, 'config/mapping_rules.yaml')
    if validate_schema(df, ['trade_id', 'trade_date', 'counterparty', 'asset_class', 'base_product', 'sub_product', 'transaction_type', 'notional_amount', 'notional_currency', 'maturity_date', 'action_type']) > 0:
        continuation_flag = False

if continuation_flag:
    log_event('Enriching reference data')
    df = enrich_with_product_reference(df, 'data/reference/product_reference.csv')
    if validate_schema(df, ['trade_id', 'trade_date', 'counterparty', 'asset_class', 'base_product', 'sub_product', 'transaction_type', 'notional_amount', 'notional_currency', 'maturity_date', 'action_type', 'isda_taxonomy', 'dsb_product_name', 'upi']) > 0:
        continuation_flag = False

if continuation_flag:
    log_event('Exporting to JSON file')
    to_json(df, 'output/ir_report.json')
    log_event('JSON file exported')

if continuation_flag:
    log_event('Exporting to XML')
    to_xml(df, 'output/ir_report.xml')
    log_event('XML file exported')

if continuation_flag:
    log_event('Program completed')
else:
    log_event('Program terminated prematurely due to errors')