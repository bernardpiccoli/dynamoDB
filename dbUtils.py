dynamodb = boto3.resource('dynamodb')

def STATUS(self, table_name):
        table = dynamodb.Table(table)

        return {
            'num_istems': table.item_count,
            'primary_key_name': table.key_schema[0],
            'status': table.table_status,
            'bytes_size': table.table_size_bytes,
            'global_secondary_indices': table.global_secondary_indexes
        }